import tkinter as tk
from tkinter import messagebox
import random
import poker_gamestate
from PIL import Image, ImageTk
import time

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit




class PokerGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("No-Limit Texas Hold'em")
        self.game_state = poker_gamestate.GameState()
        self.custom_font = ("Helvetica", 20, "bold")
        self.deck = [
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                ]
        self.new_deck = [
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                ]


        ###
        #   Image Resources
        ###
        self.player_display = Image.open("resources/player_bar.jpg")
        self.table = Image.open("resources/table.png")


        ###
        #  Load Resources
        ##
        self.player_display_img = ImageTk.PhotoImage(self.player_display)
        self.table_display = ImageTk.PhotoImage(self.table)
        ###
        #  Connect to root display
        ###

        self.game_display = tk.Frame(root, width=1080, height=720)
        self.poker_table = tk.Label(self.game_display, image=self.table_display, width= 1080, height=720)
        self.poker_table.pack()

        self.deal_player_card_button = tk.Button(self.game_display, width=50, height= 20, bg="black", command=self.fold)
        self.deal_player_card_button.pack()
        self.game_display.pack()

        self.deal_community_card = tk.Button(self.game_display, width=50, height= 20, bg="blue", command=self.update_community_cards)
        # self.deal_community_card.place(x=0, y=720)
        # self.game_display.pack()


        self.shuffle_button = tk.Button(self.game_display, width=50, height= 20, bg="green", command=self.bet)
        self.shuffle_button.place(x=600, y=720)

        self.gamestart = tk.Button(self.game_display, width=50, height= 20, bg="red", command=self.gameloop)
        self.gamestart.place(x=0, y=720)


        ###
        #  Handling card image and card label management for players, and community cards
        ###
        self.card_images = {}
        self.community_card_images = {}
        self.community_card_labels = []
        self.player_card_labels = []

    def bet(self):
        bet = 20

        if bet > self.game_state.player_stacks[self.game_state.betting_round % 6]:
            print(self.game_state.player_names[self.game_state.betting_round], "bet too large")
            return
        elif self.game_state.betting_round == self.game_state.NUM_PLAYERS:
            self.game_state.betting_round = 0
            PokerGameGUI.deal_community_cards(self)
            self.update_community_cards()
            return
        elif ((len(self.game_state.community_cards) == 5) and (self.game_state.betting_round + 1 == self.game_state.NUM_PLAYERS)):
            PokerGameGUI.gameloop(self)
            return
        else:
            self.game_state.pot_size += bet
            self.game_state.player_stacks[self.game_state.betting_round % 6] = self.game_state.player_stacks[self.game_state.betting_round % 6] - bet
            print(self.game_state.pot_size,  self.game_state.player_stacks[self.game_state.betting_round % 6], self.game_state.betting_round)
            self.game_state.betting_round += 1
            self.update_player_cards()
            return

    def check(self):
        if self.game_state.betting_round == self.game_state.NUM_PLAYERS:
            self.game_state.betting_round = 0
            PokerGameGUI.deal_community_cards(self)
            self.update_community_cards()
        elif ((len(self.game_state.community_cards) == 5) and (self.game_state.betting_round + 1 == self.game_state.NUM_PLAYERS)):
            PokerGameGUI.shuffle(self)
            PokerGameGUI.gameloop(self)
        else:
            self.game_state.betting_round += 1

    def fold(self):
        ### Win conditional
        print(self.game_state.player_names[self.game_state.betting_round % 6], "folded")
        self.game_state.active_players[self.game_state.betting_round % 6] = False
        self.game_state.betting_round += 1
        self.game_state.num_folded += 1
        for i in range(self.game_state.NUM_PLAYERS):
            if ((self.game_state.num_folded == self.game_state.NUM_PLAYERS - 1) and (self.game_state.active_players[i] == True)):
                print("Player", self.game_state.player_names[i], "Wins")
                self.game_state.player_stacks[i] += self.game_state.pot_size
                self.game_state.pot_size = 0
                self.game_state.num_folded = 0
                self.game_state.betting_round = 0
                PokerGameGUI.gameloop(self)

        

        
    def start_round(self):
        self.game_state.player_hands = [[] for _ in range(self.game_state.NUM_PLAYERS)]
        self.deck = self.game_state.deck
        PokerGameGUI.deal_player_card(self)
        for i in range(self.game_state.NUM_PLAYERS):
            self.game_state.active_players[i] = True
      
    def player_turn(self):
        #NOTE: Template for testing in the future the first person to act would shift through hands
        #Sets name1 as the first person to act whenever the fucntion is called
        self.game_state.player_turn[0] = True

        #NOTE: This function call is good for one round of play
        for i in range(self.game_state.NUM_PLAYERS):
            if (self.game_state.player_turn[i] == True):
                #NOTE: Player activity happens here.
                choice = random.randint(1, 3)
                if choice == 1:
                    PokerGameGUI.fold(self)
                if choice == 2:
                    PokerGameGUI.check(self)
                if choice == 3:
                    PokerGameGUI.bet(self)

            self.game_state.player_turn[i % 6] == False
            self.game_state.player_turn[(i+1) % 6] == True

            if self.game_state.betting_round == self.game_state.NUM_PLAYERS:
                time.sleep(1)
                self.root.update()
                PokerGameGUI.update_community_cards(self)

            if ((len(self.game_state.community_cards) == 5) and (self.game_state.betting_round + 1 == self.game_state.NUM_PLAYERS)):
                PokerGameGUI.gameloop(self)

            PokerGameGUI.player_turn(self)


    def gameloop(self):
        # while(1):
            self.shuffle()
            self.start_round()
            self.update_player_cards()
            self.root.update()
            time.sleep(.25)
            self.player_turn()


            #NOTE: Function for tracking player turn too keep the action inside of gameloop


            # time.sleep(1)
            # self.deal_community_card.invoke()
            # self.root.update()
            # time.sleep(1)
            # self.deal_community_card.invoke()
            # self.root.update()
            # time.sleep(1)
            # self.deal_community_card.invoke()
            # self.root.update()
            # time.sleep(1)
            # self.shuffle_button.invoke()
            # self.root.update()



        ###
        #   Assigns user bal card and name for game creation
        ###
    def update_player_cards(self):

        for i in range(self.game_state.NUM_PLAYERS):
            x = 130
            player_display = tk.Label(self.game_display, image=self.player_display_img)
            player_name = tk.Label(player_display, text=self.game_state.player_names[i], font=self.custom_font, bg ="white")
            player_bal = tk.Label(player_display, text= self.game_state.player_stacks[i], font=self.custom_font, bg="gold")
            player_name.place(anchor="center", relx=.75, rely=.3)
            player_bal.place(anchor="center", relx=.75, rely=.7)

            if (i==0 or i ==1):
                player_display.place(x=540, y=640)
                player_display.place(anchor="center",relx=.3, y=260+(i*250))
            if (i==2 or i ==5):
                player_display.place(x=540, y=640)
                player_display.place(anchor="center",relx=0, y=150+(-1*(x*(i-5))))
            if (i==4 or i ==3):
                player_display.place(x=540, y=640)
                player_display.place(anchor="center",relx=-.3, y=260+((i-4)*-250))


            ###
            #  Dealing PLayer Cards
            ###
            self.c1 = self.game_state.player_hands[i][0]
            self.c2 = self.game_state.player_hands[i][1]
            self.card1 = Image.open(f"resources/cards/{self.c1}.jpg")
            self.card2 = Image.open(f"resources/cards/{self.c2}.jpg")
            self.player_c1 = ImageTk.PhotoImage(self.card1)            
            self.player_c2 = ImageTk.PhotoImage(self.card2)
            self.card_images[i] = (self.player_c1, self.player_c2)

            player_card1 = tk.Label(player_display, image=self.player_c1, width=60, height=80)
            player_card2 = tk.Label(player_display, image=self.player_c2, width=60, height=80)
            player_card1.place(x=0, rely=0)
            player_card2.place(x=60, rely=0)

            self.player_card_labels.append(player_card1)

        

        ###
        #   Deals and displays community cards to the screen.
        ###
    def update_community_cards(self):

        print(self.game_state.community_cards)
        for i in range(len(self.game_state.community_cards)):
                self.card = self.game_state.community_cards[i]
                self.cCard = Image.open(f"resources/cards/{self.card}.jpg")
                self.community_card_x = ImageTk.PhotoImage(self.cCard)            

                self.community_card_images[i] = (self.community_card_x)
                self.community_card = tk.Label(self.game_display, image=self.community_card_x, width=60, height=80)
                self.community_card.place(x=370+ (i*70), y=300)
                self.community_card_labels.append(self.community_card)


        ###
        #  Helper Functions for code
        ###


    def remove_community_cards(self):
        for label in self.community_card_labels:
            label.destroy()

        self.community_card_labels = []
        self.game_state.community_cards = []

    def remove_player_cards(self):
        for label in self.player_card_labels:
            label.destroy()
        
        self.player_card_labels = []


    def shuffle(self):
        for i in range(len(self.game_state.dealt_cards)):
            self.deck.append(self.game_state.dealt_cards[i])

        PokerGameGUI.remove_community_cards(self)
        PokerGameGUI.remove_player_cards(self)
        self.game_state.dealt_cards = []

    def generate_random_card(self):        
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.game_state.dealt_cards.append(card)
        return card

    def update_gui(self):
        self.community_cards_var.set(", ".join([f"{card}" for card in self.game_state.community_cards]))

    def update_player_hand(self):
       balance = self.game_state.player_stacks
       for i, hand in enumerate(self.game_state.player_hands):
            self.player_hands_labels[i].config(text=f"bal: {balance[i]} Player {i+1} Hand: {hand[0]}, {hand[1]}")

    def deal_community_cards(self):

        if len(self.game_state.community_cards) == 0:
            self.game_state.deal_community_cards([PokerGameGUI.generate_random_card(self)])
            self.game_state.deal_community_cards([PokerGameGUI.generate_random_card(self)])
            self.game_state.deal_community_cards([PokerGameGUI.generate_random_card(self)])
            return
        if len(self.game_state.community_cards) >= 3:
            self.game_state.deal_community_cards([PokerGameGUI.generate_random_card(self)])


        
    def deal_player_card(self):
        for i in range (len(self.game_state.player_hands)):
            if len(self.game_state.player_hands[i]) < 2:
                self.game_state.deal_player_hand(i, [PokerGameGUI.generate_random_card(self)])
                self.deal_player_card()
                #self.update_player_hand()

    def reset_game(self):
        self.game_state.reset_game()
        self.update_gui()
        for i, label in enumerate(self.player_hands_labels):
            label.config(text=f"bal: {self.game_state.player_stacks[i]} Player {i+1} Hand: ")



if __name__ == "__main__":
    poker_game = tk.Tk()
    poker_game_gui = PokerGameGUI(poker_game)
    canvas = tk.Canvas(poker_game, width=1080, height=500)
    canvas.pack()
    poker_game.mainloop()