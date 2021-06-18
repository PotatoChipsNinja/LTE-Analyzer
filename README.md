# LTE-Analyzer
数据库系统原理课程设计：LTE 网络干扰分析系统

## 运行
``` shell
# 克隆仓库
git clone https://github.com/PotatoChipsNinja/LTE-Analyzer.git

# 进入项目目录
cd LTE-Analyzer

# 安装依赖
pip install -r requirements.txt

# 启动 MySQL
service mysql start

# 启动
python app.js
```

## 容器化
> 目前还没通过测试

### 构建&运行
```
docker-compose up -d
```

### 停止
```
docker-compose stop
```

### 删除容器
```
docker-compose down -v
```