# Anaconda

- Anaconda 解决了官方 Python 的两大痛点
    - 包管理
    - 环境管理

## 环境管理

```cmd
# 查看帮助
conda -h
# 查看所有环境
conda info -e

# 创建环境
conda create --name python36 python=3.6
# 激活环境
conda activate python36
# 退出环境
conda deactivate
# 删除环境
conda remove -n python36 --all
```

## 包管理

```cmd
# 安装包
conda install packageName
# 查看已安装的包
conda list
# 更新包
conda update packageName
# 删除包
conda remove packageName

# 更新 conda
conda update conda
# 更新 Anaconda
conda update anaonda
# 更新 Python
conda update python
```

