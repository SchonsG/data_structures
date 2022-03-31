def find_the_biggest(values):
    if len(values) == 2:
        return values[0] if values[0] > values[1] else values[1]

    sub_max = find_the_biggest(values[1:])
    print(sub_max)
    return values[0] if values[0] > sub_max else sub_max
        
values = [8, 4, 2, 7]

print(find_the_biggest(values))

