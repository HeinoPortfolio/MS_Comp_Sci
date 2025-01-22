library(tidyverse)
library(hrbrthemes)
library(viridis)

setwd(dirname(rstudioapi::getSourceEditorContext()$path))


# load the data
data(mpg)

# look at the data
glimpse(mpg)
view(mpg)
names(mpg)


# Basic Scatter plot
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ, fill=class, shape=as.factor(cyl))) +
  geom_point(alpha=0.5, color="black") +
  scale_fill_viridis(discrete=TRUE, option="A") +
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")


# To hide the legend  
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ, fill=class, shape=as.factor(cyl))) +
  geom_point(alpha=0.5, color="black") +
  scale_fill_viridis(discrete=TRUE, option="A") +
  theme(legend.position="none") +
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")

# To hide the legend method #2
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ, fill=class, shape=as.factor(cyl))) +
  geom_point(alpha=0.5, color="black") +
  scale_fill_viridis(discrete=TRUE, option="A") +
  guides(fill=FALSE, shape=FALSE) +
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")

# To show the legend in a location
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ, fill=class, shape=as.factor(cyl))) +
  geom_point(alpha=0.5, color="black") +
  scale_fill_viridis(discrete=TRUE, option="A") +
  theme(legend.position="bottom") +
  guides(fill=guide_legend(title = "Users By Guides")) + 
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")

# change to rows 
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ, fill=class, shape=as.factor(cyl))) +
  geom_point(alpha=0.5, color="black") +
  scale_fill_viridis(discrete=TRUE, option="A") +
  theme(legend.position="right") +
  guides(shape=guide_legend(nrow=2, byrow=TRUE, title ="Cyl")) +
  guides(fill=guide_legend(nrow=4, ncol=2, byrow=TRUE, title="Class")) + 
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")