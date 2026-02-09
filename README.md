## RPG System: Character Management & Guild Builder

# [ FINISHED. YOU CAN PLAY THE GAME BUT NOT OPTIMIZED ]

Welcome to the **RPG System**, a modular Python-based framework designed for managing player accounts and building unique character guilds. This system allows users to create accounts with varying difficulties and recruit specialized character classes to their ranks.

---

## 🚀 Features

### 👤 Account Management

* **Secure Creation**: Create new player accounts with hashed passwords using `pbkdf2_hmac` for security.
* **Difficulty Settings**: Choose your journey with **Easy**, **Medium**, or **Hard** difficulty levels.
* **Guild System**: Every account features a personal guild where you can recruit and store your characters.

### ⚔️ Diverse Character Classes

Explore five distinct character types, each with unique stats and roles:

| Class | Role | HP | Attack | Stamina | Unique Ability |
| --- | --- | --- | --- | --- | --- |
| **Warrior** | Tank / Melee | 150 | 25 | 20 | High Survivability |
| **Mage** | Glass Cannon | 80 | 40 | 30 | High Magic Damage |
| **Archer** | Ranged DPS | 110 | 15 | 50 | High Mobility/Stamina |
| **Healer** | Support | 100 | 5 | 30 | Heal (20 HP) |
| **Shielder** | Defensive Support | 85 | 15 | 20 | Shield (30 Points) |

---

## 🛠️ How It Works

### 1. Interactive Interface

The system uses a command-line interface (`Interface` class) to guide users through:

* Navigating the **Game Menu**.
* Setting up account credentials and difficulty.
* Reviewing character **Info Sheets** before recruitment.

### 2. Recruitment Flow

Once an account is created, you are prompted to:

1. **Set Main Character**: Choose between a Warrior, Mage, or Archer.
2. **Set Sub Character**: Choose between a Healer or Shielder.
3. **Confirmation**: Confirm your choice to add them to your account's guild.

---

## 📂 Project Structure

* `gamePlay.py`: The entry point for the application.
* `interface.py`: Manages all user interactions and menus.
* `account.py`: Logic for account creation, password hashing, and guild management.
* `character.py`: The base class for all character entities.
* `character_types/`: Directory containing specific class implementations (Warrior, Mage, etc.).

---

## 📝 Usage

To start your adventure, simply run the main gameplay script:

```bash
python gamePlay.py

```

Follow the on-screen prompts to create your account and build your first guild!