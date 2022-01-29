def mysum(*args):
    for total in args:
        total += total

    return total


print(mysum(1, 3, 4))
