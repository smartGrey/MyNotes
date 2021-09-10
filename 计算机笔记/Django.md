# Django

## 数据库查询

- 查询顺序

    ```python
    serializer(modelClass.objects.filter().all()[1:5])
    ```

- 查询包含关系

    ```python
    query_result.filter('name__in'=arr)
    query_result.filter(**{k+'__in':arr})
    ```

    

## 定时任务

> 参考链接
>
> - 详解django中使用定时任务的方法
>
>     https://www.cnblogs.com/linqiaobao/p/14230337.html

- 使用的模块: `django-crontab`
- 是独立于 runserver 运行的

### 常用命令

```cmd
#添加并启动 settings.py 中配置的定时任务
python manage.py crontab add
#显示当前已启动的所有定时任务
python manage.py crontab show
#删除所有定时任务
python manage.py crontab remove
```

