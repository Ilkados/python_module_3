import time
from typing import Generator


def generate_events(total: int) -> Generator[tuple[str, int, str], None, None]:
    names = ["alice", "bob", "charlie"]
    event_types = ["killed monster", "found treasure", "leveled up"]

    for i in range(total):
        name = names[i % len(names)]
        event_type = event_types[i % len(event_types)]
        level = (i % 15) + 1
        yield (name, level, event_type)


def stream_analytics(total: int) -> None:
    total_count = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for _, level, event_type in generate_events(total):
        total_count += 1

        if level >= 10:
            high_level_count += 1

        if event_type == "found treasure":
            treasure_count += 1

        if event_type == "leveled up":
            levelup_count += 1

    print("Total events processed:", total_count)
    print("High-level players (10+):", high_level_count)
    print("Treasure events:", treasure_count)
    print("Level-up events:", levelup_count)
    print("Memory usage: Constant (streaming)")


def generate_fibonacci(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def generate_prime(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        i = 2

        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            yield num
            count += 1

        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    start_time = time.time()
    total_game_event = 10

    print(f"Processing {total_game_event} game events...")
    event_index = 1
    for name, level, event_type in generate_events(total_game_event):
        print(f"Event {event_index}: Player {name} "
              f"(level {level}) {event_type}")
        event_index += 1

    print("\n=== Stream Analytics ===")
    stream_analytics(total_game_event)
    end_time = time.time()

    processing_time = round(end_time - start_time, 4)
    print(f"Processing time: {processing_time} seconds")

    print("\n=== Generator Demonstration ===")

    fibonacci_total = 10
    fib_numbers = ", ".join(
        str(num) for num in generate_fibonacci(fibonacci_total)
    )
    print(f"Fibonacci sequence (first {fibonacci_total}): {fib_numbers}")

    prime_total = 5
    prime_numbers = ", ".join(str(num) for num in generate_prime(prime_total))
    print(f"Prime numbers (first {prime_total}): {prime_numbers}")


if __name__ == "__main__":
    main()
