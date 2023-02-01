'''
Author: philosophylato
Date: 2022-12-01 17:17:32
LastEditors: philosophylato
LastEditTime: 2022-12-01 17:30:11
Description: your project
version: 1.0
'''
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from matplotlib import font_manager
# fname中选择一个你本机查询出来的字体 若没有中文字体则需要你本人手动安装
#font = font_manager.FontProperties(fname="/root/largeModel/SimHei.ttf")

x_axis_data = [i for i in range(2000,16319,2000)]
y_axis_data1 = [90.23,90.54,91.12,93.09,94.45,95.90,96.34,97.02]
y_axis_data2 = [90.06,90.08,91.02,92.43,93.06,93.25,93.57,92.75]
y_axis_data3 = [81.43,83.32,79.78,78.89,78.23,83.55,80.55,82.55]

plt.title('随电表数量准确率的变化')
plt.plot(x_axis_data, y_axis_data1,label='使用预训练模型-epoch=50',linewidth=5,linestyle=':')#,fontproperties=font)
plt.plot(x_axis_data, y_axis_data2,label='不使用预训练模型-epoch=600',linewidth=2,linestyle='--')#,fontproperties=font)
plt.plot(x_axis_data, y_axis_data3,label='不使用预训练模型-epoch=50',linewidth=3,linestyle='-')#,fontproperties=font)
plt.xlabel('电表数量')#,fontproperties=font)
plt.ylabel('准确率%')#,fontproperties=font)
plt.legend()
plt.show()
plt.savefig('./demo.jpg')  # 保存该图片
