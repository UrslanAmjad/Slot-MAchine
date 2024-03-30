import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3
SYMBOL = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}
VALUE = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(columns, lines, bet, value):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += value[symbol] * bet
            winning_line.append(line + 1)

    return winning , winning_line




def deposit():
    while True:
        amount = input("Please Enter Amount you would like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount Must be greater than 0")
        else:
            print("Please Enter a Number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Please Enter Number of lines You want to bet on (1-" + str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= 3:
                break
            else:
                print("Please enter valid number of lines")
        else:
            print("Please enter a Number")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please Enter Amount Between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please Enter a number")

    return bet

def get_slot_machine_spins(rows , cols , symbols):
    all_symbols = []
    for symbol , symbol_count in SYMBOL.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row],  end = "")

        print()


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet on, Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines , so your total bet = ${total_bet}")

    slot = get_slot_machine_spins(ROWS, COLS, SYMBOL)
    print_slot_machine(slot)
    winning, winning_line = check_winnings(slot, lines, bet, VALUE)
    print(f"You won $ {winning} on:", *winning_line, )

    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spim = input("Press enter to spin ( q to quit): ")
        if spim == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")







main()

