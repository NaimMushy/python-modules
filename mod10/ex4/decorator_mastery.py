import functools
import time
import re
import random
from typing import Callable as callable


def spell_timer(func: callable) -> callable:

    @functools.wraps(func)
    def timer() -> str:

        start_time: float = time.time()

        print(f"Casting {func.__name__}...")

        result = func()
        end_time: float = time.time()

        print(f"Spell completed in {end_time - start_time:.3f} seconds")

        return result

    return timer


def power_validator(min_power: int) -> callable:

    @functools.wraps(lambda min_power: min_power)
    def check_power(func: callable) -> callable:

        @functools.wraps(func)
        def check(*args) -> str:

            print(f"Trying to cast {args[1]}...")

            return (
                (
                    f"Insufficient power ({args[0]}) for this spell "
                    f"- Minimum {min_power} required\n"
                )
                if args[0] < min_power
                else func(*args)
            )

        return check

    return check_power


def retry_spell(max_attempts: int) -> callable:

    @functools.wraps(lambda max_attempts: max_attempts)
    def retrying(func: callable) -> callable:

        attempt: int = 0

        @functools.wraps(func)
        def retry() -> str:

            nonlocal attempt

            try:

                result: str = func()

            except Exception:

                attempt += 1

                print(
                    "Spell failed, retrying... (attempt "
                    f"{attempt}/{max_attempts})"
                )

                return (
                    f"\nSpell casting failed after {max_attempts} attempts\n"
                    if attempt == max_attempts
                    else retry()
                )

            else:

                return result

        return retry

    return retrying


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        return (
            True
            if len(name) >= 3 and
            re.fullmatch("[a-z ]+", name, re.I)
            else False
        )

    def cast_spell(self, spell_name: str, power: int) -> callable:

        @power_validator(min_power=10)
        def validate_power(power: int, spell_name: str) -> str:

            return f"Successfully cast {spell_name} with power {power}!\n"

        return validate_power(power, spell_name)


@spell_timer
def fireball() -> str:

    return "Fireball cast!"


@retry_spell(max_attempts=10)
def difficult_spell() -> str:

    success: float = random.random()

    if success > 0.1:
        raise Exception

    return "\nSuccessfully cast difficult spell!\n"


def main() -> None:

    print("\n==== Testing spell timer ====\n")

    print(f"Result: {fireball()}")

    print("\n==== Testing MageGuild ====\n")

    for name in ["no", "marcel67", "ElSinge"]:
        print(
            f"Mage name '{name}' validated: "
            f"{MageGuild.validate_mage_name(name)}"
        )

    print("")

    guild: MageGuild = MageGuild()

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice Shard", 8))

    print("\n==== Testing retrying spell ====\n")

    print(difficult_spell())


if __name__ == "__main__":

    main()
