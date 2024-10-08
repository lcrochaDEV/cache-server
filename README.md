### Para Instalação no Windows 10 foi criado um Ambiente Virtual

### Instalação do ambiente Virtual

```shell
python -m venv .venv
```

### Ativação do ambiente virtual no Windows

```shell
.venv/Scripts/activate
```

### Para Instalação no Debia 12 foi criado um Ambiente Virtual
 #### Crie um ambiente virtual usando venv ou virtual env Certifique-se venv de que esteja instalado executando:
```shell
sudo apt install python3-venv
```
#### Para criar um novo ambiente virtual em um **diretório chamado env**, execute:
```shell
python3 -m venv env
```
#### Para ativar este ambiente virtual (que modifica a PATH variável de ambiente), execute:
```shell
source env/bin/activate
```
#### Agora você pode instalar uma biblioteca neste ambiente virtual:
```shell
pip install XYZ
```
Os arquivos serão instalados no env/diretório.

Se quiser sair do ambiente virtual, você pode executar:
```shell
deactivate
```

### Instalação de Bibliotecas: 
```shell
#pip install selenium
#pip install python-dotenv
#pip install fastapi
#pip install "uvicorn[standard]" ou pip install "uvicorn[all]"
#pip install pydantic
```
#### Iniciando o servidor Uvincorn
```shell
uvicorn app:app --reload
```

### Projeto em andamento

Este projeto visa automatizar, busca e armazenamento de dados, ele é chamado por métodos CRUD, onde é usado como um servidor Cache local.

### FRONT-END
#### CABEÇALHO FETCH

```js
var myHeaders = new Headers({
    'Content-Type': 'application/json',
});

let bodyObj = {
    "cache":{
                'QUALQUER OBJETO'
            } 
}


let conectApi = async (url, obj) => {
    var options = {
      method: "POST",
      body: JSON.stringify(obj),
      headers: myHeaders,
      mode: "cors",
      cache: "default",
    };

    try{
        const conexao = await fetch(url, options)
        if(conexao.status === 200){
            const openConexao = await conexao.json();
            return openConexao;
        } 
    }catch(error){
        console.log('Falha no link!')
    }
}

conectApi('http://127.0.0.1:8000/host', bodyObj)
```
