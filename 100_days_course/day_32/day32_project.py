import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "testowy100daysms@gmail.com"
password = 'REMOVED'  # TODO Remove

raw_birthdays_data = pd.read_csv("birthdays.csv")
birthdays_data = pd.DataFrame.to_dict(raw_birthdays_data, orient="records")

now = dt.datetime.now()
current_day = now.day
current_month = now.month

for birthday_person in birthdays_data:
    if birthday_person['day'] == current_day and birthday_person['month'] == current_month:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_data:
            letter = letter_data.read().replace('[NAME]', birthday_person['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="testowy100daysms@gmail.com",
                msg=f"Subject:Happy Birthday!\n\n"
                    f"{letter}")
