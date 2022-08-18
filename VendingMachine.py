def main():
    
    pick = input("What beverage would you like?\n\n   \033[4mDrink | Price\033[0m\n 1. Coke | $1.25\n 2. Sprite | $1.25\n 3. Gatorade | $2.00\n 4. Iced Tea | $1.50\n 5. Water | $1.00\n Choice: ")

    # program runs if accepted input is given
    if pick == "1" or pick == "2" or pick == "3" or pick == "4" or pick == "5":
        price = selection(pick)
        print("Amount due: ", price)
        print("Insert 5, 10, or 25 cents in decimal value format (Ex: 25 cents --> 0.25)")
        payment(float(price))

    else:
        print("That's not an option, please select a valid input\n")
        return main()
        

# Returns appropiate drink and drink price given user input
def selection(x):
    if x == "1":
        print("\nDrink: Coke")
        return "1.25"
    elif x == "2":
        print("\nDrink: Sprite")
        return "1.25"
    elif x == "3":
        print("\nDrink: Gatorade")
        return "2.00"
    elif x == "4":
        print("\nDrink: Iced Tea")
        return "1.50"
    elif x == "5":
        print("\nDrink: Water")
        return "1.00"





def payment(due):
    sum = 0 # variable to track total amount paid
    ori = due # stores original price of drink

    # prompts user to continue inputting coins until drink is paid off
    while due > 0:
        coin = float(input("Coin Inserted: "))

        # only accepts 5, 10 or 25 cents
        if coin == .05 or coin == .1 or coin == .25:
            due -= coin
            sum += coin
            if due > 0:
                print("Amount Due:", round(due,2))

        else:
            print("Please input a valid coin amount. ")
         
    # returns total change to be given to user
    if due <= 0:
        ch = abs(sum-ori)
        print("Thank you! Enjoy your drink!\nChange: ", round(ch,2))




main()