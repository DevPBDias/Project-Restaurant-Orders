import csv


def reader_csv(file):  # [{customers: maria, meals: hamburguer, days: domingo}]
    try:
        with open(file) as csv_file:
            data_headers = ["customers", "meals", "days"]
            data = csv.DictReader(csv_file, fieldnames=data_headers)
            return list(data)

    except FileNotFoundError:
        if not file.endswith(".csv"):
            raise FileNotFoundError(f"Extensão inválida: '{file}'")
        else:
            raise FileNotFoundError(f"Arquivo inexistente: '{file}'")


def max_meal(data):
    maria_meals = {}  # {hamburguer: 10}

    for order in data:
        if order["customers"] == "maria":
            if order["meals"] in maria_meals:
                maria_meals[order["meals"]] += 1
            else:
                maria_meals[order["meals"]] = 1
    # https://datagy.io/python-get-dictionary-key-with-max-value/
    return max(maria_meals, key=maria_meals.get)


def times_hamburger(data):  # 1
    arnaldo_hamburguer = 0

    for order in data:
        if order["customers"] == "arnaldo":
            if order["meals"] == "hamburguer":
                arnaldo_hamburguer += 1
    return arnaldo_hamburguer


def no_meals_asked(data):
    all_meals = set()
    meals_asked_by_joao = set()
    not_asked_by_joao = set()

    for order in data:
        all_meals.add(order["meals"])
        if order["customers"] == "joao":
            meals_asked_by_joao.add(order["meals"])

    for meal in all_meals:
        if meal not in meals_asked_by_joao:
            not_asked_by_joao.add(meal)

    return not_asked_by_joao


def no_attendance_days(data):
    all_days = set()
    joao_attendance = set()
    joao_missed_days = set()

    for order in data:
        all_days.add(order["days"])
        if order["customers"] == "joao":
            joao_attendance.add(order["days"])

    for day in all_days:
        if day not in joao_attendance:
            joao_missed_days.add(day)

    return joao_missed_days


def writing_txt(path_to_file):
    data_csv = reader_csv(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(max_meal(data_csv)) + '\n')
        file.write(str(times_hamburger(data_csv)) + '\n')
        file.write(str(no_meals_asked(data_csv)) + '\n')
        file.write(str(no_attendance_days(data_csv)) + '\n')


def analyze_log(path_to_file):
    writing_txt(path_to_file)
