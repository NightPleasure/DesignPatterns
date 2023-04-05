class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def set_dough(self, dough):
        self.pizza.dough = dough

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese

    def add_toppings(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self):
        return self.pizza


class Pizza:
    def __init__(self):
        self.size = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return f"{self.size}-inch {self.dough} crust pizza with {self.sauce} sauce, {self.cheese} cheese, and {', '.join(self.toppings)}."

