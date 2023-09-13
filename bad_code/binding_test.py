import tkinter as tk

def move_labels(event):
    frame.place(x=event.x, y=event.y)

root = tk.Tk()
root.title("Grouping Labels")

# Create a frame to group the labels
frame = tk.Frame(root, width=200, height=100, bg="lightgray")
frame.pack_propagate(False)  # Prevent the frame from resizing to its content

# Create labels within the frame
label1 = tk.Label(frame, text="Label 1")
label1.pack()

label2 = tk.Label(frame, text="Label 2")
label2.pack()

# Bind mouse click to move the frame
root.bind("<Button-1>", move_labels)

root.mainloop()