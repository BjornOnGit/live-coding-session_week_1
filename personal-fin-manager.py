class PersonalFinanceManager:
    def __init__(self):
        self.balance = 0.0
        
    def add_income(self, amount):
        self.balance += amount
        print(f"Income of {amount} added. New balance: {self.balance}")
        
    def add_expense(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Expense of {amount} deducted. New balance: {self.balance}")
        else:
            print("Insufficient balance!")
        
    def view_balance(self):
        print(f"Current balance: {self.balance}")

def finance_manager():
        manager = PersonalFinanceManager()
        
        while True:
            print("\nPersonal Finance Manager:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. Exit")
            
            choice = int(input("Choose an option (1-4): "))
            
            if choice == 1:
                amount = float(input("Enter income amount: "))
                manager.add_income(amount)
            elif choice == 2:
                amount = float(input("Enter expense amount: "))
                manager.add_expense(amount)
            elif choice == 3:
                manager.view_balance()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid option selected!")

finance_manager()