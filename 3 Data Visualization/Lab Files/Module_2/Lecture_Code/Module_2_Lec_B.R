# Code from the lecture videos
# Covers the following:
#
#   1) Import data from a file using:
#       - library readr
#       - read.csv()
#       - read_tsv
#
#   2) Import data  from a MS Excel file using:
#       - library readxl
#       - read_excel()
#
#   3) Using statistical packages
#       - haven
#   4) 
#
# ------------------------------------------------------------------------------
#install.packages("carData")

library(carData)
data("salaries")
names("salaries")

# Use the readr library readr
library(readr)


# Import data from a comma limited file

salaries <- read.csv('salaries.csv')

# import data from a tab delimited file - a text file

salaries_txt <- read_tsv("salaries.txt")


# Excel Spreadsheets 
# To read Excel spreadsheets, the readxl package can import data from Excel 
# workbooks. Both xls and xlsx formats are supported

library(readxl)


# Workbooks can have more than one worksheet, you can specify the sheet desired 
# with the sheet=1 argument

Salaries2 <- read_excel("Salaries.xlsx", sheet=1)


# Statistical packages
# Haven package provides functions for importing data from a variety 
# of statistical packages

library(haven)

# Import data from Stata

salaries <- read_dta("salaries.dta")

# Import data from SPSS

salaries <- read_sav("salaries.sav")

# Import data from SAS
salaries <- read_sas("salaries.sas7bdat")
















