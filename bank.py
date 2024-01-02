

accounts = {}

def create_account(name, money):
    if name in accounts.keys():
        accounts[name] += money
    else:
        accounts[name] = money

def deposit(acct_name, amt):
    if acct_name in accounts.keys():
        accounts[acct_name] += amt
    else:
        print(f"Account {acct_name} does not exist")

def withdraw(acct_name, amt):
    if acct_name in accounts.keys():
        accounts[acct_name] -= amt
    else:
        print(f"Account {acct_name} does not exist")

def check_money(acct_name):
    if acct_name in accounts.keys():
        return accounts[acct_name]
    else:
        print("Account does not exist")

def help():
    print("ca, d, w, cm, h")

def run():
    while True:
        user_input = input("Please enter a command (ca, d, w, cm, h)")

        match(user_input):
            case "ca":
                name = input("Please enter a name")
                money = int(input("Please enter an initial deposit"))
                create_account(name, money)
            case "d":
                name = input("Please enter a name")
                money = int(input("Please enter an amount to deposit"))
                deposit(name, money)
            case "w":
                name = input("Please enter a name")
                money = int(input("Please enter an amount to withdraw"))
                withdraw(name, money)
            case "cm":
                name = input("Please enter a name")
                print(check_money(name))
            case "h":
                help()

if __name__ == '__main__':
    # This is the main method, our code starts here.
    run()