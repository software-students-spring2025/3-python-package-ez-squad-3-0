import pytest
from pypokemon import luckypokemon, select_pokemon
from unittest.mock import patch
def test_luckypokemon():
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
    for i in range(100):
        result = luckypokemon()
        lucky_pokemon = result.split("... ")[1].split("!")[0]  # Extract Pokémon name
        assert lucky_pokemon in pokemon_list

def test_select_two_correct_input():
    # Mock input responses for valid selections (case insensitive, extra spaces)
    with patch("builtins.input", side_effect=["venusaur ", "charizard"]):
        p1, p2 = select_pokemon()
        assert p1 == "Venusaur"  # Ensuring correct name matching
        assert p2 == "Charizard"
    

def test_select_two_correct_one_wrong_input():
    with patch("builtins.input", side_effect=["blastoise", "InvalidPokemon", "charizard"]):
        p1, p2 = select_pokemon()
        assert p1 == "Blastoise"
        assert p2 == "Charizard"
    
def test_select_duplicate_input():
    # by design, users can select duplicate pokemons
    with patch("builtins.input", side_effect=["blastoise", "pikachu", "blastoise"]):
        p1, p2 = select_pokemon()
        assert p1 == "Blastoise"
        assert p2 == "Blastoise"
