import random

deck1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = deck1 * 8
player_hand = []
computer_hand = []
player_name = input("Input player name: ")


class Money:
    def __init__(self, name, balance, bet = 0, insur = 0):
        self.name = name
        self.balance = balance
        self.bet = bet
        self.insur = insur

    def betting(self,):
        while True:
            try:
                money = int(input("How much you want to bet: "))
            except:
                print("Numbers only!")
            else:
                if money > self.balance:
                    print(f"You only have {self.balance} ")
                else:
                    self.balance -= money
                    self.bet += money
                    print(f'Your current balance is {self.balance}')
                    print(f'Current bet is {self.bet}')
                    break

    def win(self, money):
        self.balance += money
        print(f'{money} added to your balance')
        print(f'Your current balance is {self.balance}')

    def insurance(self):
        insur = input("Do you want insurance? y or n: ").upper()
        while insur not in ['Y', 'N']:
            insur = input("Yes or no ? y or n: ").upper()
        if insur == 'Y':
            self.insur += self.bet / 2
            print(f"{self.insur} added to insurance")


class Deck:
    def __init__(self, player, deck, score = 0):
        self.deck = deck
        self.player = player
        self.score = score

    def card_name(self):
        sel_card = random.choice(self.deck)
        deck.remove(sel_card)
        self.player.append(sel_card)
        try:
            card = int(self.player[-1])
        except:
            if self.player[-1] == 'A':
                card = 11
            else:
                card = 10
        finally:
            self.score += card
            if len(computer_hand) >= 2:
                print(f'\n{player_name}:', user_deck.score, '\n', ('[' + "] [".join([str(x) for x in player_hand]) + ']'), '\n')
                print(' [X]', '[' + "] [".join([str(x) for x in computer_hand[1:]]) + ']', '\nComputer\n')

class Win_Check:
    def __init__(self, user_score, computer_score):
        self.user_score = user_score
        self.computer_score = computer_score

    def check(self):
        if self.user_score > 21 and 'A' not in player_hand:
            return False
        elif self.computer_score > 21 and 'A' not in computer_hand:
            return True
        elif self.user_score > 31 and 'A' in player_hand:
            return False
        elif self.computer_score > 31 and 'A' in computer_hand:
            return True
        elif self.computer_score > self.user_score:
            return False
        else:
            return True

    def ace(self,score):
        if score < 21 and 'A' not in player_hand:
            return True
        elif score < 31 and 'A' in player_hand:
            return True
        else:
            return False


def double_bet():
    sec_bet = input("Do you want to double the bet? y or n: ").upper()
    while sec_bet not in ['Y', 'N']:
        sec_bet = input("Yes or no ? y or n: ").upper()
    return sec_bet


def another_card():
    next_card = input("Do you want next card? y or n: ").upper()
    while next_card not in ['Y', 'N']:
        next_card = input("Yes or no ? y or n: ").upper()
    return next_card


def play_again():
    play = input("next round ? y or n: ").upper()
    while play not in ['Y', 'N']:
        play = input("Yes or no ? y or n: ").upper()
    return play


user_money = Money(player_name, 300)
user_deck = Deck(player_hand, deck)
computer_deck = Deck(computer_hand, deck)

while user_money.balance > 0:
    if len(deck) < 10:
        for crd in deck1:
            deck.append(crd)
    print("\nYour balance is:", user_money.balance)
    user_money.betting()
    user_deck.card_name()
    computer_deck.card_name()
    user_deck.card_name()
    computer_deck.card_name()
    user_money.insurance()
    win = Win_Check(user_deck.score, computer_deck.score)
    if double_bet() == 'Y' and user_deck.score != 21:
        user_money.bet *= 2
        print(f"Current bet is {user_money.bet}")
        user_deck.card_name()
        while computer_deck.score < 17 and win.ace(user_deck.score) == True:
            computer_deck.card_name()
        if computer_deck.score == user_deck.score:
            user_money.bet /= 2

    else:
        while win.ace(user_deck.score) == True:
            x = another_card()
            if x == 'Y':
                user_deck.card_name()
                if computer_deck.score < 17 and win.ace(user_deck.score)== True:
                    computer_deck.card_name()
            else:
                while computer_deck.score < 17 and win.ace(user_deck.score) == True:
                    computer_deck.card_name()

            if x == 'N':
                while computer_deck.score < 17 and win.ace(user_deck.score) == True:
                    computer_deck.card_name()
                break
            if computer_deck.score > 17 and win.ace(user_deck.score) == False:
                break

    if (21 < user_deck.score <= 31) and 'A' in player_hand:
        user_deck.score -= 10
    if (21 < computer_deck.score <= 31) and 'A' in computer_hand:
        computer_deck.score -= 10

    print("\nFinal score:")
    print(f'{player_name}:', user_deck.score, '\n', '[' + "] [".join([str(x) for x in player_hand]) + ']')
    print(' [' + "] [".join([str(x) for x in computer_hand]) + ']', '\n' "Computer:", computer_deck.score, )

    win = Win_Check(user_deck.score, computer_deck.score)
    if computer_deck.score == user_deck.score:
        print("\nIt's a tie !")
        user_money.win(user_money.bet)
    elif win.check() == True:
        print("\nYou won !")
        if user_deck.score == 21 and len(player_hand) == 2:
            user_money.win(user_money.bet * 3)
        else:
            user_money.win(user_money.bet * 2)
    else:
        print("\nYou lost !")

    if 'A' in computer_hand and computer_deck.score == 21 and len(computer_hand) == 2 and user_deck.score != 21:
        if user_money.insur != 0:
            print("You got your insurance back")
            user_money.win(user_money.insur * 2)

    player_hand.clear()
    computer_hand.clear()
    user_deck.score = 0
    computer_deck.score = 0
    user_money.bet = 0
    if play_again() == 'N':
        break

if user_money.balance > 0:
    print(f"You won {user_money.balance}")
else:
    print('You lost, no money left')


