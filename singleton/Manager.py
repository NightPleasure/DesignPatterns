from CompanyStock import StockManager, Stock
# Crearea unei instanțe a clasei Singleton
stock_manager = StockManager()

# Adăugarea câtorva stocuri în instanța clasei Singleton
stock_manager.add_stock(Stock("Apple Inc.", 100, 150.0))
stock_manager.add_stock(Stock("Microsoft Corporation", 50, 200.0))
stock_manager.add_stock(Stock("Amazon.com, Inc.", 75, 300.0))

# Eliminarea unui stoc din instanța clasei Singleton
microsoft_stock = stock_manager.get_stock("Microsoft Corporation")
stock_manager.remove_stock(microsoft_stock)

# Afișarea informațiilor despre stocul rămas (fără Microsoft)
print("Informații stocuri:")
for stock in stock_manager.stock_data:
    print(stock.name, stock.quantity, stock.price)
