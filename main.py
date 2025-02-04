from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Inicialize o modelo de linguagem com Hugging Face
model_name = "gpt2"  # Exemplo de modelo; você pode trocar por outro modelo
generator = pipeline('text-generation', model=model_name)

# Criação da aplicação FastAPI
app = FastAPI()

# Modelo de entrada para a requisição
class TextRequest(BaseModel):
    text: str

# Rota de geração de texto
@app.post("/generate")
async def generate_text(request: TextRequest):
    try:
        input_text = request.text
        # Gera o texto com base no modelo
        generated = generator(input_text, max_length=100, num_return_sequences=1)
        generated_text = generated[0]['generated_text']
        return {"generated_text": generated_text}
    
    except Exception as e:
        return {"error": str(e)}
    