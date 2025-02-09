# Step 1 #######################################################################

library(tidyverse)
library(raster)          #raster()
library(sf)              #st_read()
library(ggspatial)       #annotation_scale,annotation_north_arrow
library(ggnewscale)      #new_scale_color() 


# Step # 2 #####################################################################
# Set the working directory 
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# Read in the unemployment rate from the CSV file
Unemployrate <-  read_csv("data/unemployment_county.csv")

# Read in the Crime rate from the CSV file
Crimerate <- read_csv ("data/crime_and_incarceration_by_state.csv")

# Read the states shape file
States <- st_read("data/tl_2019_us_state/tl_2019_us_state.shp")

# Step #3 Process the USA Polygon shape file ###################################
Contiguous_state <- States %>% filter(STUSPS != "AK" & STUSPS != "AS" &
                                        STUSPS != "MP" & STUSPS != "PR" &
                                        STUSPS != "VI" & STUSPS != "HI" &
                                        STUSPS != "GU")

# check the length
length(unique(Contiguous_state$STUSPS))

# 4. Process the Unemployment Rate Data ########################################
unique(Unemployrate)
length(unique(Unemployrate$State))

Unemployrate <- Unemployrate %>% filter(State != 'AK' & State != "HI") %>%
  group_by(State, Year) %>% 
  summarise(Totalforce = sum(`Labor Force`), Totalemployed=sum(Employed),
            Totalunemployed=sum(Unemployed), Meanrate = mean(`Unemployment Rate`,
                                                             rm.na=TRUE)
            )
# Check the length 
length(unique(Unemployrate$State))

# Change the column state to STUSPS 
Unemployrate <- Unemployrate %>% rename("STUSPS" = "State") %>%
  filter(Year %in% c(2007:2014))

# 5. Process the Crime rate #####################################################
unique(Crimerate$jurisdiction)
length(unique(Crimerate$jurisdiction))
head(Crimerate)

# Change the column name
Crimerate <- Crimerate %>% 
  rename("STUSPS" = "jurisdiction") %>%
  rename("Year" = "year") %>%
  filter(STUSPS != "FEDERAL" & STUSPS != "ALASKA" & STUSPS != "HAWAII") %>%
  filter(Year %in% c(2007:2014))
  
length(unique(Crimerate$STUSPS))

# Change the state names in the STUSPS column
Crimerate$STUSPS <- state.abb[match(str_to_title(Crimerate$STUSPS), state.name)]

# Calculate the crime rate
Crimerate <- Crimerate %>% 
  mutate(Crimerate=(violent_crime_total/state_population) * 100) %>%
  dplyr::mutate_if(is.numeric, round, 1)


# 6 Join relational tables
CS_Erate <- right_join(Contiguous_state, Unemployrate, by= c("STUSPS"))

CS_Erate_Crate <- right_join(CS_Erate, Crimerate, by= c("STUSPS", "Year"))

#CS_Erate_Crate1 <- CS_Erate_Crate %>% 
#  select(REGION, STUSPS, NAME, Year, Meanrate, Crimerate) %>%
#  rename("Unemplyrate" = "Meanrate")

# 7 Check the missing values
#which(is.na(CS_Erate_Crate1$REGION))
















