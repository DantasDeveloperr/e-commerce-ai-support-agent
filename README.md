# E-commerce AI Support Agent

Agente de atendimento para e-commerce desenvolvido em Python utilizando Large Language Models (LLMs), busca semântica e RAG (Retrieval-Augmented Generation).

O projeto simula um agente de suporte capaz de responder dúvidas de clientes, consultar pedidos e utilizar uma base de conhecimento para gerar respostas contextualizadas.

## Objetivo

O objetivo do projeto é explorar, de forma prática, conceitos relacionados a:

* Large Language Models (LLMs)
* Agentes de IA
* RAG (Retrieval-Augmented Generation)
* Embeddings
* Busca semântica
* Processamento e análise de dados
* Avaliação de sistemas baseados em LLMs
* Testes automatizados

## Funcionalidades

### Atendimento com LLM

O agente utiliza o modelo Gemini para gerar respostas em linguagem natural.

### Consulta de pedidos

O sistema permite consultar pedidos a partir do número informado pelo cliente.

Exemplo:

```text
Cliente: Onde está meu pedido?

Agente: Claro! Para consultar seu pedido, poderia me informar o número do pedido?

Cliente: 1001
```

Os dados dos pedidos são armazenados em `data/orders.csv` e carregados utilizando Pandas.

### Base de conhecimento

O projeto possui uma base de conhecimento contendo informações sobre:

* Entrega
* Trocas de produtos

Os documentos estão armazenados no diretório `knowledge_base/`.

### Busca semântica

Os documentos da base de conhecimento são transformados em embeddings.

Para uma nova pergunta:

1. A pergunta é transformada em embedding.
2. O sistema calcula a similaridade entre a pergunta e os documentos.
3. Os documentos são ordenados por relevância.
4. Um limiar mínimo de similaridade é utilizado para evitar recuperação de conteúdo pouco relevante.
5. O contexto mais relevante é enviado ao LLM.

### RAG

O contexto recuperado pela busca semântica é utilizado para orientar a resposta do Gemini.

O agente recebe instruções para utilizar somente as informações presentes no contexto recuperado e evitar a criação de políticas, prazos ou procedimentos que não estejam na base de conhecimento.

### Registro das conversas

As interações são armazenadas em:

```text
data/conversation_logs.csv
```

Os registros incluem informações como:

* Pergunta do usuário
* Resposta do agente
* Fonte recuperada
* Score de relevância
* Timestamp

### Análise dos logs

O projeto possui uma rotina de análise utilizando Pandas para obter métricas sobre as interações registradas.

Entre as métricas analisadas estão:

* Número total de interações
* Taxa de recuperação de contexto
* Similaridade média
* Similaridade mínima e máxima
* Distribuição das fontes recuperadas

## Avaliação

O projeto possui um conjunto inicial de 10 perguntas para avaliar o comportamento da busca semântica e das respostas.

A avaliação de recuperação apresentou:

* 10/10 perguntas com a fonte esperada recuperada
* 4/4 consultas relacionadas a entrega
* 4/4 consultas relacionadas a trocas
* 2/2 consultas fora do escopo corretamente identificadas

As respostas também foram avaliadas utilizando critérios definidos para cada categoria.

Nesse conjunto inicial:

* 100% das respostas foram não vazias
* 100% de cobertura dos critérios definidos
* 100% de comportamento esperado nas consultas fora do escopo

> Observação: os resultados acima correspondem a um conjunto inicial de 10 consultas e a critérios específicos de avaliação. Eles não representam uma medida geral de precisão ou qualidade do sistema.

Os resultados das avaliações são armazenados em:

```text
data/retrieval_evaluation_results.csv
data/response_evaluation_results.csv
data/response_quality_results.csv
```

## Testes automatizados

O projeto utiliza `pytest` para testar componentes importantes da aplicação.

Atualmente existem 8 testes automatizados:

* 2 testes para carregamento e consulta de pedidos
* 3 testes para busca semântica
* 3 testes para o agente

Execução:

```powershell
python -m pytest
```

Resultado atual:

```text
8 passed
```

## Tecnologias

* Python 3.13
* Google Gemini
* Google GenAI
* Pandas
* NumPy
* pytest
* Embeddings
* RAG
* Git
* GitHub

## Estrutura do projeto

```text
e-commerce-ai-support-agent/
│
├── data/
│   ├── orders.csv
│   ├── knowledge_embeddings.json
│   ├── conversation_logs.csv
│   ├── evaluation_dataset.csv
│   ├── retrieval_evaluation_results.csv
│   ├── response_evaluation_results.csv
│   └── response_quality_results.csv
│
├── knowledge_base/
│   ├── entrega.txt
│   └── trocas.txt
│
├── src/
│   ├── agent.py
│   ├── analyze_evaluation.py
│   ├── analyze_logs.py
│   ├── conversation_logger.py
│   ├── data_loader.py
│   ├── embedding_client.py
│   ├── evaluate_response_quality.py
│   ├── evaluate_responses.py
│   ├── evaluate_retrieval.py
│   ├── gemini_client.py
│   ├── list_models.py
│   ├── main.py
│   ├── semantic_search.py
│   └── vector_search.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_data_loader.py
│   └── test_semantic_search.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/DantasDeveloperr/e-commerce-ai-support-agent.git
cd e-commerce-ai-support-agent
```

### 2. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Configurar a API do Gemini

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave não deve ser adicionada ao Git.

### 5. Executar o agente

```powershell
python src/main.py
```

### 6. Executar os testes

```powershell
python -m pytest
```

## Próximos passos

Possíveis evoluções do projeto:

* Melhorar a estratégia de avaliação das respostas
* Utilizar mocks para evitar chamadas reais ao LLM durante testes automatizados
* Expandir a base de conhecimento
* Melhorar o gerenciamento de contexto da conversa
* Adicionar novas ferramentas ao agente
* Desenvolver uma interface web
* Explorar arquiteturas multiagente

## Status

🚧 V1 funcional em desenvolvimento contínuo.

O projeto já possui integração com LLM, consulta de pedidos, embeddings, busca semântica, RAG, registro de conversas, avaliação e testes automatizados.
