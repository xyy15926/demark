# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt
TMP_PNG = "../tmp/tmp2.png"
TMP_VIDEO = "../tmp/tmp.gif"

# %% [markdown]
#
# ## 常用常量
# 
# |ConstantPrefix|Desc|
# |-----|-----|
# |`COLOR_`|颜色空间|
# |`WINDOW_`|窗口模式|
# |`IMREAD_`|图像读取模式|
# |`FONT_`|字体|
# |`BORDER_`|边框（添加）类型|
# |`CV_CAP_PROP_`|视频捕获属性|
# |`LINE_`|线条类型|
# |`EVENT_`|事件类型|
# |`INTER_`|插值算法|
# |`THRESH_`|阈值|
# |`ADAPTIVE_THRESH_`|自适应阈值算法|
# |`CV_`|数据类型|
# |`MORPH_`|形态学|

# %% [markdown]
#
# ## IMIO
#
# ### `imread`, `imwrite`
#
# - `imread(filename[, flags])`：缺省将图像读取为BGR3通道
#   - `flags`：可以指定读取图像的标志，部分常量如下
#
#     |Constant|Value|Desc|
#     |-----|-----|-----|
#     |`IMREAD_UNCHANGED`|-1||
#     |`IMREAD_GRAYSCALE`|0|灰度模式读取|
#     |`IMREAD_COLOR`|1|彩色模式读取|
#
# - `imwrite(name, img[, params])`
#   - `img`三颜色通道应该为BGR顺序
#
# ### `imshow`
#
# - `imshow(winname, mat)`：在`winname`指定窗口中展示`mat`
# - `namedWindow(winname[, flags])`：创建具名窗口
#   - 之后可以通过`winame`指定其，修改大小、在其中展示图像
#   - `flags`指定窗口大小，部分常量如下
#
#     |Constant|Value|Desc|
#     |-----|-----|-----|
#     |`WINDOW_NORMAL`|0|此时可通过`resizeWindow`设置大小|
#     |`WINDOW_FULLSCREEN`|1||
#     |`WINDOW_AUTOSIZE`|1||
#
# ### Destroy Window
#
# - `.destroyWindow(name)`：删除窗口
# - `.destroyAllWindows()`：删除所有建立的窗口
#   - 必须被调用以释放资源，否则会报错
#
# <https://juejin.cn/post/6870776834926051342>
# 

win = cv2.namedWindow("im", 0)
cv2.resizeWindow("im", 100, 100)
im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
cv2.imshow("im", im)
while True:
    # wait util key pushed down, or window just flashed out
    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
cv2.imwrite("tmp.png", im)

# %% [markdown]
#
# ## 图像处理
#
# ### 基本变换
#
# |function|desc|
# |-----|-----|
# |`split(mv[, dst])`|拆分图像通道|
# |`merge(b,g,r)`|合并图像通道|
# |`copyMakeBorder(src,top,bottom,left,right,borderType)`|添加边框|
# |`add(src1,src2[,dst[,mask[,dtype]]])`|图像饱和叠加（超过255置255）|
# |`addWeighted(src1,alpha,src2,beta,gamma[,dst[,dtype]])`|加权混合|
# |`bitwise_and(src1,src2[,dst[,mask]])`|按位与|
# |`bitwise_or(src1,src[,dst[,mask]])`|按位或|
# |`bitwise_xor(src1,src[,dst[,mask]])`|按位异或|
# |`bitwise_not(src[,dst[,mask]])`|按位否|

im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
b,g,r = cv2.split(im)
im_copy = cv2.merge((b, g, r)) 
bordered = cv2.copyMakeBorder(im, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

# %% [markdown]
#
# ### Color Space Conversion
#
# - 主要的色彩空间：RGB(BGR)、GREY、HSV
#   - RGB(BGR)：三颜色通道
#   - GERY：灰度
#   - HSV：Hue(0-179), Saturation(0-255), Value(0-255)
#     - 不同规范下HSV取值范围可能不同
#     - HSV空间下方便选取特定颜色，根据特定Hue设置Saturation、Value
#       即可
#
# - `cvtColor(src,code[,dst[,dstCn]])`：图像色彩空间转换
#   - 部分常用色彩空间转换常量`code`
#
#     |Cvt2Clr|Desc|
#     |-----|-----|
#     |`COLOR_BGR2RGB`||
#     |`COLOR_BRG2GREY`||
#     |`COLOR_BGR2HSV`||
#
# - `inRange(src,lowerb,upper[,dst])`：检查各像素点是否位于指定范围
#   - 在范围内的像素点被置为255，否则置为0

im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
im_mask = cv2.inRange(im_hsv, np.uint8([0, 0, 0]), np.uint8([0, 255, 255]))
plt.imshow(im_mask)

# %% [markdown]
#
# ### 几何变换
#
# |function|desc|
# |-----|-----|
# |`flip(src, flipCode[, dst])`|反转图像|
# |`resize(src,dsize[,dst[,fx[,fy[,interpolation]]]])`||
# |`warpAffine(src,M,dsize[,dst[,flags[,borderMode[,borderValue]]]])`|仿射变换|
# |`warpPerspective(src,M,dsize[,dst[,flags[,borderMode[,borderValue]]]])`|透视变换|

# 0: flip around x-axis; positive: y-axis; negtive: both
im_fliped = cv2.flip(im, 0)
# Resize
im_lg = cv2.resize(im, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
im_sm = cv2.resize(im, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Mix
im_mixed = cv2.addWeighted(im, 0.5, im_fliped, 0.5, 0)

# Affine Transformation: y = (A|b)x, A旋转，b平移，x像素点坐标
# `dtype` must be `float`
mv_mtrx = np.array([[1,0,100], [0,1,100]], dtype=np.float64)
im_mv = cv2.warpAffine(im, mv_mtrx, (512, 512))
# Create matrix (A|b) with ratation params
rot_mtrx = cv2.getRotationMatrix2D((256, 256), 45, 0.6)
im_rot = cv2.warpAffine(im, rot_mtrx, (512, 512))
# Create matrix (A|b) with positions of 3points in ori and new im
ori_pos = np.float32([[20, 20], [26, 40], [78, 60]])
new_pos = np.float32([[23, 56], [32, 78], [100, 12]])
pts_mtrx = cv2.getAffineTransform(ori_pos, new_pos)
im_pts = cv2.warpAffine(im, pts_mtrx, (512, 512))
plt.imshow(im_pts)

# Perspective Transformation
ori_pos = np.float32([[56,65],[368,52],[28,387],[389,390]])
new_pos = np.float32([[0,0],[300,0],[0,300],[300,300]])
pspt_mtrx = cv2.getPerspectiveTransform(ori_pos, new_pos)
im_pspt = cv2.warpPerspective(im, pspt_mtrx, (1000, 1000))
plt.imshow(im_pspt)

# %% [markdown]
#
# ### Threshold
# 
# |function|desc|
# |-----|-----|
# |`threshold(src,thresh,maxval,type[,dst])`|阈值过滤|
# |`adaptiveThreshold(src,maxVal,adaptiveMethod,thresholdType,blockSize,C[,dst])`|自适应阈值过滤|
#
# - 阈值过滤常量包括
#   - `THRESH_BINARY`：二值化，高
#   - `THRESH_BINARY_INV`：二值化、反转
#   - `THRESH_TRUNC`：截断
#   - `THRESH_TOZERO`：高于阈值置0
#   - `THRESH_TOZERO_INV`：低于阈值置0
#   - `THRESH_OTSU`：Otsu's选择阈值过滤，适合有双峰灰度图（选择双峰直接
# - 自适应阈值过滤方法常量包括
#   - `ADAPTIVE_THRESH_MEAN_C`：阈值取为临近区域均值（-`C`）
#   - `ADAPTIVE_THRESH_GAUSSIAN_C`：阈值取为临近区域高斯加权 （-`C`）

im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Threshold
trsh, im_trsh_bi = cv2.threshold(im_grey, 127, 255, cv2.THRESH_BINARY)
# 1. Set thresh with 0
# 2. `trsh` returned was the threshold found with Otsu's
trsh, im_trsh_otsu = cv2.threshold(im_grey, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# AdaptiveThreshold
im_trsh_ada = cv2.adaptiveThreshold(im_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
plt.imshow(im_trsh_ada)

# %% [markdown]
#
# ### Filter
#
# - *Low-pass Filter*低通滤波：去除噪音，模糊图像
# - *High-pass Filter*高通滤波：梯度滤波，提取轮廓
#
# |Function|Desc|
# |-----|-----|
# |`filter2D(src,ddepth,kernel[,dst[,anchor[,delta[,borderType]]]])`|二维卷积|
# |`getStructuringElement(shape,ksize[,anchor])`|创建核|

im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
kernel = kernel / kernel.sum()
# ddepth(-1): src's depth
im_filtered = cv2.filter2D(im, cv2.CV_8U, kernel)
cv2.imshow("", im_filtered)
cv2.waitKey()
cv2.destroyAllWindows()

# %% [markdown]
#
# #### Blur
#
# |Function|Desc|
# |-----|-----|
# |`blur(src,ksize[,dst[,anchor[,borderType]]])`|正则化box filter|
# |`GaussianBlur(src,ksize,sigmaX[,dst[,sigmaY[,borderType]]])`|高斯blur|
# |`medianBlur(src,ksize[,dst])`|中值blur|
# |`bilateralFilter(src,d,sigmaColor,sigmaSpace[,dst[,borderType]])`|双边filter|
#
# > - 图像深度：实际存储图像灰度、色彩所需的bits
# > - 像素深度：存储每个像素需要bits

kernel = np.ones((5,5)) / 25
im_blured = cv2.blur(im, (5, 5))
# 0: calculate `sigmaX` according to ksize
im_gauss = cv2.GaussianBlur(im, (5,5), 0)
im_med = cv2.medianBlur(im, 5)
# d: kernel diameter
im_bi = cv2.bilateralFilter(im, 9, 0, 0)
cv2.imshow("", im_gauss)
cv2.waitKey()
cv2.destroyAllWindows()

# %% [markdown]
#
# #### Gradient
#
# - 梯度滤波器
#   - Sobel算子：一阶、二阶导数
#   - Scharr算子：使用小卷积核求解梯度角度时的优化
#   - Laplacian算子：二阶导数
#
#   |Function|Desc|
#   |-----|-----|
#   |`Sobel(src,ddepth,dx,dy[,dst[,kszie[,scale[,delta[,borderType]]]]])`||
#   |`Scahrr(src,ddepth,dx,dy[,dst[,kszie[,scale[,delta[,borderType]]]]])`||
#   |`Laplacian(src,ddepth[,dst[,kszie[,scale[,delta[,borderType]]]]])||

im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
# Use `ddepth=cv2.CV_64F` to keep negtive pixel
im_lap = cv2.Laplacian(im, cv2.CV_64F)
im_sobel_x = cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=5)
im_sobel_y = cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("", im_sobel_x)
cv2.waitKey()
cv2.destroyAllWindows()

# %% [markdown]
#
# #### Morphology Transformation
#
# - 腐蚀：腐蚀前景（高亮）边界，高亮区域变小
#   - 卷积核沿图像滑动，若卷积核对应的所有元素均为高亮，则`anchor`处
#     元素设置为高亮
#   - 用途
#     - 去除白噪声
#     - 断开相连接的物体
# - 膨胀：膨胀前景（高亮）边界，高亮区域变大
#   - 卷积核沿图像滑动，若卷积核存在对应元素为高亮，则`anchor`处元素
#     设置为高亮
# - 衍生运算
#   - `MORPH_OPEN`开运算：先腐蚀再膨胀
#     - 消除白噪声：腐蚀去白噪声，膨胀恢复原前景（高亮）部分
#   - `MORPH_CLOSE`闭运算：先膨胀再腐蚀
#     - 填充前景（高亮）部分低亮
#   - `MORPH_GRADIENT`：膨胀与腐蚀的差别
#     - 类似前景的轮廓
#   - `MORPH_TOPHAT`：原始图像与进行开运算之间的差
#   - `MORPH_BLACKHAT`：闭运算图像与原始图像直接差
#
# |Function|Desc|
# |-----|-----|
# |`erode(src,kernel[,dst[,anchor[,iteration[,borderType[,borkderValue]]]]])`|腐蚀|
# |`dilate(src,kernel[,dst[,anchor[,iteration[,borderType[,borkderValue]]]]])`|膨胀|
# |`morphotogyEx(img,op,kernel[,dst[,anchor[,iterations[,borderType[,borderValue]]]]])`|形态学变换|

im = cv2.imread(TMP_PNG, cv2.IMREAD_UNCHANGED)
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
# `kernel`: just specifies the coverage, A.K.A. boolean
im_eroded = cv2.erode(im_gray, kernel, iterations=1)
im_dilated = cv2.dilate(im_eroded, kernel, iterations=1)
# morphology open
im_open = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
# morphology close
im_close = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
# morphology gradient
im_grad = cv2.morphologyEx(im, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("", im_grad)
cv2.waitKey()
cv2.destroyAllWindows()


# %% [markdown]
#
# ## 图像绘制
#
# ### 基本几何

bimg = np.zeros((512, 512, 3), np.uint8)
# Line: bg, start, end, color, thichness, linestyle
cv2.line(bimg, (0,0), (260, 130), (12, 43, 32), 5)
# Rectange: bg, vertex, opposite vertex, color, thickness, linestyle
cv2.rectangle(bimg, (200,200), (340, 230), (123, 45, 78), 2)
# Circle: bg, center, radius, color, thickness, linestyle
cv2.circle(bimg, (255,0), 49, (77, 177, 123), 3)
# ellipse: img, (a,b), rotation, start_angle, end_angle, color, thickness, linestyle
cv2.ellipse(bimg, (255, 255), (70, 45), 45, 0, 90, (123, 222, 11), 3)

# Poly: img, ptrs, closed, color, linestyle
ptrs = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# Points should follow the format `N * 1 * 2`
ptrs = ptrs.reshape((-1, 1, 2))
cv2.polylines(bimg, [ptrs], True, (233, 233, 233), 3)

# Font:m img, text, bottom-left, font-type, font-scale, color, thickness, linestyle, bottomLeftOrigin
cv2.putText(bimg, "OpenCV蛤", (10, 500),
        cv2.FONT_HERSHEY_SIMPLEX, 2,
        (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("", bimg)
while True:
    if cv2.waitKey() & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break


# %%
#
# ## VideoCapture, VideoWriter
# 
# ### `VideoCapture`
#
# - `VideoCapture()`：捕获视频
#   - 缺省值`0`表示计算机默认摄像头，可以用数字指定其他摄像头
#   - 可以通过文件名从文件中捕获，包括GIF文件（但是因为专利无法存储）
#
# - `<VideoCapture>`：捕获视频类
#   - `.get(propID)`：获取视频参数信息，propID取值0-18，具体
#     常量名称如下
#
#     |Constant|Desc|
#     |-----|-----|
#     |`CV_CAP_PROP_POS_MSEC`||
#     |`CV_CAP_PROP_POS_FRMAES`||
#     |`CV_CAP_PROP_POS_AVI_RATIO`||
#     |`CV_CAP_PROP_FRAME_WIDHT`||
#     |`CV_CAP_PROP_FRAME_HEIGHT`||
#     |`CV_CAP_PROP_FPS`||
#     |`CV_CAP_PROP_FOURCC`||
#     |`CV_CAP_PROP_FORMAT`||
#     |`CV_CAP_PROP_MODE`||
#     |`CV_CAP_PROP_BRIGHTNESS`|仅摄像头捕获|
#     |`CV_CAP_PROP_CONSTRACT`|仅摄像头捕获|
#     |`CV_CAP_PROP_SATURATION`|仅摄像头捕获|
#     |`CV_CAP_PROP_HUE`|仅摄像头捕获|
#     |`CV_CAP_PROP_GAIN`|仅摄像头捕获|
#     |`CV_CAP_PROP_EXPOSURE`|仅摄像头捕获|
#     |`CV_CAP_PROP_CONVERT_RGB`|是否应该转换为RGB|
#     |`CV_CAP_PROP_WHITE_BALANCE`||
#     |`CV_CAP_PROP_RECTIFICATION`||
#
# ### `VideoWriter`
# 
# - `VideoWriter(name,fourcc,fps,(width, height))`
#   - 图像帧长、宽都必须为`height, width`，否则生成文件无效
# 
# - `VideoWriter_fourcc`：将四字符转换为视频编码格式
#   - 实际上就是把参数字符8bits值拼接为32bits的整形（逆序）

cap = cv2.VideoCapture(TMP_VIDEO)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
width, height = int(cap.get(3)), int(cap.get(4))
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (width, height))
# check if inited successfully
while(out.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()

# %%
#
# ## Event Listening
# 
# ### KeyboardEvent
#
# #### `waitKey`
#
# - `waitKey(T)`：等待键盘输入ms，缺省0永久等待
#   - HighGUI窗口唯一获取和处理事件的方法
#     - 直接监听键盘输入
#     - 在其之前创建的HighGUI（OpenCV GUI）窗口才起作用
#     - 控制图像展示的时间
#   - 大多数平台上，`.waitKey`返回0-255之间的值，但是在某些
#     平台上返回值超过255，因此常用`0xFF`截断
#
# ### MosueEvent
#
# #### `setMouseCallback`
#
# - `setMouseCallback(windowName, onMouse[, param])`
#   - `onMouse(event, x, y, flags, param)`：回调函数，常用的监听事件
#
#       |Event|Desc|
#       |-----|-----|
#       |`EVENT_LBUTTONDBLCL`||
#       |`EVENT_MOUSEMOVE`||
#       |`EVENT_FLAG_LBUTTON`||
#       |`EVENT_LBUTTONUP`||
#       |`EVENT_LBUTTONDOWN`||

drawing = False
mode = False
ix, iy = -1, -1
bimg = np.zeros((512, 512, 3), np.uint8)
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(bimg, (x, y), 10, (233, 233, 233), 1)
def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(bimg, (ix,iy), (x,y), (0, 255, 0), -1)
            else:
                cv2.circle(bimg, (x,y), 0, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
cv2.namedWindow("event")
cv2.setMouseCallback("event", draw_rect)
while True:
    cv2.imshow("event", bimg)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# %%
#
# ## Utils
#
# |Function|Util|
# |-----|-----|
# |`createTrackbar(trackbarname,winname,value,count,onChange)`|滑轨|
#
# ### Trackbar

def nothing(x):
    pass
bimg = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
for clr in list("RGB"):
    cv2.createTrackbar(clr, "image", 0, 255, nothing)
cv2.createTrackbar("0:OFF\n1:ON", "image", 0, 1, nothing)
while True:
    cv2.imshow("image", bimg)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

    rgb = [0] * 3
    for idx, clr in enumerate("RGB"):
        rgb[idx] = cv2.getTrackbarPos(clr, "image")
    s = cv2.getTrackbarPos("0:OFF\n1:ON", "image")
    if s == 0:
        bimg[:] = 0
    else:
        bimg[:] = rgb[::-1]

# %%
#
# ## Others
#
# ### Efficience
#
# |Function|Desc|
# |-----|-----|
# |`getTickCount()`|获取tick数|
# |`getTickFrequency()`|获取时钟频率，即每秒tick数|
# |`useOptimized()`|优化是否被开启
# |`setUseOptimized()`|开启优化|

e1 = cv2.getTickCount()
e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()


# %%
