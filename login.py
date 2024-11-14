import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "12345":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Criar a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Criar e posicionar os elementos da interface
label_username = tk.Label(root, text="Usuário")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Senha")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Executar a aplicação
root.mainloop()
