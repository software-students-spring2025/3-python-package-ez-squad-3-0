import pytest
from pypokemon import show_pokemon, pokemon_ascii

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