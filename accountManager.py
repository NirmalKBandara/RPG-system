import sqlite3
import json

class AccountManager:
    _instance = None 

    def __new__(cls, *agr, **kwrags):
        if not cls._instance:
            cls._instance = super(AccountManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name = "accounts.db"):
        if hasattr(self, 'initialized'):
            return

        self.conn = sqlite3.connect(db_name) # The road to the database
        self.coursor = self.conn.cursor() # The Truck on the road
        self._create_table()
        self.initialized = True
        print(" [SYSTEM] Database Connection Established.")

    def _create_table(self):
        self.coursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                            (username TEXT PRIMARY KEY,
                            salt TEXT NOT NULL,
                            password_hash TEXT NOT NULL,
                            difficulty TEXT NOT NULL,
                            main_character TEXT,
                            sub_character TEXT)''') # Define a load space 
        self.conn.commit() # Creating the load space

    def save_account(self, account):
        try:
            main_char_json = json.dumps(account.main_character.to_dict())
            sub_char_json = json.dumps(account.sub_character.to_dict())

            query = "INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?)"
            data = (account.username, account.salt, account.password_hash, account.difficulty, main_char_json, sub_char_json)
            self.coursor.execute(query, data)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Error !!! {account.username} is already taken")
            return False
        except Exception as e:
            print(f"Database Error: {e}")
            return False
            
    def close(self):
        self.conn.close()

