library(tidyverse)
starwars

# Q1. arrange in descending mass
#starwars %>% arrange(desc(mass))

# Q2. arrange by mass and height with height in descending order
#starwars %>% arrange(mass, desc(height)) # correct
#starwars %>% desc(mass, height)
#starwars %>% arrange(mass, height)
#starwars %>% desc(arrange(mass), height)

# Q3. group by sex and species
#st1 <-  starwars %>% select(name, sex, species)
#st2 <- st1 %>% group_by(sex, species)
#st3 <- st1 %>% group_by("sex, species")
#st4 <- st1 %>% group_by("sex", "species")
#st5 <- st1 %>% group_by(sex & species) # no


# Q4. related answers
# Note: n() function the number of observations in the current group
st_o <- starwars
st1 <- starwars %>%
  group_by(species) %>%
  summarise(n = n(), mass = mean(mass, na.rm=TRUE)) %>%
  filter(n > 1, mass >50)

# Q5. rename "hair_color" to "HairColor"
#st_r <- starwars %>% rename("HairColor" = "hair_color")

#class(starwars)




