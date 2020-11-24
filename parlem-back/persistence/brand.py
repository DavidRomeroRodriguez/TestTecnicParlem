from model import Brand

class BrandPersistence:
    nintendo = Brand(0, 'Nintendo', 'Calle Falsa 123, Tokyo', 'contacto@nintendo.com', '111222333')
    pixar = Brand(1, 'Pixar', 'Calle Falsa 124, Emervylle', 'contacto@pixar.com', '111222334')
    brands = [nintendo, pixar]

    def get_all_brands(self):
        return self.brands

    def get_brand_by_id(self, id):
        for brand in self.brands:
            if brand._id == id:
                return brand