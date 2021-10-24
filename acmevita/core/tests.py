import requests

class TestDepartamento:
    url_base_departamentos = 'http://localhost:8000/api/departamento/'
    def test_get_departamentos(self):
        departamentos = requests.get(url=self.url_base_departamentos)

        assert departamentos.status_code == 200

    def test_get_departamento(self):
        departamento = requests.get(url=f'{self.url_base_departamentos}1/')

        assert departamento.status_code == 200


    def test_post_departamento(self):
        novo ={
            "departamento":"Marketing"
        }

        resultado = requests.post(url=self.url_base_departamentos, data = novo)

        assert resultado.status_code == 201


    def test_put_departamento(self):
        atualizado ={
            "departamento":"Marketing e Design"
        }

        resposta = requests.put(url=f'{self.url_base_departamentos}4/', data = atualizado)

        assert resposta.status_code == 201
        assert resposta.json()['departamento'] == atualizado['departamento']


    def test_delete_departamento(self):
        resposta = requests.delete(url=f'{self.url_base_departamentos}4/')

        assert resposta.status_code == 204 and len(resposta.text) == 0
