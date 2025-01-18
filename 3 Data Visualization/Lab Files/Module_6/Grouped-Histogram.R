# ##############################################################################
#
# File Purpose: Show how to create a grouped histogram from a data set
#
# Notes:
#
#   1) makes use of colorspace
#   2) uses diverge_hcl() function
#   3) Uses a different way to install the package
#       - if(!require(colorspace)) {install.packages('colorspace')}; require(colorspace)
#   4) will filter to get two years from the data set
#
# ##############################################################################

library(tidyverse)

if(!require(colorspace)) {install.packages('colorspace')}; require(colorspace)

# Read data
income_df <- read.csv("Income by states.csv")

# Make a color vector
#
# Notes:
#
#   n_col:   Is the number of unique years in the data set
#   colorspace: is used to create a vector of colors
#   diverge(n_col): 

#
# ##############################################################
n_col = length(unique(income_df$Year))
colrs = colorspace::diverge_hcl(n_col)


# Retrieve years from the data set
# setup the plot with ggplot 
# setup the histogram
# add the layers using the "+" sign to the histogram plot
#
# ##############################################################################

income_df %>% filter(Year %in% c(2015:2017)) %>%
  ggplot(aes(x=income, color=as.factor(Year), fill=as.factor(Year))) +
  geom_histogram(position = "dodge", alpha=0.5, bins=10) +
  scale_color_manual(values=colrs) +
  scale_fill_manual(values=colrs, name="Year") +
  labs(title="Income Histogram Plots", x="Income($)", y="Count", color="Year") +
  theme(plot.title=element_text(hjust=0.5)) #+
  #theme_classic()



