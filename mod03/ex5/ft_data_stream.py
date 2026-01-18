import random
import sys
from typing import Generator
import time


DEFAULT_PLAYERS = ["alice", "bob", "charlie"]
DEFAULT_EVENT_NB = 20


class Player:
    """
    A class that represents a player.
    """
    def __init__(
        self,
        name: str = "anonymous",
        level: int = 0,
        kills: int = 0,
        treasures: int = 0
    ) -> None:
        """
        Initializes the player's data.

        Parameters
        ----------
        name
            The player's name.
        level
            The player's level.
        kills
            The player's kills.
        treasures
            The player's treasures.
        """
        self.name = name
        self.level = level
        self.kills = kills
        self.treasures = treasures

    def update(self, event_type: str) -> None:
        """
        Updates the player's data based on the event given.

        Parameters
        ----------
        event_type
            The type of the event.
        """
        if event_type == "leveled up":
            self.level += 1
            Event.lvl_up_count += 1
        elif event_type == "killed monster":
            self.kills += 1
        elif event_type == "found treasure":
            self.treasures += 1
            Event.treasure_count += 1


class Event:
    """
    A class that represents an event.

    Attributes
    ----------
    event_count
        The total event count.
    treasure_count
        The total number of treasure events.
    lvl_up_count
        The total number of level up events.
    """
    event_count: int = 0
    treasure_count: int = 0
    lvl_up_count: int = 0

    def __init__(self, event_type: str, player: Player) -> None:
        """
        Initializes the event's data.

        Parameters
        ----------
        event_type
            The type of the event.
        player
            The player to which the event is happening.
        """
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
    """
    Chooses randomly a player amongst the list of players provided.

    Parameters
    ----------
    all_players
        The list of players.

    Returns
    -------
    Player
        The player chosen at random.
    """
    random_pl: int = random.randint(0, len(all_players) - 1)
    return all_players[random_pl]


def generate_events(
    event_nb: int,
    players: list[Player]
) -> Generator[Event, None, None]:
    """
    Generates a list of random events.

    Parameters
    ----------
    event_nb
        The number of events to generate.
    players
        The list of players.

    Returns
    -------
    Generator[Event, None, None]
        The generator containing all the randomly generated events.
    """
    while event_nb > 0:
        yield choose_event(players)
        event_nb -= 1


def choose_event(players: list[Player]) -> Event:
    """
    Chooses randomly an event happening to a random player.

    Parameters
    ----------
    players
        The list of players.

    Returns
    -------
    Event
        The event randomly selected.
    """
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
    """
    Processes the stream of events to keep the important ones.

    Parameters
    ----------
    events
        The generator containing all the randomly generated events.

    Returns
    -------
    Generator[Event, None, None]
        The generator containing all the important events.
    """
    for event in events:
        Event.event_count += 1
        if event.important:
            yield event


def stream_analytics(players: list[Player]) -> None:
    """
    Displays data about the events stream.

    Parameters
    ----------
    players
        The list of players.
    """
    print("\n=== Stream Analytics ===")
    print(f"total events processed: {Event.event_count}")
    high_lvl_count: int = 0
    for player in players:
        if player.level >= 10:
            high_lvl_count += 1
    print(f"high-level players (10+): {high_lvl_count}")
    print(f"treasure events: {Event.treasure_count}")
    print(f"level-up events: {Event.lvl_up_count}\n")


def fibonacci_seq(loop: int) -> Generator[int, None, None]:
    """
    Calculates the fibonacci sequence based on the length given.

    Parameters
    ----------
    loop
        The length of the sequence.

    Returns
    -------
    Generator[int, None, None]
        The generator containing the elements of the sequence.
    """
    current: int = 1
    prev: int = 0
    while loop > 0:
        yield prev
        temp: int = current
        current += prev
        prev = temp
        loop -= 1


def prime_nb(count: int) -> Generator[int, None, None]:
    """
    Calculates a list of prime numbers based on the length given.

    Parameters
    ----------
    count
        The length of the list.

    Returns
    -------
    Generator[int, None, None]
        The generator containing the prime numbers.
    """
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


def gen_demon() -> None:
    """
    Displays a demonstration of generator capabilities.
    """
    print("=== Generator Demonstration ===")
    fib_seq: Generator[int, None, None] = fibonacci_seq(10)
    print("fibonacci sequence (first 10): ", end="")
    print(*fib_seq)
    all_primes: Generator[int, None, None] = prime_nb(5)
    print("prime numbers (first 5): ", end="")
    print(*all_primes)


def is_integer(to_convert: str) -> bool:
    """
    Checks if the given string can be converted to an integer.

    Returns
    -------
    bool
        True if the string can be converted, False otherwise.
    """
    try:
        int(to_convert)
    except ValueError:
        return False
    else:
        return True


def parse_args(
    args: list[str]
) -> (int, list[Player]):
    """
    Parses a list of arguments and determines
    both the number of events to generate and the list of players.

    Parameters
    ----------
    args
        The arguments to parse, either from the command line, or the default.

    Returns
    -------
    int
        The number of events to generate.
    list[Player]
        The generator containing all the players.
    """
    start: int = 0
    event_nb: int = 0
    players: list[Player] = []
    if is_integer(args[0]):
        if int(args[0]) >= 1:
            event_nb = int(args[0])
        else:
            print(
                f"error: {int(args[0])} number of events "
                f"is insuffisant - resorting to default {DEFAULT_EVENT_NB}\n"
            )
            event_nb = DEFAULT_EVENT_NB
        start += 1
    else:
        event_nb = DEFAULT_EVENT_NB
    for pl in range(start, len(args)):
        if not is_integer(args[pl]):
            players.append(Player(args[pl]))
        else:
            print(
                f"ValueError: invalid type integer '{args[pl]}' "
                f"for character name - character creation [IGNORED]\n"
            )
    return event_nb, players


def main() -> None:
    """
    Manages and displays data about randomized events using generators.
    """
    print("=== Game Data Stream Processor ===\n")
    start: float = time.time()
    if len(sys.argv) == 1:
        args: list[str] = DEFAULT_PLAYERS
    else:
        args = sys.argv[1:] + DEFAULT_PLAYERS
    event_nb, all_players = parse_args(args)
    print(f"processing {event_nb} game events...\n")
    events: Generator[Event, None, None] = generate_events(
        event_nb, all_players
    )
    processed_events: Generator[Event, None, None] = process_events(events)
    count: int = 0
    for cur_event in processed_events:
        count += 1
        cur_event.player.update(cur_event.event_type)
        print(
            f"event {count}: player {cur_event.player.name} "
            f"(level {cur_event.player.level}) {cur_event.event_type}"
        )
    stream_analytics(all_players)
    print("memory usage: constant (streaming)")
    end: float = time.time()
    print(f"processing time: {round(end - start, 3)} seconds\n")
    gen_demon()


if __name__ == "__main__":
    main()
