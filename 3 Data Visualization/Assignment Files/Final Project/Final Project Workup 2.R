library(tidyverse)
library(raster)          
library(sf)             
library(ggspatial)       
library(ggnewscale)      
#library(ggsn)            
library(shiny)           
library(plotly)          
library(gridExtra) 

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

all_info_from_RDS <- readRDS("CS_Erate_Crate1.Rds")

info_for_year_2014 <- all_info_from_RDS %>% filter(all_info_from_RDS$Year == 2014)

# Plot the graph for the 2014 data
# Create a spatial map over the contiguous USA for the unemployment rate and 
# crime rate respectively for the specific year 2014 using ggplot()
# Graph for unemployment rate 
ggplot(data=info_for_year_2014) + 
  geom_sf(data= info_for_year_2014$geometry, 
          aes(fill=info_for_year_2014$Unemplyrate)) + 
  xlab("Longitude") +
  ylab("Latitude") +
  guides(fill=guide_legend(title= "Unemployment Rate for 2014")) + 
  labs(title = "Unemployment Rate Over Contiguous USA ",
       subtitle = "Unemployment Color Coded by State",
       caption = "Data source: Unknown") + 
  theme(panel.background = element_blank())

# Graph for crime rate respectively
ggplot(data=info_for_year_2014) + 
  geom_sf(data= info_for_year_2014$geometry, 
          aes(fill=info_for_year_2014$Crimerate)) + 
  xlab("Longitude") +
  ylab("Latitude") +
  guides(fill=guide_legend(title= "Crime Rate")) + 
  labs(title = "Crime Rate Over Contiguous USA ",
       subtitle = "Crime Rate Color Coded by State",
       caption = "Data source: Unknown") + 
  theme(panel.background = element_blank())


# Create Scatter plot using Crime rate (x-axis) and unemployment rate (y-axis)
fig <- plot_ly(data= info_for_year_2014, x= ~Crimerate, y= ~Unemplyrate,
                color= ~REGION) %>%
  add_markers() %>%
  layout(title="Unemployment Rate and Crime Rate for 2014",  
         xaxis=list(title= "Crime Rate Per 100,000 People"),
         yaxis=list(title="Unemployment Rate Per 100 People"), showlegend=TRUE)
  
fig


# Create new data frame for the states
states <- c("California", "Idaho", "Illinois", "Indiana") 
four_states_year_2014 <- all_info_from_RDS %>% filter(NAME %in% states)

stats_df <-  as.data.frame(four_states_year_2014)

une <- plot_ly(data=stats_df, x= ~as.factor(Year), y= ~Unemplyrate,color= ~NAME) %>%
  #filter(NAME %in% states) %>%
  #add_markers() %>%
  filter(NAME %in% states) %>%
  group_by(NAME) %>%
  add_lines() %>%
  layout(title="Unemployment Rate Changes by Year",  
         xaxis=list(title= "Year"),
         yaxis=list(title="Unemployment Rate"))

une  

cr <- plot_ly(data=stats_df, x= ~as.factor(Year), y= ~Crimerate, color= ~NAME) %>%
  #filter(NAME %in% states) %>%
  #add_markers() %>%
  filter(NAME %in% states) %>%
  group_by(NAME) %>%
  add_lines() %>%
  layout(title="Crime Rate Changes by Year",  
         xaxis=list(title= "Year"),
         yaxis=list(title="Crime Rate"))

cr  
  