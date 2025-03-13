def choose(pokemon_name):
    """Allows the player to choose a Pokémon."""
    
    valid_pokemon = ["Charmander", "Bulbasaur", "Squirtle"]
    
    if pokemon_name not in valid_pokemon:
        raise ValueError(f"Invalid choice! Please select from {valid_pokemon}")
    
    print(f"You have chosen {pokemon_name}!")
    return pokemon_name
