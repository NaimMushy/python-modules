import sys


def get_total(inventory: dict) -> int:
    return sum(quantity for quantity in inventory.values())


def system_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {get_total(inventory)}")
    print(f"Unique items types: {len(inventory)}\n")


def current_inventory(inventory: dict) -> None:
    print("=== Current Inventory ===")
    sorted_inventory: dict = {}
    max_quantity: int = max(inventory.values())
    min_quantity: int = min(inventory.values())
    while max_quantity >= min_quantity:
        for item, quantity in inventory.items():
            if quantity == max_quantity:
                sorted_inventory[item] = quantity
        max_quantity -= 1
    for it, quant in sorted_inventory.items():
        print(
            f"{it}: {quant} units "
            f"({round(quant * 100 / get_total(sorted_inventory), 1)}%)"
        )


def inventory_stats(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    inventory["max_item"] = {
        key: val for key, val in inventory.items()
        if val == max(inventory.values())
    }
    print("Most abundant:", end="")
    for key, val in inventory["max_item"].items():
        print(
            f" {key} ({val} "
            f"{'units' if val > 1 else 'unit'})", end=""
        )
    del inventory["max_item"]
    inventory["min_item"] = {
        key: val for key, val in inventory.items()
        if val == min(inventory.values())
    }
    print("\nLeast abundant:", end="")
    for key, val in inventory["min_item"].items():
        print(
            f" {key} ({val} "
            f"{'units' if val > 1 else 'unit'})", end=""
        )
    print("")
    del inventory["min_item"]


def item_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    item_categories: dict = {}
    for item, quantity in inventory.items():
        if quantity <= 3:
            if "scarce" not in item_categories:
                item_categories["scarce"] = {}
            item_categories["scarce"][item] = quantity
        elif quantity <= 9:
            if "moderate" not in item_categories:
                item_categories["moderate"] = {}
            item_categories["moderate"][item] = quantity
        else:
            if "plentiful" not in item_categories:
                item_categories["plentiful"] = {}
            item_categories["plentiful"][item] = quantity
    for categories, items in item_categories.items():
        print(f"{categories.capitalize()}: {items}")


def management_sugg(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")
    restock: list[str] = [
        item for item, quantity in inventory.items()
        if quantity == min(inventory.values())
    ]
    print(f"Restock needed: {restock}\n")


def dict_prop_demo(inventory: dict, sample_item: str) -> None:
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {[key for key in inventory.keys()]}")
    print(f"Dictionary values: {[val for val in inventory.values()]}")
    print(
        f"Sample lookup - '{sample_item}' in inventory: "
        f"{sample_item in inventory}"
    )


def main() -> None:
    if len(sys.argv) == 1:
        print(
            "Inventory empty - "
            "Usage: python3 ft_inventory_system.py "
            "<item1:quantity1> <item2:quantity2> ..."
        )
    else:
        inventory: dict = {}
        for item in range(1, len(sys.argv)):
            dict_item: list[str] = sys.argv[item].split(":")
            if dict_item[0] in inventory:
                if int(dict_item[1]) > 0:
                    inventory[dict_item[0]] += int(dict_item[1])
            else:
                if int(dict_item[1]) > 0:
                    inventory[dict_item[0]] = int(dict_item[1])
        system_analysis(inventory)
        current_inventory(inventory)
        inventory_stats(inventory)
        item_categories(inventory)
        management_sugg(inventory)
        dict_prop_demo(inventory, "sword")


if __name__ == "__main__":
    main()
