import tkinter as tk
from tkinter import messagebox
import random
import poker_gamestate
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import messagebox
import random
import poker_gamestate
from PIL import Image, ImageTk

root = tk.Tk()

# Create PhotoImage objects for your images within a loop
image_paths = ["resources/player_bar.jpg", "resources/table.png"]
image_labels = []

for image_path in image_paths:
    img = Image.open(image_path)
    image = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=image, height=60, width=80)
    label.image = image  # Keep a reference to the image to prevent it from being garbage collected
    label.pack()
    image_labels.append(label)

# Function to remove the displayed image
def remove_image():
    global current_image_index
    
    # Remove the current image label from the parent widget
    if current_image_index < len(image_labels):
        image_labels[current_image_index].pack_forget()

        # Decrement the current_image_index if possible
        if current_image_index >= 0:
            current_image_index -= 1

# Button to remove the current image
remove_button = tk.Button(root, text="Remove Image", command=remove_image)
remove_button.pack()

# Initialize the current_image_index
current_image_index = 0

root.mainloop()