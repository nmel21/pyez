import numpy as np
print('Hello')
print(np.cos(6))

np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size = (3, 4, 5))

# print("x3 ndim: ", x3.ndim)
# print("x3 shape: ", x3.shape)
# print("x3 size: ", x3.size)
# print("dtype: ", x3.dtype)
# print("itemsize:" , x3.itemsize, "bytes")
# print("nbytes: ", x3.nbytes, "bytes")

print(x1)
print(x1[0])
print(x1[4])
print(x2)
print(x2[2, -1])
x2[0, 0] = 12
print(x2[0,0])

x = np.arange(10)
x

x[:5]


S = 0.3
b = 2.0

AR = b**2 / S

print('Aspect Ratio:',AR)

def AspectRatio(span, surfArea): 
    c = span**2 / surfArea
    return print('Aspect Ratio is:',c)

AspectRatio(2.5, 0.3)

def fun(x):
    a = 10.0
    return print('function evaluation is ',a * x **2)

fun(3.0)
# def PreCurser()
