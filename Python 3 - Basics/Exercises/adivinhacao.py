from random import randint

def playAdivinhacao():
    print('*'*30)
    print('Bem vindo ao jogo de adivinhação!')
    print('*'*30)

    number = randint(1, 100)
    attemps = 0
    pontuation = 1000
    total_shoots = 0

    print('\nNível de dificuldade:')
    print('(1) Fácil (2) Médio (3) Difícil')
    difficult = int(input('Insira o nível de dificuldade: '))

    if (difficult == 1):
        attemps = 15
    elif (difficult == 2):
        attemps = 10
    else:
        attemps = 5

    for round in range(1, attemps + 1):
        print(f'\nRodada {round} de {attemps}.')
        shoot = int(input('Insira um número: '))

        correct = shoot == number
        higher = shoot > number
        lower = shoot < number

        if (shoot < 1 or shoot > 100):
            print('Insira um número entre 1 e 100.')
            continue

        if correct:
            print('Você acertou!\n')
            break
        else:
            attemps -= 1
            if higher:
                print('Você errou! Seu chute foi muito alto.')
            elif lower:
                print('Você errou! Seu chute foi muito baixo.')
        if (attemps == 0):
            break

        total_shoots += shoot

        attemps += 1

    pontuation = pontuation - (total_shoots)
    if pontuation < 0:
        pontuation = 0

    print(f'\nSua pontuação foi: {pontuation}')
    print(f'O número secreto era {number}.\n')


if (__name__ == "__main__"):
    playAdivinhacao()