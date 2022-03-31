def sum(values):
    if values == []:
        return 0
    else:
        return values[0] + sum(values[1:])

values = [2, 4, 6]

print(sum(values))

