from model import Customer

class CustomerPersistence:
    customers = [
        Customer(555555, 'nif', '11223344E', 'it@parlem.com', 'Enriqueta', 'Parlem', '668668668'),
        Customer(555556, 'nif', '44332211F', 'davromrod@gmail.com', 'David', 'David Enterprise', '667667667')
    ]

    def get_all_customers(self):
        return self.customers

    def get_customer_by_id(self, id):
        for customer in self.customers:
            if customer._id == id:
                return customer