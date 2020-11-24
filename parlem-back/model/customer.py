class Customer:
    def __init__(self, _id, docType, docNum, email, givenName, familyName1, phone):
        self._id = _id
        self.docType = docType
        self.docNum = docNum
        self.email = email
        self.givenName = givenName
        self.familyName1 = familyName1
        self.phone = phone

    def serialize(self):  
        return {           
            '_id': self._id,
            'docType': self.docType,
            'docNum': self.docNum,
            'email': self.email,
            'givenName': self.givenName,
            'familyName1': self.familyName1,
            'phone': self.phone
        }