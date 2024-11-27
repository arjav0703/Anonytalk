# Anonytalk
## A string Encryptor/Decryptor Using Fernet

This Python-based Graphical User Interface (GUI) program allows users to securely encrypt and decrypt strings using the **Fernet** encryption algorithm. The program provides an intuitive interface where users can easily enter a string, encrypt it using a key, and decrypt the string with the same key.
[![Watch the video](https://cloud-qptgbw0gx-hack-club-bot.vercel.app/0image.png)](https://cloud-iu24iauzr-hack-club-bot.vercel.app/0screencast_from_2024-11-27_19-30-17.mp4)
## Features:
- Encrypt and decrypt strings with Fernet symmetric encryption.
- User-friendly GUI built with Tkinter.
- Securely generate and store encryption keys.
- Clear messages on successful encryption/decryption.
- Simple interface for easy usage.

---

---

## Installation

To use the program, you'll need to have Python 3.x installed along with a few required dependencies.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arjav0703/Anonytalk.git
   ```

2. **Run the program:**
   After installation, run the program using the following command:
   ```bash
   python3 ./Anonytalk/src/main.py
   ```

---

## Dependencies

This program requires the following Python libraries:
- `cryptography` - for the Fernet encryption and decryption functions.
- `tkinter` - for creating the GUI.

To install these libraries, use the following:
```bash
pip install cryptography tkinter
```


## Example

### Encrypt:
- **Input:** `"Hello, World!"`
- **Key:** `"YourGeneratedFernetKeyHere"`
- **Encrypted Output:** `"gAAAAABgGJvYeGnyo..."

### Decrypt:
- **Input (Encrypted String):** `"gAAAAABgGJvYeGnyo..."`
- **Key:** `"YourGeneratedFernetKeyHere"`
- **Decrypted Output:** `"Hello, World!"`

---

## License

This project is licensed under the MIT License

---

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Push to your branch.
5. Create a pull request.

---

Feel free to contribute to this project to improve it further. If you encounter any issues or have suggestions, please create an issue on the GitHub repository.

## Assets
Image: https://unsplash.com/photos/black-and-silver-door-knob-3wPJxh-piRw



