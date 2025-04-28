import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
# Create the window
root = tk.Tk()
root.title("Choose an Image")
root.geometry("800x600")

# List of images and their information
images_info = [
    {"path": "image/monopoly.png", "description": "A beautiful sunset."},
    {"path": "image/monopoly.png", "description": "Snowy mountains."},
    {"path": "image/monopoly.png", "description": "Sunny beach day."}
]


# Frame to hold everything
frame = tk.Frame(root)
frame.pack(pady=20)

# Keep a reference to PhotoImage to prevent garbage collection
photo_images = []

# Display each image with its info and button
for idx, info in enumerate(images_info):
    img = Image.open(info['path'])
    img = img.resize((200, 200))  # Resize if needed
    photo = ImageTk.PhotoImage(img)
    photo_images.append(photo)

    img_label = tk.Label(frame, image=photo)
    img_label.grid(row=0, column=idx, padx=10)


    desc_label = tk.Label(frame, text=info['description'], wraplength=180)
    desc_label.grid(row=2, column=idx)

    select_button = tk.Button(frame, text="Select", command=lambda i=idx: select_image(i))
    select_button.grid(row=3, column=idx, pady=10)

root.mainloop()