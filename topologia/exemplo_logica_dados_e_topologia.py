dados = {
    "canal": {
        "clássico": {
            "A": {
                "B": {
                    "comprimento": 1000,
                    "tipo": "fibra",
                    "ruído": [],
                    "num_portas_entrada": 100,
                    "num_portas_saida": 1,
                },
                "C": {"comprimento": 1500, "tipo": "fibra", "ruído": []},
            }
        },
        "quântico": {"A": {"B": {"comprimento": 1000, "tipo": "fibra", "ruído": []}}},
    }
}

dados3 = {
    "canal": {
        "clássico": {
            ("A", "B"): {"comprimento": 1000, "tipo": "fibra", "ruído": []},
            ("A", "C"): {"comprimento": 1500, "tipo": "fibra", "ruído": []},
        }
    },
    "quântico": {"A": {"B": {"comprimento": 1000, "tipo": "fibra", "ruído": []}}},
}


dados2 = {
    "canal": {
        "A": {
            "B": {
                "classico": {"comprimento": 1000, "tipo": "fibra", "ruído": []},
                "quantico": {},
            }
        },
        "B": {},
    }
}


dados4 = {
    "nó": {
        "A": {
            "num_qubits": 2,
            "tipo": "supercondutor",
            "processador": True,
            "detector": True,
            "numero_de_portas": {"classico": 1, "quantico": 1},
            "ruído": [],
        },
        "B": {
            "num_qubits": 1,
            "tipo": "supercondutor",
            "processador": True,
            "detector": True,
            "ruído": [],
        },
        "C": {
            "num_qubits": 7,
            "tipo": "supercondutor",
            "processador": True,
            "detector": True,
            "ruído": [],
        },
    },
    "canal": {
        "clássico": {
            "A": {
                "B": {"comprimento": 1000, "tipo": "fibra", "ruído": []},
                "C": {"comprimento": 1500, "tipo": "fibra", "ruído": []},
            }
        },
        "quântico": {"A": {"B": {"comprimento": 1000, "tipo": "fibra", "ruído": []}}},
    },
}


def definir_topo_canal(dados):
    for k, v in dados.items():
        definir_classico_canal(v) if k == "classico" else definir_quantico_canal(v)


def definir_classico_canal(dados):
    for no1, v in dados.items():
        for no2 in v.items():
            criar_canal()
    ...


def definir_classico2(dados):
    for no, v in dados.items():
        return no[0], no[1]


def definir_quantico_canal(dados):
    ...


def criar_canal(dados):
    fisica = Topologia.InterfaceFisica("canal", dados)
    app = Topologia.InterfaceAplicação("canal", dados)
