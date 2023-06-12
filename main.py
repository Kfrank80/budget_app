from budget import Category
from budget import create_spend_chart

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cat = Category("")
    food = Category("food")
    food.deposit(1000, "Initial Deposit")
    food.withdraw(150, "To buy beams")
    food.withdraw(230, "To buy some rice")
    food.print_category()
    clothing = Category("clothing")
    clothing.deposit(2000, "Initial Deposit")
    clothing.withdraw(250, "Buying some t-shirts")
    clothing.withdraw(500, "Buying pants")
    clothing.print_category()
    cars = Category("car")
    cars.deposit(250000, "Initial Deposit")
    cars.withdraw(100000, "My son first car")
    cars.withdraw(120000, "Family car")
    cars.print_category()
    home = Category("home")
    home.deposit(20000, "Initial deposit")
    home.withdraw(500, "Living room decoration")
    home.withdraw(1400, "Utils for the kitchen")
    home.print_category()
    print(create_spend_chart([food, clothing, cars, home]))
pass
