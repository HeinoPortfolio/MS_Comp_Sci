# Load the required libraries
library(tidyverse)
library(lubridate)


# set the directory
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# Read in the file
crime_bat <- readRDS("Crime3years.rds")

# Filter years using the filter method
two_year_crime <- crime_bat %>% filter(between(as_date(Date), 
                                               as_date("2018-01-01"),
                                               as_date("2018-01-01") + 730))

# integrate the time series data into weekly and monthly data series
# Create new variables as covered in module 10

two_year_crime_new <- two_year_crime %>% 
  mutate(hour = hour(two_year_crime$Date),week= weekdays(two_year_crime$Date),  
         month = month(two_year_crime$Date),year=year(two_year_crime$Date)) %>% 
  mutate(weeknum= strftime(Date, format = '%V')) %>%
  mutate(monthnum= strftime(Date, format = '%m')) 

# Aggregate the hourly data in to Weekly data
two_year_crime_weekly <- two_year_crime_new %>% 
  group_by(weeknum,year) %>%
  summarize(case_weekly=sum(Battery)) %>%
  mutate(yearweek=paste(year,weeknum, 1, sep=''))
  
two_year_crime_weekly <- 
  two_year_crime_weekly[two_year_crime_weekly$year != 2020, ]

two_year_crime_weekly <- arrange(two_year_crime_weekly,
        two_year_crime_weekly$year, 
        two_year_crime_weekly$weeknum)

# Create a new column 
two_year_crime_weekly <- two_year_crime_weekly %>%
  mutate(weeklydate = as.Date(yearweek,"%Y%W%w"))


glimpse(two_year_crime_weekly)

two_year_crime_weekly%>%
  ggplot(aes(x = weeklydate, y = case_weekly,group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Year-Week", y = "Number of Crimes")+
  scale_x_date(date_labels = "%Y/%U")




glimpse(two_year_crime_weekly)