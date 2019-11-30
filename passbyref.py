#!/usr/bin/env python3

# Created by : Khang Le
# Created on : September 2019
# This use pass by Reference


def rounding(decimal, digit):

    decimal[0] = float(decimal[0])
    decimal[0] = decimal[0] * 10 ** digit
    decimal[0] = decimal[0] + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / 10 ** digit

    return decimal


def main():

    decimal = []
    user_decimal = float(input("Enter a decimal number: "))
    digit = int(input("Enter a number of how many "
                      "decimal place you want to round up: "))
    decimal.append(user_decimal)
    rounding(decimal, digit)
    print("The rounded number is: {}".format(decimal[0]))


if __name__ == "__main__":
    main()
