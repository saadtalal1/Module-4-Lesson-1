start_value = int(input("Enter starting value: "))
end_value = int(input("Enter ending value: "))

odd_squares = []
even_squares = []

for i in range(start_value, end_value + 1):
    square = i**2
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Odd squares:", odd_squares)
print("Even squares:", even_squares)