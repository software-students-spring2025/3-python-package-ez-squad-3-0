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
    print("\n Available Pokémon \n")
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

    if p1 == p2:
        return f"{p1} (1)", f"{p2} (2)"
    else:
        return p1, p2

# 3 Function: Battle System with Randomized Attack & Defense
def battle(player_pokemon, opponent_pokemon):
    """Turn-based battle with random attack and defense values."""
    player_base = player_pokemon.split(" (")[0]
    opponent_base = opponent_pokemon.split(" (")[0]

    player_hp = pokemon_data[player_base]["HP"]
    opponent_hp = pokemon_data[opponent_base]["HP"]

    print("\n Battle Start! \n")
    print(f"{player_pokemon} enters the battlefield!")
    print(pokemon_ascii[player_base])  # Show player Pokémon
    print(f"{opponent_pokemon} appears as the opponent!")
    print(pokemon_ascii[opponent_base])  # Show opponent Pokémon

    while player_hp > 0 and opponent_hp > 0:
        # Player attacks
        damage = calculate_damage(player_base, opponent_base)
        opponent_hp -= damage
        print(f"\n{player_pokemon} attacks {opponent_pokemon} for {damage} damage! {opponent_pokemon} HP: {max(0, opponent_hp)}")

        if opponent_hp <= 0:
            print(f"\n {opponent_pokemon} fainted! {player_pokemon} wins!")
            return

        # Opponent attacks
        damage = calculate_damage(opponent_base, player_base)
        player_hp -= damage
        print(f"\n{opponent_pokemon} attacks {player_pokemon} for {damage} damage! {player_pokemon} HP: {max(0, player_hp)}")

        if player_hp <= 0:
            print(f"\n {player_pokemon} fainted! {opponent_pokemon} wins!")
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
    
    return f" Today your lucky Pokémon is... {lucky_pokemon}! "