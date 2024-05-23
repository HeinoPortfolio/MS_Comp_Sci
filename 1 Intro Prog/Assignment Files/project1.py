# -*- coding: utf-8 -*-
# 
# Matthew Heino
#******************************************************************************
import matplotlib.pyplot as plt
import numpy as np
import random

def get_number_of_tests() -> int:
    
    ''' Get the number of tests from the user.'''
    
    num_tests = int(input("Please enter the number of tests: "))
    
    return num_tests


def randu_test(tests:int) -> int:
    print("Tests: ", tests, "Type:",type(tests))
    
    return 0

def random_num_gen_test(tests:int) -> int: 
    
    random_num = []
    random_num = [random.randrange(0, 10) for val in range(0, tests)]
    
    return random_num

def return_nine(tests: int) -> int:
    
    random_num = []
    random_num += tests * [9]   

    return random_num
 
    
def menu() -> str:
    
    print("Please enter a menu options from the list below.\n")
    print("1: Use Random Number Generator Function")
    print("2: Non-random (All 9s)")
    print("3: Randu Test")
    print("4: Quit")
    
    user_choice = input("Enter your choice: ")

    return user_choice

def plot_occurences(ran_num: int):
    
    numbers = np.array(ran_num)
    
    #plot the frequency of the numbers.
    plt.hist(numbers)
    
    # show the graph
    plt.show()
    

# Defining main function. 
def main(): 
    
    num_tests = 0
    random_numbers = []
    
    while True:
        
        option = menu()
      
        # Process the user's choice
        if option == '1':
            
            print("Random number generator test.")
            num_tests = get_number_of_tests()
            random_numbers = random_num_gen_test(num_tests)
            plot_occurences(random_numbers)
            random_numbers.clear()
        
        elif option == '2': 
            
            print("Non-random test")
            num_tests = get_number_of_tests()
            random_numbers = return_nine(num_tests)
            random_numbers.clear()
            
        elif option == '3':
            print("Randu test test")
            print("Not implemented!")
            #num_tests = get_number_of_tests()
        
        elif option == '4':
            print("Quit")
            break
        else:
            print("Entered invalid choice. Please make another selection")
            
        print("Number of Tests: ", num_tests)
  

if __name__=="__main__": 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    main()