import random

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.job = ''
        self.credit = 0
        self.loan_amount = 0

    def __str__(self):
        return f"Name: {self.fname} {self.lname}\nAge: {self.age}\nJob: {self.job}\nCredit Score: {self.credit}\nRequested Loan Amount: ${self.loan_amount}"

    def set_job(self, job):
        self.job = job

    def set_credit_score(self, score):
        self.credit = score

    def set_loan_amount(self, amount):
        self.loan_amount = amount


class Game:
    def __init__(self, capital):
        self.capital = capital
        self.loans = []

    def get_capital(self):
        return self.capital

    def adjust_capital(self, amt):
        self.capital += amt

    def generate_customer(self):
        """Generates a random customer with a name, age, job, credit score, and loan amount."""
        first_names = ["Alex", "Taylor", "Jordan", "Morgan", "Casey"]
        last_names = ["Smith", "Johnson", "Lee", "Brown", "Garcia"]
        jobs = ["Teacher", "Engineer", "Artist", "Doctor", "Cashier"]

        fname = random.choice(first_names)
        lname = random.choice(last_names)
        age = random.randint(20, 65)
        job = random.choice(jobs)
        credit_score = random.randint(300, 850)
        loan_amount = random.randint(1000, 50000)

        customer = Person(fname, lname, age)
        customer.set_job(job)
        customer.set_credit_score(credit_score)
        customer.set_loan_amount(loan_amount)
        return customer

    def evaluate_loan(self, customer):
        """Evaluates whether a loan should be approved or denied based on customer data."""
        print("\n--- Customer Profile ---")
        print(customer)
        decision = input("Approve this loan? (yes/no): ").strip().lower()

        if decision == "yes":
            if customer.credit >= 600:
                profit = int(customer.loan_amount * 0.1)  # 10% profit if loan is approved
                self.adjust_capital(profit)
                print(f"Loan approved! You earned ${profit} in interest.")
                self.loans.append(customer)
            else:
                loss = customer.loan_amount
                self.adjust_capital(-loss)
                print(f"Loan approved, but defaulted! You lost ${loss}.")
        elif decision == "no":
            print("Loan denied. No change to capital.")
        else:
            print("Invalid input. Loan automatically denied.")

        print(f"Current capital: ${self.get_capital()}")

    def play(self):
        """Main game loop."""
        print("Welcome to the Bank Teller Game!")
        print(f"You start with ${self.capital} in capital.")
        print("Your goal is to approve or deny loans to grow your capital. Be careful!")
        print("Loans with a credit score below 600 are more likely to default.")

        while True:
            print("\n--- New Customer ---")
            customer = self.generate_customer()
            self.evaluate_loan(customer)

            # Check if the bank runs out of money
            if self.capital <= 0:
                print("\nYou ran out of capital! Game over!")
                break

            # Option to continue or quit
            play_on = input("Do you want to continue? (yes/no): ").strip().lower()
            if play_on != "yes":
                print(f"Game over! Final capital: ${self.get_capital()}")
                break


# Start the game
if __name__ == "__main__":
    initial_capital = 10000  # Starting capital
    game = Game(initial_capital)
    game.play()
