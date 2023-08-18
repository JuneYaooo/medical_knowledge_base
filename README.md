# medical_knowledge_base

# 环境配置
python 3.8
```
pip install -r requirements.txt
```

# django使用

## django数据库表结构迁移
```
python manage.py makemigrations
python manage.py migrate
```

## 创建超级管理员
```
python manage.py createsuperuser
```

## 运行项目
```
python manage.py runserver
```

## 后台管理
打开页面http://127.0.0.1:8000/admin/ ，用刚刚创建的超级管理员账号登录

## 技术架构
Django(3.2.5) + MySQL(8.0)