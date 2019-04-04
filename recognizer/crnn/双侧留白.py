import cv2
import os
import numpy as np

img = cv2.imread('00328_gt_.jpg')
print(img.shape)

# 生成画布
back_groud = np.zeros((img.shape[0], img.shape[1]+32, 3))
print(back_groud.shape)
# print(back_groud)
# 提取左上和左下的像素点，取平均
upper_left_corner = img[3, 3, :]
print(upper_left_corner)

lower_left_corner = img[img.shape[0]-3, 3, :]
print(lower_left_corner)

average_pixel = upper_left_corner + lower_left_corner
print(average_pixel, average_pixel.dtype)

# 给左右区域赋值
back_groud[0:img.shape[0], 16:img.shape[1]+16, :] = img
print(back_groud.shape)

back_groud[:, img.shape[1]+16:back_groud.shape[1], :] = average_pixel
back_groud[:, 0:16, :] = average_pixel
x = back_groud[:, img.shape[1]+16:back_groud.shape[1], :]

# 保存
print(x.shape, x.dtype)
cv2.imwrite('留白部分.png', x)
cv2.imwrite('单侧留白.png', back_groud)