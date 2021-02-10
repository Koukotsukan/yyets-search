# yyets_search
Python写的用来查询人人影视的小工具

## 使用需要：
+ sqlite3
+ yyets.db(即数据库文件)
+ python3

## 使用指南(Linux)：
0. (可选)建立索引：
   + 输入指令：
   ```bash
   sqlite3 你的数据库地址/yyets.db
   ```
   + 输入sql命令：
   ```sql
   CREATE INDEX index ON yyets (name);
   ```
1. 输入指令：
```bash
wget https://raw.githubusercontent.com/Koukotsukan/yyets_search/main/src/yyets.py
```
2. 输入指令：
```bash
python yyets.py
```
3. (仅第一次使用时)键入数据库的绝对地址

## 免责声明
本人不提供相关数据库
