import collections

class BankAccount:
    def __init__(self, account_number, username, balance):
        self.account_number = account_number
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"{self.username} (Acc: {self.account_number}) - Balance: {self.balance}"

accounts = []
transaction_history = []
bill_queue = collections.deque()
account_requests = collections.deque()

def handle_transaction(action_type):
    name = input("Enter username: ")
    for acc in accounts:
        if acc.username.lower() == name.lower():
            amt = float(input("Enter amount: "))
            if action_type == "deposit":
                acc.balance += amt
                transaction_history.append(f"Deposit {amt} to {name}")
            else:
                acc.balance -= amt
                transaction_history.append(f"Withdraw {amt} from {name}")
            print(f"Success! New balance: {acc.balance}")
            return
    print("User not found!")

def bank_menu():
    print("\n1. Submit Account Request\n2. Deposit\n3. Withdraw\n4. Bill Payment\n5. Undo Last Action")
    opt = input("Choice: ")
    if opt == "1":
        name = input("Enter your name: ")
        account_requests.append(BankAccount("Pending", name, 0))
        print("Request added to queue.")
    elif opt == "2":
        handle_transaction("deposit")
    elif opt == "3":
        handle_transaction("withdraw")
    elif opt == "4":
        bill_name = input("Enter bill name (e.g. Internet): ")
        bill_queue.append(f"{bill_name} Bill")
        print("Bill added to queue.")
    elif opt == "5":
        if transaction_history:
            removed = transaction_history.pop()
            print(f"Undo: {removed} removed")
        else:
            print("History is empty.")

def admin_menu():
    print("\n1. Process Account Request\n2. Process Bill Payment\n3. View All Accounts")
    opt = input("Choice: ")
    if opt == "1" and account_requests:
        new_acc = account_requests.popleft()
        new_acc.account_number = f"PY-{100 + len(accounts)}"
        accounts.append(new_acc)
        print(f"Processed: {new_acc.username} is now a client.")
    elif opt == "2" and bill_queue:
        print(f"Processing: {bill_queue.popleft()}")
    elif opt == "3":
        for acc in accounts:
            print(acc)
    else:
        print("Nothing to process or list is empty.")

def main():
    initial_data = [
        BankAccount("101", "Ali", 150000),
        BankAccount("102", "Sara", 220000),
        BankAccount("103", "Diyar", 50000)
    ]
    accounts.extend(initial_data)

    while True:
        print("\n--- MINI BANKING SYSTEM ---")
        print("1 - Enter Bank\n2 - Admin Area\n3 - Exit")
        choice = input("Select: ")
        if choice == "3":
            break
        elif choice == "1":
            bank_menu()
        elif choice == "2":
            admin_menu()
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()