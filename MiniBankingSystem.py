names = ['Rahul','Anu','Vikram']
pins = [1234,5678,4321]
balances = [1000, 2000, 1500]
histories = [[],[],[]]

#creating an account
def create_account():
    name = str(input("Enter your name: "))
    pin = int(input('Enter your pin: '))
    balance = int(input('Enter your current balance: '))

    names.append(name)
    pins.append(pin)
    balances.append(balance)
    histories.append([])

#Logging in
def login():
    name = str(input('Enter your name: '))
    Password = 0
    RollNo = -1
    print('If your serial number is -1, then this means that you haven\'t registered to this bank account yet')
    for i in range(len(names)):
        if name == names[i]:
            RollNo = i
            while Password != pins[RollNo]:
                Password = int(input('Enter your pin: '))
                if Password == pins[RollNo]:
                    print('Welcome back')
                else:
                    print('Wrong pin\tPlease try again')
    return RollNo                

#Withdrawal
def withdrawal():
    money = int(input('How much money do you want to withdraw?: '))
    while money > balances[SNo]:
        print('Withdrawal amount was greater than the current amount of money you have\nPlease try again.')
        money = int(input('How much money do you want to withdraw?: '))
    balances[SNo] = balances[SNo] - money
    print('Thank you\nThe withdrawal was successful\nYour current balance is ',balances[SNo])
    histories[SNo].append('Withdrawal of '+str(money))

#Deposit
def deposit():
    money = int(input('How much money do you want to deposit?: '))
    balances[SNo] = balances[SNo] + money
    print('Thank you, your new balance is: ', balances[SNo])
    histories[SNo].append('Deposit of '+str(money))

#Checking the balance
def check_balance():
    print('Your current balance is: ',balances[SNo])

#Transferring Money
def transfer():
    name = str(input('Who do you want to give your money to?: '))
    recipient_found = False
    for i in range(len(names)):
        if name == names[i]:
            money = int(input('How much money do you want to give to him/her?: '))
            while money > balances[SNo]:
                print('Withdrawal amount was greater than the current amount of money you have\nPlease try again.')
                money = int(input('How much money do you want to give to him/her?: '))
            balances[SNo] = balances[SNo] - money
            balances[i] = balances[i] + money
            recipient_found = True
            print('Congratulations, youe current balance is ',balances[SNo],' and his/her current balance is ',balances[i])
            break
    if recipient_found:
        histories[SNo].append('Transfer of '+str(money)+' to '+names[i])
        histories[i].append('Received '+str(money)+' from '+names[SNo])
    else:
        print('Recipient not found')

#Distplaying transaction history
def transaction_history():
    print(histories[SNo])
    
create_account()
SNo = login()
check_balance()
withdrawal()
