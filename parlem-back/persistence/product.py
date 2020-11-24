from model import Product
from .brand import BrandPersistence as brands

class ProductPersistence:
    products = [
        Product(1111111, 'FIBRA 1000 ADAMO', 'ftth', 933933933, '2019-01-09 14:26:17', 555555, brands.nintendo),
        Product(1111112, 'Toy Story 5', 'Bluray Disc', 922922922, '2020-11-24 09:23:17', 555556, brands.pixar),
        Product(1111113, 'FIBRA 1000 ADAMO', 'ftth', 933933933, '2020-11-24 09:23:18', 555556, brands.nintendo)
    ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, id):
        for product in self.products:
            if product._id == id:
                return product