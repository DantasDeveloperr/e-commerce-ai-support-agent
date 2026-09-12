# E-commerce AI Support Agent

Agente de atendimento para e-commerce baseado em **Large Language Models (LLMs)**, desenvolvido em Python.

O projeto simula um agente capaz de interpretar solicitações de clientes, consultar informações de pedidos e recuperar informações relevantes de uma base de conhecimento para auxiliar no atendimento.

## Objetivo

O objetivo do projeto é desenvolver, de forma incremental, um agente de IA para atendimento ao cliente em um cenário de e-commerce.

Durante o desenvolvimento, são explorados conceitos e tecnologias relacionados a:

* Large Language Models (LLMs)
* Agentes de IA
* Embeddings
* Busca semântica
* RAG (Retrieval-Augmented Generation)
* Análise exploratória de dados (EDA)
* Avaliação de modelos de IA
* Machine Learning

## Funcionalidades atuais

* Atendimento conversacional via terminal
* Consulta de pedidos
* Identificação de pedidos pelo número
* Consulta de status, transportadora, código de rastreamento e previsão de entrega
* Base de conhecimento em arquivos `.txt`
* Busca de informações utilizando embeddings
* Busca semântica baseada em similaridade por cosseno
* Integração com modelos Gemini

## Tecnologias

* Python
* Google Gemini API
* Gemini Embeddings
* Pandas
* NumPy
* Git e GitHub

## Estrutura do projeto

```text
e-commerce-ai-support-agent/
├── data/
│   └── orders.csv
├── knowledge_base/
│   ├── entrega.txt
│   └── trocas.txt
├── notebooks/
├── src/
│   ├── agent.py
│   ├── data_loader.py
│   ├── embedding_client.py
│   ├── gemini_client.py
│   ├── knowledge_loader.py
│   ├── main.py
│   ├── semantic_search.py
│   └── vector_search.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Próximos passos

* Integrar a busca semântica ao agente
* Implementar um fluxo completo de RAG
* Melhorar a recuperação de contexto
* Registrar conversas e interações
* Analisar os dados utilizando Pandas
* Criar métricas para avaliação das respostas
* Realizar análise exploratória dos dados
* Documentar experimentos e resultados

## Status

🚧 Em desenvolvimento
