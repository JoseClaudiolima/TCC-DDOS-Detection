import sys
import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.authentication import authenticate_user

def authenticate(user_name, password, window):
    authentication = authenticate_user(user_name, password)
    if not authentication:
        # Now... Code the error interface
        # sys.exit() # Finalize the process

        destroy_widgets_in_interface(window)
        create_an_error_authentification_interface(window)
    else:
        # Now... Code the method to reuse the interface and show the network
        print('Sucesso!')

def create_an_error_authentification_interface(window):
    def countdown (countdown_label, time_left):
        if time_left > 0:
            countdown_label.config(text=f"Sendo redirecionado em: {time_left}...")
            window.after(1000, countdown, countdown_label, time_left - 1)  # Update every second
        
        if time_left == 0:
            destroy_widgets_in_interface(window)
            create_an_authentification_interface(window)

    window.title("Authentication Failed")
    
    ttk.Label(window, text="Autentificação falhou", font=("Arial", 11)).grid(row=0, column=0, padx=(60,0), pady=(20,10))

    countdown_label = ttk.Label(window, text="Sendo redirecionado em: 5...", font=("Arial", 11))
    countdown_label.grid(row=2, column=0, padx=(60,0))

    window.after(1000, countdown, countdown_label, 4)


def destroy_widgets_in_interface(window):
    for widget in window.winfo_children():
        widget.destroy()
    return

def create_an_authentification_interface(window=False):
    if not window: # If there is not a old window (if its the first time running this code)
        # Create the main window
        window = ttk.Window(themename="superhero")

        # Code below is for centralize the window on screen
        x,y = 0,0
        # Calculating the central position on screen
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 200) // 2
        window.geometry(f"{350}x{200}+{x}+{y}")

        # Configure column weights
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        
    window.title("Authentication")

    # Username label and entry
    ttk.Label(window, text="Username:", font=("Arial", 11)).grid(row=0, column=0, padx=0, pady=(20,10), sticky="e")
    username_entry = ttk.Entry(window, font=("Arial", 11))
    username_entry.grid(row=0, column=1, padx=0, pady=(20,10))
    username_entry.focus()

    # Password label and entry
    ttk.Label(window, text="Password:", font=("Arial", 11)).grid(row=1, column=0, padx=0, pady=10, sticky="e")
    password_entry = ttk.Entry(window, show="*", font=("Arial", 11))
    password_entry.grid(row=1, column=1, padx=0, pady=10)

    # Bind the Enter key to trigger the authentication function
    window.bind("<Return>", lambda event: authenticate(username_entry.get(), password_entry.get(), window))

    # Larger button (rectangular)
    login_button = tkinter.Button(
        window, text="LOGIN", font=("Arial", 12),
        command=lambda: authenticate(username_entry.get(), password_entry.get(), window),
        width=8, height=1  # Width is in characters, height is in text lines
    )
    login_button.grid(row=2, column=0, columnspan=2, pady=20)  # Increased padding for spacing


    window.mainloop()

