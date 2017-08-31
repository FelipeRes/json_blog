# json_blog
O arquivo *generate_database.py* faz uma leitura do arquivo *db.json* e faz as requisições http para inserir os dados no sistema.
Para isso, o servidor deve estar rodando na porta 8000 e todas as migrações devem ter sido feitas.

Para fazer a requisição de inserção do usuario e endereço é necessário recuperar a url da geolocalização inserida:
```python
response, content = h.request(uri="http://localhost:8000/geo/", method="POST", headers=headers, body=post_data_format)
geo_url = json.loads(content.decode())
```

Essa url será utilizada na inserção do endereço para fazer o link entre os objetos. Abaixo está escrito o json do post para inserir o endereço. Observe como o campo geo usa o dicionário *geo_url*.
```python
address_data = {
    	"street": user['address']['street'],
    	"suite": user['address']['suite'],
    	"city": user['address']['city'],
    	"zipcode": user['address']['zipcode'],
    	"geo": geo_url['url'],
	}
  ```
O mesmo processo deve ser realizado para os endereços dos usuarios, mas isso só funciona caso não haja nenhum *SlugRelatedField* em *serializars.py*.
