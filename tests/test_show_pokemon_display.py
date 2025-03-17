import pytest
from pypokemon import show_pokemon

def test_show_pokemon_display(capsys):
    """Check if all Pokémon names appear in output."""
    show_pokemon()
    captured = capsys.readouterr()
    
    assert "Venusaur appears!" in captured.out
    assert "Charizard appears!" in captured.out
    assert "Blastoise appears!" in captured.out
