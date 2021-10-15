class Helmet:

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    
    def set_brand(self,brand):
        self.__brand = brand
        
    def set_model(self,model):
        self.__model = model

    
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model
        