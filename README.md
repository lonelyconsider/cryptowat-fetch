### 用途
从网站Cryptowat取汇率数据到数据仓库。Cryptowat整合了30多家交易所的公共数据，并给出自己的API提供使用，但是API限制是一个很大的问题。

### API信息
文档网址：https://cryptowat.ch/docs/api

API限制：***Each client has an allowance of 8000000000 nanoseconds (8 seconds) of CPU time per hour.***

用到的接口:  
1. Market Order Book

### 环境
Python 3.7.3 + Scrapy 1.6.0

### 依赖库
requests, pymssql, sqlalchemy, zimbrasmtp, pandas

### 备注
*zimbrasmtp是自定义的一个模块，用于当程序出错时，发送一封邮件到zimbrasmtp邮箱*

