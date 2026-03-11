import sys


def main() -> None:

    args = sys.argv

    if len(args) == 1:
        print("No inventory items provided.")
        return

    inventory = dict()

    for item in args[1:]:
        parts = item.split(":")

        if len(parts) != 2:
            print(f"Invalid format: {item}")
            continue

        name = parts[0]

        try:
            quantity = int(parts[1])
        except ValueError:
            print(f"Invalid quantity for item: {item}")
            continue

        if quantity < 0:
            print(f"Invalid quantity for item: {item}")
            continue

        current_quantity = inventory.get(name, 0)
        inventory.update({name: current_quantity + quantity})

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    total_number_of_items = 0
    for value in inventory.values():
        total_number_of_items += value

    print("\n=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_number_of_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    displayed = dict()
    while len(displayed) < len(inventory):
        biggest_name = ""
        biggest_quantity = -1

        for name, quantity in inventory.items():
            if displayed.get(name) is None:
                if biggest_name == "" or quantity > biggest_quantity:
                    biggest_name = name
                    biggest_quantity = quantity

        displayed.update({biggest_name: biggest_quantity})
        percentage = (biggest_quantity * 100) / total_number_of_items
        print(f"{biggest_name}: {biggest_quantity} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")

    first = True
    most_item = ""
    least_item = ""
    max_value = 0
    min_value = 0

    for name, quantity in inventory.items():
        if first:
            most_item = name
            least_item = name
            max_value = quantity
            min_value = quantity
            first = False
        else:
            if quantity > max_value:
                max_value = quantity
                most_item = name
            if quantity < min_value:
                min_value = quantity
                least_item = name

    print(f"Most abundant: {most_item} ({max_value} units)")
    print(f"Least abundant: {least_item} ({min_value} units)")

    print("\n=== Item Categories ===")

    categories = {
        "Moderate": dict(),
        "Scarce": dict()
    }

    for name, quantity in inventory.items():
        if quantity >= 4:
            categories["Moderate"].update({name: quantity})
        else:
            categories["Scarce"].update({name: quantity})

    for key, value in categories.items():
        if len(value) > 0:
            print(f"{key}: {value}")

    print("\n=== Management Suggestions ===")

    restock_items = []
    for name, quantity in inventory.items():
        if quantity <= 1:
            restock_items.append(name)

    if len(restock_items) > 0:
        print("Restock needed:", ", ".join(restock_items))
    else:
        print("No restocking needed.")

    print("\n=== Dictionary Properties Demo ===")

    dictionary_keys = inventory.keys()
    print("Dictionary keys:", ", ".join(dictionary_keys))

    dictionary_values = inventory.values()
    print(
        "Dictionary values:",
        ", ".join(str(value)for value in dictionary_values))

    check_key = "sword"
    found = inventory.get(check_key)
    print(f"Sample lookup - '{check_key}' in inventory: {found is not None}")


if __name__ == "__main__":
    main()
