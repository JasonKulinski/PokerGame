import tkinter as tk
from tkinter import messagebox
import random
import poker_gamestate
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Poker Table")

plr = Image.open("resources/player_bar.jpg")
plr_load = ImageTk.PhotoImage(plr)

card = Image.open('resources/cards/2H.jpg')
card_load = ImageTk.PhotoImage(card)

# Create the central area (centered in the grid)
central_frame = tk.Frame(root, width=1080, height=720, bg="green")
central_frame.grid(row=1, column=1, rowspan=720, columnspan=1080)

# Create six items (labels in this example)
item1 = tk.Label(root, image=plr_load)
plr_card = tk.Label(root, image=card_load)
item2 = tk.Label(root, image=plr_load)
plr_card2 = tk.Label(root, image=card_load)
item4 = tk.Label(root, text="Item 4", bg="purple")
item5 = tk.Label(root, text="Item 5", bg="orange")
item6 = tk.Label(root, text="Item 6", bg="pink")

# Place items around the central frame
item1.grid(row=5, column=5, padx=0, pady=0)  # Top
plr_card.grid(row=4, column=5)

item2.grid(row=8, column=8, padx=0, pady=0)  # Top
plr_card2.grid(row=7, column=8)


root.mainloop()