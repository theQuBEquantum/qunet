"""
lógica da camada de aplicação:
- receber os dados vindos da aplicação
    - tipo de protocolo a ser chamado
    - dado
- vai realizar a chamada do protocolo da camada de aplicação
- vai repassar a chamada para a camada de enlace
    - tipo de protocolo a ser chamado por ela
    - dado
- vai receber o resultado/resposta da camada de enlace
- verificar os requisitos para prosseguir ou repetir o protocolo
- enviar o resultado para a aplicação
"""