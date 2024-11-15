import dice_roller

def main():
    num_rolls = int(input("Enter the number of rolls: "))
    sides = int(input("Enter the number of sides on the die: "))
    
    # Initialize dictionary with each side as a key and 0 as the count
    roll_counts = {side: 0 for side in range(1, sides + 1)}
    
    # Roll the dice and record the results
    for _ in range(num_rolls):
        roll = dice_roller.roll_die(sides)
        roll_counts[roll] += 1
    
    # Calculate probabilities and display results
    print(f"\n{'Side':<10}{'Rolls':<10}{'Probability (%)':<15}")
    for side, count in roll_counts.items():
        probability = (count / num_rolls) * 100
        print(f"{side:<10}{count:<10}{probability:.2f}")
    
if __name__ == "__main__":
    main()
