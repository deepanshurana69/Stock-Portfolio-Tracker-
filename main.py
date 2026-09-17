STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00
}


def display_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")


def get_positive_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            return quantity
        except ValueError:
            print("Please enter a whole number.")


def track_portfolio():
    portfolio = {}

    print("\n=== CodeAlpha Stock Portfolio Tracker ===")
    display_stocks()

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Stock not found in the available list.")
            continue

        quantity = get_positive_quantity()
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("\nNo stocks were added.")
        return

    print("\n=== Portfolio Summary ===")
    total_value = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        print(f"{symbol}: {quantity} shares × ${price:.2f} = ${value:.2f}")

    print(f"\nTotal Investment Value: ${total_value:.2f}")

    save = input("Save the result to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("CodeAlpha Stock Portfolio Tracker\n")
            file.write("=" * 35 + "\n")
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = price * quantity
                file.write(
                    f"{symbol}: {quantity} shares × ${price:.2f} = ${value:.2f}\n"
                )
            file.write(f"\nTotal Investment Value: ${total_value:.2f}\n")
        print("Portfolio saved to portfolio.txt")


if __name__ == "__main__":
    track_portfolio()
