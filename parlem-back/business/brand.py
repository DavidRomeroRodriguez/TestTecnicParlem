from persistence import BrandPersistence

class BrandBusiness:
    persistence = BrandPersistence()

    def get_all_brands(self, format_json = False):
        all_brands = self.persistence.get_all_brands()
        if format_json:
            all_brands_json = []
            for brand in all_brands:
                all_brands_json.append(brand.serialize())
            return all_brands_json
        return all_brands

    def get_brand_by_id(self, id, format_json = False):
        for brand in self.persistence.get_all_brands():
            if brand._id == id:
                if format_json:
                    return brand.serialize()
                return brand