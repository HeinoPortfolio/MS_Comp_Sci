### ts() object

# Note this makes use of base R no further packages are needed

sstoi.pa <- read.table("sstoi_pa.txt", header=T)

# will give the total months in the data set
# Removed the last 11 entries because it is not a full year
mo.sstoi <- length(sstoi.pa$YR) - 11

# to get total number of years
yr.sstoi <- mo.sstoi/12

# using the ts() and the third variable 
sstoi.pa34 <- ts(sstoi.pa[3], start=c(1950, 1), end=c(1996,12), frequency=12)
class(sstoi.pa34)


# using either ts.plot() or plot() will give the same result
ts.plot(sstoi.pa34)
plot(sstoi.pa34)