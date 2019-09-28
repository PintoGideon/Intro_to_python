import pdb


def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        output_values.append(func(values[index]))
        index += 1

    return output_values


def addOne(val):
    return val+1


returned_values = map(addOne, [1, 2, 3, 4, 5])
print(returned_values)
