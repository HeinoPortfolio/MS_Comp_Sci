# Folder Overview
This directory holds the Jupyter Notebooks that were created for the weekly assignment. You will find a listing of the notebook files and a short description at the end of the page. 

# Competencies
- The ability to write functions to facilitate code reuse
- The ability to to use control structures (looping and conditional statements).
- The ability to create a tuple, lists, dictionaries, and other structures.
- Create list comprehensions.

# Technologies and Concepts Used

The concepts and technologies used to create and complete the assessments are the following:
* Libraries used:

   - random
   - pandas
   - math
   - numpy
   - re
   - requests
   - TextBlob (NaiveBayesAnalyzer)
   - nltk
   - Textatistic
   - BeautifulSoup
     
- Data cleaning, data analysis, and data visualization
- Web scraping

# Assignment Files 

**Note:** Some items discussed in the notebook are not available in this saved version.  These items are only available on the course site.

|**File Name**|**Purpose**|**Additional Comments**|
|:-----:|:-----:|:-----|
| [Assignment3a.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment3a.ipynb) | To gain familiarity with Jupyter Notebooks and simple function creation| Simple and introductory assignment that covers the basics of function use and creation.  It introduces how to use the Notebook in an the academic environment. 
|[Assignment3b.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment3b.ipynb)|Practice defining (creating) a function, practice calling (using) a function and using interation| None
|[Assignment4.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment4.ipynb)| Gain practice creating functions by creating two functions and integrating these functions into a single program| None
|[Assignment5.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment5.ipynb)|A program that will loop through grades. These grades will stored in a simple list. The average of the grades willl be calculated | Makes use of a for loop |
|[Assignment6a.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment6a.ipynb)  | Assignment to convert a string to a list of individual characters. Use the **slice()** operator to create a list that contains every other character in the original list. Functions in this program: 1. Returns an integer that represents the number of times the letter 'e' is found in a string. 2) A function that takes uses one argument and returns every other characted from that string. Function that will return a tuple that contains the only the first 5 characters in a string.   | Makes use of the  **slice()** method. |
|[Assignment6b.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment6b.ipynb) | Practice manipulating lists. Practice using for loops with lists. Practice sorting loops. Functions in this program: 1) Functions that will append a new word as long it is not already in the list. 2) Functions accepts a list of words and returns a copy of the list with the words converted to **title case**.   | Makes use of the **title()** method. and the **sort()** method. |
|[Assignment7a.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment7a.ipynb)|  Function that will multiply a list element by 100. Function # 2 will accomplich the same tasks as function as  the first function, but will use a **list comprehension** to accomplisth the task. | Uses a **list comprehension** and a formatted printed statement for the output.|
|[Assignment7b.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment7b.ipynb)|First function task is to convert a string containing a Roman numeral into and integer and then return the resulting number. |Create a **dictionary**.  |
|[Assignment8.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment8.ipynb)|Practice in using text files.  To read in text from a file and then manipulate the contents of the file. Practiced using a **dictionary**.  First function was to read in the given file and add the words to the **dictionary**.  This function counted the number of times the word appeared in the text.  | Made use of the **split()** function.  This notebook made use of the **Macbeth.txt** file that is located in the directory. |
|[Assignment9.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment9.ipynb)|This assignment was to practice creating an ndarray. Additionally, this assignment was to practice using the concept of **slicing** to view subsets of an array. The assignment made use of a **DataFrame** to view the results. The first fucntion was to create an 2D array of student exam scores. The next function was to create the **DataFrame**.  This DataFrame had custom rows and column labels. | Concepts of **slicing** and the use of a **DataFrame** were used.  -- Custom columns and rows. |
|[Assignment10.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment10.ipynb)|This assigment will practice ways on how to manipulate strings.  The first function is to center all words in a string vertically. This method will find the longest string. The function will output the each element of the string on a separate line.  These elements will be centered based on the length of the longest word. The second function will replace all occurrences of the word "the" with a grinning emoji. The third function will replace all  four letter words with a different emoji. The replacement emoji will change each time and will start with the grinning emojis. This function will return the string with the emojis inserted into it. | Makes use of **emojis**.  Uses f'some_text' format string|
|[Assignment11a.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment11a.ipynb)|This is a program will translate English to pirate speak. It will use **regular expressions** to do the translation.  The first function will take a string and substitute a pirate word based on those words in the dictionary.  | Uses **regular expressions** and a **dictionary** |
|[Assignment11b.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment11b.ipynb)|The purpose of the assignment is to review data that can be found on a webpage. It will make use of the **re** package.  It will make use of the MSDSwebsite.txt file that can be found in this directory. The first function will take a string for the file and return the contents of the file.  The second function will extract only the phone numbers, as a list, that were found in the file an no other information. The final function will extract all numbers that are five digits in length. | Uses the **re** package.  Will read the text from a file. |
|[Assignment12a.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment12a.ipynb)|This assignment will perform the following tasks.  First it will report the total number of words in the **corpus**. Will output the **noun phrases** that are found in the supplied text. Will determine the **polarity** and **subjectivity** of the corpus (**sentiment analysis**). There is a function will generate the word counts for the text. Another function will generate the noun phrases found in the text. There will be function that will perform sentiment analysis yielding  polarity and the subjectivity of the text. | Makes use of the **TextBlob** module, and the **nltk** module. This is a menu driven program.  Will read the text from a file. |
|[Assignment12b.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment12b.ipynb)| Program will prompt the user to enter a sentence and it will perform sentiment analysis on the inputted text.  The program will output one of five **emojis** based on the sentiment of the sentence entered. There is a function that will determine the number of sentences in the text. Another function will report on the sentiment of the text.  The final function will utilize **NaiveBayesAnalyzer** for the sentiment of the text. | Makes use of **TextBlob** and **NaiveBayesAnalyzer**. |
|[Assignment13.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment13.ipynb)|This assignment will connect to a website, and extract text using **BeautifulSoup** package.  It will remove any **HTML** tags and then return the cleaned text for further processing. One function will use the **Textatistic** library to return a readability score for the text.  A function will perform sentiment analysis providing the polarity score. A function will print the first N sentences of the text.    | Makes use of **Textatistic** and **BeautifulSoup**.  Determines a readability score (Dale-Chall readability score).|
|[Assignment14.ipynb](https://github.com/HeinoPortfolio/MS_Comp_Sci/blob/main/1%20Intro%20Prog/Jupyter%20Notebook%20Assignments/Assignment14.ipynb)| Assignment will create a simple web browser.  Will make use of the **JSON** object for data/information storage. A method will connect to Wikipedia to request a specific article. This function will return a **JSON** object. The next function will return a string that will contain information about the sections contained in the article. | Makes use of the **JSON** object. Requesting information from a website using **requests**. |










