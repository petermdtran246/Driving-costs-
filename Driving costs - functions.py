def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon


if __name__ == '__main__':
    miles = float(input())
    dollars = float(input())

    cost_10_miles = driving_cost(miles, dollars, 10)
    cost_50_miles = driving_cost(miles, dollars, 50)
    cost_400_miles = driving_cost(miles, dollars, 400)

    print(f'{cost_10_miles:.2f}')
    print(f'{cost_50_miles:.2f}')
    print(f'{cost_400_miles:.2f}')





