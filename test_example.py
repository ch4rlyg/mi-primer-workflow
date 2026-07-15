"""
Tests simples para validar que el workflow funciona correctamente.
"""


def test_suma():
    """Prueba que 3 + 4 = 7"""
    assert 3 + 4 == 7


def test_resta():
    """Prueba que 10 - 5 = 5"""
    assert 10 - 5 == 5


def test_archivo_readme_existe(tmp_path):
    """Prueba que el README existe"""
    import os
    assert os.path.exists("README.md"), "README.md debería existir"
