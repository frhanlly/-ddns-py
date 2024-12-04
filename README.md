
# ddns-py

## Como usar?

#### 01 - Faça o clone do repositório 

#### 02 - Vá até o diretório do repositório criado

#### 03 - Crie um arquivo .env e preencha com as variáveis abaixo

API_TOKEN='TOKEN DA API'

ZONE_ID='ID DA ZONA NA CLOUDFLARE'

DNS_ID='ID DO REGISTRO DNS'

DNS_ENTRY='FQDN DO REGISTRO'

DNS_TYPE='TIPO DO REGISTRO (A para IPV4 ou AAAAA para IPV6'

#### 04 - dê permissão de execução para o arquivo main.py

#### 05 - Crie uma entrada no /etc/crontab para executar periodicamente [OPCIONAL, LINUX]


## Kubernetes

#### 01 - Se você tiver um cluster k8s onde você quer usar esse script, você pode optar por usar um cronjob dentro do k8s com os manifestos no diretório manifests.

#### 02 - Primeiro é necessário fazer o build da imagem e jogar para alguma registry a partir do Dockerfile do repositório (docker build -t TAG_NAME {DIR_DO_DOCKERFILE})

#### 03 - Após isso, preencha os manifestos yaml com os valores adequados (API Token, imagem do build da aplicação, etc)

#### 04 - Por fim, execute: kubectl apply -f manifests