from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
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
                    if target.name not in target_attacked:
                        targets_attacked.append(target.name)
        else:
            for card in hand:
                if isinstance(card, SpellCard) and len(enemy_targets):
                    card.resolve_effect(enemy_targets)
                    hand.remove(card)
                if isinstance(card, ArtifactCard) and len(enemy_targets):


    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, (CreatureCard, EliteCard))
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
