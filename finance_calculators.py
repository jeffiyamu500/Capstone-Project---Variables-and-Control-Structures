import math
# Welcome to the Finance Calculators Program!
# This program allows user to access two different financial calculators to work out their investments
# or loan repayments

# Function to calculate simple interest. Simple interest is calculated by multiplying the
# principal amount by the interest rate and time
def calculate_simple_interest(principal, interest_rate, years):
    # Simple interest calculation
    interest = principal * (interest_rate / 100) * years
    return round(interest, 2)

# Function to calculate compound interest. Compound interest is calculated using the formula A = P (1 + r/n)^nt
# 'A' is the final value of your savings/costs
# 'P' is the principal amount
# 'r' is the annual interest rate
# 'n' is the amount of times that interest is compounded per unit t
# 't' is the number of years the money is invested or loaned for
def calculate_compound_interest(principal, interest_rate, years):
    # Compound interest calculation
    interest = principal * (math.pow(1 + interest_rate / 100, years) - 1)
    return round(interest, 2)

# Function to calculate bond repayment. The formula used to calculate bond repayment is (i * P)/(1 - (1 + i)**(n))
# 'P' is the current value of the house
# 'i' is the monthly interest rate 
# 'n' is the numer of months it will take for the bond to be repaid
def calculate_bond_repayment(present_value, annual_interest_rate, months):
    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # Monthly repayment calculation
    if monthly_interest_rate > 0:
        monthly_repayment = (present_value * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -months))
        return round(monthly_repayment, 2)
    else:
        return present_value / months

# Function to manage investment calculations
def investment_calculator():
    print("\nInvestment Calculator")

    # Get input for investment calculator
    # Casting method will be used here to convert string into a float in order for the program to run efficiently
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate (%): "))
    years = int(input("Enter the number of years: "))
    
    # Ask user to enter type of interest they want to use, either 'simple' interest or 'compound' interest
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == 'simple':
        result = calculate_simple_interest(principal, interest_rate, years)
        print(f"\nThe amount you'll get back after {years} years at {interest_rate}% simple interest is: {result}")
    # This message will be displayed if user enters 'simple'

    elif interest_type == 'compound':
        result = calculate_compound_interest(principal, interest_rate, years)
        print(f"\nThe amount you'll get back after {years} years at {interest_rate}% compound interest is: {result}")
    # This message will be displayed if user enters 'compound'

    else:
        print("Invalid input for interest type. Please enter 'simple' or 'compound'.")
    # An error message like this will be displayed if user enters anything other than 'simple' or 'compound'

# Function to manage bond calculations
def bond_calculator():
    print("\nBond Calculator")

    # Get input for bond calculator
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    months = int(input("Enter the number of months for bond repayment: "))

    # Ask for the bond repayment calculator function
    result = calculate_bond_repayment(present_value, interest_rate, months)
    print(f"\nThe monthly repayment amount is: {result}")

# Main program. User will be met with the message "Welcome to the Financial Calculators program!"
# Using print() function, each of the following messages will be displayed
def main():
    print("Welcome to the Financial Calculators program!")
    print("Enter 'investment' to calculate the amount of interest you'll earn on your investment.")
    print("Enter 'bond' to calculate the amount you'll have to pay on a home loan.")

# Carry out the calculations based on user choice. if-elif-else statement as well as logical operator will be used here
# in order for the program to run efficiently. User must enter either 'investment' or 'bond'
    valid_choices = ['investment', 'bond']

    while True:
        choice = input("Enter your choice from the menu above to proceed: ").lower()

        if choice == 'investment' or choice == 'bond':
            if choice == 'investment':
                investment_calculator()

            elif choice == 'bond':
                bond_calculator()

            break  # exit the loop if a valid choice is made

        else:
            print("Invalid input. Please enter either 'investment' or 'bond'.")

# Execute main function if script is run directly. The main() function holds the main logic of the entire program
# including the welcoming section, the user entries, and the calculations
if __name__ == "__main__":
    main()