from interface import Interface
from accountManager import AccountManager

database = AccountManager()
Interface.start_menu()
database.close()