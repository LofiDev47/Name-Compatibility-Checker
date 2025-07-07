import random
import tkinter as tk
from tkinter import messagebox, font
import webbrowser

# Calculate a compatibility score between 0 and 100 based on the names
def compatibility_score(name1, name2):
    combined = name1 + name2
    random.seed(sum(ord(c) for c in combined))  # Seed for consistent results per name pair
    return random.randint(0, 100)  # Score between 0 and 100

# Handle the button click or Enter key event
def check_compatibility(event=None):
    name1 = entry_name1.get().strip().title()  # Get and format first name
    name2 = entry_name2.get().strip().title()  # Get and format second name
    if not name1.isalpha() or not name2.isalpha():  # Validate input
        messagebox.showerror("Invalid Input", "Please enter valid names (letters only).")
        return
    score = compatibility_score(name1, name2)  # Calculate score
    result_label.config(text=f"The compatibility score for {name1} and {name2} is {score}%!")
    entry_name1.delete(0, tk.END)  # Clear first name entry
    entry_name2.delete(0, tk.END)  # Clear second name entry
    entry_name1.focus()            # Focus back to first entry

# Function to open the GitHub link
def open_github():
    webbrowser.open_new("https://github.com/LofiDev47")

# Create the main application window
root = tk.Tk()
root.title("Name Compatibility Checker")
root.geometry("420x340")  # Set window size
root.resizable(False, False)  # Prevent resizing

# Set custom fonts for labels and header
custom_font = font.Font(family="Segoe UI", size=11)
header_font = font.Font(family="Segoe UI", size=15, weight="bold")

# Main frame for padding and layout
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# Header label with hearts and title
header = tk.Label(
    main_frame,
    text="💖 Name Compatibility Checker 💖",
    font=header_font,
    fg="#d6336c",
    wraplength=400,   # Wrap text to fit width
    justify="center"
)
header.grid(row=0, column=0, pady=(10,15), sticky="ew")  # Add top and bottom padding

# First name label and entry
tk.Label(main_frame, text="Enter the first name:", font=custom_font).grid(row=1, column=0, sticky="w", pady=(0,5))
entry_name1 = tk.Entry(main_frame, font=custom_font)
entry_name1.grid(row=2, column=0, sticky="ew", pady=(0,10))

# Second name label and entry
tk.Label(main_frame, text="Enter the second name:", font=custom_font).grid(row=3, column=0, sticky="w", pady=(0,5))
entry_name2 = tk.Entry(main_frame, font=custom_font)
entry_name2.grid(row=4, column=0, sticky="ew", pady=(0,10))

# Button to check compatibility
check_btn = tk.Button(main_frame, text="Check Compatibility", font=custom_font, bg="#4CAF50", fg="white", command=check_compatibility)
check_btn.grid(row=5, column=0, pady=(0,10), sticky="ew")

# Label to display the result
result_label = tk.Label(
    main_frame,
    text="",
    font=custom_font,
    fg="#333366",
    wraplength=320,  # Wrap result text
    justify="center" # Center the result text
)
result_label.grid(row=6, column=0, pady=(10,20))  # Add bottom padding

# Add GitHub link label
github_link = tk.Label(
    main_frame,
    text="My github",
    font=custom_font,
    fg="#1a0dab",
    cursor="hand2"
)
github_link.grid(row=7, column=0, pady=(0,10))
github_link.bind("<Button-1>", lambda e: open_github())

# Add Exit button
exit_btn = tk.Button(
    main_frame,
    text="Exit",
    font=custom_font,
    bg="#d9534f",
    fg="white",
    command=root.destroy
)
exit_btn.grid(row=8, column=0, pady=(0,10), sticky="ew")

main_frame.columnconfigure(0, weight=1)  # Make column expand

root.bind('<Return>', check_compatibility)  # Bind Enter key to check
entry_name1.focus()  # Focus on first entry at start

root.mainloop()  # Start the Tkinter

# Made by LofiDev47 on Github! Thanks for Playing