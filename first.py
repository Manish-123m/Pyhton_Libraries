import numpy as np
import array as arr

 l1=[1,2,3,4,"Manish",5,6,9,8,7]
l1.append(12)
print(l1)



arr1 = arr.array(i, [1, 2, 3, 6, 5, 4])
print(arr1)


arr2=np.array([1,2,3,6,5,4],int)
print(arr2*2)
print(arr2+5)
####  ================= 1D array  ==================

import numpy as np
arr1=np.array([1,2,3,4,5,6])
sum=0
for i in range (0,len(arr1)):
    sum=sum+arr1[i]
print(sum)


####  ================= 2D array  ==================


import numpy as np
import array as arr
array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(array_2d)
print(array_2d[2,2])
print(array_2d[1,3])
print(array_2d.shape)
resh_2d=array_2d.reshape(3,3)
print(resh_2d)
print("===============================================")
print(resh_2d.shape)



#########===========  Slicing ==========
array_2d=np.array([[1,2,3],[4,5,6],[7,8,9],[7,23,15]]) 
print(array_2d[:,1])
print(array_2d[0,:])
print(array_2d)
print(array_2d[:])
# print(array_2d[::3,:])
print(array_2d[::2,::2])
print(array_2d[:,-1])
print(array_2d.shape)
reshape=array_2d.reshape(3,12)
reshape=array_2d.reshape(3,4)
reshape=array_2d.reshape(4,4)
print(reshape)
print(len(array_2d))   
print(len(array_2d[3]))

row_len=len(array_2d)
col_len=len(array_2d[3])
print(row_len-1,col_len-1)
print(array_2d[0,0]+array_2d[row_len-1,col_len-1])

 #########   ==========================================       3D array           ===================================================
# arr_3d=np.array([[[1,2,3],[4,5,6],[8,9,7],[7,8,9],[78,89,45],[54,65,21]]])
# print(arr_3d)
# print(arr_3d.ndim)
# print(arr_3d.shape)



arr_3d=np.array([[[1,2,3],[4,5,6],[8,9,7]],[[7,8,9],[78,89,45],[54,65,21]]])
print(arr_3d)
print(arr_3d.ndim)
print(arr_3d.shape)


arr_3d=np.array([[[1,2,3],[5,6,4]],[[7,8,9],[10,11,12]],[[45,65,78],[78,96,12]]])
print(arr_3d.ndim)
print(arr_3d.shape)
print(arr_3d)
print(arr_3d[0,1,1])
print(arr_3d[1,1,0])
print(arr_3d[:,0,:])   #####  print all 0 indexing in all block``
print(arr_3d[0:2])
print(arr_3d[::2,::2])
print(arr_3d[1:3])
# =============================   Arange ,,  it arange in 1 d array and also in increasing order  =========================================================")
num=np.arange(24)
print(num)
print("==========================================")
reshape_3d=num.reshape(2,3,4)
print(reshape_3d)
print("==========================================")
print(reshape_3d.shape)
print("==========================================")
print(reshape_3d.size)
print("==========================================")
##########  ===================================== Transpose ================================
trans_3d=np.transpose(reshape_3d,(0,1,2))
print(trans_3d)
print("==========================================")
trans_3d=np.transpose(reshape_3d,(1,0,2))
print(trans_3d)

arr1=np.array([1,2,3,6,5,4])
arr2=np.array([9,8,7,45,46,12])
ar=np.concatenate((arr1,arr2))
print(ar)


arr1=np.array([1,2,3,6,5,4])
arr2=np.array([9,8,7,45,46,12])
arr3=np.array([12,36,45])
ar=np.concatenate((arr1,arr2,arr3))
print(ar)

###########      ========================concatenate=============================
arr1=np.array([[3,6,9,12],[7,8,9,6],[9,6,5,4]])
arr2=np.array([9,12,3,6,18])
conc=np.concatenate([arr1,arr2])
print(conc)
######        ===================   Add column wise  ============================
arr1=np.array([[12,52,3,6],[7,8,9,6],[9,6,5,4]])
arr2=np.array([[78,96,2,6],[7,8,9,6],[9,6,5,4]])
# conc=np.concatenate((arr1,arr2),axis=0)   ##   add by row wise  ===================
conc=np.concatenate((arr1,arr2),axis=1)
print(conc)

########   ========================================                 split   ==============================================

arr=np.array([1,2,3,6,5,4])
split=np.array_split(arr,3)
print(split)


#######   ========================================    raval and flatter   ==============================================
##  i tconvert multi dimensional array into 1D array

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr1.ndim)
ravel=arr1.ravel()
ravel[0]==99
print(arr1)
print(ravel)
print(ravel.ndim)


print("====================================================================================")

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.ndim)
flatter=arr1.flatten()
flatter[0]==525
print(flatter)
print(arr1)
print(flatter.ndim)


import numpy as np
array=np.array([[1,32,3],[4,5,9],[79,54,64]])
print(array.ndim)
ravel_array=array.ravel()
ravel_array[0]=99
print(ravel_array)
print(array)
print(ravel_array.ndim)

print("================================")
import numpy as np
array=np.array([[1,32,3],[4,5,9],[79,54,64]])
print(array.ndim)
flatten_array=array.flatten()
flatten_array[0]=88
print(flatten_array)
print(array)
print(flatten_array.ndim)




arr1d=np.array([1,2,3,6,5,8,4,1,7,8,9])
print(arr1d)
unique=np.unique(arr1d)
print(unique)

arr1d=np.array([1,2,3,6,5,8,4,1,7,8,9])
print(arr1d)
unique=np.unique(arr1d,return_index=True)
print(unique)

arr1d=np.array([1,2,3,6,5,8,4,1,7,8,9])
print(arr1d)
unique=np.unique(arr1d,return_counts=8)
print(unique)

arr2d=np.array([[1,2,3,6],[4,5,6,9],[7,8,9,6]])
unique=np.unique(arr2d)
print(unique)


arr2d=np.array([[1,2,3,6],[4,5,6,9]],[[7,8,9,6],[7,8,9,6]],[[12,36,45,36],[78,89,56,4]])
arr2d=np.array([[1,2,3,6],[1,2,3,6],[4,5,6,9]])
unique=np.unique(arr2d,axis=0)
print(unique)



arr=np.zeros((2,3))
print(arr)

arr=np.ones((2,3))
print(arr)


arr=np.linspace(0,10,5)
print(arr)

arr=np.arange(24)
print(arr)


arr_2d=np.arange(24).reshape(4,6)
print(arr_2d)
print()


arr_3d=np.arange(36).reshape(3,3,4)
print(arr_3d)


import numpy as np
arr_2d = np.arange(24).reshape(4, 6)
print(arr_2d)
print(arr_2d[0:2, 0:2])
arr_2d[0:2,0:2]=0
print(arr_2d)
