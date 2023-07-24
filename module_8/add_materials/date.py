from datetime import datetime

def get_days():
    """Скрипт расчёта количества дней до заданной даты """
    user_input = input("Введите дату в формате dd.mm: ")
    user_date = datetime.strptime(user_input, "%d.%m")
    current_date = datetime.now()
    user_date = user_date.replace(year=current_date.year)
    delta_days = user_date - current_date
    target_date = datetime.strftime(user_date, "%d-%B-%Y")

    print(f"{delta_days.days} days between now and target date {target_date}")

def make_record(record):
    current_time = str(datetime.now().timestamp()).split(".")[0]
    with open(f"backup_{current_time}.txt", 'w') as fh:
        fh.write(record)

if __name__=="__main__":
    #get_days()
    record = "AC/DC"
    make_record(record)
