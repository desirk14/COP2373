class BankAcct:
    # Function to set up the account
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adj_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Add money to the account
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print('Deposit amount must be positive.')

    # Take money out of the account
    def withdraw(self, amount):
        if amount > self.amount:
            print('Insufficient funds.')
        elif amount <= 0:
            print('Withdrawal amount must be positive.')
        else:
            self.amount -= amount

    # Show the balance for the account
    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        #Use the Simple interest formula to calculate interest: A = P * r * t
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def __str__(self):
        return (f'Account Holder: {self.name}\n'
                f'Account Number: {self.account_number}\n'
                f'Balance: ${self.amount:.2f}\n'
                f'Interest Rate: {self.interest_rate * 100:.2f}%')


# Function to test the class
def test_bank_acct():
    # Create the new account
    acct = BankAcct('Aly Desir', '273489250', 1250.0, 0.03)

    print('Initial Account:')
    print(acct)
    print()

    # Deposit money
    acct.deposit(500)
    print('After depositing $500:')
    print(f'Balance: ${acct.get_balance():.2f}')
    print()

    # Withdraw money
    acct.withdraw(200)
    print("After withdrawing $200:")
    print(f"Balance: ${acct.get_balance():.2f}")
    print()

    # Change the interest rate
    acct.adj_interest_rate(0.04)
    print('After adjusting interest rate to 4%:')
    print(acct)
    print()

    # Calculate interest
    days = 30
    interest = acct.calculate_interest(days)
    print(f'Interest for {days} days: ${interest:.2f}')
    print()

#Run the test function
if __name__ == "__main__":
    test_bank_acct()