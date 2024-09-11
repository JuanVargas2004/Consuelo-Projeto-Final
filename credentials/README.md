# Configuração de Credenciais AWS

Este projeto utiliza a AWS (Amazon Web Services) para acessar o serviço S3, onde armazenamos e recuperamos arquivos. Para rodar o projeto, você precisará configurar suas próprias credenciais da AWS.

## Passos para Configurar as Credenciais

### 1. Criar Conta na AWS
Se você ainda não tem uma conta AWS, siga os passos abaixo:
1. Acesse [aws.amazon.com](https://aws.amazon.com).
2. Crie uma conta preenchendo as informações solicitadas.
3. Após criar a conta, faça login no **Console da AWS**.

### 2. Gerar Credenciais (Access Key e Secret Key)
Para gerar suas chaves de acesso (Access Key ID e Secret Access Key):
1. No console da AWS, clique no seu nome de usuário no canto superior direito e selecione **Minhas credenciais de segurança**.
2. Role para baixo até **Chaves de acesso** e clique em **Criar nova chave de acesso**.
3. Salve as chaves geradas (Access Key ID e Secret Access Key) em um local seguro, pois você usará essas informações mais tarde.

### 3. Criar o Arquivo `.env`

Crie um arquivo chamado **`.env`** na pasta `credentials/`. Este arquivo será utilizado para armazenar suas credenciais de forma segura e evitar que elas sejam comitadas no repositório.

#### Estrutura do arquivo `.env`:
No arquivo `.env`, adicione as credenciais da AWS no seguinte formato:

```ini
AWS_ACCESS_KEY_ID=seu_id_de_acesso
AWS_SECRET_ACCESS_KEY=sua_chave_secreta_de_acesso
