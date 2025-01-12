# Q1. Commands for tidyverse 

#install.package(tidyverse)
#install.packages(tidyverse)
#install.packages("tidyverse")
#remove.packages("tidyverse")

#remove.packages("dplyr")

#install.packages("dplyr")

# Q2. starwars load
library(tidyverse)
starwars
#print(starwars)
#remove.packages("dplyr")

# Q3. print variables of starwars

#  names(starwars) # yes
# name(starwars) # no
#columns(starwars) # no
#column(starwars)


# Q4. variables name, height, mass, gender
#starwars %>% select(columns("name", "height", "mass", "gender")) 
#starwars %>% select(c(1,2,3,9))
#starwars %>% select(1,2,3,9)
#starwars %>% select(name:mass, gender) 
#starwars %>% select(names("name", "height", "mass", "gender")) 
#starwars %>% select(c("name", "height", "mass", "gender")) 
#starwars %>% select("name", "height", "mass", "gender")

# Q5. species is droid

#starwars %>% filter(species == 'Droid')

# q6. species == droid or human
#starwars %>% filter(species == 'Droid' | species == 'Human')

# q7. bmi 
#st1 <- starwars %>% mutate(bmi = mass / (height /100)^2)
st1 <- starwars %>% mutate("bmi" = mass / (height /100)^2)


