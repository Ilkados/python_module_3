import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv

    if len(args) == 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    my_list = []

    for arg in args[1:]:
        try:
            value = int(arg)
            my_list.append(value)
        except ValueError:
            continue

    if not my_list:
        print("No valid scores provided.")
        return

    total_players = len(my_list)
    total_score = sum(my_list)
    average_score = total_score / total_players
    high_score = max(my_list)
    low_score = min(my_list)
    score_range = high_score - low_score

    print("Scores processed:", my_list)
    print("Total players:", total_players)
    print("Total score:", total_score)
    print("Average score:", average_score)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)


if __name__ == "__main__":
    main()
