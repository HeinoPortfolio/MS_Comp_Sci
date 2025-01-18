# Notes:
#
# May need to install the dslabs to gain access to the murders data set

# ############################################################################

library(ggplot2)
library(dplyr)
library(dslabs)

data(murders)

# Global aesthetic mapping and local aesthetic mapping  ########################

# Global aesthetic mapping

print(ggplot(data= murders,
       mapping = aes(x= population/10^6, y = total)) + 
  geom_point() +
  geom_smooth()
)

# Local aesthetic mapping

print(ggplot(data = murders) +
        geom_point(mapping = aes(x = population/10^6, y = total)) +
        geom_smooth(mapping = aes(population/10^6, y = total))
      )

# Drop x and y , data and mapping
print(ggplot(murders, aes(population/10^6, total)) +
        geom_point() +
        geom_smooth()
      )
