import pytest
from pypokemon import battle

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

    assert len(results) > 1, "Different battles should sometimes have different winners."