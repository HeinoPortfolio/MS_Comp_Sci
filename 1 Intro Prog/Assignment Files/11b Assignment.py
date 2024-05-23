# -*- coding: utf-8 -*-
"""
Created on Fri May 17 04:13:15 2024

@author: mehei
"""

#x = re.findall(r"\b[0-9]{5}\b", txt)




import re

file_name = "MSDSwebsite.txt"


file_name2 = "philbert.txt"




def prcocess_webpage(filename):
    
    contents = ''
    
    try: 
        with open(filename, 'r') as web_file:
            line = web_file.readline()
        
            while line: 
                contents += line.strip()
                # read the next line
                line = web_file.readline()
                
        return contents
    
    except FileNotFoundError:
        return 'There is no file named '+ filename +' in this directory.'
    
    
    

    
str_result = prcocess_webpage(file_name)

print(str_result)
    
"""
#print(file_txt)

#file1 = open('testtext.txt', 'w')

#file1.close()

# look for phone number
# parse the string for phone numbers
match_list =[]

for phone_num in re.finditer(
        r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b"
        , file_txt):
   
   # print("Found: ", phone_num)
    match_list.append(phone_num.group())
   
# print the results
print(match_list)



# look for 5 digit numbers.

#zip_list= re.findall(r"\b[0-9]{5}\b", file_txt)
zip_list= re.findall(r"[0-9]{5}", file_txt)

print(zip_list)



"""
"""with open('testtext.txt','w') as write_file:
    write_file.write(file_txt)
    
"""
"""
test_str = "Hello my cell phone number is (516) 884-0416 and my home phoe is 8603768186"
test_str2 ='<div class="contactline">Ball State University 2000 W. University Ave. Muncie, IN 47306 800-382-8540 and 765-289-1241</div> <div class="contactline">Ball State University 2000 W. University Ave. Muncie, IN 47306 800-382-8540 and 765-289-1241</div>'
test_str3 = ' <script src="/Components/Design/ResponsiveV2/js/v-638193146760000000/jquery-1.11.1.min.js"></script>'


match_list =[]

# parse the string for phone numbers
for phone_num in re.finditer(
        r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b"
        , test_str2):
   
   # print("Found: ", phone_num)
    match_list.append(phone_num.group())
   
# print the results
#print(match_list)

for index in range(0, len(match_list)):
    print (match_list[index])
    
    
# Find zip code-like numbers

zip_list= re.findall(r"\b[0-9]{5}\b", test_str3)

print('\n', zip_list)
   
""" 
