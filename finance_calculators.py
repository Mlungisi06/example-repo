
import math


# Initialize to prevent errors
duration = 0

print('Welcome to Mlungisi financial calculator program.')
print('Choose either "investment" or "bond" from the menu below to proceed:')


calculator_choice = input('Enter your choice here: ').lower()

if calculator_choice == 'investment':
    
    principal_amount = float(input('Enter the amount you are depositing: '))
    annual_interest_rate = float(input('Enter interest rate (percentage) %: '))
    duration = int(input('Enter the number of years: ')) 
    interest_type = input('Enter "simple" or "compound": ').lower()
    
    r = annual_interest_rate / 100
    
    if interest_type == 'simple':
        total_amount = principal_amount * (1 + r * duration)
    elif interest_type == 'compound':
        total_amount = principal_amount * math.pow((1 + r), duration)
    else:
        print('Invalid interest type selected.')
        total_amount = None
        
    if total_amount is not None:
        print(f'The total amount after {duration} years is R: {total_amount:.2f}')
        year_str = str(duration)
        receipt_no = calculator_choice[:2] + year_str[:2]
        print(f"Transaction Successful. Receipt: {receipt_no}")


elif calculator_choice == 'bond':
    present_value_of_house = float(input('Enter the house value: '))
    annual_interest_rate = float(input('Enter the annual interest rate: '))
    duration = int(input('Enter the number of months: '))
    
    
    monthly_rate = (annual_interest_rate / 100) / 12
    power_calc = math.pow((1 + monthly_rate), -duration)
    monthly_repayment = (monthly_rate * present_value_of_house) / (1 - power_calc)
    
    print(f'The monthly repayment amount is R: {monthly_repayment:.2f}')
    
    year_str = str(duration)
    receipt_no = calculator_choice[:2] + year_str[:2]
    print(f"Transaction Successful. Receipt: {receipt_no}")

else:
    print('Invalid choice. Please choose either "investment" or "bond".')

print('Thank you for using Mlungisi financial calculator program.')