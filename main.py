import random

def Winner(playerNum, computerNum):
    gapPlayer = 21 - playerNum
    gapComputer = 21 - computerNum
    if gapPlayer < gapComputer:
        return "The player wins!"
    elif gapPlayer > gapComputer:
        return "The house wins!"
    else:
        return "Draw!"        


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to the blackjack game!")

#listas que armazenam quanto de numeros o jogador e o computador tem
computerCards = []
playerCards = []

#player card 1 & 2 acrescentadas na lista
playerCards.append(random.choice(cards))
playerCards.append(random.choice(cards))

#computer cad 1 & 2
computerCards.append(random.choice(cards))
computerCards.append(random.choice(cards))

#somatorio para armazenar os numeros iniciais
playerNumber = sum(playerCards)

if playerNumber == 21:
    print()

computerNumber = sum(computerCards)

#variavel flag para fazer repeticao
gameStillOn = True

#revela uma só carta da mesa, mas as duas do player
print(f"The table got: {computerCards[0]},...")
print(f"You got: {playerCards}, total: {playerNumber:.0f}")

if playerNumber == 21:
    print("Player BlackJack, the player wins!")
    gameStillOn = False
elif computerNumber == 21:
    print("Computer BlackJack, the table wins!")
    gameStillOn = False         

while gameStillOn == True:
    #pergunta para o jogador se ele vai querer mais cartas
    hitAnother = input("Do you want to get another card? (Y/N) ")

    #se a resposta for sim, vai ser adicionada mais uma carta para o player
    if hitAnother == 'y' or hitAnother == 'Y':
        playerCards.append(random.choice(cards))
        playerNumber = sum(playerCards)
    
    #imprime quantos pontos o player tem para manter ele atualizado
    print(f"You got: {playerCards}, total: {playerNumber:.0f}")

    #para o jogo caso o player ultrapasse 21 pontos
    if playerNumber > 21:
        print("Busted!")
        gameStillOn = False
    #Caso o player tenha exatos 21
    elif playerNumber == 21:
        print(f"21!!! you got {playerCards}, total: {playerNumber:.0f}")
        gameStillOn = False    

    #caso o player decida seguir em frente, o computador vai fazer jogadas 
    #nas regras, a casa só joga se tiver com 16 ou menos
    if hitAnother == 'N' or hitAnother == 'n':
        print(f"The table got: {computerCards}, total: {computerNumber}")
        
    if computerNumber <= 16:
            computerCards.append(random.choice(cards))
        #momento de comparar as pontuações e determinar o vencedor
        gameStillOn = False
        print(Winner(playerNumber,computerNumber))    
          

