class Project:

    def __init__(self, projID,projDesc,consultants,dueDate):
        self.__projID = projID
        self.__projDesc = projDesc
        self.__consultants = consultants
        self.__dueDate = dueDate


    def set_projID(self,projID):
        self.__projID = projID
    
    def set_projDesc(self,projDesc):
        self.__projDesc = projDesc

    def set_consultants(self,consultants):
        self.__consultants = consultants

    def set_dueDate(self,dueDate):
        self.__dueDate = dueDate



    def get_projID(self):
        return self.__projID

    def get_projDesc(self):
        return self.__projDesc

    def get_consultants(self):
        return self.__consultants

    def get_dueDate(self):
        return self.__dueDate

        
