import smtplib
import random
import datetime as dt

my_email = "testowy100daysms@gmail.com"
password = 'REMOVED'  # TODO Remove

now = dt.datetime.now()
current_day_of_week = now.weekday()
if current_day_of_week == 0:  # Send mail only in Monday
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="testowy100daysms@gmail.com",
            msg=f"Subject:Monday Motivation\n\n"
                f"{random_quote}"
        )
