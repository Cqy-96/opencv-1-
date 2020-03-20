# opencv-1-
opencv基础学习笔记【1】--图像读取与显示
函数及参数详细说明：
Blog：https://www.cnblogs.com/Cqy-96/
B站：https://space.bilibili.com/301389626

1、cv.imread(const String& filename,int flags)

　　const String& filename：该参数表示的是图片的地址 斜杠可以任意（"/"、"\"、"\\"、"//"）

　　　　在Windows操作系统下，OpenCV的imread函数支持如下类型的图像载入：

　　　　　　JPEG文件 - *.jpeg, *.jpg, *.jpe

　　　　　　JPEG 2000文件- *.jp2

　　　　　　PNG图片 - *.png

　　　　　　便携文件格式- *.pbm, *.pgm, *.ppm

　　　　　　Sun rasters光栅文件 - *.sr, *.ras

　　　　　　TIFF 文件 - *.tiff, *.tif

　　　　　　Windows位图 - *.bmp,*.dib

　　int flags:该参数是图片读取方式：载入标识，它指定一个加载图像的颜色类型。正常情况这个参数都是忽略的。如果调用时忽略就默认三通道彩色图像。（大概理解、正常这个参数用不上）

　

　　　　　　flags >0返回一个3通道的彩色图像。

　　　　　　flags =0返回灰度图像。

　　　　　　flags <0返回包含Alpha通道的加载的图像。

　　注意的点：正常情况下不载入Alpha通道。如果我们需要载入Alpha通道的话呢，这里就需要取负值。 

 

2、cv.NamedWindow( const char* name, int flags )：用于创建一个窗口  （这个代码不写 通过下面一个cv.imshow函数也可以展示图片）

　　const string& winname：该参数就是窗口名。

　　int flags ：这个参数表示的是窗口的类型。有两个值：

　　　　WINDOW_NORMAL：设置了这个值，用户便可以改变窗口的大小；也可以设为0

　　　　WINDOW_AUTOSIZE：如果设置了这个值，窗口大小会自动调整以适应所显示的图像，并且不能手动改变窗口大小；可以忽略不写

 

3、cv.imshow(const string& winname, InputArray mat):显示图片窗口

　　const string& winname：窗口名（注意：如果写了NamedWindow()函数，这个名称要与它一样，不然会出现两个窗口，一个是NamedWindow的空白窗口，一个是imshow的图片窗口。）

　　InputArray mat:  要显示的图片

 

　　　【篇外知识】imshow 函数详解：

　　　　imshow 函数用于在指定的窗口中显示图像。如果窗口是用CV_WINDOW_AUTOSIZE（默认值）标志创建的，那么显示图像原始大小。

                             否则，将图像进行缩放以适合窗口。而imshow 函 数缩放图像，取决于图像的深度：

　　　　　　　　     如果载入的图像是8位无符号类型（8-bit unsigned），就显示图像本来的样子。

　　　　　　　　     如果图像是16位无符号类型（16-bit unsigned）或32位整型（32-bit integer），便用像素值除以256。也就是说，值的范围是[0,255 x 256]映射到[0,255]。

　　　　　　　　     如果图像是32位浮点型（32-bit floating-point），像素值便要乘以255。也就是说，该值的范围是[0,1]映射到[0,255]。

 

4、waitKey(K) 窗口显示时间，单位：毫秒  

  　　　　k=0: （也可以是小于0的数值）一直显示，键盘上按下一个数字键即会消失

    　　　  k>0:     显示多少毫秒

5、destroyAllWindows()：删除建立的全部窗口，释放资源
