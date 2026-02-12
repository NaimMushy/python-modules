from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card
from ex1.SpellCard import SpellCard
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
        mana_pool: int,
        health: int,
        combat_type: str,
        known_spells: list[SpellCard] = []
    ) -> None:
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.defense: int = defense
        self.mana_pool: int = mana_pool
        self.__health: int = health
        self.combat_type: str = combat_type
        self.known_spells: list[SpellCard] = known_spells

    def set_attack(self, new_attack: int) -> None:
        if isinstance(new_attack, int) and new_attack >= 0:
            self.__attack = new_attack
        else:
            self.__attack = 0

    def set_health(self, new_health: int) -> None:
        if new_health < self.get_health():
            self.defend(self.get_health() - new_health)
        else:
            if isinstance(new_health, int) and new_health > 0:
                self.__health = new_health
            else:
                self.__health = 0

    def get_attack(self) -> int:
        return self.__attack

    def get_health(self) -> int:
        return self.__health

    def learn_spell(self, new_spell: SpellCard) -> None:
        if new_spell in self.known_spells:
            print(f"Spell {new_spell.name} already learned\n")
        else:
            print(f"{self.name} is learning a new spell...")
            print(f"{new_spell.name} learned!\n")
            self.known_spells.append(new_spell)

    def attack(self, target) -> dict:
        attack_result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage": self.get_attack(),
            "combat_type": self.combat_type
        }
        print(
            "Combat phase:\n"
            f"Attack result: {attack_result}\n"
        )
        return attack_result

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage > self.defense:
            damage_taken: int = incoming_damage - self.defense
            self.__health -= damage_taken
            if self.get_health() < 0:
                self.__health = 0
        else:
            damage_taken = 0
        defense_result: dict = {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.get_health() > 0
        }
        print(f"Defense result: {defense_result}\n")
        return defense_result

    def get_combat_stats(self) -> dict:
        return {
            "Combatable": ["attack", "defend", "get_combat_stats"]
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used: int = 0
        for spell in self.known_spells:
            if spell.name == spell_name:
                mana_used = spell.cost
                spell_to_cast: SpellCard = spell
        mana_channel_result: dict = self.channel_mana(mana_used)
        if not mana_used:
            print(f"Spell {spell_name} not learned by {self.name}\n")
        elif not mana_channel_result["success"]:
            mana_used = 0
        elif targets:
            spell_to_cast.resolve_effect(targets)
        print("Magic phase:")
        cast_result: dict = {
            "caster": self.name,
            "spell": (
                None if not mana_used else spell_name
            ),
            "targets": [target.name for target in targets],
            "mana_used": mana_used,
            "success": mana_used > 0
        }
        print(
            f"Spell cast: {cast_result}"
            f"Mana channel: {mana_channel_result}\n"
        )
        return cast_result

    def channel_mana(self, amount: int) -> dict:
        if amount > self.mana_pool:
            print(
                "Impossible to channel sufficient mana - "
                f"{self.mana_pool} still available\n"
            )
            amount = 0
        else:
            self.mana_pool -= amount
        return {
            "success": amount > 0,
            "mana_channeled": amount,
            "mana_remaining": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "Magical": ["cast_spell", "channel_mana", "get_magic_stats"]
        }

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["available_mana"]):
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
            return {}
        play_result: dict = {}
        active_spells: list[SpellCard] = [
            card for card in game_state["hand"]
            if isinstance(card, SpellCard) and
            card in self.known_spells
        ]
        if active_spells:
            spell_to_cast: SpellCard = random.choice(active_spells)
            cast_result: dict = self.cast_spell(
                spell_to_cast.name,
                spell_to_cast.get_correct_targets(
                    game_state["ally_beings"],
                    game_state["living_targets"]
                )
            )
            if cast_result["success"]:
                game_state["cards_to_remove"].append(spell_to_cast)
                play_result["effects"] = (
                    f"Cast spell {spell_to_cast.name} "
                    f"on {cast_result['targets']}"
                )
            play_result["mana_used"] = cast_result["mana_used"]
        elif game_state["living_targets"]:
            attack_result: dict = self.attack(
                random.choice(game_state["living_targets"])
            )
            play_result["mana_used"] = self.cost
            play_result["effects"] = f"Attacked {attack_result['target']}"
        else:
            print(f"No available targets for {self.name}\n")
            return {}
        play_result = {"card_played": self.name}
        print(f"Play result: {play_result}\n")
        return play_result

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            "type": "Elite",
            "attack": self.get_attack(),
            "defense": self.defense,
            "mana_pool": self.mana_pool,
            "health": self.get_health(),
            "combat_type": self.combat_type,
            "known_spells": self.known_spells
        }

    def __repr__(self) -> str:
        return "elites"
