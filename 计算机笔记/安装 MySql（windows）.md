# 装MySql

## 装VMWare(虚拟机软件)

1. 下载 - https://my.vmware.com/en/web/vmware/downloads/info/slug/desktop_end_user_computing/vmware_workstation_pro/16_0
2. 安装 - 基本一直下一步
3. 遇到需要秘钥,百度随便搜索一个对应版本的秘钥,一般就可以了

## 在虚拟机中安装操作系统

1. 下载操作系统镜像(.iso)

   https://windows.sczmwj.com/win1064.html

2. 稍后安装操作系统

3. 选择windows10

4. 设置名称/安装位置(桌面)

5. 使用建议的大小,存储为单个文件

6. 自定义设置中

   1. 修改网络:桥接模式,复制物理网络连接状态
   2. cd/dvd: 选择iso镜像文件
   3. **选项-》最下面：高级-》固件类型：选BIOS**
   4. https://blog.csdn.net/qq_34672033/article/details/87885827
   5. https://blog.csdn.net/panjunnn/article/details/108130011

7. 点击[虚拟机->电源->打开电源时进入固件]，进入安装操作系统的界面

8. （按Ctrl+alt可以退出虚拟机）

## 安装MySql

- 安装教程 - https://www.runoob.com/mysql/mysql-install.html
- 下载地址 - https://dev.mysql.com/downloads/mysql/
- 使用教程 - https://www.runoob.com/mysql/mysql-tutorial.html

1. 从上面下载地址下载
2. 解压缩下载好的压缩包(.zip文件)

- 记一下安装时候的初始密码

  ```
  user:     root
  password: P7quS,fl)Za%
  修改后的密码： 123456
  端口：3306（在my.ini文件里可以修改）
  host:localhost(=127.0.0.1)
  ```

- 成功启动了service.一个mysql服务，会一直在后台提供数据服务

  `Service successfully installed.`

- 登录数据库

  ```cmd
  cd C:\web\mysql-8.0.23-winx64\bin
  mysql -u root -p
  ```

- 数据库服务的开关 - 先启动服务后连接

  https://jingyan.baidu.com/article/870c6fc37ca6feb03fe4beac.html

  ```cmd
  # 启动数据库服务
  net start mysql
  
  # 查看mysql是否启动
  管理->服务->查看mysql是否正在运行
  
  # 关闭数据库服务
  net stop mysql
  ```

- 使用编程语言操作mysql (Python)

  https://www.runoob.com/python/python-mysql.html

  ```cmd
  # 首先安装python中用来连接mysql的工具库
  pip install mysqlclient
  ```

  ```python
  import MySQLdb
  
  
  # 1.建立连接
  db = MySQLdb.connect("localhost", "root", "123456", "runoob", charset='utf8' )
  # 1.1检查是否连接成功，如果未成功，print错误信息
  
  # 2.执行操作
  db.cursor().execute("CREATE TABLE HAHAHA (Id_P int);")
  # 2.2检查是否创建成功，如果未成功，print错误信息
  
  # 3.断开连接
  db.close()
  ```

### 解决错误

- mysql安装，出现错误 mysqld: Can't create directory 'C:\web\mysql-8.0.11\data\'

  https://my.oschina.net/u/4357584/blog/3345786

## 安装Navicat for mysql(数据库可视化工具[图形化界面])

- 下载地址 - http://www.navicat.com.cn/download/navicat-for-mysql
- 注册机（破解器） - https://www.jb51.net/database/712269.html

## python

### 使用

1. 新建`xxx.py`文件

2. 在`sublime text`或任意编辑器编辑`xxx.py`文件

3. 编译`xxx.py`

4. 在`CMD`终端执行命令

   ```cmd
   python xxx.py
   ```

## CMD常用

```cmd
# 移动目录
cd ../       # 上一级
cd 目录名

# 查看当前目录下有哪些文件
dir

# 新建文件夹
mkdir 文件夹的名字

# 执行.py结尾的 python 文件
python xxx.py

# 清空屏幕
cls
```

## For linux

- 端口相关

    https://www.cnblogs.com/zhao-shan/p/9713904.html

```cmd
# 
```

## 进入数据库并设置密码

```bash
sudo mysql -uroot -p
set password for root@localhost = password('123');
```

