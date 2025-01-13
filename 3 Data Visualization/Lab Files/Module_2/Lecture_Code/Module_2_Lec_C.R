# Covers the following:
#
#   1) Reshaping data into long formats from wide:
#       - using spread()
#
#   2) Reshaping data into wide formats from long:
#       - using gather()
#
# ------------------------------------------------------------------------------

library(tidyverse)


interviews <- read.csv("SAFI_clean.csv")

# convert from long format to the wide format
#
# Notes: 
#
#     1) use the mutate() function to create a new columns for the combined data 
#         to use a logical value to assign the new columns
#
#     2) respondent_wall_type is the variable that will be split 
#
#     3) wall_type_logical the value that will be assigned to the new column
#
#     4) fill --> if nothing meets the combination fill with FALSE values
#
#     5) The old column ,the column that was split, will disappear from 
#         the new table
#
# #############################################################################

wide <- interviews %>% 
  mutate(wall_type_logical = TRUE) %>%
  spread(respondent_wall_type, wall_type_logical, fill = FALSE)

# Convert  from wide back to long
#
# Notes:
#
#   1) will need to create some new variable(s) for the column, can use 
#       previous names or a new name for the variable-- can be defined 
#       by the programmer
#
#   2) (ncol(wide) - 3): ncol(wide) -- the number of columns that will 
#       be combined
#
#   3) ncol() -- a function to see how many columns are -- the width 
#       of the data frame
#
#   4) na.rm = TRUE -- remove the missing values from the resulting data frame 
#
# ##############################################################################


back_To_long <- wide %>%
  gather(wall_type, logical_value, (ncol(wide) - 3): ncol(wide), na.rm = TRUE)



















