from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        for item in hand:
            if not isinstance(item, Card):
                available_mana: int = item
                hand.remove(item)
        attackers: list[Card] = self.prioritize_targets(hand)
        enemy_targets: list[Card] = self.prioritize_targets(battlefield)
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        mana_used: int = 0
        damage_dealt: int = 0
        if len(attackers) and len(enemy_targets):
            for card in attackers:
                if card.cost <= 3:
                    target: Card = random.choice(enemy_targets)
                    card.attack(target)
                    mana_used += card.cost
                    damage_dealt += card.get_attack()
                    cards_played.append(card.name)
                    if target.name not in targets_attacked:
                        targets_attacked.append(target.name)
        else:
            for card in hand:
                if isinstance(card, SpellCard):
                    if len(card.get_correct_targets(hand, battlefield)):
                        card.resolve_effect(
                            card.get_correct_targets(hand, battlefield)
                        )
                        hand.remove(card)
                if isinstance(card, ArtifactCard):
                    game_state: dict = {
                        "available_mana": available_mana
                    }
                    card.apply_effect(
                        card.play(game_state)["effect"],
                        card.play(game_state)["target"]
                    )

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, (CreatureCard, EliteCard))
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
