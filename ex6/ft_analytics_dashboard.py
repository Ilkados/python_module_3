players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
            "sharp_shooter"
        ]
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": [
            "first_kill",
            "level_5",
            "collector"
        ]
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": False,
        "region": "north",
        "achievements": [
            "first_kill",
            "level_10",
            "speed_runner",
            "boss_slayer",
            "treasure_hunter",
            "collector",
            "combo_master"
        ]
    },
    {
        "name": "diana",
        "score": 2050,
        "active": True,
        "region": "central",
        "achievements": [
            "level_10",
            "healer",
            "boss_slayer",
            "team_player"
        ]
    }
]

print("=== Game Analytics Dashboard ===")
print("\n=== List Comprehension Examples ===")

high_scorers = [
    player["name"] for player in players if player["score"] > 2000
]
scores_doubled = [player["score"] * 2 for player in players]
active_players = [
    player["name"] for player in players if player["active"]
]

print("High scorers (>2000):", high_scorers)
print("Scores doubled:", scores_doubled)
print("Active players:", active_players)

print("\n=== Dict Comprehension Examples ===")

player_scores = {
    player["name"]: player["score"] for player in players
}
achievement_counts = {
    player["name"]: len(player["achievements"])
    for player in players
}

categories = ["high", "medium", "low"]
score_categories = {
    category: len([
        player for player in players
        if (
            (category == "high" and player["score"] > 2000)
            or (
                category == "medium"
                and 1500 <= player["score"] <= 2000
            )
            or (category == "low" and player["score"] < 1500)
        )
    ])
    for category in categories
}

print("Player scores:", player_scores)
print("Score categories:", score_categories)
print("Achievement counts:", achievement_counts)

print("\n=== Set Comprehension Examples ===")

unique_players = {player["name"] for player in players}
unique_achievements = {
    achievement
    for player in players
    for achievement in player["achievements"]
}
active_regions = {
    player["region"] for player in players if player["active"]
}

print("Unique players:", unique_players)
print("Unique achievements:", unique_achievements)
print("Active regions:", active_regions)

print("\n=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(
    player["score"] for player in players
) / len(players)
top_performer = max(players, key=lambda player: player["score"])

print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print("Average score:", average_score)
print(
    "Top performer:",
    top_performer["name"],
    f'({top_performer["score"]} points, '
    f'{len(top_performer["achievements"])} achievements)'
)
