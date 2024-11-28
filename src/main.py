from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64

def generate_key(secret_key):
    key = base64.urlsafe_b64encode(secret_key.ljust(32).encode()[:32])
    return key

def encrypt():
    try:
        data = txt_1.get(1.0, END).strip()
        secret_key = txt_2.get(1.0, END).strip()

        if not data or not secret_key:
            messagebox.showerror("Error", "Please enter both data and secret key.")
            return

        key = generate_key(secret_key)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        
        output_text.delete(1.0, END)  # Clear previous output
        output_text.insert(END, encrypted_data.decode())  # Display encrypted data
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt():
    try:
        encrypted_data = txt_1.get(1.0, END).strip()
        secret_key = txt_2.get(1.0, END).strip()

        if not encrypted_data or not secret_key:
            messagebox.showerror("Error", "Please enter both encrypted data and secret key.")
            return

        key = generate_key(secret_key)
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data.encode())
        
        output_text.delete(1.0, END)  # Clear previous output
        output_text.insert(END, decrypted_data.decode())  # Display decrypted data
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    window.clipboard_clear()  # Clear the clipboard
    window.clipboard_append(output_text.get(1.0, END))  # Append the output text to the clipboard
    messagebox.showinfo("Copied", "Output copied to clipboard!") # Create a message box that shows confirmation 

def load_screen():
    global txt_1
    global txt_2
    global window
    global output_text
    
    window = Tk()
    window.title("Anonytalk - Encrypt & Decrypt")
    window.geometry("600x600")
    window.configure(bg="#f0f0f0")

    # Load background image
    background_image = PhotoImage(file="b.png")  # Use .png format for transparency
    background_label = Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Main Frame
    main_frame = Frame(window, bg="#f0f0f0")
    main_frame.pack(pady=20)

    # Input Frame
    input_frame = LabelFrame(main_frame, text="Input", font=("Arial", 16), bg="#f0f0f0", bd=2)
    input_frame.pack(padx=10, pady=10, fill="both", expand="yes")

    Label(input_frame, text="Enter a string:", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
    txt_1 = Text(input_frame, font="Arial 12", fg="black", bg="white", height=2, width=30)
    txt_1.grid(row=0, column=1, padx=10, pady=10)

    Label(input_frame, text="Enter the secret key:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
    txt_2 = Text(input_frame, font="Arial 12", fg="black", bg="white", height=2, width=30)
    txt_2.grid(row=1, column=1, padx=10, pady=10)

    # Output Frame
    output_frame = LabelFrame(main_frame, text="Output", font=("Arial", 16), bg="#f0f0f0", bd=2)
    output_frame.pack(padx=10, pady=10, fill="both", expand="yes")

    output_text = Text(output_frame, font="Arial 12", fg="black", bg="white", height=2, width=30)
    output_text.pack(padx=10, pady=10 )

    # Button Frame
    button_frame = Frame(main_frame, bg="#f0f0f0")
    button_frame.pack(pady=20)

    Button(button_frame, text="ENCRYPT", width=15, height=2, bg='red', fg="white", command=encrypt).grid(row=0, column=0, padx=10)
    Button(button_frame, text="DECRYPT", width=15, height=2, bg="green", fg="white", command=decrypt).grid(row=0, column=1, padx=10)
    Button(button_frame, text='COPY TO CLIPBOARD', width=30, height=2, bg="orange", fg='white', command=copy_to_clipboard).grid(row=1, column=0, columnspan=2, pady=10)
    Button(button_frame, text='RESET', width=30, height=2, bg="blue", fg='white', command=lambda: [txt_1.delete(1.0, END), txt_2.delete(1.0, END), output_text.delete(1.0, END)]).grid(row=2, column=0, columnspan=2, pady=10)

    window.mainloop()

load_screen()