#Python Example to loop through an array of numbers and print them

def set_of_numbers(num_array):

    index = 0
    while index < len(num_array):
        print("Number is: " + str(num_array[index]))
        index += 1

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    set_of_numbers(numbers)
