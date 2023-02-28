# """
# -*- coding: utf-8 -*-
#
# @作者(Author) : Chen Jiahao
# @时间(Time) : 2023/2/16 18:56
# @File : confirm_center.py
# """
#
# import cv2 as cv
# import glob
# import os
# import numpy as np
# path = r"E:\pycharm_project\FPI_tool\train_dataset"
#
# for i in (glob.glob(os.path.join(path, "*"))):
#     satellite_path = i +"/Satellite/0.tif"
#     print(satellite_path)
#     uav_path = i +"/UAV/0.JPG"
#     satellite_map = cv.imread(satellite_path)
#     uav_map = cv.imread(uav_path)
#
#     satellite_map = cv.resize(satellite_map, [800, 800])
#
#
#     satellite_map = cv.circle(satellite_map, [400, 400], 1, [0, 0, 255],3)
#     satellite_map = satellite_map[200:600, 200:600, :]
#     satellite_map = cv.resize(satellite_map, [800, 800])
#     uav_map = cv.resize(uav_map, [800, 800])
#     uav_map = cv.circle(uav_map, [400, 400], 2, [0, 0, 255],5)
#     cv.imshow("aa", satellite_map)
#     cv.imshow("bb", uav_map)
#     cv.waitKey(0)

# from pyheatmap.heatmap import HeatMap
import numpy as np
N = 10000
X = np.random.rand(N) * 255  # [0, 255]
Y = np.random.rand(N) * 255
data = []
for i in range(N):
  tmp = [int(X[i]), int(Y[i]), 1]
  data.append(tmp)
heat = HeatMap(data)
heat.clickmap(save_as="1.png") #点击图
heat.heatmap(save_as="2.png") #热图