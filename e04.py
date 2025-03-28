# Save data03.csv to kor txt file for readability

from datetime import datetime
import pandas as pd

# Get today's date

today_month = datetime.today().month
today_day = datetime.today().day
day_of_week = datetime.today().strftime('%A')
net = 0

# Load the data
df = pd.read_csv("data03.csv")

# Open file
file = open('o_kor.txt', 'w', encoding="utf-8")
def index_csv(category_name):
    return int(df.loc[df['Category'] == category_name, '# of Items Sold'].values[-1])

en2kor = {
    "Food" : "음식",
    'Spicy Pork': "제육",
    'Bulgogi' : "불고기",
    'Noodle' : "누들",
    'Fried Rice' : "볶음밥",
    'Korean Taco' : "타코",
    'Crazy Chicken' : "크레이지",
    'Katsu' : "카츠",
    'Kimchi Fried Rice': "김치 볶음밥",
    'Sides': "사이드",
    'Tteokbokki': "떡볶이",
    'Kimchi': "김치",
    'Korean Noodle (Side)': "잡채",
    'Noodle (Side)': "누들",
    'Yum Yum Sauce': "얌얌",
    'Dumpling': "만두",
    'Egg Roll': "에그롤",
    'Fried Rice (Side)': "볶음밥",
    'Radish': "단무지",
    'Drinks' : "드링크",
    'Snacks' : "스낵",
    'Set Menu'  : "세트 메뉴",
    'Boba' : "버블티",
}
# Headers
file.write(f"{today_month}/{today_day}({day_of_week})\n")
file.write(f"Gross {net}\n")

# Special
all_keys = en2kor.keys()
current_keys = set(df['Category'])
food_total = 0
food_group = ['Spicy Pork', 'Bulgogi', 'Noodle', 'Fried Rice', 'Korean Taco', 'Crazy Chicken', 'Katsu', 'Kimchi Fried Rice']
side_total = 0
side_group = ['Tteokbokki', 'Kimchi', 'Korean Noodle (Side)', 'Noodle (Side)', 'Yum Yum Sauce', 'Dumpling', 'Egg Roll', 'Fried Rice (Side)', 'Radish']
food_tmp  = []
side_tmp = []

# Must iterate in order
for item in all_keys:
    # For Food Group
    if item not in current_keys:
        continue

    if item in ['Food'] or item in food_group:
        if item == 'Food':
            food_total = index_csv(item)
        if item in food_group:
            food_tmp.append(f'{en2kor[item]} {index_csv(item)}')
            food_total = index_csv(item) + food_total

    if item in ['Side'] or item in side_group:
        if item == 'Side':
            side_total = index_csv(item)
        if item in side_group:
            side_tmp.append(f"{en2kor[item]} {index_csv(item)}")
            side_total += index_csv(item)
file.write(f"{en2kor["Food"]} {food_total} ({', '.join(map(str, food_tmp))}) \n")
file.write(f"{en2kor["Sides"]} {side_total} ({', '.join(map(str, side_tmp))}) \n")

for item in ['Drinks', 'Snack', 'Set Menu', 'Boba']:
    if item in current_keys:
        file.write(f"{en2kor[item]} {index_csv(item)} \n")

file.close
        
