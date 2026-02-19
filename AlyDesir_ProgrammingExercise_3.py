import functools

def main():
    expenses = []
    print("--- Monthly Expense Tracker ---")
    print("Enter your expenses (type 'done' for the name to finish):")

    #While loop for user to input their expenses
    while True:
        name = input("Expense name: ").strip()
        if name.lower() == 'done':
            break

        try:
            amount = float(input(f"Amount for {name}: "))
            expenses.append({"name": name, "amount": amount})
        #Check for input errors
        except ValueError:
            print("Invalid amount. Please enter a number.")

    if not expenses:
        print("No expenses recorded.")
        return

    #Lambda functions to find total, highest expense, and lowest expense
    total = functools.reduce(lambda acc, x: acc + x['amount'], expenses, 0)

    highest = functools.reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses)

    lowest = functools.reduce(lambda a, b: a if a['amount'] < b['amount'] else b, expenses)

    #Print results
    print("\n--- Summary ---")
    print(f"Total Monthly Expenses: ${total:,.2f}")
    print(f"Highest Expense: {highest['name']} (${highest['amount']:,.2f})")
    print(f"Lowest Expense: {lowest['name']} (${lowest['amount']:,.2f})")


if __name__ == "__main__":
    main()