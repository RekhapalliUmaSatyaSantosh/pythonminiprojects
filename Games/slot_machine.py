import random

max_lines=3
min_bet=300
max_bet=3000

rows=3
cols=3

symbols_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

symbols_values={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns       


def solt_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!=len(columns)-1:
                print(col[row],end="|")
            else:
                print(col[row],end=" ")
        print()

def get_winning(col, lines, bet, values):
    winning = 0
    winning_lines = []

    for line in range(lines):
        symbol = col[0][line]

        for column in col:
            if symbol != column[line]:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines



def deposit():
    while True:
        try:
            amount=int(input("Enter Money to Deposite= ₹"))
            if amount>0:
                break
            else:
                print("Amount must be greater than Zero(0).")
        except:
            print("Please Enter a Valid Amount.")
    return amount


def no_lines():
    while True:
        try:
            lines=int(input(f"Enter Number of Lines between 1 - {max_lines}= "))
            if 1<=lines<=max_lines:
                break
            else:
                print(f"Lines must be between 1 and {max_lines}.")
        except:
            print("Please Enter a Valid Lines.")
    return lines


def get_bet():
    while True:
        try:
            bet=int(input("Enter Money to Bet= ₹"))
            if bet>0:
                break
            else:
                print("Amount must be greater than Zero(0).")
        except:
            print("Please Enter a Valid Amount.")
    return bet


def spin(balance):
    lines=no_lines()
    while True:
        bet=get_bet()
        
        total_bet=bet*lines
        if total_bet>balance:
            print("Insufficient to Bet.")
        else:
            break    
    print(f"You are betting ₹{bet} on {lines} lines, and total amount is ₹{total_bet}")
    solts=get_slot_machine(rows,cols,symbols_count)
    solt_machine(solts)
    winnings, winning_lines = get_winning(solts, lines, bet, symbols_values)
    print(f"You Won: ₹{winnings}")
    print("You Won on line:", *winning_lines)

    return winnings - total_bet

def main():
    balance=deposit()
    while True:
        if balance <= 0:
            print("Your balance is ₹0. Game over!")
            break
        print(f'Current balance= ₹{balance}')
        again=input('Press enter to play (q to quit)= ').lower()
        if again=='q':
            break
        balance+=spin(balance)
    print(f"You left with ${balance}")
main()
        
