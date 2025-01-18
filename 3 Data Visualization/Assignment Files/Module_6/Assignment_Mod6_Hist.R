library(tidyverse)

if(!require(colorspace)) {install.packages('colorspace')}; require(colorspace)



#Set the working directory
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#getwd()

# Load the data and then inspect
crime_rate_df <- read.csv("Sampledata2.csv")

# Select the appropriate variables
# Create the first color gvector
n_col = length(unique(crime_rate_df$Year))
col1 = colorspace::diverge_hcl(n_col)

# Create the second color vector
col2 = c("green","blue","red")



new_crime_rate_df <- crime_rate_df %>% select(Year, CrimeRate) %>%
  mutate(RangeGroup = case_when(CrimeRate < 250 ~ "CrimeRate < 250",
                                250 <= CrimeRate &  CrimeRate <= 500 ~ "250 <= CrimeRate <= 500",
                                CrimeRate > 500 ~ "CrimeRate > 500"))

new_crime_rate_df %>% filter(Year %in% c(2013:2018)) %>%
  ggplot(aes(x=CrimeRate, color=as.factor(Year), fill=as.factor(Year))) +
  geom_histogram(position = "dodge", alpha=0.5, bins=10) +
  scale_color_manual(values=col1) +
  scale_fill_manual(values=col1, name="Year") +
  labs(title="Crime Rate Histogram Plots", x="Crime rate per 100, 1000 people",
       y="Count", color="Year") +
  theme(plot.title=element_text(hjust=0.5)) +
  theme_classic()
  
  
new_crime_rate_df %>% filter(Year %in% c(2013:2018)) %>%
  ggplot(aes(x=CrimeRate, color=as.factor(RangeGroup), fill=as.factor(RangeGroup))) + 
  geom_histogram(position = "dodge", alpha=0.5, bins=10) +
  scale_color_manual(values=col2) +
  scale_fill_manual(values=col2, name="Range Group") +
  labs(title="Crime Rate Histogram Plots", x="Crime rate per 100, 1000 people",
       y="Count", color="Range Group") +
  theme(plot.title=element_text(hjust=0.5)) +
  theme_classic()
  






