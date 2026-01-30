from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card
from ex1.SpellCard import SpellCard


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
        self._health: int = health
        self.combat_type: str = combat_type
        self.known_spells: list[SpellCard] = known_spells

    def set_attack(self, new_attack: int) -> None:
        """
        Verifies and updates the creature card's attack damage
        if it's a positive value (superior or equal to zero).

        Parameters
        ----------
        new_attack
            The creature card's new attack damage.
        """
        if new_attack >= 0:
            self._attack = new_attack
        else:
            self._attack = 0

    def set_health(self, new_health: int) -> None:
        """
        Verifies and updates the creature card's health points
        if it's a positive value (superior or equal to zero).

        Parameters
        ----------
        new_health
            The creature card's new health points.
        """
        if new_health < self.get_health():
            self.defend(self.get_health() - new_health)
        else:
            if new_health > 0:
                self._health = new_health
            else:
                self._health = 0

    def get_attack(self) -> int:
        """
        Returns
        -------
        int
            The creature card's attack damage.
        """
        return self._attack

    def get_health(self) -> int:
        """
        Returns
        -------
        int
            The creature card's health points.
        """
        return self._health

    def learn_spell(self, new_spell: SpellCard) -> None:
        if new_spell in self.known_spells:
            print(f"Spell {new_spell.name} already learned")
        else:
            self.known_spells.append(new_spell)

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage > self.defense:
            damage_taken: int = incoming_damage - self.defense
            self._health -= damage_taken
            if self.get_health() < 0:
                self._health = 0
        else:
            damage_taken = 0
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.get_health() > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "Combatable": ["attack", "defend", "get_combat_stats"]
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used: int = 0
        for spell in self.known_spells:
            if spell.name == spell_name:
                mana_used = spell.cost
        if not mana_used:
            print("Spell {spell_name} not learned by {self.name}")
        elif not self.channel_mana(mana_used)["success"]:
            mana_used = 0
        return {
            "success": mana_used > 0,
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        if amount > self.mana_pool:
            print(
                "Impossible to channel sufficient mana - "
                f"{self.mana_pool} still available"
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

    def get_card_info(self) -> dict:
        return super().get_card_info | {
            "attack": self.attack,
            "defense": self.defense,
            "mana_pool": self.mana_pool,
            "health": self.health,
            "combat_type": self.combat_type,
            "known_spells": self.known_spells
        }

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            play_result: dict = {
                "card_played": self.name,
                "mana_cost": self.cost,
                "effects": [
                    self.get_combat_stats(),
                    self.get_magic_stats()
                ]
            }
            game_state["available_mana"] -= self.cost
            print(f"Play result: {play_result}\n")
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result
