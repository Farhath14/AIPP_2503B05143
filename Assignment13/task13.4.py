nums = []

n = int(input("How many numbers? "))

for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    nums.append(value)

squares = [i * i for i in nums]

print("Squares:", squares)