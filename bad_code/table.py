import tkinter as tk
from PIL import Image, ImageTk
import poker_gamestate
import poker_gui




gamestate = poker_gamestate.GameState()







root = tk.Tk()
root.title("Poker Table")
root.geometry("1080x720")
name_font = ("Helvetica", 20, "bold")

image = Image.open("resources/player_bar.jpg")
table = Image.open("resources/table.png")

photo = ImageTk.PhotoImage(image)
table = ImageTk.PhotoImage(table)



player_card1 = Image.open("resources/cards/2H.jpg")
player_card2 = Image.open("resources/cards/2H.jpg")

player1_card1 = ImageTk.PhotoImage(player_card1)
player1_card2 = ImageTk.PhotoImage(player_card2)




# for i, hand in enumerate(gamestate.player_hands):
#     player_card1 = gamestate.player_hands[i],{hand[0].rank},{hand[0].suit}




main_frame = tk.Frame(root, width=1080, height=720)
###
# Created a format for labels and framing for a player at a poker table
# First declare a frame with the correct size of the image and bounded regions
# Load the images into the frame the image box in this case is called player1
# The following Labels are text lables and include text that says player1 and 1000 representing names and balances
# After use place to place the labels inside the frame or outside the frame with pack
###

###
#       START OF PLAYER 1
###
poker_table = tk.Label(main_frame, image=table, width=1080, height=720)
poker_table.pack()

#Main frame for player information
player1_frame = tk.Frame(main_frame, width=240, height=200)
player1 = tk.Label(player1_frame, image=photo, width=240, height=280)
player1.pack()

#Actual player information such as name, stack size etc
player1_name = tk.Label(player1_frame, text= gamestate.player_names[0], font=name_font)
player1_bal = tk.Label(player1_frame, text= gamestate.player_stacks[0], font=name_font)
player1_name.place(relx=0.5, rely=0.4, anchor="center")
player1_bal.place(relx=0.5, rely=0.6, anchor="center")


#Player card information
player1_cards = tk.Frame(player1_frame, width= 120, height=80)
player_card1 = tk.Label(player1_cards, image=player1_card1, width=60, height=80)
player_card2 = tk.Label(player1_cards, image=player1_card2, width=60, height=80)
player_card1.place(x=0, y= 0)
player_card2.place(x=60, y= 0)
player1_cards.place(relx=0.5, rely=0.15, anchor="center")

#Places the playerframe at this position on the main frame
player1_frame.place(x=420, y =500)

###
#         END OF PLAYER 1
##



player2_frame = tk.Frame(main_frame, width=240, height=120)
player2 = tk.Label(player2_frame, image=photo, width=240, height=120)
player2_name = tk.Label(player2_frame, text= gamestate.player_names[1], font=name_font)
player2_bal = tk.Label(player2_frame, text= gamestate.player_stacks[1], font=name_font)
player2.pack()
player2_name.place(relx=0.5, rely=0.3, anchor="center")
player2_bal.place(relx=0.5, rely=0.7, anchor="center")

player2_frame.place(x=50, y =400)


player3_frame = tk.Frame(main_frame, width=240, height=120)
player3 = tk.Label(player3_frame, image=photo, width=240, height=120)
player3_name = tk.Label(player3_frame, text= gamestate.player_names[2], font=name_font)
player3_bal = tk.Label(player3_frame, text= gamestate.player_stacks[2], font=name_font)
player3.pack()
player3_name.place(relx=0.5, rely=0.3, anchor="center")
player3_bal.place(relx=0.5, rely=0.7, anchor="center")

player3_frame.place(x=50, y =130)

player4_frame = tk.Frame(main_frame, width=240, height=120)
player4 = tk.Label(player4_frame, image=photo, width=240, height=120)
player4_name = tk.Label(player4_frame, text= gamestate.player_names[3], font=name_font)
player4_bal = tk.Label(player4_frame, text= gamestate.player_stacks[3], font=name_font)
player4.pack()
player4_name.place(relx=0.5, rely=0.3, anchor="center")
player4_bal.place(relx=0.5, rely=0.7, anchor="center")

player4_frame.place(x=420, y =50)


player5_frame = tk.Frame(main_frame, width=240, height=120)
player5 = tk.Label(player5_frame, image=photo, width=240, height=120)
player5_name = tk.Label(player5_frame, text= gamestate.player_names[4], font=name_font)
player5_bal = tk.Label(player5_frame, text= gamestate.player_stacks[4], font=name_font)
player5.pack()
player5_name.place(relx=0.5, rely=0.3, anchor="center")
player5_bal.place(relx=0.5, rely=0.7, anchor="center")

player5_frame.place(x=790, y =130)


player6_frame = tk.Frame(main_frame, width=240, height=120)
player6 = tk.Label(player6_frame, image=photo, width=240, height=120)
player6_name = tk.Label(player6_frame, text= gamestate.player_names[5], font=name_font)
player6_bal = tk.Label(player6_frame, text= gamestate.player_stacks[5], font=name_font)
player6.pack()
player6_name.place(relx=0.5, rely=0.3, anchor="center")
player6_bal.place(relx=0.5, rely=0.7, anchor="center")

player6_frame.place(x=790, y = 400)

main_frame.place(x=0,y=0)


root.mainloop()