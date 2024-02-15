class Stock:
    def __init__(self, name, num_shares, share_price):
        self.name = name
        self.num_shares = num_shares
        self.share_price = share_price

    def calculate_value(self):
        return self.num_shares * self.share_price


class StockPortfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def calculate_portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.calculate_value()
        return total_value

    def print_report(self):
        print("Stock Report:")
        for stock in self.stocks:
            print(f"Stock Name: {stock.name}")
            print(f"Number of Shares: {stock.num_shares}")
            print(f"Share Price: {stock.share_price}")
            print(f"Total Value: {stock.calculate_value()}")
            print()
        print(f"Total Portfolio Value: {self.calculate_portfolio_value()}")


if __name__ == "__main__":
    num_stocks = int(input("Enter the number of stocks: "))
    portfolio = StockPortfolio()

    for _ in range(num_stocks):
        name = input("Enter the stock name: ")
        num_shares = int(input("Enter the number of shares: "))
        share_price = float(input("Enter the share price: "))
        stock = Stock(name, num_shares, share_price)
        portfolio.add_stock(stock)

    portfolio.print_report()
