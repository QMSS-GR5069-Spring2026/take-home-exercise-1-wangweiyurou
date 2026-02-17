def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Test the function
data = [10, 20, 30, 40, 50]
avg = calculate_average(data)
print(f"Average: {avg}")
