import adivinhacao
import forca


print('*'*30)
print('Escolha o seu jogo')
print('*'*30)

game = int(input('(1) Adivinhação (2) Forca'))
if (game == 1):
    print('Jogando Adivinhação!')
    adivinhacao.playAdivinhacao()
elif (game == 2):
    print('Jogando Forca')
    forca.playForca()
else:
    print('Opção Inválida')
