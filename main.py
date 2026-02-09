from ui.interface import Interface
from repositories.accountManager import AccountManager

database = AccountManager()
Interface.start_menu()
database.close()