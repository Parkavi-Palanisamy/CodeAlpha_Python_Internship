# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number.")

print("\n===== Your Portfolio =====")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\nTotal Investment: ${total_investment}")

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment}\n")

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")