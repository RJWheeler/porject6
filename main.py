
class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = "-Vegetarian-"
        print(f"Pizza {self.name} : ${self.price} " + veg_str)
        print(", ".join(self.ingredients))
        print()


class CustomPizza(Pizza):
    BASE_PRICE = 5
    PRICE_PER_INGREDIENT = .75
    last_number = 0

    def __init__(self, ):
        CustomPizza.last_number += 1
        self.pizza_num = CustomPizza.last_number
        super().__init__("Custom " +str(self.pizza_num), 0, [])
        self.ask_user_for_ingredient()
        self.compute_price()

    def ask_user_for_ingredient(self):
        print()
        print(f"Ingredients for pizza number {self.pizza_num}")
        while True:
            ingredient = input("Add an ingredient (or press ENTER to finish): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def compute_price(self):
        self.price = self.BASE_PRICE + len(self.ingredients) * self.PRICE_PER_INGREDIENT


def pizza_sort(e):
    return len(e.ingredients)


pizzas = [
    Pizza("4 cheese", 8.99, ("blue cheese", "brie", "emmental", "mozarella"), True),
    Pizza("Pepparoni", 7.99, ("pepparoni", "mozarella")),
    Pizza("Meat lover's", 10.99, ("pepparoni", "sausage", "bacon", "ham", "chicken")),
    Pizza("Veggie delight", 10.99, ("green peppers", "black olives", "onions"), True),
]

while True:
    add_pizza = input("Add a Custom pizza? ")
    if add_pizza == "no" or add_pizza == "":
        break
    pizzas.append(CustomPizza())

# pizzas.sort(key=pizza_sort)


for i in pizzas:
    i.display()