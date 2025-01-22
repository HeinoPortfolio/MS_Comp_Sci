
library(ggplot2)
setwd("C:/Users/ali3/OneDrive - Ball State University/Desktop/Courses/Coursera/DSCI605/Week6")
df <- read.csv("Income by states.csv")

#plot the basic histogram
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=10000,color="black", fill="blue")

#save as jpeg
jpeg(file="Histogram_jep.jpeg",width = 800, height = 1000,res=300)
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="blue")
dev.off()




#save as png
png(file="Histogram_png.png",
    width=600, height=350)
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="blue")
dev.off()
#save as bmp: specify ppi with res
bmp(file="Histogram_bmp.bmp",
    width=6, height=4, units="in")
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="blue")
dev.off()
#save as tiff
tiff(file="Histogram_tif.tiff",
     width=6, height=4, units="in")
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="blue")
dev.off()







#save into a pdf
pdf(file="Histogram.pdf",width = 8, height = 10)
ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="blue")

ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="red")

ggplot(df, aes(x=income)) + 
  geom_histogram(binwidth=5000,color="black", fill="green")
dev.off()