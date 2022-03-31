def sum(values):
    if len(values) == 0:
        return 0
    else:
        return values.pop(0) + sum(values)

values = [2, 4, 6]

print(sum(values))

