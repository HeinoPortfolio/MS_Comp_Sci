library(ggplot2)
library(dplyr)
library(dslabs)
library(car)

#summary(mtcars)

#view(mtcars)

#data(car)

#view(mtcars)



# Q3. #################################

# yes
#print(mpg %>% ggplot(aes(x=displ, y=hwy)) +geom_point())

#yes
#print(ggplot(mpg, aes(x=displ, y=hwy)) + geom_point(size=2))

# Q4. ############################################################

data("murders")


print(ggplot(data = murders, mapping = aes(population/10^6, y=total))+ geom_point() + geom_smooth())

print(ggplot(data = murders) + geom_point(mapping=aes(population/10^6, y=total)) +geom_smooth(mapping = aes(x = population/10^6, y=total)))


# Q5 Purple points and blue texts #############################
#Yes
#print(murders %>% ggplot() + geom_point(aes(population/10^6, total, size=3), color="purple") + geom_text(aes(population/10^6, total, label=abb), color="blue", nudge_x = 1))

