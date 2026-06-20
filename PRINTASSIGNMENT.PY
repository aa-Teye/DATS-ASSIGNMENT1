def countdown(n):
    """Print a countdown from n to 0."""
    for i in range(n, -1, -1):
        print(i)


if __name__ == "__main__":
    try:
        value = int(input("Enter a number to count down from: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        countdown(value)
print("Countdown complete!")