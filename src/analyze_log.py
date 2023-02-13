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


def max_meal_ordered_by_customer(data, customer):
    customer_meals = {}  # {hamburguer: 10}

    for order in data:
        if order["customers"] == customer:
            if order["meals"] in customer_meals:
                customer_meals[order["meals"]] += 1
            else:
                customer_meals[order["meals"]] = 1
    # https://datagy.io/python-get-dictionary-key-with-max-value/
    return max(customer_meals, key=customer_meals.get)


def most_meal_ordered(data, customer, meal):  # 1
    customer_meal = 0

    for order in data:
        if order["customers"] == customer:
            if order["meals"] == meal:
                customer_meal += 1
    return customer_meal


def no_meals_ordered_by_customer(data, customer):
    all_meals = set()
    meals_asked_by_customer = set()
    not_asked_by_customer = set()

    for order in data:
        all_meals.add(order["meals"])
        if order["customers"] == customer:
            meals_asked_by_customer.add(order["meals"])

    for meal in all_meals:
        if meal not in meals_asked_by_customer:
            not_asked_by_customer.add(meal)

    return not_asked_by_customer


def no_attendance_days_by_customer(data, customer):
    all_days = set()
    customer_attendance = set()
    customer_missed_days = set()

    for order in data:
        all_days.add(order["days"])
        if order["customers"] == customer:
            customer_attendance.add(order["days"])

    for day in all_days:
        if day not in customer_attendance:
            customer_missed_days.add(day)

    return customer_missed_days


def writing_txt(path_to_file):
    data_csv = reader_csv(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(max_meal_ordered_by_customer(data_csv, "maria")) + '\n')
        file.write(
            str(most_meal_ordered(data_csv, "arnaldo", "hamburguer")) + '\n')
        file.write(str(no_meals_ordered_by_customer(data_csv, "joao")) + '\n')
        file.write(str(no_attendance_days_by_customer(data_csv, "joao")))


def analyze_log(path_to_file):
    writing_txt(path_to_file)
