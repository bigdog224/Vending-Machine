vending_key = {"A1" : ("Coca-Cola", 2.25), "A2" : ("Sprite", 2.25), "A3" : ("Fanta", 2.25), 
                    "A4" : ("Powerade", 2.00), "A5" : ("Lemonade", 2.00), "A6" : ("Root Beer", 2.25), 
                    "A7" : ("Apple Juice", 1.75), "A8" : ("Gatorade", 2.00), "A9" : ("Iced Tea", 1.75), 
                    "A10" : ("Water", 1.50)}

def main():


    # prints drinks and code for drinks
    print(
    '''
Welcome to my Virtual Vending Machine! Find the drink you'd like and input the code!\n
\033[4mDrink        | Code\033[0m
Coca-Cola    | A1
Sprite       | A2
Fanta        | A3
Powerade     | A4
Lemonade     | A5
Root Beer    | A6
Apple Juice  | A7
Gatorade     | A8
Iced Tea     | A9
Water        | A10

    '''
    )
    pick = input("What beverage would you like? ").strip()

    # program runs if accepted input is given
    if pick in vending_key:
        global drink
        drink = vending_key[pick][0] #accessing values in dict, use brackets
        price = vending_key[pick][1]

        print("Amount due: $", price)
        payment(price)

    else:
        print("That's not an option, please select a valid drink\n")
        return main()


def payment(due):
    sum = 0 # variable to track total amount paid
    ori = due # stores original price of drink

    # prompts user to continue inputting coins until drink is paid off
    while due > 0:
        coin = float(input("Amount Inputted: $"))

        # accepts US standardized values (1, 5, 10 and 25 cents and $1 and $5)
        if coin == .01 or coin == .05 or coin == .1 or coin == .25 or coin == 1.00 or coin == 5.00 or coin == 10.00 or coin == 20.00:
            due -= coin
            sum += coin
            if due > 0:
                print("Amount Due: $" + str(round(due,2)))

        else:
            print("Please input a valid payment amount. ")
         
    # returns total change to be given to user
    if due <= 0:
        ch = round(abs(sum-ori),2)
        print("Thank you! Enjoy your " + str(drink) +  "!")
        print("Change: $" + str(ch))


main()