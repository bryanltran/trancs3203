def sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return(sum)

def product(arr):
    product = 1

    for i in arr:
        product = product * i

    return(product)

def reverse_array(arr):
    return arr[::-1]

def main():
    # Initialize an empty list to store the integers
    integer_list = []

    while True:
        try:
            # Read an integer from the user
            user_input = input("Enter an integer (or -1 to stop): ")

            # Convert the input to an integer
            num = int(user_input)

            # Check if the user wants to stop
            if num == -1:
                break

            # Append the integer to the list
            integer_list.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer or -1 to stop.")

    # Print the results
    print("Sum: " + str(sum(integer_list)))
    print("Product: " + str(product(integer_list)))
    print("Reverse: " + str(reverse_array(integer_list)))


if __name__ == "__main__":
    main()
