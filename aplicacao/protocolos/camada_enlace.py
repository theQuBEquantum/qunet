"""
lógica da camada de enlace:
- receber os dados vindos da camada de aplicação
    - tipo de protocolo a ser chamado
    - dado
- vai realizar a chamada do protocolo da camada de enlace
- vai repassar a chamada para a camada física
    - tipo de protocolo a ser chamado por ela
    - dado
- vai receber o resultado/resposta da camada física
- verificar os requisitos para prosseguir ou repetir o protocolo
- enviar o resultado para a camada de aplicação
"""
