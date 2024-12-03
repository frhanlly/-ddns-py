
# ddns-py

## Como usar?

01 - Faça o clone do repositório 

02 - Vá até o diretório do repositório criado

03 - Crie um arquivo .env e preencha com as variáveis abaixo
API_TOKEN='TOKEN DA API'
ZONE_ID='ID DA ZONA NA CLOUDFLARE'
DNS_ID='ID DO REGISTRO DNS'
DNS_ENTRY='FQDN DO REGISTRO'
DNS_TYPE='TIPO DO REGISTRO (A para IPV4 ou AAAAA para IPV6'

04 - dê permissão de execução para o arquivo main.py

05 - Crie uma entrada no /etc/crontab para executar periodicamente [OPCIONAL, LINUX]