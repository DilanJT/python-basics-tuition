colors = ["blue", "red", "green"]

print(colors)

last_item_method_one = colors[len(colors) - 1]
last_item_method_two = colors[-1]

print("last item method one :", last_item_method_one)
print("last item method two :", last_item_method_two)


colors.append("purple")

colors.pop(0)

print(colors)