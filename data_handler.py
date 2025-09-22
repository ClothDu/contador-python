import json
import os

class JsonStrings:
    @staticmethod
    def createString(infos):
        return json.dumps(infos)


class File:
    @staticmethod
    def updateFile(strF, nomeArq):
        with open(nomeArq, "w") as f:
            f.write(strF)
            
    @staticmethod
    def arquivoParaString(nomeArq):
        if os.path.exists(nomeArq):
            with open(nomeArq, "r") as f:
                return f.read()
        else:
            raise FileNotFoundError("sem arquivo existente")
        
        
class Data:
    @staticmethod
    def salvarFile(infos, nomeArq):
        strF = JsonStrings.createString(infos)
        File.updateFile(strF, nomeArq)
            
    @staticmethod
    def abrirFile(nomeArq):
        if os.path.exists(nomeArq):
            newClass = File.arquivoParaString(nomeArq)
            return json.loads(newClass)
        else:
            raise FileNotFoundError("sem arquivo existente")
