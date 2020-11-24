class Brand:
    def __init__(self, _id, brandName, address, email, phone):
        self._id = _id
        self.brandName = brandName
        self.address = address
        self.email = email
        self.phone = phone

    def serialize(self):  
        return {           
            '_id': self._id,
            'brandName': self.brandName,
            'address': self.address,
            'email': self.email,
            'phone': self.phone
        }