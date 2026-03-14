from app import calcular_prioridad


def test_prioridad_normal():
    assert calcular_prioridad(3) == "prioridad normal"


def test_prioridad_alta():
    assert calcular_prioridad(6) == "prioridad alta"


def test_dias_negativos():
    assert calcular_prioridad(-1) == "error: dias negativos"
