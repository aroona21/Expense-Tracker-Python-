


# Expense Tracker 

total = 0.0  
expense_count = 0 

print("Welcome to the Expense Tracker!")
print("Type 'quit' to stop and see your total.")
print("------------------------------------------")


        
while True:
    user_input=input(" Enter expense amount: ")
    if user_input.lower () == "quit": 
        break

    try:
        expense = float(user_input)  
        if expense <=0:
            print(" Please enter a positive amount!")
            continue
        total += expense
        expense_count += 1
        print(f"Added! Running total: ${total:.2f}")  

    except ValueError:
        print("Invalid input! Please enter a number.")

print("------------------------------------------")
print(f"Total Spent: ${total:.2f}")  
if expense_count > 0:
    print(f"Number of expenses: {expense_count}")
    print(f"Average expense: ${total/expense_count:.2f}")