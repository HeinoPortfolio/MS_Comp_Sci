library(tidyverse)
library(lubridate)

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

crime_bat <- readRDS("Crime3years.rds")

# Filter years using the filter method
two_year_crime <- crime_bat %>% filter(between(as_date(Date), 
                                               as_date("2018-01-01"),
                                               as_date("2018-01-01") + 730))

# Create new variables
# Create new variables 
two_year_crime_new <- two_year_crime %>% 
  mutate(hour = hour(two_year_crime$Date),week= weekdays(two_year_crime$Date),  
         month = month(two_year_crime$Date),year=year(two_year_crime$Date)) %>% 
  mutate(weeknum= strftime(Date, format = '%V')) %>%
  mutate(monthnum= strftime(Date, format = '%m'))
  
  


# Group data into monthly data
two_year_crime_monthly <- two_year_crime_new %>% 
  mutate(hour = hour(two_year_crime_new$Date), week=weekdays(two_year_crime_new$Date),
         month = month(two_year_crime_new$Date), year=year(two_year_crime_new$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, monthnum)) %>%
  mutate(first=1) %>%
  mutate(myDate=as.Date(format(as.Date(paste(1,monthnum,year,sep="."),"%d.%m.%Y"),"%Y-%m-%d")))

  

two_year_crime_monthly <- 
  two_year_crime_monthly[two_year_crime_monthly$year != 2020, ]

# order by the year then by month
two_year_crime_monthly <- arrange(two_year_crime_monthly,two_year_crime_monthly$year, 
                                              two_year_crime_monthly$monthnum)


two_years <- two_year_crime_monthly %>% 
 mutate(monthDay= as.Date(paste(first, monthnum, sep="."), "%d.%m"))



####Stack the two years data by two lines 
ggplot(two_years, aes(x= monthDay, y=case_monthly, color=as.factor(year))) +
  geom_point() + 
  geom_line() +
  xlab("Date") +
  scale_x_date(date_breaks = "1 month", date_labels = "%b")+
  theme(axis.text.x=element_text(angle=30, hjust=1)) +
  guides(color=guide_legend(title = "Year"))











two_year_crime_monthly %>%
  ggplot(aes(x = yearmonth, y = case_monthly, group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq((min(two_year_crime_monthly$yearmonth)),
                                max(two_year_crime_monthly$yearmonth),
                                1))


