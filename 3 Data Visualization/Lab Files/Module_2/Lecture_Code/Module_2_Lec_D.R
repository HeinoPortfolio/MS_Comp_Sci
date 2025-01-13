# Covers the following:
#
#   1) Using the functions:
#       -- pivot_wider()
#       -- pivot_longer()
#
#   2) 
#
# ------------------------------------------------------------------------------

library(tidyverse)

interviews  <- read_csv("SAFI_clean.csv")

view(interviews)


# create  a new column to detect if wall type is true or false
# 
temp <- interviews %>%
  mutate(wall_type_logical = TRUE)



# Using spread(): deprecated function
#wide <- interviews %>% 
#  mutate(wall_type_logical = TRUE) %>%
#  spread(respondent_wall_type, wall_type_logical, fill = FALSE)


# Using pivot_wider(): new function
#
# Notes:
#
#   1) names_from --  new column names from the original data
#
#   2) values_from -- values come from the named column
#
#   3) values_fill -- set the value to TRUE or FALSE, if set to  FALSE
#     -- FALSE may correspond to null types if the value is not there 
#
#   4) 
#
# ##############################################################################

wide <- interviews %>%
  mutate(wall_type_logical = TRUE) %>%
  pivot_wider(names_from = respondent_wall_type, values_from = wall_type_logical,
              values_fill = FALSE)
  
  
  
# Using the gather(): deprecated function 
#long <- wide %>%
#  gather(wall_type, logical_value,(ncol(wide) - 3): ncol(wide), na.rm = TRUE)

# ##############################################################################
# using pivot_longer(): new function
#
# Notes:
#
#   1) (ncol(wide)-3):ncol(wide) -- which columns that will working on 
#
#   2) names_to -- want to combine the columns in the previous 
#       argument (ncol()...) to a new column of wall_type 
#
#   3) values_to -- this will be a new column name, the name is defined by 
#       the programmer
#
# ############################################################################## 

long <- wide %>%
  pivot_longer((ncol(wide)-3):ncol(wide), names_to = "wall_type",
               values_to = "logical_value", values_drop_na = )
  
  
  