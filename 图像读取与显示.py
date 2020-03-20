
#opencv基础学习【1】--读取并显示图片
#自学笔记 仅供参考 欢迎指正

# 这是本人自学的一些笔记 仅供参考  更多的学习笔记大家可以参照我的博客 第一篇https://www.cnblogs.com/Cqy-96/p/12532005.html
# 里面对每个函数的参数都有详细解释
# 谢谢大家！
# 1.导入opencv库
import  cv2 as cv

# 2.读取某个路径下的图片
src=cv.imread("F:\opencv learn\p11.jpg")

# # 3.创建窗口
# cv.namedWindow("P11",cv.WINDOW_AUTOSIZE)

# 4.显示图片
cv.imshow("picture",src)


# 注意如果上面nameWindow函数中第一个参数"picture"和imshow中第一个参数“picture"使用不同名称 会显示两个窗口
# 平时 我们可以把namewindow这个代码省去不写

# 5.窗口显示时间
cv.waitKey(0) #这里可以不填0 都表示一直显示

# 6.删除建立的窗口 释放资源
cv.destroyAllWindows()

