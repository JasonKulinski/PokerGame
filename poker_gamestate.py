class Card:
    def __init__(self, rank, suit):
        self.deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH'
                      '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD'
                      '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'
                      '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                      ]

class GameState:
    def __init__(self):
        self.NUM_PLAYERS = 6
        self.community_cards = []
        self.player_hands = [[] for _ in range(self.NUM_PLAYERS)]
        self.betting_round = 0
        self.betting_actions = [[] for _ in range(self.NUM_PLAYERS)]
        self.pot_size = 0
        self.player_stacks = [1500] * self.NUM_PLAYERS
        self.button_position = 0
        self.active_players = [True] * self.NUM_PLAYERS
        self.current_bet_size = 0
        self.betting_round_history = []
        self.player_names = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6']
        self.dealt_cards = []
        self.num_folded = 0
        self.player_turn = [False] * self.NUM_PLAYERS
        self.deck = [
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
                ]


    def deal_community_cards(self, cards):
        self.community_cards.extend(cards)

    def deal_player_hand(self, player_index, cards):
        self.player_hands[player_index].extend(cards)

    def record_player_action(self, player_index, action, amount=0):
        self.betting_actions[player_index].append({'action': action, 'amount': amount})

    def update_pot_size(self, amount):
        self.pot_size += amount

    def update_player_stack(self, player_index, amount):
        self.player_stacks[player_index] += amount

    def update_button_position(self):
        self.button_position = (self.button_position + 1) % self.NUM_PLAYERS

    def end_betting_round(self):
        self.current_bet_size = 0
        self.betting_round += 1
        self.betting_round_history.append(self.betting_actions)
        self.betting_actions = [[] for _ in range(self.NUM_PLAYERS)]

    def reset_betting_round(self):
        self.betting_actions = [[] for _ in range(self.NUM_PLAYERS)]

    def fold_player(self, player_index):
        self.active_players[player_index] = False

    def is_betting_round_completed(self):
        return all(len(actions) > 0 for actions in self.betting_actions)

    def is_hand_completed(self):
        return self.betting_round >= 4

    def reset_game(self):
        self.community_cards = []
        self.player_hands = [[] for _ in range(self.NUM_PLAYERS)]
        self.betting_round = 0
        self.betting_actions = [[] for _ in range(self.NUM_PLAYERS)]
        self.pot_size = 0
        self.player_stacks = [1000] * self.NUM_PLAYERS
        self.button_position = 0
        self.active_players = [True] * self.NUM_PLAYERS
        self.current_bet_size = 0
        self.betting_round_history = []


# Usage example:
if __name__ == "__main__":
    # Create a new game state
    game_state = GameState()

    # Deal community cards and player hands


    # Record player actions
    game_state.record_player_action(0, 'raise', amount=50)
    game_state.record_player_action(1, 'fold')

    # Update pot size and player stack
    game_state.update_pot_size(50)
    game_state.update_player_stack(0, -50)

    # Move to the next betting round
    game_state.end_betting_round()

    # Reset the betting actions for the new round
    game_state.reset_betting_round()

    # Check if the betting round is completed
    print(game_state.is_betting_round_completed())

    # Check if the hand is completed (4 betting rounds completed)
    print(game_state.is_hand_completed())

    # Reset the game state for a new hand
    game_state.reset_game()