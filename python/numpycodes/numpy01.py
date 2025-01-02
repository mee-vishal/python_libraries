import numpy as np
# here we can export numpy in any format

# for 0d array
_0d=np.array(45)
print(_0d)

# for 1d array
_1d=np.array([1,2,3,4,5])
print(_1d)

# for 2d array
_2d=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(_2d)


# for 3d array
_3d=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(_3d)


# we can also make 5d array as follows
_5d=np.array([1,2,3,4,5],ndmin=5)
print(_5d)



# indexing the multidimensional arrays

# for 1d array
# it  is simple
oned=np.array([1,2,3,4,5])
print(oned[1])
# it will print 2

twod=np.array([[1,2,3,4],[5,6,7,8]])
print()