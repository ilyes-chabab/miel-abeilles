import random

def generate_flower_positions(num_flowers):
    positions = []
    for _ in range(num_flowers):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        positions.append((x, y))
    return positions

def save_positions_to_file(positions, num_flowers):
    filename = f"field{num_flowers}.txt"
    with open(filename, "w") as file:
        file.write("x\ty\n")
        for x, y in positions:
            file.write(f"{x}\t{y}\n")

if __name__ == "__main__":
    num_flowers = int(input("Enter the number of flowers to generate: "))
    positions = generate_flower_positions(num_flowers)
    save_positions_to_file(positions, num_flowers)
    print(f"{num_flowers} flower positions have been generated and saved to 'field{num_flowers}.txt'.")
