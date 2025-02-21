class ATM:

    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.run()

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount. Please enter a positive integer.")

    def validate_pin(self, input_pin):
        return input_pin == self.__pin

    def verify_pin(self):
        if self.__pin is None:
            print("No PIN set. Please create a PIN first.")
            return False
        entered_pin = input("Enter your PIN: ")
        if self.validate_pin(entered_pin):
            return True
        else:
            print("Incorrect PIN.")
            return False

    def run(self):
        while True:
            self.show_menu()

    def show_menu(self):
        try:
            user_input = int(input("""
            Hello! Welcome to the ATM.
            Please choose an option:
            1. Create PIN
            2. Deposit Money
            3. Change PIN
            4. Check Balance
            5. Withdraw Money
            6. Exit
            Enter your choice: """))

            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit_money()
            elif user_input == 3:
                self.change_pin()
            elif user_input == 4:
                self.check_balance()
            elif user_input == 5:
                self.withdraw_money()
            elif user_input == 6:
                self.exit_program()
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def create_pin(self):
        if self.__pin is None:
            self.__pin = input("Enter your new PIN: ")
            print("Your PIN has been successfully created.")
        else:
            print("PIN already exists. Use 'Change PIN' to update it.")

    def deposit_money(self):
        if self.verify_pin():
            try:
                amount = int(input("Enter the amount to deposit: "))
                self.set_balance(amount)
                print(f"Successfully deposited {amount}.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def change_pin(self):
        if self.verify_pin():
            new_pin = input("Enter your new PIN: ")
            self.__pin = new_pin
            print("Your PIN has been successfully updated.")

    def check_balance(self):
        if self.verify_pin():
            print(f"Your current balance is: {self.get_balance()}")

    def withdraw_money(self):
        if self.verify_pin():
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= self.__balance:
                    self.__balance -= amount
                    print(f"Successfully withdrew {amount}.")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def exit_program(self):
        confirm = input("Are you sure you want to exit? (Y/N): ").upper()
        if confirm == 'Y':
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            print("Returning to the main menu.")

atm = ATM()
