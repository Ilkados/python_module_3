import math


def main() -> None:
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    origin = (0, 0, 0)

    print("Position created:", position)

    x1, y1, z1 = origin
    x2, y2, z2 = position

    distance = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    print(f"Distance between {origin} and {position}: {round(distance, 2)}")

    coord_str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_str}"')

    parts = coord_str.split(",")

    if len(parts) != 3:
        print("Invalid coordinate format.")
        return

    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        parsed_position = (x, y, z)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)
        return

    print("Parsed position:", parsed_position)

    x1, y1, z1 = origin
    x2, y2, z2 = parsed_position

    distance2 = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    print(
        f"Distance between {origin} and {parsed_position}: "
        f"{round(distance2, 2)}"
    )

    print("\nUnpacking demonstration:")

    # Explicit unpacking demonstration
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":

    main()
