from pytest import fixture
import json


@fixture(scope="session")
def feedback():
    with open("feedback.jsonc", "r") as handle:
        fixed_json = "".join(
            line for line in handle if not line.strip().startswith("//")
        )
        return json.loads(fixed_json)


def test_dar_uma_nota_de_0_a_10_ao_projeto(feedback):
    nota = feedback.get("nota")
    assert type(nota) is int
    assert 0 <= nota <= 10


def test_falar_dos_pontos_positivos(feedback):
    comentario = feedback.get("pontos_positivos")
    assert type(comentario) is not None
    assert comentario.strip() != ""


def test_falar_dos_pontos_negativos(feedback):
    comentario = feedback.get("pontos_negativos")
    assert type(comentario) is not None
    assert comentario.strip() != ""
