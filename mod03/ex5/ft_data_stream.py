import random
from typing import Generator
import time
import sys


DEFAULT_PLAYERS = ["vax'ildan", "pike", "keyleth"]
DEFAULT_EVENT_NB = 1000


class Player:
    def __init__(
        self,
        name: str = "anonymous",
        level: int = 0,
        kills: int = 0,
        treasures: int = 0
    ) -> None:

        self.name: str = name
        self.level: int = level
        self.kills: int = kills
        self.treasures: int = treasures

    def update(self, event_type: str) -> None:
        if event_type == "leveled up":
            self.level += 1
            Event.lvl_up_count += 1
        elif event_type == "killed monster":
            self.kills += 1
        elif event_type == "found treasure":
            self.treasures += 1
            Event.treasure_count += 1


class Event:
    event_count: int = 0
    treasure_count: int = 0
    lvl_up_count: int = 0

    def __init__(self, event_type: str, player: Player) -> None:
        self.event_type: str = event_type
        self.player: Player = player

        if (
            event_type == "leveled up"
            or event_type == "killed monster"
            or event_type == "found treasure"
        ):
            self.important: bool = True
        else:
            self.important = False


def choose_player(all_players: list[Player]) -> Player:
    random_pl: int = random.randint(0, len(all_players) - 1)
    return all_players[random_pl]


def generate_events(
    event_nb: int,
    players: list[Player]
) -> Generator[Event, None, None]:

    while event_nb > 0:
        yield choose_event(players)
        event_nb -= 1


def choose_event(players: list[Player]) -> Event:
    random_range: int = random.randint(1, 1000)
    random_nb: int = random.randint(1, 44)
    random_pl: Player = choose_player(players)

    if random_range % random_nb == 0:
        return Event("leveled up", random_pl)

    elif random_range % random_nb == 1:
        return Event("killed monster", random_pl)

    elif random_range % random_nb == 2:
        return Event("found treasure", random_pl)

    else:
        return Event("moved", random_pl)


def process_events(
    events: Generator[Event, None, None]
) -> Generator[Event, None, None]:

    for event in events:
        Event.event_count += 1
        if event.important:
            yield event


def stream_analytics(players: list[Player]) -> None:
    print("\n=== Stream Analytics ===")

    print(f"Total events processed: {Event.event_count}")

    high_lvl_count: int = 0
    for player in players:
        if player.level >= 10:
            high_lvl_count += 1

    print(f"High-level players (10+): {high_lvl_count}")
    print(f"Treasure events: {Event.treasure_count}")
    print(f"Level-up events: {Event.lvl_up_count}\n")


def fibonacci_seq(loop: int) -> Generator[int, None, None]:
    current: int = 1
    prev: int = 0

    while loop > 0:
        yield prev
        prev, current = current, prev + current
        loop -= 1


def prime_numbers(count: int) -> Generator[int, None, None]:
    nb: int = 2

    while count > 0:
        prime_check: int = 2
        is_prime: bool = True

        while prime_check <= nb // 2:
            if nb % prime_check == 0:
                is_prime = False
                break
            prime_check += 1

        if is_prime:
            count -= 1
            yield nb
        nb += 1


def gen_demon(fib_nb: int, prime_nb: int) -> None:
    print("=== Generator Demonstration ===")

    fst: bool = True
    print(f"Fibonacci sequence (first {fib_nb}): ", end="")
    for fib in fibonacci_seq(fib_nb):
        if not fst:
            print(", ", end="")
        print(f"{fib}", end="")
        fst = False

    fst = True
    print(f"\nPrime numbers (first {prime_nb}): ", end="")
    for prime in prime_numbers(prime_nb):
        if not fst:
            print(", ", end="")
        print(f"{prime}", end="")
        fst = False


def parse_args(
    args: list[str]
) -> tuple[int, list[Player]]:

    start: int = 0
    players: list[Player] = []

    try:
        event_nb: int = int(args[0])
    except ValueError:
        if len(args) > len(DEFAULT_PLAYERS):
            print(
                "No specific number of events provided - "
                f"Resorting to default {DEFAULT_EVENT_NB}\n"
            )
        event_nb = DEFAULT_EVENT_NB
    else:
        if event_nb < 1:
            print(
                f"Error: {int(args[0])} number of events "
                f"is insuffisant - Resorting to default {DEFAULT_EVENT_NB}\n"
            )
            event_nb = DEFAULT_EVENT_NB
        start += 1

    for pl in range(start, len(args)):
        try:
            int(args[pl])
        except ValueError:
            players.append(Player(args[pl]))
        else:
            print(
                f"Caught ValueError: Invalid type integer '{args[pl]}' "
                f"for character name (string required)"
                " - character creation [IGNORED]\n"
            )

    return event_nb, players


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    start: float = time.time()
    args: list[str] = DEFAULT_PLAYERS

    if len(sys.argv) == 1:
        print(
            "No custom players nor specific number "
            "of events given\n-> Usage:\n"
            "[SPECIFIC NUMBER OF EVENTS] ft_data_stream.py <event_number>\n"
            "[CUSTOM PLAYERS] ft_data_stream.py <player1> <player2> ...\n"
            "[BOTH] ft_data_stream.py "
            "<event_number> <player1> <player2> ...\n\n"
            f"Resorting to default players {DEFAULT_PLAYERS} "
            f"and default number of events {DEFAULT_EVENT_NB}\n"
        )
    else:
        args = sys.argv[1:] + args

    event_nb, all_players = parse_args(args)
    print(f"Processing {event_nb} game events...\n")
    count: int = 0

    for cur_event in process_events(generate_events(event_nb, all_players)):
        count += 1
        cur_event.player.update(cur_event.event_type)
        print(
            f"Event {count}: Player {cur_event.player.name.capitalize()} "
            f"(level {cur_event.player.level}) {cur_event.event_type}"
        )

    stream_analytics(all_players)
    print("Memory usage: constant (streaming)")

    end: float = time.time()
    print(f"Processing time: {round(end - start, 3)} seconds\n")

    gen_demon(10, 5)


if __name__ == "__main__":
    main()
