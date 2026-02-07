# Dashboard Analytics

Browser
↓
Django (views + templates + static files)
↓
Oracle Database

Características da implementação:

- Django como servidor web
- Backend e frontend no mesmo projeto
- Frontend estático (HTML, CSS, JS)
- Conexão direta com Oracle Database
- Queries SQL executadas manualmente
- Sem uso de ORM
- Deploy simples por cliente
- Configuração via variáveis de ambiente

---

## Evolução futura (planejada)

O projeto foi estruturado para permitir evolução gradual para uma arquitetura desacoplada:

Frontend (React / Next / Vue)
↓
Django REST API
↓
Oracle Database

Possíveis melhorias futuras:

- Django REST Framework
- API RESTful
- Frontend SPA
- Containerização (Docker)
- Gateway API
- Autenticação centralizada
- Cache (Redis)
- Filas (Celery / RabbitMQ)
- Observabilidade e logging estruturado

---

## Tecnologias utilizadas

### Backend
- Python
- Django
- oracledb

### Frontend
- HTML
- CSS
- JavaScript

### Infraestrutura
- Servidor Linux ou Windows
- Ambiente virtual Python
- Domínio válido (recomendado)

---

## Requisitos do sistema

Para executar o projeto em um servidor cliente:

### Software necessário

- Python 3.10+
- pip
- virtualenv (recomendado)
- acesso ao Oracle Database
- Oracle Client (quando necessário)

Opcional:

- Nginx
- Apache
- Gunicorn

---

## Infraestrutura mínima

O projeto foi desenhado para rodar com infraestrutura mínima:

- 1 servidor para executar a aplicação Django
- acesso ao banco Oracle
- domínio válido (recomendado)

Exemplo:

Cliente Server
├─ Django App
└─ Oracle Database

Ou:

Nginx → Django → Oracle DB

---

## Instalação

### 1. Clonar o repositório

```bash
git clone <repo>
cd <repo>
