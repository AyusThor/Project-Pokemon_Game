# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:38:21 2023

@author: Acer
"""

from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background = "gold1")

img=ImageTk.PhotoImage(Image.open ("abra.jpg"))
img=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
img=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
img=ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
img=ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
img=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
img=ImageTk.PhotoImage(Image.open ("charmender.jpg"))
img=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
img=ImageTk.PhotoImage(Image.open ("persion.jpg"))
img=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
img=ImageTk.PhotoImage(Image.open ("paras.jpg"))
img=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
img=ImageTk.PhotoImage(Image.open ("button.jpg"))


player1 = Label(root, text = "Player 1",bg = "snow2",fg  = "firebrick2")
player1.place(relx =  0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "snow2",fg = "firebrick2")
player2.place(relx = 0.9,rely = 0.3, anchor = CENTER)
    
player_1_score_label = Label(root, bg = "gold2",fg = "firebrick2")
player_1_score_label.place(relx = 0.1,rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "gold2",fg = "firebrick2")
player_2_score_label.place(relx = 0.9,rely = 0.4, anchor = CENTER)

random_pokemon_label = Label(root,bg = "chocolate2", fg = "cyan1")
random_pokemon_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()