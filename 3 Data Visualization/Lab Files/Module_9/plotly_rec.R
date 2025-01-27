#
#  Function: plot_ly(): plotly.js ++ ggplot2

library(plotly)
library(tidyverse)

view(iris)

# Creating a scatter plot using built-in data set Iris from tidyverse

plot_ly(data=iris, x= ~Sepal.Length, y= ~Petal.Length, color= ~Species,
        type="scatter", mode="markers")

#  to add markers and other items in to the graph use add_markers function
plot_ly(data=iris, x= ~Sepal.Length, y= ~Petal.Length) %>% add_markers()

# box plot with plotly 
# in a boxplot the variable needs to be numeric
plot_ly(data=iris, x= ~Petal.Width, color= ~Species, type= "box")

# Bar plot
categories <- c("Apples","Oranges","Bananas")
values <- c(15, 10, 8)
plot_ly(x= categories, y= values, type="bar")

# pipe operation
iris %>% plot_ly(x= ~Sepal.Length, y= ~Petal.Length,
                     type="scatter", mode="markers",
                     text= ~paste("Length: ", Sepal.Length, '<br>Width: ', Sepal.Width),
                     color= ~Species, size= ~Sepal.Length) %>%
  layout(title="Length vs Width", plot_bgcolor="#e5ecf6", 
         xaxis=list(title= "Sepal Length"),
         yaxis=list(title= "Sepal Width"))

## ggplotly
# To convert ggplot to a plotly graph
set.seed(100)

d <- diamonds[sample(nrow(diamonds), 1000),  ]

p <- ggplot(data = d, aes(x = carat, y= price)) + 
  geom_point(aes(text= paste("Clarity: ", clarity)), size=1) +
  geom_smooth(aes(colour= cut, fill= cut)) +
  facet_wrap(~cut)
ggplotly(p)








