if(!require(tidyverse)) {install.packages('tidyverse')}; require(tidyverse)
if(!require(colorspace)) {install.packages('colorspace')}; require(colorspace)
if(!require(gridExtra)) {install.packages('gridExtra')}; require(gridExtra)

library(tidyverse)
library(readxl)
library(gridExtra)

#Set the working directory
setwd(dirname(rstudioapi::getSourceEditorContext()$path))


# Read the data from the xlsx file named Sampledata2.xlsx
# will need to read file using  

crime_rates_df = readxl::read_xlsx('Sampledata2.xlsx')


# Inspect the data
glimpse(crime_rates_df)
View(crime_rates_df)
names(crime_rates_df)

# Create the colors for the graphs
n_col = length(unique(crime_rates_df$Year))
col1 = colorspace::diverge_hcl(n_col)

# create the histogram 
hist_plt <- ggplot(crime_rates_df,aes(x=CrimeRate, color=as.factor(Year), fill=as.factor(Year))) +
  geom_histogram(position = "dodge", alpha=0.5, bins=10) +
  scale_color_manual(values=col1) +
  scale_fill_manual(values=col1, name="Year") +
  labs(title="Crime Rate Histogram Plots", x="Crime rate per 100, 1000 people",
       y="Count", color="Year") +
  theme(plot.title=element_text(hjust=0.5))+
  ggtitle("Histogram Plot")

hist_plt

# create the scatter plot
crime_rates_df_new <- crime_rates_df %>%
  group_by(Year) %>%
  summarize(mean_rate=mean(CrimeRate),max_rate=max(CrimeRate),min_rate=min(CrimeRate))

line_plt <- ggplot(crime_rates_df_new, aes(x = Year, y = mean_rate)) + 
  geom_point(color='red', shape=10) + 
  geom_line(color='blue') +
  labs(title="Crime Rate Histogram Plots", x="Year",
       y="Mean Crime Rate per 100, 1000 people over USA") +
  theme(plot.title=element_text(hjust=0.5)) +
  ggtitle("Point line plot")

line_plt


# Grouped boxplot


min <- min(crime_rates_df$Year)
max <- max(crime_rates_df$Year)


#box_plt <- ggplot(crime_rates_df, aes(x=Year, y= CrimeRate,fill=as.factor(Year))) + 
#  geom_boxplot(outlier.colour="red", outlier.shape=8, outlier.size=2) +
#  guides(fill="none")

box_plt <- ggplot(crime_rates_df) + 
  geom_boxplot(aes(x=Year, y= CrimeRate, fill=as.factor(Year)),
               outlier.colour="red", outlier.shape=8, outlier.size=2) +
  guides(fill="none") +
  scale_x_continuous(breaks=seq(min, max, by=1)) + 
  ggtitle("Boxplot")

box_plt

# Create the grid 

lay <- rbind(c(1, 1, 2, 2),
             c(1, 1, 2, 2),
             c(3, 3, 3, 3),
             c(3, 3, 3, 3))


grid_plt <- grid.arrange(hist_plt, line_plt, box_plt, layout_matrix=lay)


