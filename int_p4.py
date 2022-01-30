def hex_output():
    decnum = 0
    hexnum = input("Enter the hexdec number")
    for power, digit in enumerate(hexnum):
        decnum += int(digit, 16)
        print(f"value of decnum {decnum}")


hex_output()
