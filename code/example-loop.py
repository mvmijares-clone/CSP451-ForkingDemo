#Python Example to loop through an array of numbers and print them

def set_of_numbers(num_array):

#More efficient Loop
    for num in num_array:
        print("Number is: " + str(num))
        
if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    set_of_numbers(numbers)
