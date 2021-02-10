import sqlite3
import json
import os
import time


class YYETS:
    def __init__(self, reader_path, regex):
        self.database_connection = None
        self.reader_path = reader_path
        self.regex = regex
        self.counter = 0

    def connect_database(self):
        self.database_connection = sqlite3.connect(self.reader_path)

    def close_database(self):
        self.database_connection.close()

    def search(self):
        global episode
        start_time = time.time()
        cursor = self.database_connection.cursor()
        selector = cursor.execute("SELECT data FROM resource WHERE name like \"%" + str(self.regex) + "%\";")
        data_list = []
        for i in selector:
            data = json.loads(i[0])
            cnname = data["data"]["info"]["cnname"]
            enname = data['data']['info']['enname']
            data_list.append(data)
            print(str(self.counter + 1) + ". " + cnname + "(" + enname + ")")
            self.counter += 1
        end_time = time.time()
        print("查询完毕,共计{}条结果，耗时{}秒\n".format(self.counter, '%.2f' % (end_time - start_time)))
        if self.counter != 0:
            choose_result = input("请输入您的结果:")
            if choose_result != "0":
                data = data_list[int(choose_result)-1]
                season = data["data"]["list"]
                count = 1
                season_number_list = []
                for i in season:
                    season_number = i["season_num"]
                    season_number_list.append(int(season_number))
                try:
                    season_number_list.sort()
                    for i in season_number_list:
                        print(str(count) + ". 第" + str(i) + "季")
                        count += 1
                except:
                    print("Something got wrong")

                choose_season = input("请输入你的结果:")
                if choose_season != "0":
                    selected = season[int(choose_season)-1]["items"]
                    count = 1

                    episode_list = []
                    for i in selected:
                        for m in selected[i]:
                            episode = m["episode"]
                            episode_list.append(int(episode))
                    episode_list = list(set(episode_list))
                    episode_list.sort()
                    for i in episode_list:
                        print(str(count) + ". 第" + str(i) + "集")
                        count += 1
                    choose_episode = input("请输入你的结果:")
                    if choose_episode != "0":
                        episode_chosen = episode_list[int(choose_episode)-1]
                        for i in selected:
                            for m in selected[i]:
                                if str(episode_chosen) == m["episode"]:
                                    way = m["files"]
                                    try:
                                        for n in way:
                                            address = n["address"]
                                            if n["passwd"]:
                                                passwd = n["passwd"]
                                            else:
                                                passwd = "无"
                                            if n["way"] == "1":
                                                n = "[" + i +"]电驴"
                                            elif n["way"] == "2":
                                                n = "[" + i +"]磁力"
                                            elif n["way"] == "9" or n["way"] == "102":
                                                n = "[" + i +"]百度网盘"
                                                address = address + ", 密码: " + passwd
                                            elif n["way"] == "12":
                                                n = "[" + i +"]城通网盘"
                                            elif n["way"] == "115":
                                                n = "[" + i +"]微云"
                                            print(n + ": " + address)
                                    except:
                                        print("Something went wrong")

    def start(self):
        try:
            self.connect_database()
        except:
            print("查询失败，请检查你的数据库或路径")
            os._exit(0)
        self.search()
        self.close_database()


if __name__ == '__main__':
    if os.path.exists("./yconfig.json"):
        with open("./yconfig.json", "r") as f:
            reader_path = f.readline()
    else:
        reader_path = input("请输入database的路径:")
        with open("./yconfig.json", "w") as f:
            f.write(reader_path)
    while(1):
        regex = input("请输入你要查询的美剧名称:")
        reader = YYETS(reader_path, regex)
        reader.start()
