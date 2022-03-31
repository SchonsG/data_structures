def counter(values):
    if values == []:
        return 0
    else:
        return 1 + counter(values[1:])

values = [0, 1, 2, 3]

print(counter(values))

