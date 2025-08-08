# sandwich_maker.py
class SandwichMaker:
    """Handles inventory checks and actually making sandwiches."""

    def __init__(self, resources: dict):
        # Keep a *mutable* reference to the shared resource pool
        self.machine_resources = resources

    def check_resources(self, ingredients: dict) -> bool:
        """Return True if all required ingredients are available; otherwise print why and return False."""
        for item, required in ingredients.items():
            available = self.machine_resources.get(item, 0)
            if required > available:
                print(f"Sorry, not enough {item}. (Need {required}, have {available})")
                return False
        return True

    def make_sandwich(self, sandwich_size: str, order_ingredients: dict) -> None:
        """Deduct ingredients from resources and 'make' the sandwich."""
        for item, qty in order_ingredients.items():
            self.machine_resources[item] -= qty
        print(f"Here is your {sandwich_size} ham sandwich 🥪. Enjoy!")
