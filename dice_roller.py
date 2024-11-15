import random

def roll_die(sides):
    if sides < 4:
        raise ValueError("Dice must have at least 4 sides.")
    return random.randint(1, sides)

def test_dice_roller():
    # Test D6
    for _ in range(100):
        roll = roll_die(6)
        assert 1 <= roll <= 6, f"Invalid roll for D6: {roll}"
    
    # Test D10
    for _ in range(100):
        roll = roll_die(10)
        assert 1 <= roll <= 10, f"Invalid roll for D10: {roll}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_dice_roller()
