
# Exemplo de classes/lógica para o fluxo Topologia -> Física




dados: dict

- classe Topologia(dados)
	- método/subclasse Topologia.InterfaceFisica(dados[...]) -> Fisica.InterfaceTopologia(dados)
  - método/subclasse Topologia.InterfaceAplicação(dados[...]) - > Aplicação.InterfaceTopologia(dados)




- classe Fisica()
	- método/subclasse Fisica.InterfaceTopologia(dados[...]) -> Fisica.CriarComponente(dados[...])
	- método/subclasse Fisica.CriarComponente(dados[...]) -> (Fisica.Componente.Processador(), Fisica.Componente.Memoria(), Fisica.Componente.MeioComunicação(), etc)
	- método/subclasse Fisica.Processador() -> (Fisica.Supercondutor(), Fisica.NV(), Fisica.RMN(), etc)
	- método/subclasse Fisica.Memoria() -> (...,)
	- método/subclasse Fisica.MeioComunicação() -> (Fisica.FibraOptica(), Fisica.Atmosfera(), Fisica.Espaço(), Fisica.Hibrida(), etc)
	- ...

- Exemplo:

	- Supercondutor()
		- numero qubits -> quantidade de termos representando a dinâmica dos qubits dentro do hamiltoniano
		- equação hamiltoniana (QuTiP)
			- template a depender do tipo de sistema
			- termos independentes (termos do proprio qubit)
			- termos dependentes
				- "interna" (interação entre os subsistemas locais)
				- "externa" (interação fora, ex: com outro sistema físico tipo uma memória quântica)
				- ligação entre interna e externa (ex: ressonador)


			- $H = \underbrace{\text{independentes}}{\frac{\omega}{2} \sigma_z} + \underbrace{\text{interação entre os subsistemas i, j}}{\sum_{ij, i \diff j}{Vint_{i,j}}}$



class Fisica(ABC):
  pass

class InterfaceTopologia(Fisica):
  pass

class CriarComponente(Fisica):
  pass

class Componente(Fisica):
  pass

class Processador(Componente):
  pass

class Supercondutor(Componente):
  pass

class Memoria(Componente):
  pass

class MeioComunicação(Componente):
  pass

class FibraOptica(Componente):
  pass
