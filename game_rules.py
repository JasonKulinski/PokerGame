import poker_gamestate
import poker_gui
import tkinter as tk
import random


class game_rules():


    def __init__(self):
        self.seven_card_hand = []
        self.game_state = poker_gamestate.GameState()
        self.player_hand = self.game_state.player_hands
        self.deck = [
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                ]

    def rank_hand(self):
        game_rules.deal_player_card(self)
        game_rules.deal_community_cards(self)
        for i in range(len(self.player_hand)):
            self.seven_card_hand.append(self.player_hand[i])
            #for i in range(len(self.game_state.community_cards)):
        game_rules.compare_cards(self)        
        
    def compare_cards(self):
        
        card1 = self.game_state.player_hands[0][0]
        card2 = self.game_state.player_hands[0][1]
        print(card1[0])

    def generate_random_card(self):        
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.game_state.dealt_cards.append(card)
        return card

    def deal_community_cards(self):
        for i in range (5):
            self.game_state.deal_community_cards([game_rules.generate_random_card(self)])

    def deal_player_card(self):
        for i in range (len(self.game_state.player_hands)):
            if len(self.game_state.player_hands[i]) < 2:
                self.game_state.deal_player_hand(i, [game_rules.generate_random_card(self)])
                self.deal_player_card()
            

if __name__ == "__main__":
    game = game_rules()
    game.rank_hand()
