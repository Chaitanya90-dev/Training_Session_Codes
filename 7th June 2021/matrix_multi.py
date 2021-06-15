#program for matrix multiplication

row = int(input("Enter a number of rows for matrix_1: "))
col = int(input("Enter a number of column for matrix_2: "))
n = int(input("Enter a number of column for matrix_1 OR Enter a number of rows for matrix_2 : "))

print("Enter elements for Matrix_1: ")

matrix_1 = [[int(input()) for i in range(n)] for j in range(row)]


print("matrix_1 : ")
for i in range(row):
    for j in range(n):
        print(format(matrix_1[i][j],"<3"),end="")
    print()


print("Enter elements for Matrix_2: ")

matrix_2 = [[int(input()) for i in range(col)] for j in range(n)]
print(matrix_2)

print("matrix_2 : ")
for i in range(n):
    for j in range(col):
        print(format(matrix_2[i][j],"<3"),end="")
    print()

result_matrix = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        for k in range(n):
            result_matrix[i][j] = result_matrix[i][j] + matrix_1[i][k] * matrix_2[k][j]


print("Resultant matrix is: ")

for i in range(row):
    for j in range(col):
        print(format(result_matrix[i][j],"<3"),end="")
    print()

