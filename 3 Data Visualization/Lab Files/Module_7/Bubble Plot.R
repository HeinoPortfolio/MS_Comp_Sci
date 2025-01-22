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

# Basic Bubble plot
mpg %>% 
  arrange(desc(class)) %>%
  ggplot(aes(x=cty, y=displ,size=cyl, fill=class)) +
  geom_point(alpha=0.5, shape=21, color="black") +
  scale_size(range=c(.1, 10), name="Model") + 
  scale_fill_viridis(discrete=TRUE, option="A") +
  theme_ipsum() +
  theme(legend.position="bottom") +
  guides(size=guide_legend(nrow=2, byrow=TRUE, title ="CYL")) +
  guides(fill=guide_legend(nrow=2, byrow=TRUE, title="Class")) + 
  ylab("Engine displacement, in liters (displ)") +
  xlab("City miles per gallon (cty)")
  
  
  
  
  
  
  
  
  
  