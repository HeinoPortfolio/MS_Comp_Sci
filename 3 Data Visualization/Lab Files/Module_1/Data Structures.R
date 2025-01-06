# Vectors
# Built for analyzing large data

# c() function - used to create vectors
v_1 = c(1, 5.5, 1e2)
v_2 = c(0.14, 0, -2)

# c() can be used to combine two vectors
v_3 = c(v_1, v_2)
v_3

# Can subset the vector by using square brackets []
# indexes start at one (1)
v_3[2]

# Matrix 
# matrix() function
# R wants the data entered by columns starting with column 1
# 1st arg: c() - the values of the elements filling the columns
# 2nd arg: 3 the number of rows
# 3rd arg: 2 the number of columns 

A <- matrix(c(2, 3, -2, 1, 2, 2), 3, 2)
A

MA <- matrix(1:6, nrow = 3, ncol = 2)
MA
dim(MA)

MB <- matrix(7:9, nrow = 3, ncol = 1)
MB

# cbind()
# rbind()

# add a new row
rbind(MB, c(10, 20, 25))

rbind(MA, c(10, 20))

 # add a new column
cbind(MA,MB)

# Arrays
# array() function
vector1 <- c(5,9,3)
vector2 <- c(10, 12, 12, 13, 14, 15)
column.names <- c("col1", "col2", "Col3")
row.names <- c("Row1", "Row2", "Row3")
matrix.names <- c("Matrix1", "Matrix2")

# Take the vectors as input into an array
result <- array(c(vector1, vector2), dim=c(3, 3, 2),
                dimnames =  list(row.names, column.names, matrix.names))

print(result)

# Data Frame
# data.frame() function
df <- data.frame(dose=c("D0.5", "D1", "D2"), len=c(4.2,10, 29.5))

head(df)

# List 
# list()
my.list <- list(MA, df)
my.list[1]
my.list[2]




















