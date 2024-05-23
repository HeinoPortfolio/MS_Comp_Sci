# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:03:57 2024

@author: mehei
"""


import random
import matplotlib.pyplot as plot


def menu():
    
    option = -1
     
     
    print('1. Test the python random.randrange()')
    print('2. Test the dilbert() function')
    print('3. Test the randu() function')
    print('4. Quit this program')
     
    while True:
         
        # ask the user for input
         option = input('Please select an option: ')
         
         # check the value entered
         if option == '1':
             return option
         elif option == '2':
             return option
         elif option == '3':
             return option
         elif option == '4':
            return option
            break
         else:
           print('That is not a valid option. Please try again.')


def test_random_randrange(num_to_test):
    ''' Tests the randomrange function '''
    
    random.seed(1)
    
    num_0 = 0
    num_1 = 0
    num_2 = 0
    num_3 = 0
    num_4 = 0
    num_5 = 0
    num_6 = 0
    num_7 = 0
    num_8 = 0
    num_9 = 0
   
    # perform the desired number of tests (num_to_test)
    for test in range(0, 25):
        
        # generate a random number
        rand_num = random.randrange(0,10)
        
        # count the frequency of the number
        
        if rand_num == 0:
            num_0 += 1
        elif rand_num == 1:
            num_1 += 1
        elif rand_num == 2:
            num_2 += 1
        elif rand_num == 3:
            num_3 += 1
        elif rand_num == 4:
            num_4 += 1
        elif rand_num == 5:
            num_5 += 1
        elif rand_num == 6:
            num_6 += 1
        elif rand_num == 7:
             num_7 += 1
        elif rand_num == 8:
             num_8 += 1
        elif rand_num == 9:
             num_9 += 1     

    # Print the number of the occurences
    print("Digit Number of times generated")
    
    print(f"{'0':^5}{num_0:^8}")
    print(f"{'1':^5}{num_1:^8}")
    print(f"{'2':^5}{num_2:^8}")     
    print(f"{'3':^5}{num_3:^8}")
    print(f"{'4':^5}{num_4:^8}")
    print(f"{'5':^5}{num_5:^8}")
    print(f"{'6':^5}{num_6:^8}")
    print(f"{'7':^5}{num_7:^8}")
    print(f"{'8':^5}{num_8:^8}")
    print(f"{'9':^5}{num_9:^8}")
    
    # create the graph using matplotlib
    # display the results as a graph
    figure = plot.figure()  # start with a blank figure
    axes = figure.add_axes([0,0,1,1])
    labels = ['0','1','2','3','4','5','6','7','8','9']
    values = [num_0, num_1,num_2, num_3
              , num_4, num_5,num_6,num_7,num_8,num_9]
    axes.bar(labels,values)
    axes.set_title('Counts: random.randrange()')
    plot.show()


#******************************************************************************
# call the menu function.

#print(f"The menu function returned {menu()}.")

# Call your function here to test it.  Does it work correctly?
test_random_randrange(25)












