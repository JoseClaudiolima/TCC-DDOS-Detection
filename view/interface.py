import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.authentication import authenticate_user

def authenticate(user_name, password):
    authentication = authenticate_user(user_name, password)
    if not authentication:
        # Now... Code the error interface
        sys.exit() # Finalize the process
    else:
        # Now... Code the method to reuse the interface and show the network
        print('Sucesso!')

def authentification_interface():
    # Create the main window
    root = ttk.Window(themename="superhero")
    root.title("Authentication")

    # Username label and entry
    ttk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = ttk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    username_entry.focus()

    # Password label and entry
    ttk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = ttk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Bind the Enter key to trigger the authentication function
    root.bind("<Return>", lambda event: authenticate(username_entry.get(), password_entry.get()))

    # Login button
    login_button = ttk.Button(root, text="Login", bootstyle=SUCCESS, command=lambda: authenticate(username_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()
