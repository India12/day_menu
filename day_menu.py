#!/usr/bin/env python
#-*- coding: utf-8 -*-

import collections

print("Today's menu").upper()

day_menu = collections.OrderedDict() # An OrderedDict considers the order the items were added

while True:
    food = raw_input("Please enter a dish: ")

    while True:
        price = raw_input("Please enter a price: ")

        try:
            price = float(price.replace(",", "."))
        except Exception as e:
            continue
        else:
            day_menu[food] = price  # saves food as key and price as its value in day_menu as dictionary
            break

    new = raw_input("Would you like to enter another dish? (y/n) ").lower()

    if new == "n" or new == "no":
        break

with open("day_menu.txt", "w+") as day_menu_file:
    i = 1
    day_menu_file.write("TODAY'S MENU: \n")
    for food in day_menu:
        if day_menu[food]:
            print (str(i) + ". " + food)
            print ("price: " + str(day_menu[food]) + " €")
            i += 1
            day_menu_file.write(str(i-1) + ". " + food + ",  price: " + str(day_menu[food]) + " €" + "\n")
