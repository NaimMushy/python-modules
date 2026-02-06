import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    args: list[str] = sys.argv
    if len(args) == 1:
        print(
            "No score provided - "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return None

    scores: list[int] = []
    for score in range(1, len(args)):
        try:
            conv_score: int = int(args[score])
        except ValueError:
            print(
                f"Caught ValueError: Invalid type {type(args[score])} "
                f"for the score {args[score]} (integer required)"
            )
        else:
            scores.append(conv_score)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
