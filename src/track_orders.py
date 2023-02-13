class TrackOrders:
    # Prato favorito por cliente;
    # Pratos nunca pedidos por cada cliente;
    # Dias nunca visitados por cada cliente;
    # Dia mais movimentado;
    # Dia menos movimentado.
    def __init__(self):
        self.orders_meals = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders_meals)

    # registra um pedido na instancia
    def add_new_order(self, customer, order, day):
        dict_order = {"customer": customer, "order": order, "day": day}
        self.orders_meals.append(dict_order)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_meals = {}

        for order in self.orders_meals:
            if order["customer"] == customer:
                if order["order"] in customer_meals:
                    customer_meals[order["order"]] += 1
                else:
                    customer_meals[order["order"]] = 1

        return max(customer_meals, key=customer_meals.get)

    def get_never_ordered_per_customer(self, customer):
        all_meals = set()
        meals_asked_by_customer = set()
        not_asked_by_customer = set()

        for order in self.orders_meals:
            all_meals.add(order["order"])
            if order["customer"] == customer:
                meals_asked_by_customer.add(order["order"])

        for meal in all_meals:
            if meal not in meals_asked_by_customer:
                not_asked_by_customer.add(meal)

        return not_asked_by_customer

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        customer_attendance = set()
        customer_missed_days = set()

        for order in self.orders_meals:
            all_days.add(order["day"])
            if order["customer"] == customer:
                customer_attendance.add(order["day"])

        for day in all_days:
            if day not in customer_attendance:
                customer_missed_days.add(day)

        return customer_missed_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
