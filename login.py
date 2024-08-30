import tkinter 
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import os
import time
from game import App

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

pencere = ctk.CTk()
pencere.title("LOGIN")
pencere.geometry("500x700")

def login():
    messagebox.showinfo("Başarılı","Giriş başarılı")
    pencere.destroy()
    game = App(tk.Tk())
    game.mainloop()

def info():
    messagebox.showinfo("Bilgi","OYUN şöyle Böyle OyNanIr!!")

oyunadi_label= ctk.CTkLabel(pencere,text="XoXo")
oyunadi_label.pack(pady=5)

play_buton = ctk.CTkButton(pencere,text="PLAY!",command=login)
play_buton.pack(pady=5)

info_buton = ctk.CTkButton(pencere,text="Info!",command=info)
info_buton.pack(pady=5)

pencere.mainloop()