from datetime import datetime, timedelta
import random

def get_random_birthdays(n):
    """Получить список случайных дней рождения"""
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    birthdays_list = []
    for i in range(n):
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1, 12)
        fake_day = random.randint(1, 31)
        # чтобы не получилось 31 февраля нужно обернуть в try
        try:
            fake_birthday = datetime(year=fake_year,month=fake_month,day=fake_day)
        except ValueError:
            continue
        if current_date >= fake_birthday:
            birthdays_list.append(fake_birthday.date())

    return birthdays_list

if __name__=="__main__":
    birthdays = get_random_birthdays(10)
    print(random.sample(birthdays, k=4)) # [datetime.date(1960, 5, 23), datetime.date(2008, 6, 12), datetime.date(2020, 4, 29), datetime.date(1991, 5, 11)]
    data = [1,2,3,4,5]
    random.shuffle(data)
    print(data)
