class Stock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class StockManager:
    _instance = None

    @staticmethod
    def get_instance():
        if StockManager._instance is None:
            StockManager._instance = StockManager()
            StockManager._instance.stock_data = []
        return StockManager._instance

    def add_stock(self, stock):
        self.stock_data.append(stock)

    def remove_stock(self, stock):
        self.stock_data.remove(stock)

    def get_stock(self, name):
        for stock in self.stock_data:
            if stock.name == name:
                return stock
        return None
