# Análise de Dados de Mercado de Trabalho para Orientação Profissional

## Extração (E):
- **Fontes de dados**: Portais de emprego (Indeed, Vagas, LinkedIn), dados abertos do governo sobre mercado de trabalho (CAGED, RAIS), pesquisas salariais, informações sobre cursos e formações profissionais.
- **Técnicas**: Web scraping, APIs de acesso a portais de emprego, download de arquivos CSV ou JSON, processamento de linguagem natural (PLN).
- **Python**: BeautifulSoup, Scrapy, requests, NLTK, spaCy, bibliotecas específicas para cada portal de emprego.

## Transformação (T):
- **Limpeza**: Remoção de stop words, caracteres especiais, formatação de texto, identificação e correção de erros ortográficos, padronização de descrições de cargos e habilidades.
- **Pré-processamento**: Tokenização, lematização/stemming, identificação de entidades nomeadas (NER), extração de habilidades e requisitos de vagas.
- **Feature Engineering**: Criação de embeddings de palavras (Word2Vec, GloVe, BERT), representação de texto (TF-IDF, bag-of-words), classificação de vagas por área de atuação, nível de experiência e habilidades requeridas, análise de tendências de mercado e salários.
- **Python**: NLTK, spaCy, Gensim, scikit-learn, TensorFlow, Keras, PyTorch, Hugging Face Transformers.

## Carregamento (L):
- **Bancos de dados**: Elasticsearch, Apache Solr, MongoDB com Atlas Search, Neo4j (para análise de grafos de habilidades e relações entre profissões).
- **Técnicas**: Indexação e busca de texto completo, suporte a consultas complexas, armazenamento de documentos estruturados e não estruturados, análise de grafos.
- **Python**: Elasticsearch client, PySolr, PyMongo, Neo4j driver.

## IA:
- **Modelos**: Recomendação de vagas e cursos com base em perfil do usuário, classificação de currículos e perfis de candidatos, modelos de matching entre candidatos e vagas, análise de tendências de mercado e salários, previsão de demanda por habilidades e profissões.
- **Python**: scikit-learn, TensorFlow, Keras, PyTorch, Surprise, NetworkX.

## Análise comparativa:
- **Cenário 1**: Carregamento em lote em um banco de dados relacional (PostgreSQL, MySQL) com extensão para busca de texto completo.
- **Cenário 2**: Carregamento em um motor de busca especializado (Elasticsearch, Solr) ou em um banco de dados de grafos (Neo4j).
- **Métricas**: Tempo de carregamento, tempo de processamento, custo de armazenamento, escalabilidade, relevância dos resultados de busca, capacidade de análise de redes e recomendações personalizadas.

## Arquivo CSV auxiliar:
- `job_postings.csv` (job_id, title, description, company, location, salary, skills, experience_level)
