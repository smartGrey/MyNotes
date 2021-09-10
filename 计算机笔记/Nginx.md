# Nginx

- 特性

    高性能

    轻量级 Web 服务器(1MB)

    反向代理服务器

    IMAP|POP3|SMTP 代理服务器

- nginx 的延伸版本: tengine(淘宝) openresrt(章亦春)

- 相关链接

    - 官网: http://nginx.org
    - 中文文档: http://www.nginx.cn/doc/index.html
    - 菜鸟教程: https://www.runoob.com/linux/nginx-install-setup.html
    - 百度百科: https://baike.baidu.com/item/nginx/3817705?fr=aladdin

## 安装（debain）

- 步骤

    ```mermaid
    graph LR
    	配置-->编译-->安装
    ```

- 安装位置:`/usr/local/nginx`

- 缺少插件

    - zlib - https://blog.csdn.net/weixin_37909391/article/details/81320735

- 相关文件位置:

    ```
    path prefix-------/usr/local/nginx
    binary file-------prefix/sbin/gninx--------启动入口
    modules path------prefix/modules-----------模块位置
    configuration-----prefix/conf/nginx.conf---配置文件
    log-prefix--------prefix/logs--------------日志目录
    pid log-----------log-prefix/nginx.pid-----进程日志
    err log-----------log-prefix/error.log-----错误日志
    http access log---log-prefix/access.log----http访问日志
    ```

```cmd
# 需要装 nginx 的环境依赖PCRE
wget https://netix.dl.sourceforge.net/project/pcre/pcre/8.40/pcre-8.40.tar.gz /usr/src
cd /usr/src/
tar -zxvf pcre-8.40.tar.gz
cd pcre-8.40
./configure
make && make install
pcre-config --version



# 获得官方源码包并解压 - 从这里找到源码包: http://nginx.org/en/download.html  (右键复制链接地址)
wget http://nginx.org/download/nginx-1.19.9.tar.gz -P /usr/src
cd /usr/src/
tar xf nginx-1.19.9.tar.gz




# 配置 - 作用:1)检查环节是否满足安装条件,依赖解决. 2)指定安装方式,配置/命令等文件放哪里,开启模块功能. 3)指定软件安装在哪.
cd nginx-1.19.9
# ./configure --help     查看配置帮助
./configure --prefix=/usr/local/nginx    # 指定安装位置



# 编译 - 生成可执行程序
make && make install



# 启动 nginx 服务
# 协议
# 监听地址
# 端口 - 默认:80
/usr/local/nginx/sbin/nginx

# 然后就可以从外部访问了!
```

## 安装（CentOS 8.2）

- https://www.cnblogs.com/shiyuelp/p/11945882.html
- https://www.cnblogs.com/wxj612/p/13696628.html
- https://blog.csdn.net/weixin_45525272/article/details/107794364

```bash
cd /
wget http://nginx.org/download/nginx-1.9.9.tar.gz
yum -y install gcc pcre pcre-devel zlib zlib-devel openssl openssl-devel
tar -zxvf nginx-1.9.9.tar.gz
rm -rf nginx-1.9.9.tar.gz
cd nginx-1.9.9
./configure --prefix=/software/nginx
make
make install

# 启动
/software/nginx/sbin/nginx
```

## 相关命令

- Linux 查看 nginx 安装目录和配置文件路径

    https://www.cnblogs.com/ryanzheng/p/13124128.html

```cmd
# 终止 nginx 服务
killall nginx

# 启动 nginx 服务
/usr/local/nginx/sbin/nginx
# 检测是否启动成功
lsof -i:80

# 检测配置文件是否有问题
/usr/local/nginx/sbin/nginx -g /usr/local/nginx/conf/nginx.conf

# 让 nginx 重读配置文件
killall -s HUP nginx
nginx -s reload
```

## 配置文件 - `/usr/local/nginx/conf/nginx.conf`

- Nginx配置文件（nginx.conf）配置详解

    https://blog.csdn.net/tjcyjd/article/details/50695922

- nginx 内置变量

    https://www.jianshu.com/p/deccac3a4fd0

```cmd
# 启动工作进程的默认用户
#user liuzhuocheng;

# 默认启动的工作进程数量,可以cpu几核建几个
# 每个工作进程:单进程多线程
worker_processes  4;

# 全局错误日志的位置以及格式
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

# 主进程日志存放位置
#pid        logs/nginx.pid;


events {
	# 每个工作进程最大的并发数(线程数)
    worker_connections  1024;
}


# http 服务器设置
http {
	# 设定 mime 类型
    include       mime.types;
    default_type  application/octet-stream;

	# 日志格式
    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';
    log_format liuzhuocheng_01 '[$time_local] $remote_addr "$request" $status'
    
	# 日志路径
    #access_log  logs/access.log  main;

	# 是否调用 sendfile 函数(零拷贝方式:https://www.jianshu.com/p/028cf0008ca5)
    sendfile        on;
    # 是否允许使用 socket 的 TCP_CORK 选项,仅在 sendfile 为 on 时可用
    #tcp_nopush     on;

	# tcp 长连接时间,可减少三次握手的次数
    #keepalive_timeout  0;
    keepalive_timeout  65;

	# 开启压缩
    #gzip  on;

	# 配置虚拟主机
	# (默认网站:nginx 可部署多个网站,只有一个 server 则其为默认网站,当有多个 server 的时候,每个 server 可作为一个虚拟主机)
    server {
    	# 监听的主机端口和域名
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  liuzhuocheng_01; # 见上面的 log_format


		# web 目录根路径
		# localhost/a  ->  /usr/local/nginx/html/a
        location / {
            root   html;
            index  index.html index.htm;
        }
        # 访问控制
        location /a {
        	allow 127.0.0.1;
        	deny all;
            # return 504;
            return http://www.jd.com;
        }
        # 用户验证
        location /b {
            auth_basic "柳卓诚登录验证";
            auth_basic_user_file /etc/nginx/htpasswd;# 保存着账号密码,需要去创建对应的目录.
        }
        # 防盗链
        location ~* \.(png|gif|bmp)$ {
        	valid_referers none blocked *.ayitula.com;
        	if ($invalid_referer) {
        		return 403;
        	}
        }
        
        #error_page  404              /404.html;
        # redirect server error pages to the static page /50x.html
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }


		# 配置反向代理,将请求转发到业务服务器:proxy_pass
        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```

- 设置访问密码

    ```cmd
    # 生成用户验证的密码文件
    apt-get install apache2-utils
    htpasswd -m /etc/nginx/htpasswd admin
    # 设置密码
    ```

- 日志格式

    https://www.rootop.org/pages/3070.html

- 虚拟主机

    一个服务器部署多个网站

    https://blog.csdn.net/yuan_xw/article/details/51254674

    - 基于 IP - 首先一个机器要拥有多个 IP,可以用域名映射
    - 基于端口 - 只需要一个 IP.缺点:端口无法告诉公网用户,可以用域名映射

## 反向代理

- 概念

    1. 客户机在发送请求时,不会直接发送给目的主机, 而是先发送给代理服务器.

    2. 代理服务器接收客户机请求后,向主机发出请求.

    3. 代理服务器接收目的主机返回的数据,存放在代理服务器的硬盘中,发送给客户机.

- 正向代理与反向代理的区别在于代理的对象不一样.正向代理代理的对象是客户端，反向代理代理的对象是服务端。

    正向代理只对客户负责,可以代替客户访问任何服务端.反向代理只对其代理的特定服务器负责.

    ```mermaid
    graph LR
    用户-->源服务器
    用户-->正向代理服务器-->所有服务器-->源服务器
    用户-->反向代理服务器-->被代理的服务器-->源服务器
    ```

- 场景/优势

    - 做堡垒机 - 不让用户直接访问私网的业务服务器

        ```mermaid
        graph LR
        用户-->公网-堡垒机-->私网-业务服务器-只对堡垒机开放一个端口
        ```

    - 通过虚拟主机代理多个业务服务器 - 适合 IP 地址不足的场景

        ```mermaid
        graph LR
        用户-->公网-提供总服务-->私网-业务服务器1
        公网-提供总服务-->私网-业务服务器2
        公网-提供总服务-->私网-业务服务器3
        ```

    - 缓存 - 对静态数据进行缓存,减小业务服务器的压力

        ```mermaid
        graph LR
        用户-->公网-缓存服务器-->私网-业务服务器
        ```

- proxy_xxx 配置参数

    https://www.runoob.com/w3cnote/nginx-proxy-balancing.html

## 限速

- 概念 - 限制某个用户在一个给定时间的内能够产生的 HTTP 请求数

- 功能

    可用于安全目的,通过限制请求速率来防止暴力破解密码攻击

    结合日志标记出目标 URL 来帮助防范 DDoS 攻击

    保护上游服务器不被大量用户请求堵塞

    保护硬盘/IO

- 实现原理

    - 设置缓存
    - 匀速处理
    - 超出缓存限制直接丢弃

- 官方限速的模块

    - 参考链接
        - Nginx限流模块limit_req_zone死磕之路 - https://www.321dz.com/2019.html
        - 官方文档 - http://nginx.org/en/docs/http/ngx_http_limit_req_module.html

    - limit_req_zone - 限制请求数 - 速率限制
    - limit_req_conn - 限制连接数 - 并发限制

## 重写

- rewrite 模块 - ngx_http_rewrite_module

- 作用

    可以在改变网站结构后,不需要修改客户原来使用的 URL

    能在一定程度上提高网站安全性(隐藏 URL)

    整理 URL

    域名变更

    用户链接跳转

    伪静态场景 - 便于 CDN 对动态页面的数据进行缓存

- 依赖于 PCRE

- 和 redirect 的区别

    - 缺货时的两种处理：让用户自己去其他地方买（Redirect）；公司从其他的地方调货（Rewrite）

    - rewrite
        - 在 server 端处理
        - 正常响应
        - 有一定的 rewrite 规则
        - 重写 URL/statusCode/content/redirect
        - 更强大
    - redirect
        - 在 client 端处理
        - 以 301 302 303 307 响应
        - 可以跳转任意地址
        - 重写 url 后让客户自己跳转

- ```mermaid
    graph LR
    	用户--请求地址---->Nginx
    	Nginx--重写后的URL/statusCode/Content---->用户
    ```

- 相关链接

    - 官网文档 - http://nginx.org/en/docs/http/ngx_http_rewrite_module.html
    - 搞懂nginx的rewrite模块 - https://segmentfault.com/a/1190000008102599wget