"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "COMP-1327 (265263) Ivan Estropigan"
__version__ = "2025/03/09"

#Importing csv and os 
import csv  #csv reads the data file of our directory 
import os #os is to clear the terminal, track valid transactions, reject records. 
 
valid_transaction_types = ['deposit', 'withdraw'] # Creating a transaction type either deposit or withdraw
customer_data = {} # Storing customer data 
rejected_transactions = [] # reject transaction if it does not align with record transaction.
transaction_count = 0  # Valid Transaction count.
transaction_counter = 0 # Transaction counter is valid or invalid.
total_transaction_amount = 0 # The accumiliative 
is_valid_record = True # If Current Transaction is valid or not 
error_message = '' # A string holds error messages relating to invalid transaction.
transaction_amount = 0 


# Clears the terminal to create a readable console. 
os.system('cls' if os.name == 'nt' else 'clear')

# Get the directory the script is saved to locate our csv file within our directory folder. 
SCRIPT_DIRECTORY = os.path.dirname(__file__)

# The name of the data file in our directory.
DATA_FILENAME = "bank_data.csv"

# The absolute path to the data file bank_data.csv
DATA_FILE_PATH = f"{SCRIPT_DIRECTORY}/{DATA_FILENAME}"

with open(DATA_FILE_PATH, 'r') as csv_file: # locates the bank_data.csv
    reader = csv.reader(csv_file) # Opens it as read mode.

    # Skip heading line examples Customer ID, Transaction Type, Amount.
    next(reader)

    # Read each transaction for each row.
    for transaction in reader:
        # Reset valid record and error message for each iteration
        is_valid_record = True
        error_message = ''

        # Gets the customer ID from the first column
        customer_id = transaction[0]
        
        # Gets the transaction type from the second column
        transaction_type = transaction[1]

        ### VALIDATION 1 ###
        if transaction_type not in valid_transaction_types: #Checking if transaction type is not in valid transaction.
            is_valid_record = False # If it is not in valid record set valid record to false 
            error_message = f"Not a valid transaction type {transaction_type}" # Error message saying "This valid record is invalid."

        ### VALIDATION 2 ###
        # Gets the transaction amount from the third column
        try:
            transaction_amount = float(transaction[2])
        except ValueError:
            is_valid_record = False
            error_message = f"{transaction[2]} Not a valid transaction type."
        
        if transaction_amount <= 0: 
            is_valid_record = False 
            error_message = f"Error Message Validation 2"


        if is_valid_record:
            # Initialize the customer's account balance if it doesn't 
            # already exist
            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}
            # Update the customer's account balance based on the 
            # transaction type
            elif transaction_type == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            elif transaction_type == 'withdrawal':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            
            # Record transactions in the customer's transaction history
            customer_data[customer_id]['transactions'].append(
                (transaction_amount, transaction_type)
                )
        
        ### COLLECT INVALID RECORDS ###
        else: 
            error_message 
            transaction_error = transaction,error_message
            rejected_transactions.append(transaction_error)



report_title = "PiXELL River Transaction Report"
print(report_title)
print('=' * len(report_title))

# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"Customer {customer_id} has a balance of {balance}.")
    
    # Print the transaction history for the customer
    print("Transaction History:")

    for rejected_transaction in data['transactions']:
        amount, type = rejected_transaction
        print(f"{type.capitalize():>16}:{amount:>12}")
try:
    average_transaction_amount = total_transaction_amount / transaction_counter 
    print(f"AVERAGE TRANSACTION AMOUNT: {average_transaction_amount}")
except ZeroDivisionError as exception: 
    print("COLLECT INVALID RECORDS") 
rejected_report_title = "REJECTED RECORDS"
print(rejected_report_title)
print('=' * len(rejected_report_title))

for rejected_transaction in rejected_transactions:
    print("REJECTED:", rejected_transaction)
