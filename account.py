import hashlib
import os

class Account:
    def __init__(self, username, salt, password_hash, difficulty):
        self.username = username
        self.salt = salt
        self.password_hash = password_hash
        self.difficulty = difficulty
        self.main_character = None
        self.sub_character = None
        self.guild = [] 
    
    @staticmethod
    def _hash_password(password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 10000).hex()

    @classmethod
    def new_account(cls, username, password, difficulty):
        salt = os.urandom(16).hex()
        password_hash = cls._hash_password(password, salt)
        return cls(username, salt, password_hash, difficulty)
    @classmethod
    def load_from_db(cls, username, salt, password_hash, difficulty):
        return cls(username, salt, password_hash, difficulty)

    def add_to_guild(self, character):
        self.guild.append(character)
        print(f"{character.name} the {type(character).__name__} has been added to your account!")

    def check_password(self, password):
        return self._hash_password(password, self.salt) == self.password_hash

