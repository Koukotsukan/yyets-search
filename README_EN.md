# yyets-search
![GitHub license](https://img.shields.io/github/license/Koukotsukan/yyets-search?style=flat-square)

### A small tool written in Python for querying yyets movies (with sqlite3) 

[中文版](./README.md)


## Screenshot:
![screenshot](screenshot/screenshot.png)

## Requirements:
+ sqlite3
+ yyets.db (The database file)
+ python3
   + packages：
      + sqlite3
      + json
      + os
      + time
## Functions:
+ Fuzzy queries
+ Select specific season or episode
+ Generate files of magnet links

## TODO list:
- [ ] One-command to output multiple seasons or episodes
- [ ] Automatic testing of magnet links' activity
- [ ] Use remote server database

## Instruction(Linux):
0. (Optional)Build an index：
   + Key in command:
   ```bash
   sqlite3 yourdatabaselocation/yyets.db 
   ```
   #yourdatabaselocation depends on the location of your database.
   
   + Type sql command：
   ```sql
   CREATE INDEX index_name ON resource (name);
   ```
1. Download Python code：
```bash
wget https://raw.githubusercontent.com/Koukotsukan/yyets-search/main/src/yyets.py
```
2. (Optional)Install related Python requirements:
```bash
wget https://raw.githubusercontent.com/Koukotsukan/yyets-search/main/src/requirements.txt
```
```bash
pip3 install -r requirements.txt
```
3. Run the program：
```bash
python3 yyets.py
```
4. (Only for first run)Key in the absolute address of your database

## Declaration:
All related data structure is from the Internet, I do not hold and provide the relevant database.
