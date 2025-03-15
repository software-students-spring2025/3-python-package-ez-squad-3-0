def select_pokemon():
    """Allows the player to choose two Pokémon for battle, including duplicates."""
    choices = ["Venusaur", "Charizard", "Blastoise"]
    
    print("\nChoose two Pokémon for battle:")
    for i, name in enumerate(choices, start=1):
        print(f"{i}. {name}")

    # Convert choices to lowercase for validation
    choices_lower = [c.lower() for c in choices]

    # Get first Pokémon
    p1 = input("Enter first Pokémon: ").strip().lower()
    while p1 not in choices_lower:
        print("Invalid choice. Try again.")
        p1 = input("Enter first Pokémon: ").strip().lower()

    # Get second Pokémon (allow duplicates)
    p2 = input("Enter second Pokémon: ").strip().lower()
    while p2 not in choices_lower:  # Removed the p1 == p2 restriction
        print("Invalid choice. Try again.")
        p2 = input("Enter second Pokémon: ").strip().lower()

    # Convert back to proper case
    p1 = choices[choices_lower.index(p1)]
    p2 = choices[choices_lower.index(p2)]

    return p1, p2

# Test the function
print(select_pokemon())
