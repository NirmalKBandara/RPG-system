import random
from gameEngine import GameEngine
from enemyAccount import EnemyAccount
from account import Account

class QuickBattle:
    game_engine = None

    @classmethod
    def battleStart(cls, user_account):
        enemy_account = cls.createAnemy()
        
        cls.game_engine = GameEngine(
                user_account.main_character,
                user_account.sub_character,
                enemy_account.main_character,
                enemy_account.sub_character
                )
        #mode = user_account.difficulty
        while(True):
            cls.game_engine.reroll_stamina()
            cls.game_engine.user_turn()
            if cls.game_engine.is_game_over_2(): 
                cls.game_engine.end_game("user")
                break
            cls.game_engine.enemy_turn()
            if cls.game_engine.is_game_over_1(): 
                cls.game_engine.end_game("enemy")
                break

        cls.game_engine = None

    @classmethod
    def createAnemy(cls):
        name_list = ['Arathorn', 'Bladewing', 'Cyrus', 'Draven', 'Eldric', 'Fenris', 'Gordan', 'Haldor', 'Ironclad', 'Jaxon', 'Kael', 'Lorian', 'Magnus', 'Noctis', 'Orion', 'Phoenix', 'Quillon', 'Ragnar', 'Soren', 'Thane', 'Ulric', 'Valen', 'Wolfe', 'Xander', 'Zephyr', 'Alaric', 'Brandt', 'Cassius', 'Daemon', 'Eirik', 'Falco', 'Gideon', 'Havoc', 'Icarus', 'Jareth', 'Kaelen', 'Lynx', 'Maddox', 'Nero', 'Obsidian', 'Pierce', 'Quinlan', 'Raze', 'Savage', 'Talon', 'Uriel', 'Vex', 'Wrath', 'Xeros', 'Zareth', 'Asher', 'Blaze', 'Crimson', 'Drake', 'Eclipse', 'Fang', 'Gale', 'Hunter', 'Inferno', 'Jett', 'Kai', 'Lyndon', 'Midnight', 'Nash', 'Onyx', 'Pyro', 'Quake', 'Ryder', 'Storm', 'Thorn', 'Umbra', 'Vortex', 'Wilder', 'Xaos', 'Zenith', 'Axel', 'Bolt', 'Cinder', 'Dusk', 'Ember', 'Frost', 'Griffin', 'Hawk', 'Ion', 'Jagger', 'Killian', 'Lance', 'Maverick', 'Nitro', 'Odin', 'Pyre', 'Quest', 'Rook', 'Spike', 'Titan', 'Uther', 'Viper', 'Warlock', 'Xavier', 'Zane', 'Ajax', 'Bane', 'Cyclone', 'Dagger', 'Edge', 'Flint', 'Grim', 'Hex', 'Ignis', 'Jinx', 'Kato', 'Lupin', 'Mortis', 'Nox', 'Omega', 'Phantom', 'Quantum', 'Ruin', 'Shadow', 'Tempest', 'Ultron', 'Vendetta', 'Wraith', 'Xylo', 'Zero', 'Archer', 'Blade', 'Crash', 'Dante', 'Ether', 'Forge', 'Ghost', 'Havok', 'Impact', 'Justice', 'Krios', 'Lunar', 'Magma', 'Nexus', 'Omen', 'Prism', 'Quasar', 'Rift', 'Specter', 'Thunder', 'Union', 'Vector', 'Warden', 'Exodus', 'Ymir', 'Zodiac', 'Atlas', 'Blitz', 'Cobra', 'Dynamo', 'Echo', 'Falcon', 'Gauntlet', 'Hydra', 'Index', 'Javelin', 'Kronos', 'Lightning', 'Matrix', 'Nova', 'Orbit', 'Pulse', 'Quiver', 'Reaper', 'Scepter', 'Torch', 'Universe', 'Vertex', 'Wyvern', 'Xerxes', 'Zeus', 'Arsenal', 'Beacon', 'Caliber', 'Delta', 'Entity', 'Fusion', 'Genesis', 'Hammer', 'Impulse', 'Jupiter', 'Kinetic', 'Legion', 'Meteor', 'Nebula', 'Odyssey', 'Praetor', 'Quorum', 'Reactor', 'Sentry', 'Trigger', 'Unity', 'Valkyrie', 'Weapon', 'Exodus', 'Yankee', 'Zenon', 'Ashford', 'Brimstone', 'Corvus', 'Draco', 'Erebus', 'Fenrir', 'Gunnar', 'Helios', 'Ignatius', 'Jorah', 'Kellan', 'Lazarus', 'Morpheus', 'Nemesis', 'Orpheus', 'Perseus', 'Quirinus', 'Remus', 'Severus', 'Tiberius', 'Ulysses', 'Victor', 'Wolfram', 'Xerxon', 'Yggdrasil', 'Achilles', 'Brutus', 'Caesar', 'Demetrius', 'Eros', 'Faustus', 'Gallus', 'Hector', 'Ikaros', 'Julius', 'Kronos', 'Lucius', 'Maximus', 'Nicolaus', 'Octavius', 'Plato', 'Quintus', 'Romulus', 'Silas', 'Theron', 'Urban', 'Vulcan', 'Wilhelm', 'Xanthus', 'Yaroslav', 'Zoltan', 'Alarion', 'Braxus', 'Calderon', 'Daedalus', 'Evander', 'Flavius', 'Gregorius', 'Hadrian', 'Isaias', 'Justinian', 'Khaldor', 'Leonidas', 'Marius', 'Nero', 'Orestes', 'Polaris', 'Quiron', 'Rexus', 'Solaris', 'Titus', 'Urion', 'Valerian', 'Wynter', 'Xylon', 'Zarathos', 'Azrael', 'Balthazar', 'Caspian', 'Darius', 'Elijah', 'Fabian', 'Gabriel', 'Horus', 'Isaiah', 'Jarvis', 'Kilian', 'Leopold', 'Malachi', 'Nathaniel', 'Oberon', 'Percival', 'Quincy', 'Roland', 'Sebastian', 'Tobias', 'Ulrich', 'Vincent', 'Wagner', 'Xenos', 'York', 'Zephyrus', 'Aldric', 'Barnabas', 'Cedric', 'Dominic', 'Edmund', 'Ferdinand', 'Garrett', 'Heinrich', 'Ingmar', 'Jasper', 'Klaus', 'Lambert', 'Matthias', 'Norbert', 'Otto', 'Patrick', 'Quentin', 'Rupert', 'Stefan', 'Tristan', 'Ulrik', 'Valdemar', 'Walter', 'Xerath', 'Yorick', 'Zachary', 'Alduin', 'Balrog', 'Chaos', 'Deimos', 'Erebos', 'Fenix', 'Grimlock', 'Hellfire', 'Incendius', 'Juggernaut', 'Kraken', 'Leviathan', 'Maelstrom', 'Nightfall', 'Oblivion', 'Pandemonium', 'Quicksilver', 'Ravager', 'Stormbreaker', 'Thunderstrike', 'Undertaker', 'Vanguard', 'Warlord', 'Xenomorph', 'Yautja', 'Zealot', 'Annihilator', 'Berserker', 'Conqueror', 'Destroyer', 'Executioner', 'Fury', 'Gladiator', 'Harbinger', 'Invader', 'Javelin', 'Killzone', 'Liberator', 'Marauder', 'Nightmare', 'Outlaw', 'Predator', 'Quickshot', 'Rampage', 'Slayer', 'Terminator', 'Unleashed', 'Vigilante', 'Warrior', 'Xenon', 'Yield', 'Zephyros', 'Abyss', 'Banshee', 'Cyclops', 'Demon', 'Enforcer', 'Frostbite', 'Goliath', 'Hellraiser', 'Immortal', 'Jaguar', 'Knight', 'Lancer', 'Minotaur', 'Nomad', 'Oracle', 'Paladin', 'Quantum', 'Ranger', 'Sentinel', 'Tactician', 'Unstoppable', 'Veteran', 'Warmonger', 'Xiphos', 'Yeoman', 'Zorro', 'Apex', 'Blitzkrieg', 'Champion', 'Dominion', 'Elite', 'Fighter', 'Guardian', 'Hero', 'Ironside', 'Judicator', 'King', 'Lord', 'Master', 'Noble', 'Overlord', 'Protector', 'Queen', 'Ruler', 'Sovereign', 'Tyrant', 'Ultimate', 'Vanquisher', 'Warchief', 'Expert', 'York', 'Zenmaster', 'Admiral', 'Battalion', 'Captain', 'Director', 'Emperor', 'Field', 'General', 'High', 'Infantry', 'Junior', 'Kommandant', 'Lieutenant', 'Major', 'Navigator', 'Officer', 'Private', 'Quartermaster', 'Recruit', 'Sergeant', 'Tribune', 'Unit', 'Vice', 'Wing', 'Xeno', 'Yard', 'Zone', 'Alpha', 'Beta', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu', 'Artemis', 'Blademaster', 'Crimsonblade', 'Darkstrike', 'Emberstorm', 'Firebrand', 'Ghostblade', 'Hawkeye', 'Icebreaker', 'Judgement', 'Knightfall', 'Lightbringer', 'Moonblade', 'Nightshade', 'Oathkeeper', 'Peacekeeper', 'Quincy', 'Ragefire', 'Shadowbane', 'Trueblade', 'Unbroken', 'Valorheart', 'Windrunner', 'Xander', 'Youngblood', 'Zealfire', 'Ashenblade', 'Bloodmoon', 'Coldheart', 'Dawnbringer', 'Everfrost', 'Fireborn', 'Goldenheart', 'Hoarfrost', 'Ironheart', 'Justicar', 'Keenblade', 'Lightseeker', 'Moonshadow', 'Nightwalker', 'Oathbreaker', 'Pathfinder', 'Quickblade', 'Ravenlight', 'Silverblade', 'Truthseeker', 'Unbowed', 'Valorborn', 'Wildheart', 'Xerath', 'Youngfire', 'Zephyrblade', 'Aetherion', 'Blackthorn', 'Crystalborn', 'Dreadnought', 'Elderborn', 'Flamekeeper', 'Grimward', 'Heartstone', 'Ironborn', 'Jadefire', 'Kingsguard', 'Lightforge', 'Moonfire', 'Nightborn', 'Oakenshield', 'Proudheart', 'Quickfire', 'Runekeeper', 'Skyborn', 'Trueborn', 'Unshaken', 'Voidborn', 'Wildfire', 'Xeric', 'Youthfire', 'Zephyrborn', 'Argentum', 'Blazeheart', 'Coldfire', 'Duskblade', 'Evenstar', 'Frostfire', 'Goldfire', 'Highborn', 'Icefire', 'Jadeborn', 'Keenfire', 'Lightborn', 'Moonborn', 'Nightfire', 'Oakfire', 'Proudfire', 'Quickborn', 'Rosefire', 'Silverfire', 'Truefire', 'Unborn', 'Voidfire', 'Wildborn', 'Xerofire', 'Youngborn', 'Zephyrfire', 'Aeris', 'Blackfire', 'Coldborn', 'Dawnfire', 'Elderfire', 'Flameborn', 'Greyfire', 'Highfire', 'Ironfire', 'Jadelight', 'Keenborn', 'Lightfire', 'Moonlight', 'Nightborn', 'Oakborn', 'Pridefire', 'Quicklight', 'Roseborn', 'Silverborn', 'Truelight', 'Uniform', 'Voidlight', 'Wildlight', 'Xeroborn', 'Younglight', 'Zephyrlight', 'Ashborn', 'Bloodfire', 'Coldlight', 'Duskfire', 'Everborn', 'Flamelight', 'Goldborn', 'Heartfire', 'Iceborn', 'Justfire', 'Kingfire', 'Lightblade', 'Moonblade', 'Nightblade', 'Oathfire', 'Pathborn', 'Quickblade', 'Rageborn', 'Shadowfire', 'Thornfire', 'Undying', 'Valorfire', 'Windborn', 'Xerolight', 'Youngblade', 'Zealborn']

        # try:
        #     with open('main_names.txt', 'r') as file:
        #         main_name_list = file.read().split('\n')
        # except FileNotFoundError:
        #     print("ERROR IN MAIN_NAMES.TXT FILE !")   

        # try:
        #     with open('sub_names.txt', 'r') as file:
        #         sub_name_list = file.read().split('\n')            
        # except FileNotFoundError:
        #     print("ERROR IN SUB_NAMES.TXT FILE !")   


        enemyAccount = EnemyAccount()

        enemyAccount.create_main_character(random.choice(name_list))        
        enemyAccount.create_sub_character(random.choice(name_list))    

        return enemyAccount
        
