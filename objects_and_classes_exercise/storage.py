class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > len(self.storage):
            self.storage.append(product)

    def get_products(self):
        return self.storage


store = Storage(4)
store.add_product("apple")
store.add_product("banana")
store.add_product("potato")
store.add_product("tomato")
store.add_product("bread")
print(store.get_products())
