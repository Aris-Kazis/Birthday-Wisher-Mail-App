import smtplib
import datetime as dt
import pandas
import random


birthdays_df = pandas.read_csv("birthdays.csv")
for i in range(len(birthdays_df)):
    birthday_day = birthdays_df["day"][i]
    birthday_month = birthdays_df["month"][i]
    today = dt.date.today()
    if birthday_day == today.day and birthday_month == today.month:
        birthday_name = birthdays_df["name"][i]
        birthday_email = birthdays_df["email"][i]

        list_of_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter_path = f"letter_templates/{random.choice(list_of_files)}"

        with open(random_letter_path) as file:
            letter1 = file.read().replace("[NAME]", birthday_name)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="aris77777kazis@gmail.com", password="zsjqtkeldyeqrifx")

        connection.sendmail(
            from_addr="aris77777kazis@gmail.com",
            to_addrs=str(birthday_email),
            msg=f"Subject::D\n\n{letter1}"
        )
