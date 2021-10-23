import requests

class TestDepartamento:

    def test_get_departamentos:
        departamentos = requests.get(url=self.url_base_departamentos)

        assert departamentos.status_code == 200

    def test_get_departamento:
        
        departamento = requests.get(url=f'{self.url_base_departamentos}1/')

        assert departamento.status_code == 200

    
    def test_post_departamento:
        
        novo ={
            "departamento":"Marketing"
        }

        resultado = requests.post(url=self.url_base_departamentos, data = novo)

        assert resultado.status_code == 201


    def test_put_departamento:
        
        atualizado ={
            "departamento":"Marketing e Design"
        }

        resposta = requests.put(url=f'{self.url_base_departamentos}4/', data = novo)

        assert resposta.status_code == 201
        assert resposta.json()['departamento'] == atualizado['departamento']
