import random
import networkx as nx

class No:
    def __init__(self,_id, _latitude,_longitude,_borda=False):
        ''' 
            Define um nó da rede.
            
            _id: string
            _latitude: float
            _longitude: float
            _borda: boolean
        '''
        
        self.id = _id
        self.latitude = _latitude
        self.longitude =_longitude
        self.borda = _borda

    
    def getInfo(self):
        
        return {"id":self.id, 
                "x":self.latitude, 
                "y":self.longitude,
                "borda":self.borda}   



class Canal:
    def __init__(self, _porta, _tamanho, _material,_natureza, _tipo):
        '''
            Define as características do canal.
            
            _porta: int
            _tamanho: float
            _material:string
            _natureza:string
            _tipo: string
        '''
        self.porta = _porta
        self.tamanho = _tamanho
        self.material = _material
        self.natureza = _natureza
        self.tipo = _tipo
        
    def getInfo(self): 
        
        return {"porta": self.porta,
                 "tamanho":self.tamanho,
                 "material": self.material,
                 "natureza": self.natureza,
                 "tipo": self.tipo}

   
class Topologia:
    '''
        Responsável pela a construção da topologia, com seus nós e canais
        
        self.network: networkx
        
    '''
    def __init__(self):
        self.network = nx.MultiGraph()
        
    def addCanal(self,_origem,_destino, _canal):
        '''
            _origem:  No
            _destino: No
            _canal: Canal
            
        '''
        self.network.add_edge(_origem, _destino, canal=_canal)

    def getInfo(self):
        json = {}
        print(self.network.edges.data())
           
          
        return json
        
a = No('A',3.4,32.4,False)
b = No('B',43.4,5.4,False)
c = No('C',5.4,8.4,False)
d = No('D',8.4,23.4,False)



ch1 = Canal(80,20,'fotons','quantica','wireless')
ch2 = Canal(40,30,'cobre','classica','cabo')
ch3 = Canal(40,10,'ondas eletromagnéticos','classica','satelite')
ch4 = Canal(200,10,'fribra ótica','classica','cabo')
ch5 = Canal(160,10,'cobre','classica','cabo')


t= Topologia()

t.addCanal(a,b,ch1)
t.addCanal(c,d,ch4)
t.addCanal(a,d, ch2)
t.addCanal(a,c, ch3)
t.addCanal(b,d, ch4)


t.getInfo()