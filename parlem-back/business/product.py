from persistence import ProductPersistence

class ProductBusiness:
    persistence = ProductPersistence()

    def get_all_products(self, format_json = False):
        all_products = self.persistence.get_all_products()
        if format_json:
            all_products_json = []
            for product in all_products:
                all_products_json.append(product.serialize())
            return all_products_json
        return all_products

    def get_product_by_id(self, id, format_json = False):
        for product in self.persistence.get_all_products():
            if product._id == id:
                if format_json:
                    return product.serialize()
                return product