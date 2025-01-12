# Code from the lecture videos
# Covers the following:
#
#   1) Filter Rows
#   2) Select columns by column name and a range of columns - select()
#   3) Using pipe (%>%)
#   4) Preview the data using - View()
#   5) Check the class using - class()
#   6) Choose rows based criteria - filter()
#   7) Group and summarize
#   8) Rename columns
#   9) Create columns
#   10) Order Columns
#   11) Create new variables using mutate()
#   12) Order variables using arrange()
#   13) Rename the variable using rename()
#
# ------------------------------------------------------------------------------
library(tidyverse)

interviews <- read_csv("SAFI_clean.csv")

# Inspect the data 

interviews

# Preview the data

View(interviews)

# Check the class of the data

class(interviews)

# Select columns throughout the data frame

select(interviews, village, no_membrs, months_lack_food)

# Select a **series** of connected columns

select(interviews, village:respondent_wall_type)

# To select all but one column, using the negative sign 

select(interviews, -village)


# Choose rows based on specific criteria using the filter() function

filter(interviews, village == "Chirodzo")

# Filter observations with "and" operator (comma)

filter(interviews, village == "Chirozdo",
       rooms > 1,
       no_meals > 2)

# Filter using the "and" statements with the & operator instead of commas
# filters observations with the "&" logical operator

filter(interviews, village == "Chirozdo",
       rooms > 1 &
       no_meals > 2)

# Filters using an "or" and the logical operator "|"
filter(interviews, village == "Chirozdo" | village == "Ruaca")


# using the pipe operator
# Examples of the Pipe operator

# Method 1 - intermediate steps

interviews2 <- filter(interviews, village == "Chirodzo")
interviews_ch <- select(interviews2, villge:respondent_wall_type)

# Method 2 - nested functions

interviews_ch <- select(filter(interviews, village == "Chirozdo"),
                        villge:respondent_wall_type)

# Method 3 ---------------------------------------------
interviews %>% 
  filter(village == "chirodzo") %>%
  select(village:respondent_wall_type)

# To return the operation by assigning a new object 
interviews_ch <- interviews %>% 
  filter(village == "chirodzo") %>%
  select(village:respondent_wall_type)


# Group and Summarize ##########################
# Note: group_by() and summarize are usually used together.
#   Can use other functions in place of the mean(), can use max(), sum() 
#   functions 


#  View unique values in the column of the data frame 
unique(interviews$village)

# Group by a single column - village
interviews2 <- interviews %>% 
  group_by(village) %>%
  summarize(mean_no_membrs = mean(no_membrs)) 

# Group by multiple columns
# mean_no_membrs is a **NEW** variable name

interviews2 <- interviews %>% 
  group_by(village, ) %>%
  summarize(mean_no_membrs = mean(no_membrs)) 


# Getting the TALLY of a specific category
# Use the count() on a categorical value

interviews %>% count(village)


# Create new variables
interviews3 <- interviews %>% 
  mutate(people_per_room = no_membrs / rooms)

view(inteviews3)


# Order the variables' values
# Note: arrange() can order the variables by ascending order

interviews4 <- interviews %>% 
  arrange(interview_date)

view(inteviews4)

# Descending order
# is.na() - used to determine a missing value

interviews4 <- interviews %>%
  filter(!is.na(memb_assoc)) %>%
  group_by(village, memb_assoc) %>%
  summarize(mean_no_membrs = mean(no_membrs),
            min_membrs = min(no_membrs)) %>%
  arrange(desc(min_membrs))

view(interviews4)

# arrange by two variables
# Note: village will ascending while min_membrs will be descending

interviews5 <- interviews %>%
  filter(!is.na(memb_assoc)) %>%
  group_by(village, memb_assoc) %>%
  summarize(mean_no_membrs = mean(no_membrs),
            min_membrs = min(no_membrs)) %>%
  arrange(village, desc(min_membrs))

view(interviews5)

# Renaming variables 

interviews5 <- interviews %>%  
  filter(!is.na(memb_assoc)) %>%
  group_by(village, memb_assoc) %>%
  summarize(mean_no_membrs = mean(no_membrs),
            min_membrs = min(no_membrs)) %>%
  arrange(desc(min_membrs))
  

interviews5 %>% rename("test" = "village")













