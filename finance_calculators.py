import math 
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

print("investment       - to calculate the amount of interest you'll earn on interest.")
print("bond             - to calculate the amount you'll have to pay on a home loan.")

# Ask the user what they chose
user_choice = input("What have you chosen ? ")

# If the user chose bond the if statement will execute
if user_choice.lower() == "bond":
 
    # variables that store the users input
    house_value = float(input("Please enter the present value of your house: "))

    interest = float(input("Please enter the interest: "))

    repay_duration = float(input("Please enter the number of months you plan to take to repay the bond: "))

    # This variable Stores the monthly interest rate 
    monthly_interest_rate = float(interest / 12)

    # This formula calculates the how much the user has to pay per month
    repayment = x = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-repay_duration)) 

    print(round(repayment))

# This elif statement executes if the user chooses investment
elif user_choice.lower() == "investment":

    # Variables storing Data related to the user
    amount_depositing = float(input("Please indicate the amount of money you are depositing: "))

    interest_rate = float(input("At what interest rate? "))

    investing_years = int(input("How many years do you plan on investing for? "))

    interest_type = input("Do you want to choose Compound interest or Simple interest? ").lower()

    final_interest = float(interest_rate / 100)

    # This if statemnt executes if the user chose compound interest
    if interest_type == "compound interest":

        # This formula calculates the compound interest
        answer = amount_depositing* math.pow((1 + final_interest), investing_years)
        print(round(answer))

    # This elif statemnet executes if the user chose simple interest
    elif interest_type == "simple interest":

        # This formula calculates the simple interest
        answer = amount_depositing* (1 + final_interest * investing_years)
        print(round(answer))

# If the user chooses an invalid option
# The error message will be printed
else:
    print("Invalid option.Please restart the program.")



    









