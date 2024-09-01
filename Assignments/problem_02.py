import numpy as np
# Problem 2 Numpy Basics (10 Points)
# # 
# 1. Create two random uniform matrices of same shape(5,3), named A and B. (3 pts)
#    Check if they are equal. (2 pts)
# #
# 2. In each row of matrix A, please replace the maximum value by 0.  
# 	 Then print both the original A and the updated A. (5 pts)
# #
# 

# method definition.
def compare_matrices(matrix1, matrix2):

	# set isTrue to false, we're going to test for true.
	isTrue = 1

	# iterate over matrix1 and matrix2, if all of the elements match in addition
	# to matrix size.
	for i in range(len(matrix1)):
		for j in range(len(matrix2)):
			if matrix1[i][j] != matrix2[i][j]:
				isTrue = 0 # set to false.
				break
			if isTrue == 0:
				break

	if isTrue:
		print("identical");
	else:
		print("not identical");

# generate two random matrices (A, B).
A = np.random.randint(0, 9, (5, 3))
B = np.random.randint(0, 9, (5, 3))

# display the matrices.
print(A)
print()
print(B)

compare_matrices(A, B);
