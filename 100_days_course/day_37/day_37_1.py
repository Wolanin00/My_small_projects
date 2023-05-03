from datetime import datetime

today = str(datetime.now()).split(' ')[0].replace('-', '')
today1 = datetime.now().strftime("%Y%m%d")

print(today)
print(today1)
