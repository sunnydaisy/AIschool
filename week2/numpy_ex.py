import numpy as np
x=[[1,2,3], [4,5,6], [7,8,9]]
def solution(data):
    arr1 = np.array(data)
    arr2 = np.zeros([2,3])
    arr3 = np.arange(0,10)
    transposed = arr1.T
    power = np.dot(arr1, transposed)
    inverse_arr = np.linalg.inv(arr1)
    diagonal = np.diagonal(arr1)
    product = np.dot(arr1, inverse_arr)
    return arr1, arr2, arr3, transposed, power, inverse_arr, diagonal, product

def print_answer(**kwargs):
    for key in kwargs.keys():
        print(key,":",kwargs[key])

arr1, arr2, arr3, transposed, power, inverse_arr, diagonal, product = solution(x)
print_answer(arr1=arr1,arr2=arr2,arr3=arr3,transposed=transposed,
    power=power,inverse_arr=inverse_arr,diagonal=diagonal,product=product)