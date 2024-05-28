# Conversor de PDF

Este projeto contém uma coleção de serviços para manipulação de arquivos PDF, incluindo conversão de PDF para texto, redução de resolução de PDF e um serviço de logs. Cada serviço é implementado em um contêiner Docker separado para facilitar o desenvolvimento, a implantação e a escalabilidade.

## Visão Geral dos Serviços

### 1. PDF to TEXT

Este serviço converte arquivos PDF para texto. Ele aceita um arquivo PDF via upload, processa o arquivo para extrair o texto e envia o resultado de volta ao cliente via um arquivo .txt. Além disso, registra a operação no serviço de logs.

### 2. PDF Reducer

Este serviço reduz a resolução de arquivos PDF. Ele aceita um arquivo PDF via upload, reduz a resolução do arquivo, utilizando o software Ghostscript, conforme a seleção do usuário e envia o resultado de volta ao cliente. Também registra a operação no serviço de logs.

### 3. Logs

Este serviço registra todas as operações realizadas pelos serviços de PDF to TEXT e PDF Reducer. Ele mantém um registro das operações e pode emitir relatórios conforme necessário.

## Configurando o ambiente de execução

### Docker

Certifique-se de que você tem o Docker instalado na sua máquina. Você pode fazer o download e instalar o Docker a partir do [site oficial do Docker](https://www.docker.com/get-started).

### Docker Compose

Se o seu projeto utiliza o Docker Compose, você também precisará instalá-lo. O Docker Compose geralmente é incluído com o Docker Desktop. Mais informações sobre a instalação podem ser encontradas na [documentação oficial do Docker Compose](https://docs.docker.com/compose/install/).

## Executando o projeto

Para executar o projeto, siga estes passos:

1. Clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/enzomazocorodrigues/pdf-converter.git
   ```

1. Navegue até o diretório do projeto:

   ```bash
   cd pdf-converter
   ```

1. Construa e execute os containers:

   ```bash
   docker-compose up --build
   ```

## Testando os Serviços

Você pode testar os serviços utilizando ferramentas como `curl`, Postman ou até mesmo um browser.

#### Usando o PDF to TEXT

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" http://localhost:5001/upload
```

#### Usando o PDF Reducer

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" -F "resolution=default" http://localhost:5002/upload
```

#### Baixando os logs

```bash
curl http://localhost:5003/
```

## Colaboradores

<ul>
    <li>
        <a href="https://github.com/bk5559" style="display: flex; align-items: center; gap: 8px;">
            <img src="https://github.com/bk5559.png" alt="Enzo Rodrigues" style="border-radius: 50%; width: 32px; height: 32px;">
            Benjamin Kim
        </a>
    </li>
    <li>
        <a href="https://github.com/enzomazocorodrigues" style="display: flex; align-items: center; gap: 8px;">
            <img src="https://github.com/enzomazocorodrigues.png" alt="Enzo Rodrigues" style="border-radius: 50%; width: 32px; height: 32px;">
            Enzo Rodrigues
        </a>
    </li>
    <li>
    <a href="https://github.com/matheuspfau" style="display: flex; align-items: center; gap: 8px;">
        <img src="https://github.com/matheuspfau.png" alt="Enzo Rodrigues" style="border-radius: 50%; width: 32px; height: 32px;">
        Matheus Pfau
    </a>
    </li>
</ul>
