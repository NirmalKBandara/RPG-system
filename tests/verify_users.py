import sys
import os
import unittest
# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from repositories.accountManager import AccountManager
from models.account import Account
from character_types.warrior import Warrior
from character_types.healer import Healer

class TestAccountManagerExceptions(unittest.TestCase):
    def setUp(self):
        self.manager = AccountManager()
        # Randomize username to avoid conflicts from previous runs if not cleaned up
        import random
        self.username = f"TestUser_{random.randint(1000, 9999)}"
        self.password = "password123"
        self.difficulty = "EASY"

    def test_duplicate_user_exception(self):
        account = Account.new_account(self.username, self.password, self.difficulty)
        account.main_character = Warrior("Main")
        account.sub_character = Healer("Sub")
        
        # First save - should succeed
        self.assertTrue(self.manager.save_account(account), "First save should succeed")
        print(f"DEBUG: Saved {self.username} successfully.")

        # Second save - should raise Exception (ValueError)
        print(f"DEBUG: Attempting to save {self.username} again...")
        with self.assertRaises(ValueError) as context:
            self.manager.save_account(account)
        
        self.assertIn("already taken", str(context.exception))
        print("SUCCESS: Caught expected Duplicate User Exception.")

    def test_load_non_existent_user(self):
        username = "NonExistentUser_99999"
        print(f"DEBUG: Attempting to load {username}...")
        with self.assertRaises(ValueError) as context:
            self.manager.load_account(username)
        
        self.assertIn("No account found", str(context.exception))
        print("SUCCESS: Caught expected Account Not Found Exception.")

if __name__ == '__main__':
    unittest.main()
