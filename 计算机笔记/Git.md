# Git

## 理念 & 技巧 & 提示

- git 关键词 & 特性

    分布式 交换 版本控制 可离线 分支 基于修改

- 代码位置

    仓库外 - 工作区(`Working Directory`) - 暂存区(`stage`) - 版本库(`Repository`) - 远程库(`origin`)

- 缺点

    - 只能跟踪管理文本文件
    
- 指针 - (`HEAD` -> `master` -> `a commit`)

    `HEAD` - 当前的`commit`版本

    `HEAD^` - 前一个`commit`版本

    `HEAD^^` - 前两个`commit`版本

    `HEAD~n` - 前`n`个`commit`版本

- `.git` - 用来管理 git 的目录, 默认隐藏, 用`ls -ah`命令可以看见

- `origin` - 远程库的默认名字

- `pull=fetch+merge`

## 命令

| 命令          | 命令作用                                                     | 参数                                                 | 参数作用                                                     |
| ------------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| `add`         | 把文件放到`Git仓库/暂存区`                                   | `<file>`                                             | 要提交的文件及路径                                           |
| `commit`      | 提交修改到本地的`Git 仓库`                                   | `-m <mesage>`                                        | 提交的描述                                                   |
| `init`        | 初始化目录为`Git仓库`                                        |                                                      |                                                              |
| `status`      | 查看`工作区`和`暂存区`的文件更改状态                         |                                                      |                                                              |
| `diff`        | 查看`工作区`文件的修改                                       |                                                      | 对比`工作区`和`暂存区`                                       |
|               |                                                              | ``<HEAD~n/commitId> -- <file>`                       | 对比`工作区`和`版本库`                                       |
|               |                                                              | `--cached`                                           | 对比`暂存区`和`版本库`                                       |
| `log`         | 显示从近到远的`commit`记录                                   | `--pretty=oneline`                                   | 缩减`log`信息到一行                                          |
|               |                                                              | `--graph`                                            | 显示分支图                                                   |
|               |                                                              | `--abbrev-commit`                                    | 显示短`commitId`                                             |
| `reset`       | 回退`commit`                                                 | `--hard`                                             |                                                              |
|               |                                                              | `<HEAD~n/commitId>`                                  | 回退版本到某个`commit`之前                                   |
|               |                                                              | `<file>`                                             | 把暂存区的修改回退到工作区                                   |
| `reflog`      | 查看产生修改的命令历史(不包括修改暂存区的)                   |                                                      |                                                              |
| `checkout`    | 检出                                                         | `-- <file>`                                          | 根据版本库(`commit`)恢复工作区                               |
|               |                                                              | `<branch-name>`                                      | 切换到已有分支                                               |
|               |                                                              | `-b <branch-name>`                                   | 创建并切换到(和当前分支一样的)新的分支                       |
|               |                                                              | `-b <branch> origin/<远程分支名>`                    | 将远程分支创建到本地                                         |
| `switch`      | 切换分支                                                     | `<branch-name>`                                      | 切换到已有分支                                               |
|               |                                                              | `-c <branch-name>`                                   | 创建并切换到(和当前分支一样的)新的分支                       |
| `branch`      | 分支操作                                                     |                                                      | 查看`当前分支`以及所有`本地分支`                             |
|               |                                                              | `<branch-name>`                                      | 创建(和当前分支一样的)新分支(不切换)                         |
|               |                                                              | `-d/-D <branch-name>`                                | 删除(已合并/未合并)分支                                      |
|               |                                                              | `--set-upstream-to=origin/远程分支名 本地分支名`     | 指定`本地分支 `与`远程分支`的连接,可以简化命令               |
|               |                                                              | `-r`                                                 | 查看所有远程分支                                             |
|               |                                                              | `-a`                                                 | 查看所有`远程分支`和`本地分支`                               |
|               |                                                              | `-m oldName newName`                                 | 重命名本地分支                                               |
| `merge`       | 合并分支                                                     | `<branch-name>`                                      | 合并某分支到当前分支                                         |
|               |                                                              | `--no-ff -m "comment of merge commit <branch-name>"` | 强制禁用`Fast forward`模式,使用一个新的 `commit`提交合并,保留合并历史 |
| `rm`          | 从版本库删除文件                                             | `<file>`                                             | 从版本库中删除文件                                           |
| `remote`      | 远程库操作                                                   |                                                      | 查看远程库名称                                               |
|               |                                                              | `-v`                                                 | 查看远程库信息                                               |
|               |                                                              | `add <远程库名> 远程库[SSH/HTTP]地址`                | 为`本地仓库`添加关联的`远程仓库`                             |
|               |                                                              | `rm <远程库名字>`                                    | 删除已有的远程库                                             |
| `push`        | 把分支推送到远程库                                           | `origin <要推送的本地分支名>`                        | 选择要推送的分支                                             |
|               |                                                              | `-u`                                                 | 把推送的本地分支与远程库中对应的分支关联起来,在以后`push/pull`时简化命令,直接用`git push/pull`,省略`origin <branchname>` |
|               |                                                              | `origin <tag-name>`                                  | 推送某个标签到远程库                                         |
|               |                                                              | `origin --tags`                                      | 推送所有标签到远程库                                         |
|               |                                                              | `origin :refs/tags/<tag-name>`                       | 删除远程标签(已删除本地标签)                                 |
| `clone`       | 把远程库拷贝到本地                                           | `git[SSH/HTTP]地址`                                  | 远程库地址,(`github/gitlab`会提供)                           |
|               |                                                              | `-b branchname git[SSH/HTTP]地址`                    | 拷贝其它分支                                                 |
| `stash`       | 把当前`工作区`的修改暂时"储藏"起来,以清空`工作区`            |                                                      |                                                              |
|               |                                                              | `list`                                               | 查看所有的`stash`                                            |
|               |                                                              | `apply [stash@{0}]`                                  | 恢复但不删除`stash`,(可指定版本)                             |
|               |                                                              | `drop [stash@{0}]`                                   | 删除`stash`,(可指定版本)                                     |
|               |                                                              | `pop [stash@{0}]`                                    | 恢复并删除`stash`,(可指定版本)                               |
| `cherry-pick` | 把某个分支某次提交的修改应用到当前分支                       | `<commitId>`                                         | 应用`commitId`对应的`commit`                                 |
| `rebase`      | 在一个分支的`commit`末尾`commit`另一个分支                   |                                                      |                                                              |
| `tag`         | `commit`的标签,别名,标签可以跟随`commit`出现多次             |                                                      | 查看所有`tag`,结果不是按时间顺序而是按字母顺序               |
|               |                                                              | `<tag-name>`                                         | 给当前分支最新提交的`commit`打上标签                         |
|               |                                                              | `<tag-name> <commitId>`                              | 给某次`commit`打标签                                         |
|               |                                                              | `-a <tag-name> -m "comment message"`                 | 给某次`commit`打带有说明的标签                               |
|               |                                                              | `-d <tag-name>`                                      | 删除一个标签                                                 |
| `show`        | 查看标签信息                                                 |                                                      | 查看当前分支最新的`commit`信息                               |
|               |                                                              | `<commitId>`                                         | 查看`<commitId>`对应的`commit`的信息                         |
|               |                                                              | `<tag-name>`                                         | 查看某个`tag`对应`commit`的信息                              |
| `config`      | 配置`git`仓库                                                | `--global`                                           | 为电脑的所有仓库进行配置                                     |
|               |                                                              | `color.ui true`                                      | 让`git`显示颜色                                              |
|               |                                                              | `user.name "username"`                               | 设置`Git仓库`的用户名                                        |
|               |                                                              | `user.email "email"`                                 | 设置`Git仓库`的邮箱                                          |
|               |                                                              | `alias.别名 全称`                                    | 为命令配置别名                                               |
| `fetch`       | 从远程库拉取新的`commit`到本地,但不移动本地的`HEAD`.还需要`merge`以更新 |                                                      |                                                              |

## 场景

### 提交一个文件

```cmd
git add readme.txt
geit commit -m "can't ignore this commit"
```

### 遇到冲突

先把有冲突的分支`pull`下来,在本地解决冲突然后再`push`

### 从别的分支拉取到当前分支

#### 方法 1

```cmd
(now)	git stash
(now)	git checkout -b mmsite origin/mmsite
(other)	git log
(other) git checkout sync-deploy
(now)	git cherry-pick 6088139b4abc6f5eac75634ef34e21d9bf3c3052
(now)	git stash pop
```

#### 从主分支拉取更新到当前分支

```bash
git stash
git checkout master
git pull
git checkout my-branch
git merge master
git stash pop
```

### `error: Your local changes to the following files would be overwritten by merge:`

```cmd
git stash  
git pull origin master  
git stash pop
```

## 优化配置

```cmd
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD'
git config --global alias.last 'log -1'
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
cat .git/config 
```

## 安装 & 配置 & 使用(`mac`)

- `global config`的位置

    ```cmd
    subl ~/.gitconfig
    ```

    

### 本地使用

1. 安装

    - [通过 homebrew](http://brew.sh/)
    - 从AppStore安装Xcode -> 运行Xcode -> Xcode -> Preferences -> Downloads -> Command Line Tools -> Install

2. 配置

    [ - - global ] 意思是为这台电脑的所有用户设置

    ```cmd
    git config --global user.name "liuzhuocheng"
    git config --global user.email "liuzhuocheng@bytedance.com"
    ```

3. 初始化一个 git 目录

    ```cmd
    git init
    ```


### 连接远程库

1. 创建SSH Key, 一台电脑对应一个`ssh key`

    检查用户主目录下有没有`.ssh`目录,`.ssh`里有没有`id_rsa`和`id_rsa.pub`两个文件,如果没有,执行以下命令

    ```cmd
    ssh-keygen -t rsa -C "youremail@example.com"
    ```

2. 在`远程Git仓库`里配置上一步得到的秘钥`id_rsa.pub`

3. 在`远程Git仓库`中创建需要的仓库

4. 开始

    - 为`本地仓库`添加关联的`远程仓库`

        ```cmd
        git remote add origin git[SSH/HTTP]地址
        ```

    - 从`远程仓库`拷贝仓库到本地

        ```cmd
        git clone git[SSH/HTTP]地址
        ```

## CentOS 8.2 安装 git

```bash
yum install git
git --version

git config --global user.email "839379037@qq.com"
git config --global user.name ‘smartGrey’
```

## 相关链接

- [廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
- [可视化学 Git 教程版](https://learngitbranching.js.org/?locale=zh_CN)
- [可视化学 Git 清净版](http://git-school.github.io/visualizing-git/#free)
- [Git 命令速查 PDF](https://gitee.com/liaoxuefeng/learn-java/raw/master/teach/git-cheatsheet.pdf)
- [修改分支名称命令大全](https://www.jianshu.com/p/cc740394faf5)
