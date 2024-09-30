from BaseData.ControlPath import ControlPath

class Rotas:
    @classmethod
    def methodPostIdCli(self, itens: list):
        try:
            self.clearCache()
            ControlPath.data(itens.cache)
            return 'Dado cadastrado com sucesso.'
        except:
            return 'Erro de cadastro'

    @classmethod
    def methodGet(self, data=None):
        try:
            return ControlPath.filterElement(data)
        except:
            return 'Dado não encontrado.'
        
    @classmethod
    def clearCache(self):
        try:
            ControlPath.delete_data()
            return 'Dado deletado com sucesso'
        except:
            return 'Erro ao deletar'