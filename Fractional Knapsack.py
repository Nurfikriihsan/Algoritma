def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    knapsack = []
    total_value = 0

    for item in items:
        if capacity >= item[0]:
            knapsack.append(item)
            total_value += item[1]
            capacity -= item[0]
        else:
            fraction = capacity / item[0]
            knapsack.append((item[0] * fraction, item[1] * fraction))
            total_value += item[1] * fraction
            break

    return knapsack, total_value

items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
capacity = 15
result, total = fractional_knapsack(items, capacity)
print("Barang yang dipilih:", result)
print("Total nilai yang diperoleh:", total)