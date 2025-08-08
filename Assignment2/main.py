# main.py
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def print_report():
    print("Resources report:")
    for item, qty in resources.items():
        unit = "slices" if item in ("bread", "ham") else "oz"
        print(f"  {item}: {qty} {unit}")

def main():
    print("Welcome to the Ham Sandwich Maker Machine!")
    print("Commands: small / medium / large / report / off")
    while True:
        choice = input("What would you like? (small/medium/large): ").strip().lower()

        if choice == "off":
            print("Shutting down. Bye!")
            break
        if choice == "report":
            print_report()
            continue

        if choice not in recipes:
            print("Sorry, I didn't get that. Try: small, medium, large, report, or off.")
            continue

        order = recipes[choice]
        ingredients = order["ingredients"]
        cost = float(order["cost"])

        if not sandwich_maker_instance.check_resources(ingredients):
            continue

        print(f"That will be ${cost:.2f}. Please insert coins.")
        coins = cashier_instance.process_coins()
        if not cashier_instance.transaction_result(coins, cost):
            continue

        sandwich_maker_instance.make_sandwich(choice, ingredients)

if __name__ == "__main__":
    main()
