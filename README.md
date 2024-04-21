
# CryptSecure

CryptSecure is a Python-based application that provides secure user registration, login, and user management functionalities using cryptographic techniques.

## Features

- **User Registration:** Allows users to register securely with a unique username and password.
- **User Login:** Provides a secure login mechanism for registered users.
- **User Management:** Supports operations such as showing users, removing users, and clearing all users from the system.
- **Password Hashing:** Utilizes bcrypt to securely hash user passwords.
- **Database Integration:** Stores user information securely in an SQLite database.

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/cryptsecure.git

2. Install the required dependencies:

   pip install -r requirements.txt

3. Run the application:

   python cryptsecure.py


## Usage

1. Register a new user: Choose option 1 and enter a username and password.
2. Login: Choose option 2 and enter your registered username and password.
3. Show users: Choose option 3 to display all registered users.
4. Remove user: Choose option 4 to remove a user by providing their username and password.
5. Clear all users: Choose option 5 to delete all registered users (use with caution).

## Dependencies

- bcrypt
- sqlite3

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.
