# Copyright (c) Ac industries All rights reserved
#
# Created by: Andrew Coxall
# Created on: May 21, 2020
# Cost of a pizza calculator

import constants


def main():
    diameter = int(input("Enter the diameter of the pizza you would" +
                         "like (inch): "))

    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
