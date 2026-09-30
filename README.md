# Cafe Food Ordering System
I have created a Cafe Ordering System. It is a program that can be run through a terminal, which you can use to order food from. It applies discount based on the order amount. 

## What it does
- Enters name and phone number of customer
- Displays menu
- Lets customer choose items that they would like to order
- Calculates the total amount and applies discount based on the amount
- Displays the order summary/bill 

## Files
- main.py - the main file
- data.py - stores the menu inside a nested dictionary
- customer.py - lets customer enter their details
- menu.py - displays the menu
- order.py - lets the customer order items 
- validation.py - checks if the entered customer name, phone number, quantity of items, item ID are valid or not
- billing.py - calculates the bill and displays the order summary

## How to run
1. Install python 3 and check it with ```python --version```
2. Open a terminal in this folder and run: ```python main.py```
3. Enter your name and phone number. Then enter the IDs of the food items that you'd like to order.

## How to test
To test it, run the the main program and enter the details that are prompted: 
1) Do not enter a name when prompted and click enter to check if it's valid or not
2) Enter an invalid phone number(length of phone number less than 10 or phone number contains characters) to check if it gets rejected or not
3) Enter an invalid order ID(order ID is not a digit or not in the menu) to check if it gets rejected or not
4) Enter valid inputs to generate the bill.
