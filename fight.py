def fight(pokemon1, pokemon2):
    """Simulates a battle between two Pokémon based on type advantages."""
    
    type_advantage = {
        "Charmander": "Bulbasaur",  # Fire beats Grass
        "Bulbasaur": "Squirtle",  # Grass beats Water
        "Squirtle": "Charmander"  # Water beats Fire
    }

    if pokemon1 == pokemon2:
        return "It's a draw! Both Pokémon are equally matched."
    elif type_advantage[pokemon1] == pokemon2:
        return f"{pokemon1} wins! 🔥"
    else:
        return f"{pokemon2} wins! 🎉"
