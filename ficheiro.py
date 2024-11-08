import json

class Ficheiro:
    
    """ 
    Save the data of python object in a json file.
    :param str filaName: The name of the file
    :param object data: The data to save
    :param string operation: The mode of writting( w or a)
    """
    def saveData(self,fileName,data,modeWriting):
        with open(fileName,modeWriting) as file:
            json.dump(data,file)#Save the information
            print("Dados salvos com sucesso")
          
          
    def loadData(self,fileName):  
        try:
            with open(fileName,'r') as file:
                pythonObject=json.load(file)
                return pythonObject
        
        except FileNotFoundError as e:
            print("Ficheiro nao encontrado: ", e)
            open(fileName,'x')
            
        except Exception as e:
            print("Houve um erro: ", e)
          
