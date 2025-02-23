def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to prevent ZeroDivisionError
    return sum(numbers) / len(numbers) 
    #Consider using statistics.mean() for better performance and handling of other edge cases.