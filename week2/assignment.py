# Task 1
print("================")
print("║    Task 1    ║")
print("================")
import re
def find_and_print(messages, current_station):
    # 所有的站名
    stations = [
        "Songshan", "NanjingSanmin", "TaipeiArena", "NanjingFuxing",
        "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", 
        "Chiang Kai-ShekMemorial Hall", "Guting", "TaipowerBuilding",
        "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang",
        "Xiaobitan", "Xindian City Hall", "Xindian"
    ]
    
    # 插入一個空的 index 在 "Xiaobitan" 和 "Xindian City Hall" 之間
    xiaobitan_index = stations.index("Xiaobitan")
    stations.insert(xiaobitan_index + 1, None)

    # 指定的車站索引
    current_index = stations.index(current_station)

    # 用來存放名字對應站名的字典
    name_to_station = {}
     # messages 字典提取站名
    for name, message in messages.items():
        # 去除訊息中的多餘空格
        message = re.sub(r'\s+', '', message)
        # 找出訊息中的站名
        station = next((station for station in stations if station and re.sub(r'\s+', '', station) in message), None)
        
        if station is not None:
            # 將名字和站名加入字典
            name_to_station[name] = station

    # 找出與指定車站最近的人的邏輯
    closest_person = None
    closest_distance = float('inf')
    # 從名字對應站名的字典取出 index 使用
    for name, station in name_to_station.items():
        if station in stations:
            station_index = stations.index(station)
            # 計算距離並找到最小的距離
            distance = abs(station_index - current_index)
            if distance < closest_distance:
                closest_distance = distance
                closest_person = name

    # 印出結果
    print(closest_person)

# 五位乘客提供的相關訊息
messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you.",
}
# 呼叫函式
find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian

# Task 2
print("================")
print("║    Task 2    ║")
print("================")
# 建立一個已預約的時間列表，每位顧問都預設空白（無預約）
booked_times={
    "John": [],
    "Bob": [],
    "Jenny": []
}
# 檢查某位顧問的預約時間是否重疊的函式
def is_overlapping(booked, hour, duration):
    for start, end in booked:
        if (hour < end and hour + duration > start):
            return True
    return False

def book(consultants, hour, duration, criteria):
    # 過濾掉預約時間重疊的顧問
    available_consultants = [
        consultant for consultant in consultants
        if not is_overlapping(booked_times[consultant["name"]], hour, duration)
    ]
   
    # 從consultant 取得 價格
    def get_price(consultant):
        return consultant["price"]
    # 從consultant 取得 評價
    def get_rate(consultant):
     return consultant["rate"]

    # 根據criteria選擇最適合的顧問
    def find_consultant(criteria):
        if not available_consultants:
            return None
        # 假如選擇價格 取最低（最便宜的）
        if criteria == "price":
            return min(available_consultants, key=get_price)
        # 假如選擇評價 取最高（評價最高的）
        elif criteria == "rate":
            return max(available_consultants, key=get_rate)

    # 找到最適合的顧問
    consultant = find_consultant(criteria)
    # 如果沒有可用的顧問，輸出"No service"
    if consultant is None:
        print("No service")
    else:
        # 如果有可用的顧問，將預約時間加入該顧問的預約時間列表
        name = consultant["name"]
        booked_times[name].append((hour, hour + duration))
        print(name)
# 顧問名單
consultants=[
    {"name":"John","rate":4.5,"price":1000},
    {"name":"Bob","rate":3,"price":1200},
    {"name":"Jenny","rate":3.8,"price":800}
    ]
# 呼叫函式
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

# Task 3
print("================")
print("║    Task 3    ║")
print("================")

def func(*data):
    # 取出每個名字的中間字
    middle_chars = []
    for name in data:
        # 2個字的名字，取第二個字
        if len(name) == 2:
            middle_chars.append(name[1])
        # 4個字的名字，取第三個字
        elif len(name) == 4:
            middle_chars.append(name[2])
        # 其他長度的名字，取中間的字
        else:
            middle_index = len(name) // 2
            middle_chars.append(name[middle_index])

    # 找出唯一的中間字對應的名字 （如果名字只出現一次放入 result ）
    result = []
    for i in range(len(data)):
        if middle_chars.count(middle_chars[i]) == 1:
            result.append(data[i])

    # 印出結果
    if result:
        for name in result:
            print(name)
    else:
        print("沒有")

# 呼叫函式
func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安


# Task 4
print("================")
print("║    Task 4    ║")
print("================")

def get_number(index):
    # 初始值為 0
    num = 0
    
    # 根據規律計算第 n 項  (觀察變化為 +4 +4 -1 ...n) 
    for i in range(1, index+1):
        if i % 3 == 1 or i % 3 == 2:
            num += 4
        elif i % 3 == 0:
            num -= 1
    
    print(num)

# 呼叫函式
get_number(1)  # print 4
get_number(5)  # print 15
get_number(10) # print 25
get_number(30) # print 70
# 測試其他的結果
# get_number(31) # print 74
# get_number(6)  # print 14

