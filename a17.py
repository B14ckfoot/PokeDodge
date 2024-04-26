import tkinter as tk


# Function to save the password
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
        clear_entries()
        load_passwords()
    else:
        display_message("Error", "Please fill in all the fields.")


# Function to display the list of saved passwords
def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
            passwords_display.config(state=tk.NORMAL)
            passwords_display.delete(1.0, tk.END)
            for password in passwords:
                passwords_display.insert(tk.END, password)
            passwords_display.config(state=tk.DISABLED)
    except FileNotFoundError:
        display_message("Error", "No passwords saved yet.")


# Function to display message boxes
def display_message(title, message):
    messagebox.showinfo(title, message)


# Function to clear entry fields
def clear_entries():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Create labels
website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=10, pady=5)
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5)
password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)

# Create entry fields
website_entry = tk.Entry(root, width=30)
website_entry.grid(row=0, column=1, padx=10, pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
show_button = tk.Button(root, text="Show Password List", command=load_passwords)
show_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Create text widget to display passwords
passwords_display = tk.Text(root, width=100, height=10, state=tk.DISABLED)
passwords_display.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the main loop
root.mainloop()
