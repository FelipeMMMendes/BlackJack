import random

def Winner(playerNum, computerNum):
    #funcao que calcula o vencedor do jogo, recebendo as pontuacoes de cada jogador
    gapPlayer = abs(21 - playerNum)
    gapComputer = abs(21 - computerNum)
    gapPlayer = abs(gapPlayer)
    gapComputer = abs(gapComputer)

    if gapPlayer < gapComputer:
        return "The player wins!"
    elif gapPlayer > gapComputer:
        return "The house wins!"
    elif gapPlayer == gapComputer:
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
computerNumber = sum(computerCards)

#variavel flag para fazer repeticao
playerTurn = True
computerTurn = True

#revela uma só carta da mesa e duas do player
print(f"The table got: {computerCards[0]},...")
print(f"You got: {playerCards}, total: {playerNumber:.0f}")

if playerNumber == 21:
    print("Player BlackJack, the player wins!")
    playerTurn = False
elif computerNumber == 21:
    print("Computer BlackJack, the table wins!")
    playerTurn = False         

while playerTurn == True:
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
        print("Busted! The house wins!")
        playerTurn = False
        exit()
    #Caso o player tenha exatos 21
    elif playerNumber == 21:
        print(f"21!!! you got {playerCards}, total: {playerNumber:.0f}")
        playerTurn = False    

    #caso o player decida seguir em frente, o computador vai fazer jogadas 
    #nas regras, a casa só joga se tiver com 16 ou menos
    if hitAnother == 'N' or hitAnother == 'n':
        print(f"The table got: {computerCards}, total: {computerNumber}")
        playerTurn = False 
        computerTurn = True

#agora passa para o turno do computador
while computerTurn == True:
    if computerNumber <= 16:
        computerCards.append(random.choice(cards))
        computerNumber = sum(computerCards)
        print(f"The table received another card: {computerCards}, total: {computerNumber}")
    elif computerNumber >= 17:
        computerTurn = False
        if computerNumber > 21:
            print("The house busted!")
            exit()

if computerTurn==False and playerTurn==False:
    print(Winner(playerNumber,computerNumber))    
    #momento de comparar as pontuações e determinar o vencedor
