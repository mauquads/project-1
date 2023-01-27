def calculate_stocks(marketplace):
    stocks = {}
    for item in marketplace:
        if item.stock_quantity > 0:
            stocks[item.name] = item.stock_quantity
    return stocks

class Item:
    def __init__(self, name, stock_quantity):
        self.name = name
        self.stock_quantity = stock_quantity

marketplace = [Item("item1", 10), Item("item2", 0), Item("item3", 5)]
print(calculate_stocks(marketplace))
