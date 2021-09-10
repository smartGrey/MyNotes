# Docker

## 概念

- 镜像

    容器的模板

## 安装

```bash
cd /
uname -r
uname -m
curl https://get.docker.com > /tmp/install.sh
cat /tmp/install.sh
chmod +x /tmp/install.sh
/tml/install.sh
# 到这里最后会报个错，但是好像安装成功了


# 去掉命令前需要的 sudo
# https://blog.csdn.net/u013948858/article/details/78429954

docker version
docker info
```

## 使用

- run=create+start

```bash
# 重启
sudo systemctl restart docker

# 启动容器
docker run debain echo '23333333'
# 启动容器在后台运行
docker run --name myredis -d redis
# 新建一个退出立即删除的容器并链接到 redis
docker run --rm -it --link myredis:redis redis /bin/bash
# 进入容器里的终端
docker run -it --rm debian /bin/bash #-i -t 表示：想要一个附有 tty 的交互会话，--rm，exit容器后删除容器
docker run --name determined_lovelace -h MYCONTAINER -it debian /bin/bash # -h 定义主机名,--name 定义 docker 实例名
docker run cowsayimage:11 /usr/games/cowsay 'Moo'

# 备份容器数据卷
docker run --rm --volumes-from myredis -v $(pwd)/backup:/backup debian cp /data/dump.rdb /backup/ # $(pwd)表示当前目录

# 查看容器输出
docker logs -f myredis # -f ,实时刷新 log

# 启动已退出容器
docker start determined_lovelace

# 停止容器
docker stop myredis

# 删除容器
docker rm -v myredis
docker rm $(docker ps -aq) # 删除所有容器

# 查看容器状态
docker ps
docker ps -a # 查看所有容器
docker inspect determined_lovelace
docker inspect determined_lovelace | grep IPAddress
docker diff determined_lovelace

# 删除容器
docker rm determined_lovelace
docker ps -aq -f status=exited
docker rm -v $(docker ps -aq -f status=exited) # -v 删除所有和由 docke r 管理的数据卷没关联的容器
# 删除镜像
docker rmi bdfoster/nvmmysql -uroot -p
docker rmi $(docker images -q -f dangling=true) # 删除所有未依赖镜像
docker rmi -f $(docker images -qa) # 删除所有镜像

# 把容器转镜像
docker commit cowsay cowsayimage:11

# 从 Dockerfile 生成镜像
mkdir cowsay
cd cousay
touch Dockerfile
vi Dockerfile
#FROM debian
#RUN apt-get update && apt-get install -y cowsay fortune
docker build -t liuzhuocheng/cowsay:1.0 . # 注意后面有个点
docker build - < Dockerfile
docker build - < context.tar.gz
docker build -f dockerfiles/Dockerfile.debug .
# --no-cache 不使用缓存（重复出现连续两条指令时，第二条指令会使用缓存中的value），或修改一条指令使缓存失效

# 查看镜像所有中间镜像层
docker history liuzhuocheng/cowsay:1.0

# 构建失败时，把失败前的一个镜像启动成容器
# 找到最后一个未失败的【!镜像!】的 id，因为容器已经被删掉了

# 从网络获取 docker
docker pull liuzhuocheng/cowsay:1.0

# 登录 docker hub
docker login
#liuzhuocheng
#dudu@991026

# 上传到 docker hub
docker push liuzhuocheng/cowsay:1.0

# 查看镜像维护者信息
docker inspect -f {{.Author}} liuzhuocheng/cowsay:1.0
```

### 端口转发

```sh
docker run -d -p 8000:80 nginx # 主机:容器

ID=$(docker run -d -P nginx) # 在容器启动 nginx，并将 80 转发到主机上任意未占用端口
docker port $ID 80
# 0.0.0.0:32771

curl localhost:32771 # 或在浏览器访问 ip:32771
```

### 容器连接

```bash
docker run -d --link 被连接容器名:被连接容器在主容器的别名 主容器名
# 查看连接后会添加在主容器的环境变量
docker run --link myredis:redis debian env
# 不支持这样建立双向连接，用到再进一步了解
```

### 用数据卷和数据容器管理数据

- 数据卷 - 在主机上被绑定挂载到容器的一个普通目录或文件
- 不能在 RUN 指令中设置卷的权限和它的所有者

### 数据卷绑定

```bash
# 找出数据卷在主机上的实际位置
docker inspect -f {{.Mounts}} hostname

# 启动并声明一个目录为数据卷（容器与主机共享），两种方式

# 第一种
# docker run -v 参数，好处是可以直接绑定主机目录
# 不加:xx,则会绑定到默认路径：
# /var/lib/docker/volumes/5cad.../_data/test-file
docker run -v "$PWD"/data:/in_docker_data -it --rm -h hostname debian /bin/bash

# 第二种
# Dockerfile(这里声明了两个挂载点，但是不能和主机的目录绑定)
VOLUME ["/docker_data1","/docker_data2"]
# 只能放到 Dockfile 的文件修改之后执行，否则后续对数据卷的写入不会有效
```

## Dockerfile

- 要时刻注意每个 dockerfile 中的命令，是在独立的容器中执行的，所以只有会产生持续性效果的命令才有作用

```dockerfile
FROM debian:stable #来源镜像,需要获取安全补丁的时候，建议使用 latest，或执行 docker pull 获取最新镜像

MAINTAINER Liuzhuozhcneg <839379037@qq.com>

RUN apt-get update && apt-get install -y cowsay fortune

COPY entrypoint.sh / # COPY ["entrypoint.sh","/"]

ENTRYPOINT ["/entrypoint.sh"]

VOLUME /data
```

### 入口文件通过脚本设置默认参数

```cmd
#!/bin/bash
if [ $# -eq 0 ]; then
    /usr/games/fortune | /usr/games/cowsay
  else
    /usr/games/cowsay "$@"
fi
```

## 疑问

- 能否合并多个 docker
- 如何编写一个 Dockerfile
- 能否导出镜像文件

## 使用 Rancher - docker web 管理

```bash
docker run -d --restart=always -p 8393:8080 rancher/server
```



