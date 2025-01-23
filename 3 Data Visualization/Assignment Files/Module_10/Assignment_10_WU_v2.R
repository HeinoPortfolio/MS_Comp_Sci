library(tidyverse)

crime_bat <- readRDS("Crime3years.rds")

#new_crime_bat <- head(crime_bat, 365*24*2)

two_years = 365*24*2
start_date = 553
end_date = start_date + two_years

new_crime_bat <- crime_bat[start_date:end_date, ]

bat_crime  <- new_crime_bat %>% 
  mutate(hour = hour(new_crime_bat$Date), week=weekdays(new_crime_bat$Date),
         month = month(new_crime_bat$Date), year=year(new_crime_bat$Date)) %>%
  mutate(monthnum= strftime(Date, format = '%m'))


bat_month <- bat_crime %>% 
  group_by(year, month) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, month)) 

# Delete a row from the table
bat_month <- bat_month[-1, ]

bat_month$new_date <- paste(bat_month$month, bat_month$year,sep='-')

label_names <- bat_month$new_date
for(lbl in label_names){
  print(lbl)
}
  
ggplot(bat_month, aes(x = yearmonth, y = case_monthly, group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-24 to 2019-09-24 in Chicago",
       x = "Week", y = "Number of Crimes") +
  scale_x_discrete(labels=label_names) +
  theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1))
 
 