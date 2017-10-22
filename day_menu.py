#!/usr/bin/env python
#-*- coding: utf-8 -*-

print("Today's menu").upper()

day_menu = {}

while True:
    food = raw_input("Please enter a dish: ")
    price = raw_input("Please enter a price: ")
    day_menu[food] = price  # saves food as key and price as it's value in day_menu as dictionary

    try:
        price = float(price.replace(",", "."))
    except Exception as e:
        price = raw_input("Please enter only a number. Enter a price: ") # Kako usmerim program na zgornji price - raw_input?.. Na tem spodnjem cele številke ne prikaže kot float.

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

# Kako urediti izpis po vrstnem redu vnosa?


