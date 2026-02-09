# """Game settings and configuration."""


# class GameSettings:
#     """Game configuration and settings."""
    
#     # Battle settings
#     STAMINA_COSTS = {
#         "N": 6,   # Normal attack
#         "E": 12,  # Enhanced attack
#         "Q": 18,  # Ultimate/Special attack
#         "H": 12,  # Heal
#         "S": 12   # Shield
#     }
    
#     # Stamina regeneration
#     STAMINA_REGEN_MIN = 6
#     STAMINA_REGEN_MAX = 18
    
#     # Difficulty settings
#     DIFFICULTIES = ["EASY", "MEDIUM", "HARD"]
    
#     # Database settings
#     DB_NAME = "accounts.db"
    
#     # Character type
# TYPES = ["Warrior", "Mage", "Archer", "Healer", "Shielder"]
    
#     # UI settings
#     BOARD_WIDTH = 50
    
#     @classmethod
#     def get_stamina_cost(cls, attack_type):
#         """Get stamina cost for an attack type."""
#         return cls.STAMINA_COSTS.get(attack_type, 0)
