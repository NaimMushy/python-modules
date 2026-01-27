from .Card import Card


class CreatureCard(Card):
    """
    A class that represents a creature card.
    """
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        """
        Initializes the creature card's data.

        Parameters
        ----------
        name
            The creature card's name.
        cost
            The creature card's mana cost to play.
        rarity
            The creature card's rarity.
        attack
            The creature card's attack damage.
        health
            The creature card's health points.
        """
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)

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
        if new_health >= 0:
            self._health: int = new_health
        else:
            self._health = 1

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

    def get_card_info(self) -> dict:
        """
        Returns
        -------
        dict
            The creature card's data (its properties).
        """
        return super().get_card_info() | {
            "type": "Creature",
            "attack": self.get_attack(),
            "health": self.get_health()
        }

    def play(self, game_state: dict) -> dict:
        """
        Plays the creature card if the available mana is sufficient.

        Parameters
        ----------
        game_state
            The game's state.

        Returns
        -------
        dict
            The playing result.
        """
        if self.is_playable(game_state["available_mana"]):
            play_result: dict = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
            print(f"Play result: {play_result}\n")
            self.attack_target(game_state["targets"][0])
            game_state["available_mana"] -= self.cost
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result

    def attack_target(self, target) -> dict:
        """
        Attacks the target.

        Parameters
        ----------
        target
            The target to attack.

        Returns
        -------
        dict
            The attack result.
        """
        print(f"{self.name} attacks {target.name}:")
        if target.get_health() - self.get_attack() <= 0:
            target.set_health(0)
        else:
            target.set_health(target.get_health() - self.get_attack())
        attack_result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.get_attack(),
            "combat_resolved": target.get_health() == 0
        }
        print(f"Attack result: {attack_result}\n")
        return attack_result
