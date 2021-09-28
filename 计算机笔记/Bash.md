# Bash
## 脚本
### 常用脚本命令
- 移动至脚本存放的目录 - `cd "$(dirname "$0")"`
- 下载脚本到本地 - `curl -skL 10.27.82.29:8088/update_gpu_driver_and_reboot.sh > can_delete_next_see_this_file.sh`

## 命令
- 新建目录（上级目录不存在时自动创建） - `mkdir -p dir_name_outer1/dir_name_outer2/dir_name`
- 在目录下的所有文本文件中搜索字符串 - `grep keyword ./*`
