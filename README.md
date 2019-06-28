Welcome! This directory contains all source code for FDUSystem (I named it :) )

#### 1. file tree

文件结构见filetree.txt文件中的内容。

#### 2. environment

##### 2.1 环境

**Django 2.1.7**  

**Bootstrap 3.3.7**

**Python 3.6.8**

##### 2.2 工具

**PyCharm 2018.2.4 PE**

**MySQL Work Bench 8.0.15 CE**

**Google Chrome  74.0.3729.131 (Official Build) (64-bit)**

#### 3. finish project

##### 3.1 生成Django项目

​		这个用PyCharm可以自动生成项目并初始化。修改settings.py关于自定义app部分，详细可见Django教程。

##### 3.2 创建数据库

​		用mysql创建数据库，并修改项目mysite目录下的settings.py文件中对应数据库绑定的部分内容，使项目可以连接到数据库。

##### 3.3 Model

​		在models.py文件中写入想要创建的模型，在admin.py文件中将所有模型进行注册。

​		然后用terminal的两个命令`python manage.py makemigrations FDUSystem` 和 `python manage.py migrate`部署到数据库中。

​		然后，在MySQL Work Bench客户端运行mysql目录下的pj_data_insert.sql文件，插入部分初始数据。

##### 3.4 Static 目录

​		把下载好的bootsrap文件导入到新建的Static目录，作为将要备用的渲染静态文件，然后再在settings.py文件中修改响相应的目录。

##### 2.4 Template 目录

​		把所有的前端页面HTML文件都写在了这个文件夹下。

##### 3.5 views.py

​		这个文件中写入了所有要用的视图函数，从登陆注册到增删查改退出登录。

##### 3.6 app.py

​		这个文件中把该项目注册成一个App并赋予名称，并修改settings.py中相应部分内容。









