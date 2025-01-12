


# Read / load the data into RStudio 
fire_data <- read.csv('Crop_Range_GOES0901_R.csv')

# View or show the contents of the table
View(fire_data)
 

# Selects the columns "year, jday, gmt, frp, BinTime" from the fire_data

print (select(fire_data, year, jday, gmt, frp, BinTime))
temp_1 <- select(fire_data, year, jday, gmt, frp, BinTime)

# Filter the rows by the jday > 227. 
# filter() is used to find rows from the data(fire_data) and gives  the rows  where column
fire_data %>% select(year, jday, gmt, frp, BinTime) %>% filter (jday > 227)