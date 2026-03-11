def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon',
    }

    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector',
    }

    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist',
    }
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))

    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    alice_only = alice.difference(bob.union(charlie))
    bob_only = bob.difference(alice.union(charlie))
    charlie_only = charlie.difference(alice.union(bob))

    rare_achievements = alice_only.union(bob_only).union(charlie_only)
    print("Rare achievements (1 player):", rare_achievements)

    alice_bob_common = alice.intersection(bob)
    print("\nAlice vs Bob common:", alice_bob_common)

    alice_unique = alice.difference(bob)
    print("Alice unique:", alice_unique)

    bob_unique = bob.difference(alice)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    main()
