# cashier.py
class Cashier:
    """Handles money in/out and transaction validation."""

    def __init__(self):
        pass

    def process_coins(self) -> float:
        """Ask for coin counts and return the total inserted (rounded to cents)."""
        try:
            q = int(input("how many quarters?: "))
            d = int(input("how many dimes?: "))
            n = int(input("how many nickels?: "))
            p = int(input("how many pennies?: "))
        except ValueError:
            print("Invalid input. Treating missing/invalid entries as 0.")
            q = d = n = p = 0
        total = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p
        return round(total, 2)

    def transaction_result(self, coins: float, cost: float) -> bool:
        """
        Return True if payment accepted, else False.
        If accepted and change is due, print the change.
        """
        if coins < cost:
            print(f"Sorry that's not enough money. ${coins:.2f} refunded.")
            return False
        change = round(coins - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
