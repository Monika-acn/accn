print("PIN authentication enabled")

balance = 5000

def check_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amt = int(input("Enter deposit amount: "))
    balance += amt
    print("Deposit successful")


def withdraw():
    global balance
    amt = int(input("Enter withdraw amount: "))
    if amt <= balance:
        balance -= amt
        print("Please collect cash")
    else:
        print("Insufficient balance")

while True:
    print("\n1.Check Balance  2.Deposit  3.Withdraw  4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you")
        break
    else:
        print("Invalid choice")
        PIN = "1234"


