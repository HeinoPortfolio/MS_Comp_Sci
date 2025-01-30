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

# Remove the 2020 year as required by the lab assignment
two_year_crime_weekly <- two_year_crime_weekly[two_year_crime_weekly$year !=
                                                 2020, ]

two_year_crime_weekly <- arrange(two_year_crime_weekly,
                                 two_year_crime_weekly$year, 
                                 two_year_crime_weekly$weeknum)

two_year_crime_weekly <- two_year_crime_weekly %>%
  mutate(weeklydate = as.Date(yearweek,"%Y%W%w"))

# Group the data into a monthly series 
two_year_crime_monthly <- two_year_crime_new %>% 
  mutate(hour = hour(two_year_crime_new$Date), week=weekdays(two_year_crime_new$Date),
         month = month(two_year_crime_new$Date), year=year(two_year_crime_new$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste(year,monthnum,sep='-')) %>%
  mutate(first=1) %>%
  mutate(yearandmonth = as.Date(format(as.Date(paste(year, monthnum, 1, sep="."),"%Y.%m.%d"),
                                       "%Y-%m-%d"))) %>%
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
  geom_line(col = "blue") +
  scale_linetype('Crime') +
  scale_x_datetime(date_breaks= "4 months", date_labels = "%m/%d/%y-00:00:00") +
  theme(axis.text.x=element_text(angle=30, hjust=1)) +
  labs(title = "Battery Crime from 2018-01-01 to 2020-01-01 in Chicago",
       x = "Hourly", y = "Number of Crimes", shape='Battery')


# graph the weekly data

two_year_crime_weekly%>%
  ggplot(aes(x = weeklydate, y = case_weekly, group=1, color="blue",lty="Battery")) +
  geom_point(col = "maroon") +
  geom_line(col = "blue") +
  scale_linetype('Crime') +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Year-Week", y = "Number of Crimes")+
  scale_x_date(date_labels = "%Y/%U")



# Graph the Monthly data

ggplot(two_year_crime_monthly, aes(x=yearandmonth, y=case_monthly, color="red")) +
  geom_point() + 
  geom_line() +
  xlab("Month") +
  ylab("Number of Grimes")+
  ggtitle("Battery Crime in Chicago") +
  labs(color="Crime") +
  scale_color_manual(labels = c("Battery"), values = c("blue")) +
  scale_x_date(date_breaks = "2 month", date_labels = "%Y-%b")+
  theme(axis.text.x=element_text(angle=45, hjust=1)) 



################################################################################
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











