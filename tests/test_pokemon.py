
import pytest
from pypokemon import luckypokemon
from pypokemon import calculate_damage, effectiveness
from pypokemon import battle
from pypokemon import show_pokemon, pokemon_ascii, pokemon_data
from pypokemon import select_pokemon
from unittest.mock import patch

def test_show_pokemon_ascii(capsys):
    """Ensure ASCII art for each Pokémon appears in output."""
    show_pokemon()
    captured = capsys.readouterr()
    
    for name, art in pokemon_ascii.items():
        assert art.strip() in captured.out

def test_show_pokemon_display(capsys):
    """Check if all Pokémon names appear in output."""
    show_pokemon()
    captured = capsys.readouterr()
    
    assert "Venusaur appears!" in captured.out
    assert "Charizard appears!" in captured.out
    assert "Blastoise appears!" in captured.out

def test_show_pokemon_stats(capsys):
    """Verify if HP, Attack, Defense, and Type are printed correctly."""
    show_pokemon()
    captured = capsys.readouterr()
    
    for name, stats in pokemon_data.items():
        assert f"HP: {stats['HP']}" in captured.out
        assert f"Attack Range: {stats['Attack']}" in captured.out
        assert f"Defense Range: {stats['Defense']}" in captured.out
        assert f"Type: {stats['Type']}" in captured.out

def test_battle_prints_output(capfd):
    """Test if battle() produces printed output."""
    battle("Charizard", "Blastoise")
    captured = capfd.readouterr()
    assert "Battle Start!" in captured.out
    assert "attacks" in captured.out
    assert "wins!" in captured.out or "fainted!" in captured.out

def test_battle_declares_winner(capfd):
    """Test if battle() always declares a winner."""
    battle("Venusaur", "Charizard")
    captured = capfd.readouterr()
    assert "wins!" in captured.out, "Battle result should declare a winner."

def test_battle_varied_results(capfd):
    """Test if battle() can have different winners over multiple simulations."""
    results = set()

    for _ in range(20):  # Run more battles to increase randomness
        battle("Charizard", "Blastoise")

    captured = capfd.readouterr()  # Capture the output after all battles

    if "Charizard wins!" in captured.out:
        results.add("Charizard")
    if "Blastoise wins!" in captured.out:
        results.add("Blastoise")


def test_calculate_damage_returns_integer():
    """Test if calculate_damage() returns an integer."""
    damage = calculate_damage("Charizard", "Blastoise")
    assert isinstance(damage, int), "Damage should be an integer."

def test_calculate_damage_positive_value():
    """Test if calculate_damage() always returns a positive value (at least 1)."""
    damage = calculate_damage("Venusaur", "Charizard")
    assert damage >= 1, "Damage should be at least 1."


def test_calculate_damage_effectiveness():
    """Test type effectiveness by controlling randomness."""
    # Save original effectiveness
    original_effectiveness = effectiveness.copy()

    # Mock random.randint to always return fixed attack and defense values
    with patch("random.randint", side_effect=[25, 15]):  # Attack=25, Defense=15
        damage_with_effectiveness = calculate_damage("Charizard", "Venusaur")

    # Disable effectiveness
    effectiveness.clear()

    with patch("random.randint", side_effect=[25, 15]):  # Same values to ensure fairness
        damage_without_effectiveness = calculate_damage("Charizard", "Venusaur")

    # Restore effectiveness
    effectiveness.update(original_effectiveness)

    assert damage_with_effectiveness > damage_without_effectiveness, \
        "Damage with type effectiveness should be greater than without it."



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


def test_luckypokemon_returns_string():
    """Test if luckypokemon() returns a string."""
    result = luckypokemon()
    assert isinstance(result, str), "The function should return a string."

def test_luckypokemon_randomness():
    """Test if luckypokemon() produces different results over multiple calls."""
    results = {luckypokemon() for _ in range(10)}
    assert len(results) > 1, "The function should return different Pokémon names over multiple calls."

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
        assert p1 == "Blastoise (1)"
        assert p2 == "Blastoise (2)"
