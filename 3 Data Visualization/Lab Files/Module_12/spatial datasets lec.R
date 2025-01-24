# tidyverse - used to conduct the data wrangling or the ggplot visualizations
# raster - can be used for geo-spatial data analysis
# sf - used to read the vector shapefile

library(tidyverse)
library(raster)
library(sf)

point_df <- read_csv("HARV_PlotLocations.csv")

polygon_sf <- st_read("HarClip_UTMZ18.shp")

CHM_HARV <- raster("HARV_chmCrop.tif")

CHM_HARV_df <- as.data.frame(CHM_HARV, xy=TRUE)

# the output should be as four class spatial class object
# as.data.frame() can change this from four classes into data frame