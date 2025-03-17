import pytest
from pypokemon import show_pokemon, pokemon_ascii

def test_show_pokemon_ascii(capsys):
    """Ensure ASCII art for each Pokémon appears in output."""
    show_pokemon()
    captured = capsys.readouterr()
    
    for name, art in pokemon_ascii.items():
        assert art.strip() in captured.out
