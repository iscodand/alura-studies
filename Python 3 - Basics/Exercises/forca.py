from random import choice
from this import d


def initial_menu():
    print('*'*30)
    print('Bem vindo ao jogo da forca!')
    print('*'*30)


def choose_secret_word():
    words_list = []
    archive = open('words.txt', 'r')
    for lines in archive:
        words_list.append(lines.strip())
    archive.close()
    secret_word = choice(words_list).upper()
    return secret_word


def organize_correct_letters(letters):
    return ['_' for letter in letters]


def correct_shoot(shoot, letters, word):
    index = 0
    for letter in word:
        if letter == shoot:
            letters[index] = letter
        index += 1

def lose_message(word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def win_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def playForca():

    initial_menu()
    secret_word = choose_secret_word()

    correct_letters = organize_correct_letters(secret_word)
    print(f'{"  ".join(correct_letters)}')

    attemps = 0

    while True:
        shoot = str(input('\nInsira uma letra: ').upper().strip())

        if shoot in secret_word:
            correct_shoot(shoot, correct_letters, secret_word)
        else:
            attemps += 1
            print(f'\nVocê errou!!!\nCHANCES {attemps} de 6.\n')
            if attemps == 6:
                lose_message(secret_word)
                break

        print(f'{"  ".join(correct_letters)}')

        if '_' not in correct_letters:
            win_message()
            break

    print('\n---- FIM DE JOGO ----\n')


if (__name__ == "__main__"):
    playForca()
