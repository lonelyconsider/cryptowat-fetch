# -*- coding: utf-8 -*-

# 环境
envir = "live"
# envir = 'staging'

debug = True

### 数据库配置
if envir == 'staging':
    USER_NAME = 'sa'
    PASSWORD = 'xxxxxx'
    IP_ADDRESS = '127.0.0.1'
    DB_PORT = '1433'
    DB_NAME = 'xxxxxx'
else:
    USER_NAME = 'sa'
    PASSWORD = 'xxxxxx'
    IP_ADDRESS = '10.0.0.88'
    DB_PORT = '1433'
    DB_NAME = 'xxxxxx'