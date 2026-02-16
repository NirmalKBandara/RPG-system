# RPG System: Character Management & Guild Builder

## [ FINISHED. YOU CAN PLAY THE GAME BUT NOT OPTIMIZED ]

Welcome to the **RPG System**, a modular Python-based framework designed for managing player accounts and building unique character guilds. This system allows users to create accounts with varying difficulties and recruit specialized character classes to their ranks.

---

##  Features

###  Account Management

* **Secure Creation**: Create new player accounts with hashed passwords using `pbkdf2_hmac` for security.
* **Difficulty Settings**: Choose your journey with **Easy**, **Medium**, or **Hard** difficulty levels.
* **Guild System**: Every account features a personal guild where you can recruit and store your characters.

###  Diverse Character Classes

Explore five distinct character types, each with unique stats and roles:

| Class | Role | HP | Attack | Stamina | Unique Ability |
| --- | --- | --- | --- | --- | --- |
| **Warrior** | Tank / Melee | 150 | 25 | 20 | High Survivability |
| **Mage** | Glass Cannon | 80 | 40 | 30 | High Magic Damage |
| **Archer** | Ranged DPS | 110 | 15 | 50 | High Mobility/Stamina |
| **Healer** | Support | 100 | 5 | 30 | Heal (20 HP) |
| **Shielder** | Defensive Support | 85 | 15 | 20 | Shield (30 Points) |

---

##  How It Works

### 1. Interactive Interface

The system uses a command-line interface to guide users through the Game Menu, account setup, and reviewing character Info Sheets.

### 2. Recruitment Flow

Once an account is created, you are prompted to set your Main Character (Warrior, Mage, or Archer) and your Sub Character (Healer or Shielder).

---

##  Running with Docker (Recommended)

This project is containerized using Docker to simplify the setup of the Python environment and the MySQL database.

### Prerequisites

* [Docker](https://www.docker.com/get-started) installed on your machine.
* [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Setup and Launch

1. **Clone the repository**:
```bash
git clone https://github.com/NirmalKBandara/rpg-system.git
cd rpg-system

```


2. **Build and Run**:
Use Docker Compose to build the application and start the MySQL database service:
```bash
docker-compose up --build

```


3. **Access the Game**:
The application will run in interactive mode within your terminal. Follow the on-screen prompts to start your adventure.

---

##  Project Structure

* `main.py`: The entry point for the application.
* `Dockerfile`: Instructions for building the Python application container.
* `docker-compose.yml`: Orchestrates the application and MySQL database services.
* `character_types/`: Directory containing specific class implementations.
* `repositories/accountManager.py`: Logic for account creation and database management.

---

##  Manual Usage (Without Docker)

If you prefer to run the project locally, ensure you have a MySQL server running and configured as per your `.env` file, then run:

```bash
pip install -r requirements.txt
python main.py

```
