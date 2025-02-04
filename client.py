import requests

# URL da API que estará rodando localmente
api_url = "http://127.0.0.1:8000/generate"

# Função para enviar o texto e receber a resposta gerada
def generate_text(input_text: str):
    # Dados a serem enviados para a API
    data = {"text": input_text}
    
    try:
        # Envia a requisição POST para a API
        response = requests.post(api_url, json=data)
        
        # Se a resposta for bem-sucedida, retorne o texto gerado
        if response.status_code == 200:
            result = response.json()
            return result.get("generated_text", "Texto gerado não encontrado")
        else:
            return f"Erro: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"Erro ao conectar com a API: {str(e)}"

# Exemplo de uso
if __name__ == "__main__":
    input_text = "A inteligência artificial está mudando o mundo porque"
    generated_text = generate_text(input_text)
    print("Texto gerado pela API:", generated_text)
