class Vehicle:
    def __init__(self, type: str, model: str, price: int, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            result = f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            result = "Sorry, not enough money"
        elif self.owner is not None:
            result = "Car already sold"
        return result

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result = f"{self.model} {self.type} is on sale: {self.price}"
        return result


vehicle_type = "car"
vehicle_model = "BMW"
vehicle_price = 30000
vehicle = Vehicle(vehicle_type, vehicle_model, vehicle_price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)


