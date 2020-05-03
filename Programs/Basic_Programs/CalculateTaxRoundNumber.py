def solve(meal_cost, tip_percent, tax_percent):
    cost = meal_cost * (1 + (tip_percent + tax_percent) / 100.0)
    total_cost = round(cost)
    print(total_cost)


if __name__ == '__main__':
    meal_cost = float(input("Enter Meal cost: "))

    tip_percent = int(input("Enter tip: "))

    tax_percent = int(input("Enter tax: "))

    solve(meal_cost, tip_percent, tax_percent)
