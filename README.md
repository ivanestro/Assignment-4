## Using exception handling

As a Software Development Manager,

I want to ensure all programs are correct, accurate and use exception handling appropriately,

So that I can be assured of the quality of our software.

## Code Modification [#]
Added comments to help me understand the first pieces of codes.

Validation 1
In the Validation 1 process is to check if transaction type is either deposit or withdraw if is not a valid transaction 
Create an error message if valid transaction type record is invalid. Set the script to false. 

Validation 2 
In the Validation 2 process is to check if the transaction amount is valid. If the transaction amount number is greater than 0:

Collect Invalid Records 
else: if validation 1 and 2 transaction is found to be invalid. Error message that this is an invalid transaction. Storing our tuple in the transaction error. 
Rejected_Transaction.append will keep track of invalid transaction error to report. 
