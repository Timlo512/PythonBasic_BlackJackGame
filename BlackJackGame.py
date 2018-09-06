# BlackJack Game

#Bankroll class - set an account for player
class bankroll():
    def __init__(self,owner,account=100):
        self.owner = owner
        self.account = account

    def __str__(self):
        return(f"Account owner: {self.owner}\nAccount balance: ${self.account}")

    def gain(self,gain_amount):
        self.account += gain_amount
        return(self.account)

    def betting(self,bet_amount):
        if bet_amount <= self.account:
            self.account -= bet_amount
            return(self.account)
        else:
            print("Sorry you are bankrupt. Enjoy the next game")

# Card - define the point of each card representing
class cards():
    def __init__(self,number,suit):
        self.suit = suit
        self.number = number
        if str(self.number).isdigit():
            self.point = int(self.number)
        elif self.number == "Ace":
            self.point = (1,11)
        else:
            self.point = 10

    def __str__(self):
        return(f"Cards: {self.number} {self.suit}")

# Deck - define a deck in which card is randomly ordered
class deck():
    '''
    Each instance in this class should return a attribute, cards_list, which contains
    52 playing cards in random order
    '''
    
    def __init__(self):
        import random
        number_list = ('Ace',2,3,4,5,6,7,8,9,10,'jack','queen','king')
        suit_list = ('diamonds','clubs','hearts','spades')
        cards_list = []
        for suit in suit_list:
            for num in number_list:
                cards_list.append(cards(num,suit))
        random.shuffle(cards_list)
        self.cards_list = cards_list

    '''
    Every time a deck has to deliver a card to game table, a function, deliver_card should
    be called and then return a playing card
    ''' 
    def deliver_card(self):
        if self.cards_list != []:
            new_cards_list = self.cards_list
            return(new_cards_list.pop(0))
            self.cards_list = new_cards_list
        else:
            print('There arent any cards in the deck, sorry!')
            return(False)
    """
    print the deck
    """
    def __str__(self):
        deck_comp = ''
        for each in self.cards_list:
            deck_comp += '\n' + each.__str__()
        return(deck_comp)
        

# ask whether the player to continue the game
def asking():
    inquiry = input("Do u want to start the game? Y/N ").upper()
    global check
    if inquiry == "Y":
        check = True
    elif inquiry == "N":
        check = False
    else:
        print('Sorry, please answer again.')
        asking()

# inputting player name
def name():
    check = True
    while(check):
        player_name = input('What is your name? ')
        if player_name =='':
            print("Sorry, please type again.")
        else:
            check = False
            return(player_name)

# game_table - shows the cards on game table
def table(show):
    print(f'Bankroll on table: {game_table.account}')
    print("Computer dealer's hands: \n")
    if show == False:
        for each in computer_cards:
            if computer_cards.index(each) == 1:
                print('      covered')
            else:
                print(f'      {each}')
    else:
        for each in computer_cards:
            print(f'      {each}')
    print('\n')
    computer_point = point_table(show,"Computer")
    if type(computer_point) == tuple:
        print(f"Points: {computer_point[0]} or {computer_point[1]}")
    else:
        print(f"Points: {computer_point}")
    print(f"{player.owner}'s hands: \n")
    for each in player_cards:
        print(f'      {each}')
    print('\n')
    player_point = point_table(show,"Player")
    if type(player_point) == tuple:
        print(f"Points: {player_point[0]} or {player_point[1]}")
    else:
        print(f"Points: {player_point}")
        
#point_table - shows the total on game table (need refinement)
def point_table(show,side):
    result1 = 0
    result2 = 0
    if side == "Computer": 
        if show == False:
            for each in computer_cards:
                if computer_cards.index(each) == 1:
                    continue
                else:
                    if each.number == "Ace":
                        result1 += each.point[0]
                        result2 += each.point[1]
                    else:
                        result1 += each.point
                        result2 += each.point
        else:
            for each in computer_cards:
                if each.number == "Ace":
                    result1 += each.point[0]
                    result2 += each.point[1]
                else:
                    result1 += each.point
                    result2 += each.point
    else:
        for each in player_cards:
            if each.number == "Ace":
                result1 += each.point[0]
                result2 += each.point[1]
            else:
                result1 += each.point
                result2 += each.point
    if show == False:
        if result2 != result1 and result2 <21:
            return((result1,result2))
        elif result2 == 21:
            return(result2)
        else:
            return(result1)
    else:
        if result2 != result1 and result2 <21:
            return(max(result1,result2))
        elif result2 == 21:
            return(result2)
        else:
            return(result1)
            
        
# clear output
import os
def clear():
    os.system("clear")
  
# player chooses whether he stand or hit
def player_choice(cards,deck):
    while(True):
        global choice
        choice = input("Do you want to stay or hit? Either h or s").lower()
        if choice[0] == "h":
            cards.append(deck.deliver_card())
            break
        elif choice[0] == 's':
            break
        else: 
            print("Sorry, please decide whether stand or hit.")
            
# player picks their betting amount
def betting_amount():
    while(True):
        try:
            betting = int(input('How much do you want to bet? '))
        except:
            print("Sorry, please fill in the correct amount.")
        else:
            if betting >= 10:
                if betting > player.account:
                    print("Sorry, you don't have enough bankroll in your account.")
                else:
                    player.betting(betting)
                    game_table.gain(betting)
                    break
            else:
                print("Sorry, please at least bet $10")

# computer dealer chooses whether it should hit
def computer_choice():
    global show
    player_point = point_table(show,"Player")
    computer_point = point_table(True,"Computer")
    if type(player_point) == tuple:
        if type(computer_point) == tuple:
            if (player_point[0]<=21 or player_point[1]<=21) and (computer_point[0]<16 or computer_point[1]<16):
                computer_cards.append(deck01.deliver_card())
                print("Computer dealer's hit card")
            else:
                pass
        else:
            if (player_point[0]<=21 or player_point[1]<=21) and computer_point<16:
                computer_cards.append(deck01.deliver_card())
                print("Computer dealer's hit card")
            else:
                pass
    else:
        if type(computer_point) == tuple:
            if player_point<=21 and (computer_point[0]<16 or computer[1]<16):
                computer_cards.append(deck01.deliver_card())
                print("Computer dealer's hit card")
            else:
                pass
        else:
            if player_point<=21 and computer_point<16:
                computer_cards.append(deck01.deliver_card())
                print("Computer dealer's hit card")

# determine whether player or computer wins
def judgement():
    global show,check
    player_point = point_table(show,"Player")
    computer_point = point_table(True,"Computer")
    
    def player_wins():
        print(f"\nCongratulation {player.owner}!! You have won the game.\n")
        player.gain((game_table.account)*2)
        computer.betting((game_table.account)*2)
        game_table.betting(game_table.account)

    def player_bust():
        print(f"\nSorry {player.owner}...your hand busts.\n")
        computer.gain(game_table.account)
        game_table.betting(game_table.account)

    def computer_wins():
        print(f"\nSorry {player.owner}...you have lost the game.\n")
        computer.gain(game_table.account)
        game_table.betting(game_table.account)
    
    def computer_bust():
        print(f"\nCongratulation {player.owner}!! Computer dealer's hand busts.\n")
        player.gain((game_table.account)*2)
        computer.betting((game_table.account)*2)
        game_table.betting(game_table.account)
        
    def tied():
        print("\nTied, you can get back your money.\n")
        player.gain(game_table.account)
        game_table.betting(game_table.account)

    if type(player_point) == tuple:
        player_point = player_point[1] 
    else:
        pass
    
    if type(computer_point) == tuple:
        computer_point = computer_point[1]
    else:
        pass

    if player_point <= 21 and computer_point <= 21 and choice[0] == "s":
        if player_point > computer_point:
            player_wins()
            show,check = True,False
        elif player_point == computer_point:
            tied()
            show,check = True,False
        else:
            computer_wins()
            show,check = True,False
    else:
        pass
        
    if len(computer_cards) == 5 and len(player_cards) == 5:
        tied()
        show,check = True,False
    else:
        pass

    if player_point == 21 and computer_point < 21:
        player_wins()
        show,check = True,False
    elif player_point <21 and computer_point == 21:
        computer_wins()
        show,check = True, False
    elif player_point == 21 and computer_point == 21:
        tied()
        show,check = True, False

    
    if player_point > 21 and computer_point > 21:
        tied()
        show,check = True, False
    elif player_point > 21:
        player_bust()
        show,check = True,False
    elif computer_point > 21:
        computer_bust()
        show,check = True,False
    else:
        pass
    
# restart button
def restart():
    global check
    if player.account >0:
        while(True):
            restart_the_game = input("Do you want to have another game? Y/N").upper()
            if restart_the_game == 'Y':
                check = True
                break
            elif restart_the_game == 'N':
                print('Have a nice day, good luck! Bye~')
                break
            else:
                print('Sorry, please answer Y/N.')
    else:
        print('Have a nice day, good luck! Bye~')
    

# Run the game, using while loop
clear()
print(f"Welcome to Blackjack game!")
player = bankroll(name())
computer = bankroll("Computer",10e10)
check = True
print(f"Welcome! {player.owner}")
print(f"{player} \n")
asking()
while(check):
    game_table = bankroll('Game Table',0)
    deck01 = deck()
    show = False
    betting_amount()
    turn,choice = "player",'hit'
    clear()
    computer_cards = [deck01.deliver_card(),deck01.deliver_card()]
    player_cards = [deck01.deliver_card(),deck01.deliver_card()]
    judgement()
    table(show)
    while(check):
        if turn == "player":
            player_choice(player_cards,deck01)
            clear()
            #table(show)
            #input("please press enter to continue...")
            turn = "computer"
        else:
            computer_choice()
            clear()
            judgement()
            table(show)
            input("Computer dealer's have completed its turn, please press enter to continue...")
            turn = "player"
    print(f"\n{player}\n")
    restart()





