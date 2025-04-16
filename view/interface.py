import sys
import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.authentication import authenticate_user

def network_manager_interface(window):
    window = manage_size_and_centralization_interface_window(window, 1000,500, True)
    window.title("Network Manager")

    # Show the network environment...

def authenticate(user_name, password, window):
    authentication = authenticate_user(user_name, password)
    if not authentication:
        destroy_widgets_in_interface(window)
        create_an_error_authentication_interface(window)
    else:
        destroy_widgets_in_interface(window)
        network_manager_interface(window)

def create_an_error_authentication_interface(window):
    def countdown (countdown_label, time_left):
        if time_left > 0:
            countdown_label.config(text=f"Sendo redirecionado em: {time_left}...")
            window.after(1000, countdown, countdown_label, time_left - 1)  # Update every second
        
        if time_left == 0:
            destroy_widgets_in_interface(window)
            create_an_authentication_interface(window)

    window.title("Authentication Failed")
    
    ttk.Label(window, text="Autentificação falhou", font=("Arial", 11)).grid(row=0, column=0, padx=(60,0), pady=(20,10))

    countdown_label = ttk.Label(window, text="Sendo redirecionado em: 5...", font=("Arial", 11))
    countdown_label.grid(row=2, column=0, padx=(60,0))

    window.after(1000, countdown, countdown_label, 4)

def destroy_widgets_in_interface(window):
    for widget in window.winfo_children():
        widget.destroy()
    return

def manage_size_and_centralization_interface_window(window, width, height, centralized=True):
    # Code below is for centralize the window on screen
    x,y = 0,0
    if centralized:
        # Calculating the central position on screen
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2


    window.geometry(f"{width}x{height}+{x}+{y}")
    return window

def create_an_authentication_interface(window=False):
    if not window: # If there is not a old window (if its the first time running this code)
        # Create the main window for the first time
        window = ttk.Window(themename="flatly") # Other options: superhero #solar #darkly #simplex #journal #flatly
        window = manage_size_and_centralization_interface_window(window, 350, 200,True)
        window.resizable(False, False) # It's not possible to resize the window

        window.iconbitmap("transparent-pixel.ico") # Replace the default icon, by a transparent 1x1 pixel

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
        window, text="LOGIN", font=("Arial", 11),
        command=lambda: authenticate(username_entry.get(), password_entry.get(), window),
        width=8, height=1  # Width is in characters, height is in text lines
    )
    login_button.grid(row=2, column=0, columnspan=2, pady=20)  # Increased padding for spacing


    window.mainloop()

