import random, sys

HEARDS = chr(9829)
DIAMONDS = chr(9829)
SPADER = chr(9829)
CLUBS = chr(9829)
BACKSIDE = "beckside"


def main():
    print("Blackjack")

    money = 5000
    while True:
        if money < 0:
            print("You're broke!")
            print("Thanks for playing")
            sys.exit()
        print(f"Money: {money}")
        bet = getBet(money)  # Ставка

        deck = getDeck()  # Колода
        dealerHand = [deck.pop(), deck.pop()]  # по две карты из колоды
        playerHand = [deck.pop(), deck.pop()]  # по две карты из колоды

        print(f"Bet: {bet}")
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Bet increased to {bet}.")
                print(f"Bet: {bet}")
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ("S", "D"):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits....")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)  # Печать кары

                if getHandValue(dealerHand) > 21:
                    break
                input("Press Enter to continue....")
                print("\n\n")

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        print(11111111)
        if dealerValue > 21:
            print(f"Dealer busts! You win ${bet}")
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif (playerValue > dealerValue):
            print(f"You won ${bet}")
            money += bet
        elif (playerValue == dealerValue):
            print(f"It's a tie, the bet is returned to you.")

        input("Press Enter to continue....")
        print("\n\n")


def getBet(maxBet):  # Ставка
    while True:
        print(f"How much do you bet? (1-{maxBet} or QUIT).")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing")
            sys.exit()
        if not bet.isdecimal():  # в строке нет чисел
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():  # Формирует колоду и перемешивает ее
    deck = []
    for suit in (HEARDS, DIAMONDS, SPADER, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):  # Печать схематически карты
    print()
    if showDealerHand:
        print(f"DEALER: {getHandValue(dealerHand)}")  # Подсчет очков у диллера
        displayCards(dealerHand)  # Отображение карт
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print(f"PLAYER: {getHandValue(playerHand)}")
    displayCards(playerHand)


def getHandValue(cards):  # Считаем стоимость карт
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 < 21:
            value += 10
    return value


def displayCards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += " ___  "
        if card == BACKSIDE:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "
            for row in rows:
                print(row)


def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tand"]

        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        movePrompt = f"{', '.join(moves)}> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()
