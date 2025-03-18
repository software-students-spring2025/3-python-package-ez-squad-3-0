import random
import time

# Pokémon Stats (HP, Attack Range, Defense Range, Type)
pokemon_data = {
    "Venusaur": {"HP": 130, "Attack": (13, 22), "Defense": (18, 22), "Type": "Grass"},
    "Charizard": {"HP": 110, "Attack": (20, 30), "Defense": (12, 18), "Type": "Fire"},
    "Blastoise": {"HP": 115, "Attack": (15, 25), "Defense": (18, 22), "Type": "Water"},
}

# Type Effectiveness
effectiveness = {
    ("Fire", "Grass"): 1.2,
    ("Grass", "Water"): 1.2,
    ("Water", "Fire"): 1.2,
    ("Grass", "Fire"): 0.8,
    ("Water", "Grass"): 0.8,
    ("Fire", "Water"): 0.8,
}

# Pokémon ASCII Art
pokemon_ascii = {
    "Venusaur": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠶⠶⠶⢦⣄⠀⠀⠀⠀⢀⣀⣤⠤⠴⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣋⣁⣀⣀⣀⠀⠀⠀⣀⣴⣤⣾⢷⡾⠛⣾⡿⢻⣤⣤⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠖⠚⠋⠉⠉⠉⠉⠉⠉⠉⠉⢉⣛⡳⣿⣿⠿⠙⠷⠟⠷⠋⠻⠾⠻⣿⣷⠶⠖⠒⠒⠒⠒⠒⠻⠿⠦⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⢀⣠⣤⡴⠶⠛⠛⠋⠉⠉⠉⠛⠛⠲⢦⣄⠀⠀⢀⣠⣤⠶⠿⠓⠒⠶⠶⠶⠦⣤⣤⣀⡀⠀⠀⠀⠉⠙⠓⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⣀⣤⣶⠾⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣷⣴⣿⣉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⢦⣄⡀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⢀⣠⡶⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⣀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡾⠛⠁⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⢦⣌⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠸⣧⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣽⠆⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⣀⣀⣤⠀⠀⠀⢠⣾⡃⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡼⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣉⣻⠶⣤⣤⣿⣿⣿⣿⣿⣿⣏⢀⣤⡈⣡⣙⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣿⡆⠀⣰⣦⣤⣴⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⣴⡶⠶⣶⣿⣟⠛⢿⣯⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢻⠷⠓⠲⣶⡤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠷⠄⠈⠉⠛⣀⣠⣽⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣄⣀⠙⠛⠉⠿⠷⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠛⠓⠚⠛⠂⠀⠀⠰⠶⠛⠛⣻⠏⠉⠹⠿⣿⣿⡛⠛⠻⠿⠿⠿⣿⣉⣤⡴⠞⠀⠀⠀⢸⣿⡇⠀⠀⠀⢀⣀⠉⢻⣿⠿⠛⠛⠛⣛⣽⣿⣿⠃⠉⢿⣿⡿⣏⠛⠻⣶⣶⠾⠛⠻⠷⢤⣄⡀⠀⠀⠀⠀
⠀⢀⣈⣭⠿⠛⠀⠀⠀⠀⣠⡆⠀⠀⠀⠋⣶⠀⠀⢀⣽⣿⣿⣦⣄⠀⠀⠀⢿⣋⣁⣤⣴⠖⠀⠀⢸⣿⠀⠀⠀⠀⠀⠙⠿⣿⡿⠀⠀⣠⣾⣿⣿⣿⣿⣄⠀⠀⠉⠃⠀⠀⠀⢻⣆⠀⠀⠀⠀⢠⣈⡉⠛⠶⣤⡄
⢸⡏⠁⣀⠀⢀⣴⡇⠀⢠⣿⠁⠀⡄⠀⣼⣿⠀⢀⣿⣟⣿⣿⣻⣿⣷⡄⠀⠘⢻⣟⠋⢀⣠⣤⠀⠈⠁⠀⠀⠸⣶⣄⣶⣤⡿⠁⠀⠾⠿⣿⣯⣿⣿⣤⣿⣧⡀⠘⣿⣆⠀⣤⣀⠹⣷⣄⠀⣦⣈⠙⢿⣷⡾⠋⠀
⠘⠛⢿⣏⣴⣿⣏⣀⣠⡟⣿⣤⣼⣷⣶⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠻⠾⣿⡿⢁⡄⠀⠀⠀⢤⣀⠘⣿⠿⠟⠀⢀⣀⣀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢷⣬⣿⣷⣤⡼⠷⠀⠀
⠀⠀⠀⠀⠁⠀⠉⠉⠉⣴⢏⣿⣿⣿⣿⣿⠟⠛⢻⣿⠟⠀⠀⠀⢴⡛⠉⠁⠀⢀⠀⠀⠻⢶⣿⠃⢀⣿⡄⢈⣿⠟⠋⠀⡀⠀⠀⠀⣉⣽⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡾⠿⠋⢹⣿⡏⠀⢀⡾⠁⠀⠀⠀⠀⣾⠛⣶⣤⣀⠸⡇⠀⠀⠀⠙⠷⢾⠟⠿⠟⠁⠀⠀⢸⡇⣀⣤⣾⣿⢹⡇⠀⠀⠀⠀⠙⣿⡛⠋⠀⢻⣿⣿⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠁⠀⠀⢸⡿⠀⠀⢾⡁⠀⠀⠀⠀⠀⠹⣄⠙⠛⣹⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠛⠿⣤⣉⣀⠼⠁⠀⣀⠀⠀⣸⡇⠀⠀⠈⣿⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣟⢀⣀⠀⠀⢸⡇⠀⠀⠘⢷⡀⠀⠲⣦⣀⡀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⠾⠋⠀⣰⡟⠀⠀⠀⠀⣿⡏⠀⠀⠀⢀⣸⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣤⣦⣾⡇⠀⠀⠀⠈⠳⢶⣤⣾⣽⣿⣟⣿⣶⡶⠶⢦⣤⣀⠀⢠⡀⠀⠀⠀⣤⠀⣠⣤⡶⠖⠛⢿⣿⣿⣽⠛⣠⣦⣴⠾⠋⠀⠀⠀⠀⠀⣿⠁⠀⢀⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⠛⢿⡄⢹⣿⣿⡀⠀⠀⠀⠉⠛⠳⠶⠶⠶⠶⠶⠛⠋⠀⠀⠀⠀⢸⣿⣿⢃⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⣫⡾⠃⠀⠀⠀⠀⠀⠀⣤⠀⠀⣸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣿⣿⣿⢿⣿⣧⡺⣧⡄⠀⠀⢀⣀⡀⠉⠻⣮⣝⣿⣿⣿⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣴⣿⣿⡿⣫⣾⠛⣁⣄⠀⠀⠀⠀⠀⠛⠋⠀⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠉⠙⠒⠋⠙⢷⣄⠀⠀⠀⠘⠛⠁⠀⠀⣠⣿⡿⢿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣽⡾⠋⠀⠀⠿⠷⠀⠀⠀⠀⠀⠀⠀⣠⡿⠳⠞⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⠃⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢉⡟⠀⠀⠀⠀⠀⠀⠀⢰⣤⣶⠆⢀⣴⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⢿⣿⡟⢿⣿⣿⣏⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣹⡆⢢⡾⠻⣧⠀⠀⣴⢶⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠉⠙⠻⣇⣠⡿⠷⠾⣧⣈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
    "Charizard": """   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢤⡀⠀⠀⠀⠀⢸⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠈⠢⡀⠀⠀⢀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⡔⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⡹⠀⠀⠘⢄⠀⠈⠲⢖⠈⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠁⢠⠞⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠉⠑⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⠇⠀⡤⡀⠀⠀⠀⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⣾⣿⣷⣶⣤⣄⣉⠑⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠞⢁⣴⣾⣿⣿⡆⢇⠀⠀⠀⠀⠀⠸⡀⠀⠂⠿⢦⡰⠀⠀⠋⡄⠀⠀⠀⠀⠀⠀⠀⢰⠁⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡴⢁⣴⣿⣿⣿⣿⣿⣿⡘⡄⠀⠀⠀⠀⠀⠱⣔⠤⡀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⡜⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢣⠀⠀⠀⠀⠀
⠀⠀⠀⡼⢠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡘⢆⠀⠀⠀⠀⠀⢃⠑⢌⣦⠀⠩⠉⠀⡜⠀⠀⠀⠀⠀⠀⢠⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣣⡀⠀⠀⠀
⠀⠀⢰⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠱⡀⠀⠀⠀⢸⠀⠀⠓⠭⡭⠙⠋⠀⠀⠀⠀⠀⠀⠀⡜⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡱⡄⠀⠀
⠀⠀⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢃⠀⠀⠀⢸⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⢀⠜⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠘⣆⠀
⠀⢸⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣆⠀⠀⡆⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⡠⠖⣡⣾⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⠀
⠀⡏⣾⣿⣿⣿⣿⡿⡛⢟⢿⣿⣿⣿⣿⣿⣿⣧⡈⢦⣠⠃⠀⠀⠀⠀⠀⢱⣀⠤⠒⢉⣾⡉⠻⠋⠈⢘⢿⣿⣿⣿⣿⠿⣿⣿⠏⠉⠻⢿⣿⣿⣿⣿⡘⡆
⢰⡇⣿⣿⠟⠁⢸⣠⠂⡄⣃⠜⣿⣿⠿⠿⣿⣿⡿⠦⡎⠀⠀⠀⠀⠀⠒⠉⠉⠑⣴⣿⣿⣎⠁⠠⠂⠮⢔⣿⡿⠉⠁⠀⠹⡛⢀⣀⡠⠀⠙⢿⣿⣿⡇⡇
⠘⡇⠏⠀⠀⠀⡾⠤⡀⠑⠒⠈⠣⣀⣀⡀⠤⠋⢀⡜⣀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠉⡃⠈⢀⠴⣿⣿⣀⡀⠀⠀⠀⠈⡈⠊⠀⠀⠀⠀⠙⢿⡇⡇
⠀⠿⠀⠀⠀⠀⠈⠀⠉⠙⠓⢤⣀⠀⠁⣀⡠⢔⡿⠊⠀⠀⠀⠀⠙⢦⡀⠀⠐⠢⢄⡀⠁⡲⠃⠀⡜⠀⠹⠟⠻⣿⣰⡐⣄⠎⠀⠀⠀⠀⠀⠀⠀⠀⢣⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠙⢦⣀⢀⡴⠁⠀⠀⠀⠀⠉⠁⢱⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠈⢏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢀⡴⠁⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣧⣠⠤⠖⠋⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠳⢄⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠊⠈⠁⠀⠀⠀⡔⠛⠲⣤⣀⣀⣀⠀⠈⢣⡀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢀⡠⢔⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢈⠤⠒⣀⠀⠀⠀⠀⣀⠟⠀⠀⠀⠑⠢⢄⡀⠀⠀⠈⡗⠂⠀⠀⠀⠙⢦⠤⠒⢊⡡⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠒⣒⡁⠬⠦⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⢺⢠⠤⡀⢀⠤⡀⠠⠷⡊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⡀⡱⠧⡀⢰⠓⠤⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
    "Blastoise": """    ⠀⡴⠊⠀⢀⣀⣀⣀⡀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⢠⣾⣿⣿⣿⣿⣿⣶⡀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢷⣶⣶⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠚⠉⠉⠙⠒⠦⣀⠀⠀
⠀⠀⠀⠈⢧⠀⠈⠻⢿⣿⣿⣿⡿⠟⠁⠀⠀⢸⣿⣿⣿⣿⡆⠀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⣠⣴⣶⣿⣷⣶⣄⠈⠣⡀
⠀⠀⠀⠀⠀⠳⡄⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⣠⣤⣄⡀⢠⠏⠀⢰⣿⣿⣿⣿⣿⣿⣿⣧⠀⢣
⠀⠀⠀⠀⢀⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣶⣦⠉⠉⠁⠀⠀⠀⢸⠋⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⡸⢹⡇⠟⠁⡤⣀⠀⠀⠀⡀⠀⢀⠀⠀⠀⠀⠈⢿⡷⣸⣿⣿⣿⠏⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡿⠃⢠⠇
⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠲⡤⠤⠤⠔⢊⡴⢋⡟⠀⢸⣀⣯⣷⡄⢸⣁⣀⡸⡀⣠⣔⡞⢣⠀⢡⣿⣿⠿⡟⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⣀⠴⠃⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⡀⠙⠢⣤⠔⠋⠀⢸⠁⢀⠀⠀⠀⠠⣄⠀⠀⠀⠈⠈⣛⠛⠓⠊⠀⢸⣿⣡⠞⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡚⠁⠀⠀⠀
⠀⠀⠀⠀⣠⣿⡿⠿⠟⠛⠛⠉⠉⠁⠀⠀⠀⢀⣿⠋⠹⣇⣀⣀⣀⣈⢉⠉⠉⠒⠋⠉⠀⠀⢠⣀⣸⡇⠙⢆⠘⢆⡀⠀⠀⠀⣀⣴⣾⣿⣿⣷⡄⠀⠀⠀
⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠲⠤⠤⠞⠀⢹⣧⠀⠀⠑⠦⡈⠉⢉⠏⣹⣿⣿⣿⣿⡿⠃⠀⠀⠀
⠀⡴⠋⠀⢀⣠⠔⠒⠛⠛⠛⠓⠢⣴⠁⠈⠑⢝⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣧⡀⠀⠀⠈⠛⠥⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⢰⠃⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠑⠬⡻⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⣟⠕⠋⠉⢣⠀⠀⠀⠀⠀⠙⠻⣿⣷⠀⠀⠀⠀⠀⠀
⢸⠀⡜⠁⠀⠀⣀⣠⠤⠤⠤⢤⣀⠀⡇⠀⠀⠀⠀⠀⠈⠑⠭⢛⡻⠿⠷⠶⠶⠶⠶⠿⣛⡫⠕⠊⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠈⠻⢧⠀⠀⠀⠀⠀
⠘⣶⠃⢀⠔⠋⠁⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⠖⠊⠉⠉⠑⠒⢤⡀⠈⢧⠀⠀⠀⠀
⠀⠘⡿⠃⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⣀⣀⡀⠀⠀⠀⠀⠀⠙⢦⢸⠀⠀⠀⠀
⠀⢠⠇⠀⠀⣠⠴⠚⠉⠉⠉⠙⠛⠶⣟⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠋⠉⠀⠉⠙⠢⣄⠀⠀⠀⠘⣿⠀⠀⠀⠀
⠀⠈⡆⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠢⢕⡲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢔⡿⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⡟⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠈⠙⠒⠭⠭⣒⣒⣂⠀⠀⣀⣀⣐⣒⣲⠮⠝⠒⠉⣡⠿⠛⠛⠒⠦⣀⠀⠀⠀⠀⣷⠀⢠⠇⠀⠀⠀⠀
⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⢸⡦⠋⠀⠀⠀⠀⠀
⠀⠀⡇⠘⣄⡀⠀⠀⠀⠀⠀⠀⣠⡴⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢿⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⢀⡼⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠀⠘⡍⠙⢲⢶⠒⠛⠋⡏⠈⠲⢤⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠤⢼⣄⠀⠀⠀⠀⠀⠀⠀⢸⠗⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣇⢀⣼⠤⠟⠒⠳⣄⣰⠓⠒⠶⣄⡉⠚⠥⣂⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠈⣶⣄⠀⠀⠀⠀⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠉⠑⠚⠭⠵⢒⣒⣶⣤⣤⣤⣶⣒⡒⠲⠿⠛⠋⢹⠈⠿⣶⠶⠛⠉⠉⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⡏⠉⠒⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⣉⡵⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢀⣧⣀⣀⠀⠀⠀⠀⠀⣀⣀⣀⣤⡴⠖⢿⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠈⠓⠶⢤⣤⣤⣀⣀⣀⣠⣤⡶⠛⠁⠀⢸⠇⠈⠉⠉⠉⠉⠉⠉⠉⡩⢻⡀⠀⠀⠀⠈⠙⠳⠶⠶⣤⣤⠶⠶⠚⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠚⢷⣀⡠⠤⠤⢤⡀⠀⢀⡠⠤⠤⠤⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣷⠒⠚⠛⠛⠓⠒⠲⠤⣄⠀⢀⠔⠋⠉⠉⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⢸⠶⣇⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⢯⡀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⠤⠚⠁⠀⠈⠑⠢⢤⣀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣆⣀⣀⣀⣀⡠⠤⠒⠋⠁⠀⠀⠉⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
}

#  1 Function: Show Pokémon
def show_pokemon():
    """Displays ASCII art of all Pokémon."""
    print("\n✨ Available Pokémon ✨\n")
    for name, art in pokemon_ascii.items():
        print(f"🔹 {name} appears!")
        print(art)
        stats = pokemon_data[name]
        print(f"  - HP: {stats['HP']}, Attack Range: {stats['Attack']}, Defense Range: {stats['Defense']}, Type: {stats['Type']}\n")
        time.sleep(1)

# 2 Function: Select Pokémon for Battle
def select_pokemon():
    """Allows the player to choose two Pokémon for battle."""
    choices = list(pokemon_data.keys())

    print("\nChoose two Pokémon for battle:")
    for i, name in enumerate(choices, start=1):
        print(f"{i}. {name}")

    choices_lower = [c.lower() for c in choices]

    # Get first Pokémon
    p1 = input("Enter first Pokémon: ").strip().lower()
    while p1 not in choices_lower:
        print("Invalid choice. Try again.")
        p1 = input("Enter first Pokémon: ").strip().lower()

    # Get second Pokémon
    p2 = input("Enter second Pokémon: ").strip().lower()
    while p2 not in choices_lower:
        print("Invalid choice. Try again.")
        p2 = input("Enter second Pokémon: ").strip().lower()

    p1 = choices[choices_lower.index(p1)]
    p2 = choices[choices_lower.index(p2)]

    return p1, p2

# 3 Function: Battle System with Randomized Attack & Defense
def battle(player_pokemon, opponent_pokemon):
    """Turn-based battle with labeled Pokémon names to distinguish duplicates."""
    # Label if Pokémon names are the same
    if player_pokemon == opponent_pokemon:
        player_label = f"{player_pokemon} 1"
        opponent_label = f"{opponent_pokemon} 2"
    else:
        player_label = player_pokemon
        opponent_label = opponent_pokemon

    player_hp = pokemon_data[player_pokemon]["HP"]
    opponent_hp = pokemon_data[opponent_pokemon]["HP"]

    print("\n🔥 Battle Start! 🔥\n")
    print(f"{player_label} enters the battlefield!")
    print(pokemon_ascii[player_pokemon])  # Show ASCII art
    print(f"{opponent_label} appears as the opponent!")
    print(pokemon_ascii[opponent_pokemon])  # Show ASCII art

    while player_hp > 0 and opponent_hp > 0:
        # Player 1 attacks
        damage = calculate_damage(player_pokemon, opponent_pokemon)
        opponent_hp -= damage
        print(f"\n{player_label} attacks {opponent_label} for {damage} damage! {opponent_label} HP: {max(0, opponent_hp)}")

        if opponent_hp <= 0:
            print(f"\n🎉 {opponent_label} fainted! {player_label} wins!")
            return

        # Player 2 attacks
        damage = calculate_damage(opponent_pokemon, player_pokemon)
        player_hp -= damage
        print(f"\n{opponent_label} attacks {player_label} for {damage} damage! {player_label} HP: {max(0, player_hp)}")

        if player_hp <= 0:
            print(f"\n💀 {player_label} fainted! {opponent_label} wins!")
            return

# 4 Function: Calculate Randomized Damage
def calculate_damage(attacker, defender):
    """Calculate battle damage using randomized attack and defense values."""
    attack = random.randint(*pokemon_data[attacker]["Attack"])
    defense = random.randint(*pokemon_data[defender]["Defense"])
    attacker_type = pokemon_data[attacker]["Type"]
    defender_type = pokemon_data[defender]["Type"]

    multiplier = effectiveness.get((attacker_type, defender_type), 1.0)

    damage = max(1, int((attack - (defense * 0.5)) * multiplier))

    return damage

# 5 Function: Get Your Lucky Pokémon
def luckypokemon():
    """Randomly selects a lucky Pokémon from a list of 50 Pokémon."""
    
    pokemon_list = [
        "Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", 
        "Meowth", "Psyduck", "Snorlax", "Eevee", "Gyarados", 
        "Lapras", "Ditto", "Vaporeon", "Jolteon", "Flareon",
        "Machamp", "Gengar", "Dragonite", "Mewtwo", "Mew",
        "Togepi", "Espeon", "Umbreon", "Scizor", "Heracross",
        "Blaziken", "Swampert", "Sceptile", "Gardevoir", "Salamence",
        "Metagross", "Lucario", "Garchomp", "Infernape", "Torterra",
        "Empoleon", "Roserade", "Glaceon", "Leafeon", "Togekiss",
        "Zoroark", "Hydreigon", "Greninja", "Aegislash", "Talonflame",
        "Sylveon", "Decidueye", "Incineroar", "Primarina", "Zacian"
    ]

    lucky_pokemon = random.choice(pokemon_list)
    
    return f"✨ Today your lucky Pokémon is... {lucky_pokemon}! ✨"
