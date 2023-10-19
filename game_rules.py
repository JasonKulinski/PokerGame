import poker_gamestate
import poker_gui
import tkinter as tk
import random


class game_rules():


    def __init__(self):
        self.seven_card_hand = []
        self.game_state = poker_gamestate.GameState()
        self.player_hand = self.game_state.player_hands
        
        self.numeric_seven = []
        self.symbol_seven = []

        self.full_house_freq = 0

        self.straight_freq = 0
        self.three_of_a_kind_freq = 0
        self.two_pair_freq = 0
        self.one_pair_freq = 0
        self.high_card_freq = 0
        self.deck = [
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                ]

    def rank_hand(self):
        for i in range(1000):
            game_rules.shuffle(self)
            self.game_state.player_hands = [[] for _ in range(self.game_state.NUM_PLAYERS)]
            game_rules.deal_player_card(self)
            game_rules.deal_community_cards(self)
            for i in range(len(self.player_hand)):
                self.seven_card_hand.append(self.player_hand[i])
                #for i in range(len(self.game_state.community_cards)):
            game_rules.compare_cards(self)        
        
    def compare_cards(self):
        
        player_card1 = self.game_state.player_hands[0][0]
        player_card2 = self.game_state.player_hands[0][1]


        self.numeric_seven.append(player_card1[0])
        self.numeric_seven.append(player_card2[0])

        for i in range (len(self.game_state.community_cards)):
            self.numeric_seven.append(self.game_state.community_cards[i][0])

        game_rules.rank(self)


        pc1pair = False
        pc2pair = False
        OP_counter = 0
        TOAK_counter = 0

        full_house = False

        straight = False
        three_of_a_kind = False
        two_pair = False
        one_pair = False
        high_card = False

        self.three_of_a_kind_freq = self.three_of_a_kind_freq
        self.two_pair_freq = self.two_pair_freq
        self.one_pair_freq = self.one_pair_freq
        self.high_card_freq = self.high_card_freq







        save_state = ""
        card = ""
        count = 0
        for i in range(len(self.numeric_seven)):
            #Two pair NOTE: Does not handle the board having two pair, or your hand having one pair and the board having one pair
            #NOTE: One Pair
            #NOTE: DOES NOT WORK AS OF 11:27 OCT 17th DUE TO RANGE CHANGE FROM 5 TO 7

            # if ((self.game_state.community_cards[i][0] == player_card1[0]) 
            #     or (self.game_state.community_cards[i][0] == player_card2 [0]) 
            #     or (player_card1 [0] == player_card2 [0])):
            #     one_pair = True
                
            #     #NOTE: Two Pair
            #     if (self.game_state.community_cards[i][0] == player_card1[0]):
            #         pc1pair = True
            #     if (self.game_state.community_cards[i][0] == player_card2 [0]):
            #         pc2pair = True
            #     if pc1pair and pc2pair:
            #         two_pair = True
            
            card = self.numeric_seven[i]
            #NOTE Three of a kind (One Case)
            if (i != 6 and self.numeric_seven[i] == self.numeric_seven[i+1]):
                count += 1
                if card == save_state and count == 2:
                    three_of_a_kind = True
                if card != save_state and one_pair: 
                    two_pair = True

                one_pair = True
                save_state = self.numeric_seven[i]
                

            if (i < 3 and
                int(self.numeric_seven[i]) == int(self.numeric_seven[i+1]) -1 
            and int(self.numeric_seven[i]) == int(self.numeric_seven[i+2]) - 2 
            and int(self.numeric_seven[i]) == int(self.numeric_seven[i+3]) - 3 
            and int(self.numeric_seven[i]) == int(self.numeric_seven[i+4]) - 4
                ):
                straight = True


            if (two_pair and three_of_a_kind):
                full_house = True
            #NOTE: High Card
            else:
                high_card = True



        if full_house: self.full_house_freq += 1

        if straight: self.straight_freq += 1
        if three_of_a_kind: self.three_of_a_kind_freq += 1
        if two_pair: self.two_pair_freq += 1
        if one_pair: self.one_pair_freq += 1
        if high_card: self.high_card_freq += 1
        

        print(self.numeric_seven)
        self.numeric_seven = []
        print("Full House", self.full_house_freq)

        print("Straight", self.straight_freq)
        print("Three of a kind", self.three_of_a_kind_freq - self.full_house_freq)
        print("Two pair", self.two_pair_freq - self.full_house_freq)
        print("One Pair", self.one_pair_freq - self.two_pair_freq - self.three_of_a_kind_freq)
        print("High Card", self.high_card_freq - (self.one_pair_freq - self.two_pair_freq) - self.two_pair_freq - self.three_of_a_kind_freq)



        # print("Three of a kind", three_of_a_kind)
        # print("Two pair", two_pair)
        # print("One pair",one_pair)
        # print("High Card", high_card)
        #print(self.game_state.community_cards)
        #print(self.game_state.player_hands[0])
        
    
    def rank(self):
        for i in range (len(self.numeric_seven)):
            if self.numeric_seven[i] == "1":
                self.numeric_seven[i] = "10"
            if self.numeric_seven[i] == "J":
                self.numeric_seven[i] = "11"
            if self.numeric_seven[i] == "Q":
                self.numeric_seven[i] = "12"
            if self.numeric_seven[i] == "K":
                self.numeric_seven[i] = "13"
            if self.numeric_seven[i] == "A":
                self.numeric_seven[i] = "14"

        game_rules.seven_card_sort(self)

    
    def seven_card_sort(self):
        
        for i in range (len(self.numeric_seven)):
            bool_sorted = True

            for j in range((len(self.numeric_seven)) - i - 1):
                if  int(self.numeric_seven[j]) > int(self.numeric_seven[j + 1]):
                    self.numeric_seven[j], self.numeric_seven[j + 1] = self.numeric_seven[j + 1], self.numeric_seven[j]
                    bool_sorted = False

        



    
            
            
    def generate_random_card(self):        
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.game_state.dealt_cards.append(card)
        return card

    def deal_community_cards(self):
        self.game_state.community_cards = []
        for i in range (5):
            self.game_state.deal_community_cards([game_rules.generate_random_card(self)])

    def deal_player_card(self):
        for i in range (len(self.game_state.player_hands)):
            if len(self.game_state.player_hands[i]) < 2:
                self.game_state.deal_player_hand(i, [game_rules.generate_random_card(self)])
                self.deal_player_card()


    def shuffle(self):
        for i in range(len(self.game_state.dealt_cards)):
            self.deck.append(self.game_state.dealt_cards[i])

        self.game_state.dealt_cards = []
            

if __name__ == "__main__":
    game = game_rules()
    game.rank_hand()
