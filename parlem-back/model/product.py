class Product:
    def __init__(self, _id, productName, productTypeName, numeracioTerminal, soldAt, customerId, brand):
        self._id = _id
        self.productName = productName
        self.productTypeName = productTypeName
        self.numeracioTerminal = numeracioTerminal
        self.soldAt = soldAt
        self.customerId = customerId
        self.brand = brand

    def serialize(self):  
        return {           
            '_id': self._id,
            'productName': self.productName,
            'productTypeName': self.productTypeName,
            'numeracioTerminal': self.numeracioTerminal,
            'soldAt': self.soldAt,
            'customerId': self.customerId,
            'brand': self.brand.serialize()
        }