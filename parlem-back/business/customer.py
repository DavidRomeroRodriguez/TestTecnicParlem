from persistence import CustomerPersistence

class CustomerBusiness:
    persistence = CustomerPersistence()

    def get_all_customers(self, format_json = False):
        all_customers = self.persistence.get_all_customers()
        if format_json:
            all_customers_json = []
            for customer in all_customers:
                all_customers_json.append(customer.serialize())
            return all_customers_json
        return all_customers

    def get_customer_by_id(self, id, format_json = False):
        for customer in self.persistence.get_all_customers():
            if customer._id == id:
                if format_json:
                    return customer.serialize()
                return customer