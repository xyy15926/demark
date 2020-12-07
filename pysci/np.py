#!/usr/bin/env python3
#----------------------------------------------------------
#   Name: np.py
#   Author: xyy15926
#   Created at: 2020-11-17 08:51:37
#   Updated at: 2020-11-17 08:52:37
#   Description: Notes for studying numpy, including some
#     code.
#----------------------------------------------------------

# %%
import numpy as np 
import os

# %% [markdown]
# ## NDA元素选择、运算
# %% [markdown]
#
# ### Numpy Index, Slice, Shape

data = np.arange(24)
# reshape
print("reshape: ", data.reshape(3, 8))
print("resize: ", np.resize(data, (3, 8)))

# flatten
print("ravel: ", data.ravel())
print("flatten: ", data.flatten())

# transpose
print("transpose: ", data.transpose())

# Index and Slice
print("index and slice: ", data.reshape(2,3,4)[:,1,:-1])
print("unravel index: ", np.unravel_index(13, (2, 3, 4)))

# %% [markdown]
# ### Constuct NDArray

print(np.identity(3))
print(np.eye(3, 4))
print(np.ones((3, 3)), np.zeros((3, 3)))
print(np.tile([1,2], [3, 2]))
# generate point's in coordinators on 2D-plane
print(np.mgrid([:3, 4:7]))

# %% [markdown]
#
# ### 自定义数据类型

T = np.dtype([("name", "U40"), ("age", np.uint8), ("math", np.float64)])
data = np.array([
    ("熊", 12, 78.2),
    ("xiaohong", 23, 67.3)
], dtype=T)

# %% [markdown] 
#
# ### Broadcast
#
# - 广播兼容规则
#   - 从两Array的shape尾部开始比对
#     - 低维Array是高维Array的子集，所以
#   - 若两数组维度相同，对应位置上轴的长度相同、或某个轴长度为1，广播兼容
#   - 若两数组维度不同，给低维数字前扩展一维，扩展维的长度为1，然后在扩展
#     维度上进行广播机制处理
#
# ### Mask
#
# - Mask机制：通过bool类型NDA选取部分元素，对其进行操作
#   - 切片、筛选结果共享数据
#   - bool类型NDA选取部分元素修改值影响原始NDA
# - 注意
#   - 筛选出的元素维度为：未参与维度 + 1（即筛选后得到元素Seq)
#   - 仅筛选结果可以修改值，对筛选结果再次切片赋值无效
#   - 可先对NDA切片再筛选元素，以修改部分值

data = np.zeros((6, 5, 4))
data[:, :, -1][np.eye(6, 5) == 1] = 1

# %% [markdown]
#
# ## 结构变化
#
# ### Merge, Concatenate, Stack

data = np.arange(2 * 3 * 4).reshape(4, 6)
data_square = data ** 2

# hstack/row_stack: stack along axis-0
hstacked = np.hstack([data, data_square, data])
print("hstack: ", hstacked)
row_stacked = np.row_stack([data, data_square, data])
print("row_stack: ", row_stacked)

# vstack/column_stack: stack along axis-1
# 1. if number of axis <= 1, new axis will be added
vstacked = np.vstack([data, data_square, data])
print("vstack: ", vstacked)
column_stacked = np.column_stack([data, data_square, data])
print("column_stack: ", column_stacked)

# dstack: stack along axis-2
# 1. if number of axis <= 1, new axis will be added
dstacked = np.dstack([data, data_square, data])
print("dstack: ", dstacked)

# concatenate: concat along any axis **existing**
concat_h = np.concatenate([data, data_square, data], axis=1)
print("concat horizontally", concat_h)
concat_v = np.concatenate([data, data_square, data], axis=0)
print("concat vertically", concat_v)

# rot90
# 1. `k`: rotate times, clock-wise when negtive
data = np.arange(9).reshape(3, 3)
print(np.rot90(data, k=1))

# %% [markdown]
# 
# ### Split

data = np.arange(2 * 3 * 4).reshape(4, 6)

# hsplit: split along axis-0
hsplited = np.hsplit(data, 3)
print("hsplited: ", hsplited)

# vsplit: split along axis-1
vsplited = np.vsplit(data, 2)
print("vsplited: ", vsplited)

# dsplit: split along axis-2
dsplited = np.dsplit(data.reshape(2, 3, 4), 2)
print("dsplited: ", dsplited)

# split: split along any axis
splited_0 = np.split(data.reshape(2, 3, 4), 2, axis=0)
splited_1 = np.split(data.reshape(2, 3, 4), 3, axis=1)
splited_2 = np.split(data.reshape(2, 3, 4), 2, axis=2)
print("splited 0, 1, 2", splited_0, splited_1, splited_2)


# %% [markdown]
#
# ## Statistics Function

iris_X = np.loadtxt(
    "./resources/iris.data",
    dtype = np.float64,
    delimiter = ",",
    usecols = [0, 1, 2, 3],
    comments = "#",
    unpack = True
)

print(np.sum(iris_X, axis=1))
print(np.mean(iris_X, axis=0))
print(np.average(iris_X, axis=0))
print(np.ptp(iris_X, axis=0))
print(np.median(iris_X, axis=0))
print(np.std(iris_X, axis=0))
print(np.var(iris_X, axis=0))
print(np.min(iris_X, axis=0), np.max(iris_X, axis=0))
print(np.argmin(iris_X, axis=0), np.argmax(iris_X, axis=0))
print(np.cov(iris_X))
print(np.corrcoef(iris_X))

# %% [markdown]
#
# ## Random
#
# |Functions|Description|
# |-----|-----|
# |`rand(d0,d1,...,dn)`| Uniform([0, 1))|
# |`uniform(low, high, size)`| Uniform|
# |`randn(d0,d1,...,dn)`| Norm|
# |`normal(loc, scale, size)`| Norm|
# |`poisson(lam, size)`| Poisson(lam)|
# |`randint(low[, high, shape])`| Uniform Int|
# |`seed(s)`||
# |`shuffle(a)`| 修改`a`|
# |`permutation(a)`| 返回新Array|
# |`choice(a[, size, replace, p])`| 按概率`p`抽取元素|


# %% [markdown]
#
# ## Math Funtions
#
# ### Basic Math Functions
# |Functions|Description|
# |-----|-----|
# |`abs`||
# |`sqrt`||
# |`square`||
# |`log`, `log2`, `log10`||
# |`rint`, `ceil`, `floor`||
# |`modf`||
# |`cos`, `cosh`, `sin`, `sinh`, `tan`, `tanh`||
# |`exp`||
#

data = np.arange(2 * 3 * 4).reshape(4, 6)
data[:2, :] *= -1

# basic math functions
print(np.abs(data))
print(np.sqrt(data))
print(np.square(data))
print(np.log(data), np.log2(data), np.log10(data))
print(np.rint(data), np.ceil(data), np.floor(data))
print(np.modf(data))
print(np.cos(data), np.cosh(data))
print(np.sin(data), np.sinh(data))
print(np.tan(data), np.tanh(data))

# %% [markdown]
#
# ### Array's Matrix Calculation

a = np.arange(2 * 3 * 4).reshape(4, 6)
b = np.arange(4, 2 * 3 * 4 + 4).reshape(4, 6)

# `inner`：向量、矩阵内积
inner_ = np.inner(a, b)
# `outer`：向量外积，克罗内克积，矩阵外积等同于其展开后向量外积
outer_ = np.outer(a, b)

# `matmul`：矩阵乘法，shape需满足线代要求
matmul_ = np.matmul(a, b.T)
# `dot`：可用于多维矩阵乘积
dot_ = np.dot(a, b.T)


# %% [markdown]
#
# ## Matrix
#
# - matrix和ndarray区别
#   - matrix和ndarray乘法规则不同，需要满足线代的要求
#   - matrix的shape维度总是2

mtx_1 = np.matrix([[1, 2, 3], [4, 5, 6]])
mtx_2 = np.matrix("1,2,3;4,5,6;7,8,9")
print("matrix multiply: ", mtx_1 * mtx_2 - np.matmul(mtx_1, mtx_2))
print("matrix shape: ", mtx_1[0].shape)

# %% [markdown]
#
# ## Linear Algebra Functions
#
# |Functions| Description|
# |-----|-----|
# |`linalg.det(a)`|行列式|
# |`linalg.matrix_rank(a)`|秩|
# |`linalg.eig(a)`|特征值、特征向量|
# |`linalg.inv(a)`, `linalg.pinv(a)`|逆矩阵、Moore-Penrose伪逆矩阵|
# |`linalg.qr(a)`|QR分解|
# |`linalg.svd(a)`|奇异值分解|
# |`linalg.solve(A, b)`|$Ax=b$求解|
# |`linalg.lstsq(A, b)`|$Ax=b$最小二乘解|
# |`linalg.norm(A, ord)`|$A$的`ord`范数|
#
# - `np.linalg`：使用浮点数计算结果可能有误差
#   - `np.linalg.det`计算浮点整数也会有误差，如以下`A`是非奇异矩阵，其行列式为
#      非零值
#   - 并由此如下的`np.linalg.solve`会认为可以正常求解，但得到错误结果
#

# linear algebra functions
A = np.arange(2 * 3 * 4).reshape(4, 6)[:, :4]
b = np.arange(4)
X = np.linalg.solve(A, b)
print(np.allclose(np.dot(A, X), b))
# vector's infinite norm
print(np.linalg.norm(A[0], ord=np.inf))
# matrix's Frobenius norm
print(np.linalg.norm(A, ord="fro"))

# %% [markdown]
# ## Polynomial Functions
# TODO


# %% [markdown]
# ## Load, Save

# load txt
iris_X = np.loadtxt(
    "./resources/iris.data",
    dtype = np.float64,
    delimiter = ",",
    usecols = [0, 1, 2, 3],
    comments = "#"
)
iris_Y = np.loadtxt(
    "./resources/iris.data",
    dtype = "S",
    delimiter = ","
)
# load txt with DIY dtype
T = np.dtype([
    ('sepal_length', 'f'),
    ('sepal_width','f'),
    ('petal_length','f'),
    ('petal_width','f'),
    ('class','S20')
])
iris = np.loadtxt("./resources/iris.data", dtype=T, delimiter=",")

# save txt
saved = np.savetxt("./resources/iris.csv", iris, fmt="%3.1f:%3.1f:%3.1f:%3.1f:%s")
