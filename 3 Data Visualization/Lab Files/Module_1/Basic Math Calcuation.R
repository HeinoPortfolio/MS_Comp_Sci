#  basic R calculation
6+4

# Assign the result of the calculation to a variable

x <- 6 + 4
print (x)

# math operation could be done using two numeric variables 
# can create another variable -- y

y <- 4
print(x / y)

# exponentiation in R
x^2

# Calculate  a natural log value using log()
log(x)

# math calculations for data frame
# Computing column and row  sums
A <- matrix(c(2, 3, -2, 1, 2, 2), 3, 2)
A

# sum the columns and rows
# Does a column sum -- colSums()
col_sum <- colSums(A)
col_sum

# Calculate row sum
row_sum <- rowSums(A)
row_sum

# Calculate the sums
total_sum <- sum(A)
total_sum

# Calculate the Column and Row mean
col_mean <- colMeans(A)
col_mean

# Row mean
row_mean <- rowMeans(A)
row_mean

# Calculate the average for all the numbers
mean_1 <- mean(A)






