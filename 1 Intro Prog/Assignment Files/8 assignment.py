# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:10:45 2024

@author: mehei
"""

# Web Address: 
    
def process_file(file_name):
    
    macbeth_dict = {}
    
    try:
        with open(file_name, 'r') as macbeth_file:
            
            for file_line in macbeth_file:
              
                if (file_line.isspace() != True):
                    
                    #print(file_line)
                    split_word_list = file_line.split()
                    
                   # print(split_word_list)
                    
                    for word in split_word_list:
                        if word not in macbeth_dict.keys():
                            macbeth_dict[str(word)] = 1
                        else:
                            macbeth_dict[word] += 1
                    
                    
    
    except:
        print('File: ', file_name, 'not found!') 
        
        macbeth_dict ={'Error' : 'File not found'}
        

    return macbeth_dict


# main progral
macbeth_filename = 'Macbeth.txt'
macbeth_filename2 = 'philbert.txt'
macbeth_filename3 = 'test.txt'
macbeth_filename4 = 'test2.txt'

# call the function
macbeth_dict = process_file(macbeth_filename)


# Print the frequencie
for key, value in macbeth_dict.items():
   print('Key: ', key, 'Value: ', value)


  
print('Value: ', macbeth_dict["the"] )
print('Value: ', macbeth_dict["The"] )
print('Value: ', macbeth_dict["thee"] )
print('Value: ', macbeth_dict["of"] )
print('Value: ', macbeth_dict['Sunne'] )
print('Value: ', macbeth_dict['place?'] )
print('Value: ', macbeth_dict['Vpon'] )
print('Value: ', macbeth_dict['shall'] )   
print('Value: ', macbeth_dict['When'] )
print('Value: ', macbeth_dict['3.'] )
    
    
    
    

