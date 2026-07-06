def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    recursion(days_until_harvest)


def recursion(days_until_harvest):
    i = 0
    while days_until_harvest > 0:
        print(f"Day {i + 1}")
        days_until_harvest -= 1
        i += 1
    print("Harvest time!")
