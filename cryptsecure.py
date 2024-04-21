import bcrypt
import sqlite3

class CryptSecure:
    def __init__(self):
        # Initialize your CryptSecure instance, e.g., load configuration, set up database connection, etc.
        self.db_connection = sqlite3.connect('cryptsecure.db')
        self.create_user_table()

    def create_user_table(self):
        # Create a user table in the database if it doesn't exist
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
        self.db_connection.commit()

    def close_db_connection(self):
        # Close the database connection
        self.db_connection.close()

    def hash_password(self, password):
        # Hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, username, password):
        # Assume a user registration scenario
        try:
            # Check if the user already exists
            cursor = self.db_connection.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                print(f"User '{username}' already exists. Please choose a different username.")
            else:
                # Hash the user's password
                hashed_password = self.hash_password(password)

                # Update the SQLite database with the new user
                self.db_connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                self.db_connection.commit()

                print(f"User '{username}' registered successfully.")
        except sqlite3.Error as e:
            print(f"Error registering user: {e}")
        
    def show_users(self):
        try:
            cursor = self.db_connection.execute("SELECT username FROM users")
            users = cursor.fetchall()
            if users:
                print("\nUsers:")
                for user in users:
                    print(user[0])
            else:
                print("\nNo users found.")
        except sqlite3.Error as e:
            print(f"Error retrieving users: {e}")

    def remove_user(self, username, password):
        try:
            # Retrieve the hashed password from the database based on the username
            cursor = self.db_connection.execute("SELECT password FROM users WHERE username=?", (username,))
            hashed_password = cursor.fetchone()

            if hashed_password:
                hashed_password = hashed_password[0]
                # Verify the input password against the stored hashed password
                is_password_valid = bcrypt.checkpw(password.encode('utf-8'), hashed_password)

                if is_password_valid:
                    # Remove the user from the database
                    self.db_connection.execute("DELETE FROM users WHERE username=?", (username,))
                    self.db_connection.commit()
                    print(f"User '{username}' removed successfully.")
                else:
                    print("Invalid password. Access denied.")
            else:
                print(f"User '{username}' not found.")
        except sqlite3.Error as e:
            print(f"Error removing user: {e}")

    def clear_all_users(self):
        try:
            confirmation = input("Are you sure you want to clear all users? This action cannot be undone. (yes/no): ")
            if confirmation.lower() == 'yes':
                # Remove all users from the database
                self.db_connection.execute("DELETE FROM users")
                self.db_connection.commit()
                print("All users cleared successfully.")
            else:
                print("Clearing users canceled.")
        except sqlite3.Error as e:
            print(f"Error clearing users: {e}")

def main():
    crypt_secure = CryptSecure()

    while True:
        print("\nOptions:")
        print("1. Register a new user")
        print("2. Show users")
        print("3. Remove user")
        print("4. Clear all users")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            crypt_secure.register_user(username, password)
        elif choice == '2':
            crypt_secure.show_users()
        elif choice == '3':
            username = input("Enter username to remove: ")
            password = input("Enter your password for confirmation: ")
            crypt_secure.remove_user(username, password)
        elif choice == '4':
            crypt_secure.clear_all_users()
        elif choice == '5':
            crypt_secure.close_db_connection()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
