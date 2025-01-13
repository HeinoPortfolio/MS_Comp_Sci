#install.packages("tidyverse")
#install.packages("readr")

library(tidyverse)
library(readr)

# 2. Set the working directory
#setwd(dirname(rstudioapi::getSourceEditorContext()$path))
#getwd()

# 3. Read csv file into R using the function read_csv().

Salaries <- read_csv("Salaries.csv")



# 4. Use select, filter, group_by, and tally (count) the results

Salaries_new <- Salaries %>% 
  select(rank, discipline, sex, salary) %>%
  filter(!is.na(salary)) %>%
  group_by(rank, discipline, sex) %>%
  count()
  


# 5. using spread() to transfer the "sex" column to many more columns based on the values in sex.
# Use spread(): spread(data, key, value, fill = NA, convert = FALSE, drop = TRUE, sep = NULL)
# + Please use the data frame "Salaries_new" for the spread() operation
# + Please split the column “sex” in the data frame "Salaries_new" to many more columns based on the values in sex
# + Have the values of n(tally count) for the new columns.
# + Fill the missing value with "FALSE" by setting "fill=FALSE"
# + Assign the output to an object "wide"
# + Use pipe operator in this case

wide<- Salaries_new %>% 
  spread(key=sex, value=n, fill=FALSE)





# 6. Reshape the table from wide to long: using gather() to combine multiple "sex" related columns to one column sex
# Use gather(): gather(data, key, value, ..., na.rm = FALSE, convert = FALSE, factor_key = FALSE)
# + Please reshape the data frame "wide" obtained from spread() into the long table 
# + In the spread() step, you will get two columns about sex "Female" and "Male"
# + Please make the two sex columns into one column and name the column as "sex"
# + Please have the values in the two sex columns for a new column "n" (tally count)
# + Remove the NA by setting "na.rm=TRUE"
# + Use pipe operator in this case

long <- wide %>% 
  gather(key = "sex", value="n", 3:4, na.rm = TRUE, convert = FALSE, factor_key = FALSE)
  
  
  
