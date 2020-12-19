from sklearn import preprocessing

class ExplainedModel():

    __le__ = None

    def __init__(self):
        self.alias_manufacturers = {'vw': 'volkswagen', 'porsche': 'porche', 'mercedes': 'mercedes-benz', 'mercedes benz': 'mercedes-benz',
                                    'aston martin': 'aston-martin', 'aston': 'aston-martin', 'alfa romeo': 'alfa-romeo'}
        self.__init_label_manufacturers__()

    def __init_label_manufacturers__(self):
        self.__le__ = preprocessing.LabelEncoder()
        self.__le__.fit(self.manufacturers)
        self.__le__.transform(self.manufacturers)

    def manufacturer_number(self, number):
        try:
            return self.__le__.inverse_transform([number]).item(0)
        except:
            return None

    def manufacturers_label(self, manufacturer):
        if manufacturer in self.alias_manufacturers.keys():
            manufacturer = self.alias_manufacturers[manufacturer]
        if manufacturer in self.manufacturers:
            return self.__le__.transform([manufacturer]).item(0)
        else:
            return None

    def manufacturers_le(self):
        return self.__le__.transform(self.manufacturers)

    @property
    def manufacturers(self):
        return ['acura', 'alfa-romeo', 'aston-martin', 'audi', 'bmw', 'buick', 'cadillac', 'chevrolet', 'chrysler',
                'dodge','ferrari', 'fiat', 'ford', 'gmc', 'harley-davidson', 'honda', 'hyundai', 'infiniti', 'jaguar', 'jeep',
                'kia','land rover', 'lexus', 'lincoln', 'mazda', 'mercedes-benz', 'mercury', 'mini', 'mitsubishi', 'morgan',
                'nissan','pontiac', 'porche', 'ram', 'rover', 'saturn', 'subaru', 'tesla', 'toyota', 'volkswagen', 'volvo']


if __name__ == "__main__":
    print(ExplainedModel().manufacturers_label('vw'))