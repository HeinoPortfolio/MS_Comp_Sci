library(ggplot2)
library(dplyr)
library(dslabs)

data(murders)

# Colors inside aes() and outside aes ##########################################

# Single color: inside aes() in global mapping
print(ggplot(murders,
       aes(population/10^6, total, color="blue")) +
  geom_path() +
  geom_smooth()
)

# Color based variable: inside aes() in global mapping
print(ggplot(murders,
             aes(population/10^6, total, color=region)) +
        geom_path() +
        geom_smooth()
)

# Single color: inside aes() in local mapping
print(ggplot(murders) +
        geom_path(aes(population/10^6, total,size = 3,  color="blue")) +
        geom_smooth(aes(population/10^6, total,  color="green"))
)

# Color based on variable: inside aes() in local mapping
print(ggplot(murders) +
        geom_path(aes(population/10^6, total,size = 3,  color=region)) +
        geom_smooth(aes(population/10^6, total,  color=region))
)



