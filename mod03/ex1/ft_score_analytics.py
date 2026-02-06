import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No score provided - "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores: list[int] = []
        for score in range(1, len(sys.argv)):
            try:
                conv_score: int = int(sys.argv[score])
            except ValueError:
                print(
                    f"Caught ValueError: Invalid type {type(sys.argv[score])} "
                    f"for the score {sys.argv[score]} (integer required)"
                )
            else:
                scores.append(conv_score)
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        total_score: int = 0
        for s in scores:
            total_score += s
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
