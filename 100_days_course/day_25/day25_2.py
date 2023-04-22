import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

primary_fur_color = data['Primary Fur Color']
gray_color_count = len(data[primary_fur_color == 'Gray'])
red_color_count = len(data[primary_fur_color == 'Cinnamon'])
black_color_count = len(data[primary_fur_color == 'Black'])
print(gray_color_count)
print(red_color_count)
print(black_color_count)

data_dict = {
    'Fur Color': ["Gray", "Cinnamon", "Black"],
    'Count': [gray_color_count, red_color_count, black_color_count]
}
print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
