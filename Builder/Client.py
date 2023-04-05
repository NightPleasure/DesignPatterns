from AdCreator import PizzaBuilder

pizza_builder = PizzaBuilder()
pizza_builder.set_size(12)
pizza_builder.set_dough("thin")
pizza_builder.set_sauce("tomato")
pizza_builder.set_cheese("mozzarella")
pizza_builder.add_toppings("pepperoni")
pizza_builder.add_toppings("mushrooms")
pizza = pizza_builder.get_pizza()
print(pizza)
