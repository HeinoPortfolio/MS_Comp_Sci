library(ggplot2)
library(dplyr)
library(dslabs)

data(murders)

# Colors inside aes() and outside aes ##########################################

# Single color: inside aes() in global mapping
print(ggplot(murders,
       aes(population/10^6, total, color="blue")) +
  geom_point() +
  geom_smooth()
)

# Color based variable: inside aes() in global mapping
print(ggplot(murders,
             aes(population/10^6, total, color=region)) +
        geom_point() +
        geom_smooth()
)

# Single color: inside aes() in local mapping
print(ggplot(murders) +
        geom_point(aes(population/10^6, total,size = 3,  color="blue")) +
        geom_smooth(aes(population/10^6, total,  color="green"))
)

# Color based on variable: inside aes() in local mapping
print(ggplot(murders) +
        geom_point(aes(population/10^6, total,size = 3,  color=region)) +
        geom_smooth(aes(population/10^6, total,  color=region))
)

# Overwrite the colors

# Overwrite color in local mapping
print(ggplot(murders, aes(population/10^6, total,  color=region)) +
        geom_point(size=3, color="purple") +
        geom_smooth(color="green")
)

# Global "global":  No
print(ggplot(murders, aes(population/10^6, total,  color=region), color="blue") +
        geom_point(size=3) +
        geom_smooth()
)

# local "global": yes
print(ggplot(murders) +
        geom_point(aes(population/10^6, total, size=3, color=region), color="blue") +
        geom_smooth(aes(population/10^6, total, color=region), color="green")
)

# Can use pipe in ggplot() ########################

murders %>% ggplot() +
  geom_point(aes(population/10^6, total), size=3, color="red") +
  geom_smooth(aes(population/10^6, total, color=region), color="green")

# Can use plot object to add layers
p2 <- murders %>% ggplot()
p2 + geom_point(aes(population/10^6, total), size=3, color="red") +
  geom_smooth(aes(population/10^6, total), color="green")
















