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
  mutate(yearweek=paste0(year,weeknum))

# Remove the 2020 year as required by the lab assignment
two_year_crime_weekly <- two_year_crime_weekly[two_year_crime_weekly$year !=
                                                 2020, ]

# Group the data into a monthly series 
# Group data into monthly data
two_year_crime_monthly <- two_year_crime_new %>% 
  mutate(hour = hour(two_year_crime_new$Date), week=weekdays(two_year_crime_new$Date),
         month = month(two_year_crime_new$Date), year=year(two_year_crime_new$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, monthnum)) %>%
  mutate(first=1) %>%
  mutate(myDate=as.Date(format(as.Date(paste(1,monthnum,year,sep="."),"%d.%m.%Y"),"%Y-%m-%d")))


# Remove the rows required by the assignment
two_year_crime_monthly <- 
  two_year_crime_monthly[two_year_crime_monthly$year != 2020, ]

# order by the year then by month
two_year_crime_monthly <- arrange(two_year_crime_monthly,
                                  two_year_crime_monthly$year, 
                                  two_year_crime_monthly$monthnum)


################################################################################
# Graph the results

# Graph the hourly data
two_year_crime %>% ggplot(aes(x = Date, y = Battery, lty="Battery")) +
  geom_point(col = "maroon") + 
  geom_line(col = "red") +
  scale_linetype('Crime') +
  scale_x_datetime(date_breaks= "4 months",
                   date_labels = "%m/%d/%y-00:00:00") +
  theme(axis.text.x=element_text(angle=30, hjust=1)) +
  labs(title = "Battery Crime from 2018-01-01 to 2020-01-01 in Chicago",
       x = "Hourly", y = "Number of Crimes", shape='Battery')



  
  





####Stack the two years data by two lines 
two_years <- two_year_crime_monthly %>% 
  mutate(monthDay= as.Date(paste(first, monthnum, sep="."), "%d.%m"))


ggplot(two_years, aes(x= monthDay, y=case_monthly, color=as.factor(year))) +
  geom_point() + 
  geom_line() +
  xlab("Month") +
  ylab("Number of Grimes")+
  ggtitle("Battery Crime in Chicago") +
  scale_x_date(date_breaks = "1 month", date_labels = "%b")+
  theme(axis.text.x=element_text(angle=30, hjust=1)) +
  guides(color=guide_legend(title = "Year"))











