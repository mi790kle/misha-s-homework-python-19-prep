import random

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")
def print_slot_machine(symbols: list[str]) -> list[str]:
    machine = []
    for _ in range(3):
        machine.append(random.choice(symbols))
    return machine
def get_bet(money: int) -> int:
    while True:
        print("If you wish to stop type [s] or [stop]")
        try:
            bet = input("Enter your bet: ")
            if bet == "stop" or bet == "s":
                return 0
            bet = int(bet.strip())
        except:
            print("Please enter a number")
            continue
        if bet > money:
            print("Looks like you don't have enough money")
            continue
        if bet < 1:
            print("Playing with real money here, friend")
            continue
        return bet
def win_check(machine: list[str], symbols: list[str], rate: list[int], bet: int) -> int:
    if any(machine.count(symb) > 2 for symb in machine):
        print("3 of a kind!")
        index = rate[symbols.index(machine[0])]
        return index * 777 * bet
    elif any(machine.count(symb) > 1 for symb in machine):
        print("2 of a kind!")
        for symb in machine:
            if machine.count(symb) > 1:
                win_symbol = symb
        index = rate[symbols.index(win_symbol)]
        return index * bet
    else:
        print("Maybe next time")
        return 0
while True:
    print(f"Your money is {money}")
    bet = get_bet(money)
    if bet == 0:
        print("Good bye")
        break
    money = money - bet
    machine = print_slot_machine(symbols)
    print(machine)
    win = win_check(machine, symbols, rate, bet)
    money = money + win
    if money == 0:
        print("You're out of money, bye bye!")
        break
    continue