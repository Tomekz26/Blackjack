import random

print("Welcome to 'TIC TAC TOE' game\nEach number corresponds to the square on the board.\nGood Luck !!!")
name1 = input("Player 1 name: ") or 'default 1'
name2 = input("Player 2 name: ") or 'default 2'
score = {f'{name1}': 0, f'{name2}': 0}
player1 = input(f'{name1}: O or X: ')
p1 = player1.upper()
while not (p1 == 'O' or p1 == 'X'):
    p1 = input('X or O:').upper()

p2 = ''
if p1 == 'X':
    p2 += 'O'
else:
     p2 += 'X'

print(f'\n{name1} is "{p1}", {name2} is "{p2}"\n')

f2 = ['0','1','2','3','4','5','6','7','8','9'] #plansza z numerami

def display_board(f1):
    print('\n   |   |' + '        ' + '   |   |')
    print(' ' + f1[7] + ' | ' + f1[8] + ' | ' + f1[9] + '      ' + ' ' + f2[7] + ' | ' + f2[8] + ' | ' + f2[9] )
    print('   |   |' + '        ' + '   |   |')
    print('-----------'+ '     ' + '-----------')
    print('   |   |' + '        ' + '   |   |')
    print(' ' + f1[4] + ' | ' + f1[5] + ' | ' + f1[6] + '      ' + ' ' + f2[4] + ' | ' + f2[5] + ' | ' + f2[6])
    print('   |   |' + '        ' + '   |   |')
    print('-----------'+ '     ' + '-----------')
    print('   |   |' + '        ' + '   |   |')
    print(' ' + f1[1] + ' | ' + f1[2] + ' | ' + f1[3] + '      ' + ' ' + f2[1] + ' | ' + f2[2] + ' | ' + f2[3])
    print('   |   |' + '        ' + '   |   |\n\n')

def playerinput():
    num1 =input('Input number corresponding to the square on the board: ')
    while not num1 in map(str, range(1,10)):
        num1 =input('Number from 1 to 9: ')
    num = int(num1)
    return num

def list_input(sym):
    x = playerinput()
    while True:
        if (f1[x] == 'X' or f1[x]=='O'):
            print('Square already taken')
            x = playerinput()
        else:
            f1[x] = sym
            break

def winning(sym):
    if f1[1:4] == [sym, sym, sym] or f1[4:7] == [sym, sym, sym] or f1[7:10] == [sym, sym, sym]:
        return True
    elif f1[1:10:3]== [sym, sym, sym] or f1[2:10:3]== [sym, sym, sym] or f1[3:10:3]== [sym, sym, sym]:
        return True
    elif f1[1:10:4]== [sym, sym, sym] or f1[3:9:2]== [sym, sym, sym]:
        return True

def game(player, name):
    print(f'{name}')
    list_input(player)
    display_board(f1)
    if not ' ' in f1:
        return False

    if winning(player) == True:
        print(f'{name} won')
        score[f'{name}'] += 1
        return False

def play_again():
    pa = input("next round ? y or n: ").upper()
    while not pa in ['Y', 'N']:
        pa = input("Yes or no ? y or n: ").upper()
    return pa

count = random.randint(1, 2)
while not score[f'{name1}'] == 3 or score[f'{name2}'] == 3:
    f1 = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(f1)

    while game:
        if count % 2 != 0:
            if game(p1, name1) == False:
                break
            if game(p2, name2) == False:
                break
        else:
            if game(p2, name2) == False:
                break
            if game(p1, name1) == False:
                break

    print(score)
    count += 1
    if play_again() == 'N':
        break




if score[f'{name1}'] > score[f'{name2}']:
    print(f'{name1} won the game')
elif score[f'{name1}'] == score[f'{name2}']:
    print("It's a tie")
else:
    print(f'{name2} won the game')

