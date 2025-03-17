import pytest
from pypokemon import show_pokemon, pokemon_data

def test_show_pokemon_stats(capsys):
    """Verify if HP, Attack, Defense, and Type are printed correctly."""
    show_pokemon()
    captured = capsys.readouterr()
    
    for name, stats in pokemon_data.items():
        assert f"HP: {stats['HP']}" in captured.out
        assert f"Attack Range: {stats['Attack']}" in captured.out
        assert f"Defense Range: {stats['Defense']}" in captured.out
        assert f"Type: {stats['Type']}" in captured.out
