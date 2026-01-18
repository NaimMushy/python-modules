import sys


def get_total(inventory: dict) -> int:
    """
    Returns
    -------
    int
        The inventory's total item count.
    """
    total: int = 0
    for quantity in inventory.values():
        total += quantity
    return total


def system_analysis(inventory: dict) -> None:
    """
    Displays information about the inventory.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
    print("=== Inventory System Analysis ===")
    print(f"total items in inventory: {get_total(inventory)}")
    print(f"unique items types: {len(inventory)}\n")


def current_inventory(inventory: dict) -> None:
    """
    Displays every item in the inventory.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
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
    """
    Displays the inventory's statistics.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
    print("\n=== Inventory Statistics ===")
    max_item: str = max(inventory, key=inventory.get)
    print(f"most abundant: {max_item} ({inventory[max_item]} units)")
    min_item: str = min(inventory, key=inventory.get)
    print(f"least abundant: {min_item} ({inventory[min_item]} units)\n")


def item_categories(inventory: dict) -> None:
    """
    Organizes inventory items in categories and displays them.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
    print("=== Item Categories ===")
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
        print(f"{categories}: {items}")


def management_sugg(inventory: dict) -> None:
    """
    Displays some management suggestions about restocking items.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    min_quantity: int = max(inventory.values())
    for item in inventory.keys():
        if inventory[item] == min_quantity:
            restock.append(item)
    print(f"restock needed: {restock}\n")


def dict_prop_demo(inventory: dict, sample_item: str) -> None:
    """
    Displays a demonstration of the inventory properties.

    Parameters
    ----------
    inventory
        A dictionary which represents an item inventory.
    """
    print("=== Dictionary Properties Demo ===")
    print(f"dictionary keys: {inventory.keys()}")
    print(f"dictionary values: {inventory.values()}")
    print(
        f"sample lookup - '{sample_item}' in inventory: "
        f"{sample_item in inventory}"
    )


def main() -> None:
    """
    Manages an inventory and displays its data.
    """
    if len(sys.argv) == 1:
        print("inventory empty.")
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
