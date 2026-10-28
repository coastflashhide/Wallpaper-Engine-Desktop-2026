from dataclasses import dataclass


@dataclass
class Item:
    name: str
    rarity: str
    quantity: int
    price: float


class Inventory:
    RARITY_ORDER = {
        "Common": 1,
        "Uncommon": 2,
        "Rare": 3,
        "Epic": 4,
        "Legendary": 5,
    }

    def __init__(self):
        self.items = {}

    def add_item(self, name, rarity, quantity, price):
        if quantity <= 0 or price < 0:
            raise ValueError("Invalid quantity or price")

        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, rarity, quantity, price)

    def remove_item(self, name, quantity=1):
        item = self.items.get(name)

        if item is None or quantity <= 0 or item.quantity < quantity:
            return False

        item.quantity -= quantity

        if item.quantity == 0:
            del self.items[name]

        return True

    def total_value(self):
        return sum(
            item.quantity * item.price
            for item in self.items.values()
        )

    def show_inventory(self):
        print("Game Inventory")
        print("==============")

        sorted_items = sorted(
            self.items.values(),
            key=lambda item: (
                self.RARITY_ORDER.get(item.rarity, 0),
                item.name
            ),
            reverse=True,
        )

        for item in sorted_items:
            value = item.quantity * item.price
            print(
                f"{item.name} | {item.rarity} | "
                f"x{item.quantity} | ${value:.2f}"
            )

        print(f"\nUnique items: {len(self.items)}")
        print(f"Total value: ${self.total_value():.2f}")


inventory = Inventory()

inventory.add_item("Iron Sword", "Common", 2, 25)
inventory.add_item("Health Potion", "Uncommon", 5, 10)
inventory.add_item("Dragon Shield", "Epic", 1, 250)
inventory.add_item("Phoenix Blade", "Legendary", 1, 1200)
inventory.add_item("Magic Ring", "Rare", 3, 85)

inventory.remove_item("Health Potion", 2)

inventory.show_inventory()