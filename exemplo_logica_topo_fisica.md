
# Exemplo de classes/lógica para o fluxo Topologia -> Física




dados: dict

- classe Topologia(dados)
	- método/subclasse Topologia.InterfaceFisica(dados[...]) -> Fisica.InterfaceTopologia(dados)




- classe Fisica()
	- método/subclasse Fisica.InterfaceTopologia(dados[...]) -> Fisica.CriarComponente(dados[...])
	- método/subclasse Fisica.CriarComponente(dados[...]) -> (Fisica.Processador(), Fisica.Memoria(), Fisica.MeioComunicação(), etc)
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


			- $H = \under{\text{independentes}}{\frac{\omega}{2} \sigma_z} + \under{\text{interação entre os subsistemas i, j}}{\sum_{ij, i \diff j}{Vint_{i,j}}}$

