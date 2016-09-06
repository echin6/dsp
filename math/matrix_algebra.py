# Matrix Algebra
import numpy as np
import math

A_array = np.array([[1, 2, 3], [2, 7, 4]])
B_array = np.array([[1, -1], [0, -1]])
C_array = np.array([[5, -1], [9, 1], [6, 0]])
D_array = np.array([[3, -2, -1], [1, 2, 3]])
u_vector = np.array([6, 2, -3, 5])
v_vector = np.array([3, 5, -1, 4])
w_vector = np.array([[1], [8], [0], [5]])
alpha = 6

print "#1.1, A's dimension"
print A_array
print A_array.shape
print ""

print "#1.2, B's dimensions"
print B_array
print B_array.shape
print ""

print "#1.3, C's dimensions"
print C_array
print C_array.shape
print ""

print "#1.4, D's dimensions"
print D_array
print D_array.shape
print ""

print "#1.5, u's dimensions"
print u_vector
print u_vector.shape
print ""

print "#1.6, v's dimensions"
print w_vector
print w_vector.shape
print ""

print "Assume alpha = 6"
print ""

print "#2.1, u + v ="
print u_vector + v_vector
print ""

print "#2.2, u - v ="
print u_vector - v_vector
print ""

print "#2.3, alpha * u ="
print alpha * u_vector
print ""

print "#2.4, u.v = "
print np.dot(u_vector, v_vector)
print ""

print "#2.5, ||u|| ="
print math.sqrt(np.dot(u_vector, u_vector))
print ""

print "#3.1, A + C ="
#print "A.array + C.array"
print "Not defined."
print ""

print "#3.2, A - transposed(C) = "
print A_array - C_array.T
print ""

print "#3.3, tranposed(C) + 3 * D = "
print C_array.T + 3*D_array
print ""

print "#3.4, B * A ="
print np.dot(B_array, A_array)
print ""

print "#3.5, B * transposed(A) ="
#print np.dot(B_array,A_array.T)
print "Not defined"
print ""

print "#3.6, B * C ="
#print np.dot(B_array, C_array)
print "Not defined"
print ""

print "#3.7, C * B ="
print np.dot(C_array, B_array)
print ""

print "#3.8, B ^ 4 ="
print np.dot(B_array, np.dot(B_array, np.dot(B_array, B_array)))
print ""

print "#3.9, A * transposed(A) ="
print np.dot(A_array, A_array.T)
print ""

print "#3.10, transposed(D) * D ="
print np.dot(D_array.T, D_array)
print ""
