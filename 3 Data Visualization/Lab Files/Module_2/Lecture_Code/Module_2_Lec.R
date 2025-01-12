# Code from the lecture videos
# Covers the following:
#
#   1) Filter Rows
#   2) Select columns by column name and a range of columns - select()
#   3) Using pipe (%>%)
#   4) Preview the data using - View()
#   5) Check the class using - class()
#   6) Choose rows based criteria - filter()
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

























