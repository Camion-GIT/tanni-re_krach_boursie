from tkinter import *
import time
import json

# Create the main window
ws = Tk()
ws.title('Menu')
ws.geometry('400x300')
ws.config(bg='white')

# Create the first button
button1 = Button(ws, text="Prix de la biere 1", font=(21), bg='white', width=20)
button1.pack(pady=10)

# Create the second button
button2 = Button(ws, text="Prix de la biere 2", font=(21), bg='white', width=20)
button2.pack(pady=10)

# Create the third button
button3 = Button(ws, text="Prix de la biere 3", font=(21), bg='white', width=20)
button3.pack(pady=10)

# Update the button texts with the prices from the JSON file
while True:
    time.sleep(1)
    PATH = "prix.json"
    with open(PATH, 'r') as outfile:
        data = json.load(outfile)
    print(data)
    prix_bierre1 = data[0]['price']
    prix_bierre2 = data[1]['price']
    prix_bierre3 = data[2]['price']
    marque_bierre1 = data[0]['brand']
    marque_bierre2 = data[1]['brand']
    marque_bierre3 = data[2]['brand']
    button1.config(text=f"{marque_bierre1} - {prix_bierre1} €")
    button2.config(text=f"{marque_bierre2} - {prix_bierre2} €")
    button3.config(text=f"{marque_bierre3} - {prix_bierre3} €")
    ws.update()

# Run the main loop
ws.mainloop()
