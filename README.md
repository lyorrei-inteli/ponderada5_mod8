# Chatbot de Normas de Segurança - LLM

## Objetivo
Desenvolver um chatbot utilizando Large Language Models (LLM) para auxiliar na pesquisa de normas de segurança em ambientes industriais com contexto.

## Enunciado
Este projeto envolve a criação de um chatbot utilizando um LLM (Local ou API externa), com o objetivo de fornecer respostas claras e sucintas sobre normas de segurança industrial. O sistema inclui uma interface gráfica para facilitar a interação do usuário e um arquivo safety_expert.txt que fornece contexto para o LLM.

### Exemplo de Uso
Usuário: "what are the rules of a workshop?"<br/>
Chatbot: "The rules of a workshop include wearing correct protective equipment, reporting any health conditions that may affect safety, not allowing food or drink in the workshop, using tools only if you have been inducted and tested for capability, checking faulty or broken equipment with the workshop supervisor, keeping work areas tidy and free from leads, avoiding talking to anyone operating electrical equipment, using safety glasses at all times, reporting any accidents or cuts, and not engaging in practical jokes or fooling around."

## Instalação e Execução

### Pré-requisitos
- Python 3
- Ollama

### Configurando o Ambiente Virtual

É recomendado usar um ambiente virtual para instalar e executar o chatbot. Siga os passos abaixo para configurar o ambiente:

1. Crie um ambiente virtual:
    ```bash
    python3 -m venv .venv
    ```

2. Ative o ambiente virtual:

    - No Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
    - No Linux ou macOS:
        ```bash
        source .venv/bin/activate
        ```

3. Instale as dependências utilizando o arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Chatbot

Após configurar o ambiente e instalar as dependências, execute o script `llm.py` para iniciar o chatbot:

```bash
python3 llm.py
```

O chatbot estará disponível localmente em `http://localhost:11434`.

## Demonstração no Youtube
https://youtu.be/Iln8vNTDoV4
