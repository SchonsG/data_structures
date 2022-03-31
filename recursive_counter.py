def counter(values, count=0):
    if len(values) == 0:
        return count
    else:
        values.pop()
        count += 1
        return counter(values, count)

values = [0, 1, 2, 3]

print(counter(values))

