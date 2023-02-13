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
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
