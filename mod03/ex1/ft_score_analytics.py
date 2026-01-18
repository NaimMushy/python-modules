import sys


def main() -> None:
    """
    Displays player scores given from the command line.
    """
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "no score provided. "
            "usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores: list[int] = []
        for score in range(1, len(sys.argv)):
            try:
                conv_score: int = int(sys.argv[score])
            except ValueError:
                print(
                    f"caught ValueError: invalid type {type(sys.argv[score])} "
                    f"for the score {sys.argv[score]}"
                )
            else:
                scores.append(conv_score)
        print(f"scores processed: {scores}")
        print(f"total players: {len(scores)}")
        total_score: int = 0
        for s in scores:
            total_score += s
        print(f"total score: {total_score}")
        print(f"average score: {total_score / len(scores)}")
        print(f"high score: {max(scores)}")
        print(f"low score: {min(scores)}")
        print(f"score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
