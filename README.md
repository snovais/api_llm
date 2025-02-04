# 
Passos para Configuração
Passo 1: Criar e Conectar à VM no Google Cloud
Crie uma instância de VM no Google Cloud com a imagem Ubuntu.
Permita o tráfego HTTP/HTTPS ao configurar o firewall da instância.
Conecte-se à instância via SSH pelo Console do Google Cloud.

Passo 2: Preparar a VM
Atualize o sistema:

sudo apt update && sudo apt upgrade -y
Instale o Python, pip, e outras dependências:


sudo apt install python3-pip python3-dev git -y
Instale o FastAPI, Uvicorn, Transformers e Torch:

pip3 install fastapi uvicorn transformers torch

Passo 3: Subir o Código para a VM
Clone seu repositório Git (ou transfira os arquivos manualmente):

git clone https://github.com/usuario/repositorio.git
cd repositorio

Passo 4: Rodar a API com Uvicorn
Inicie o servidor:

uvicorn app:app --host 0.0.0.0 --port 8000 --reload
A API estará disponível externamente na porta 8000.

Passo 5: Configurar o Firewall do Google Cloud
Crie uma regra de firewall para permitir tráfego na porta 8000:
No Console do Google Cloud, vá em VPC Network > Firewall Rules.
Crie uma nova regra para permitir o tráfego TCP na porta 8000 de qualquer IP.

Passo 6: Acessar a API
Obtenha o IP Externo da VM no Console do Google Cloud.
Acesse a API no navegador:
http://<IP-da-Virtual-Machine>:8000

Passo 7: Rodar o Cliente Python
Atualize o cliente (client.py) com o IP da sua VM:

api_url = "http://<IP-da-Virtual-Machine>:8000/generate"
Execute o cliente:
python3 client.py


Agora sua API está rodando no Google Cloud e pode ser acessada por qualquer lugar! Se precisar de mais algum detalhe, só me avisar.

