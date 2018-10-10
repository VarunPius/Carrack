import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    '''
    :return=> boolean: value indicating if won or lost
    '''

    roll = random.randint(1,100)

    if roll == 100:
        #print(roll, "You lose")
        return False
    elif roll<=50:
        #print(roll, "Roll between 1 to 50. You lose")
        return False
    else:
        #print(roll, "You win")
        return True

def simple_bettor(funds: int, initial_wager: int, wager_count: int):
    '''
    :param funds: Initial amount to begin with
    :param initial_wager: bet amount for each round
    :param wager_count: number of bets
    :return=> void
    '''
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value+=wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -=wager
            wX.append(currentWager)
            vY.append(value)
        #print("Funds:", value)
        currentWager+=1

    plt.plot(wX, vY)

def main():
    x = 0       # x here is number of people betting.
    while x <=10:
        simple_bettor(10000, 100, 100000)
        #print(x)
        x+=1

    plt.xlabel("Bet Count")
    plt.ylabel("Value")
    plt.show()
    # Plot saved as Figure_1.png. Plot shows that our current approach is not perfect as over large bets, we are losing money.

if __name__ == '__main__':
    main()
