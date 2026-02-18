import functools
import time
import re
import random
from typing import Callable as callable


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def timer() -> str:
        start_time: time = time.time()
        print(f"Casting {func.__name__}...")
        result = func()
        end_time: time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    @functools.wraps(min_power)
    def check_power(func: callable) -> callable:
        @functools.wraps(func)
        def check(*args) -> str:
            if args[2] < min_power:
                return "Insufficient power for this spell"
            return func(*args)
        return check
    return check_power


def retry_spell(max_attempts: int) -> callable:
    @functools.wraps(max_attempts)
    def retrying(func: callable) -> callable:
        attempt: int = 0

        @functools.wraps(func)
        def retry() -> str:
            nonlocal attempt
            try:
                result: str = func()
            except Exception:
                attempt += 1
                print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                if attempt == max_attempts:
                    return f"\nSpell casting failed after {max_attempts} attempts"
                return retry()
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

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@retry_spell(max_attempts=10)
def difficult_spell() -> str:
    success: float = random.random()
    if success > 0.1:
        raise Exception
    return "\nSuccessfully cast difficult spell!"


def main() -> None:

    print("\n==== Testing spell timer ====\n")
    fireball()

    print("\n==== Testing MageGuild ====\n")
    for name in ["no", "marcel67", "ElSinge"]:
        print(f"Mage name '{name}' validated: {MageGuild.validate_mage_name(name)}")

    print("")
    guild: MageGuild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ice Shard", 8))

    print("\n==== Testing retrying spell ====\n")
    print(difficult_spell())


if __name__ == "__main__":
    main()
