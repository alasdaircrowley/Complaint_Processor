# 📊 Customer Complaint Processing System

Проект предназначен для обработки клиентских жалоб с помощью FastAPI, SQLite, анализа тональности, автоматической классификации по категориям, и интеграции с n8n для автоматизации уведомлений.

---

## 🚀 Функционал

* REST API для создания и просмотра жалоб
* Автоматический анализ тональности текста (Sentiment Analysis) через `transformers`
* Классификация жалобы в одну из категорий: `техническая`, `оплата`, `другое`
* Хранение данных в SQLite
* n8n-интеграция для:

  * уведомления в Telegram по техническим жалобам
  * запись жалоб об оплате в Google Sheets
  * автоматическое закрытие жалоб

---

## 🌐 Технологии

* Python 3.12+
* FastAPI
* SQLite (через SQLAlchemy)
* Hugging Face `transformers` (анализ тональности)
* OpenAI или Together AI (категоризация текста)
* n8n (автоматизация)

---

## 🛠️ Установка

```bash
git clone https://github.com/yourusername/customer-complaints.git
cd customer-complaints
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создайте файл `.env` в корне проекта:

```ini
OPENAI_API_KEY=sk-...
TOGETHER_API_KEY=your_together_key (если используете)
DATABASE_URL=sqlite:///./complaints.db
PROXY_URL=http://yourproxy:port (если нужно)
```

---

## 🚧 Запуск

```bash
uvicorn app.main:app --reload
```

---

## 📄 Примеры API-запросов

### ✉️ Создание жалобы

```bash
curl -X POST http://localhost:8000/complaints \
-H "Content-Type: application/json" \
-d '{"text": "Сайт не работает, ошибка 500"}'
```

### 📊 Получение всех жалоб

```bash
curl http://localhost:8000/complaints
```

---

## 🪜 Структура проекта

```
report_processor/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── sentiment.py
│   ├── category.py
│   └── config.py
├── requirements.txt
├── .env
└── n8n/workflow.json
```

---

## 🌊 n8n-интеграция

В `n8n/workflow.json` содержится экспорт готового workflow:

* каждый час запрашивает API `/complaints`
* фильтрует только `status=open` и `timestamp` за последний час
* для жалоб `техническая` → отправляет в Telegram
* для `оплата` → добавляет строку в Google Sheets
* все обработанные → меняет статус на `closed`

Для работы требуется:

* подключение Telegram-бота через BotFather и указание Chat ID
* OAuth2-подключение Google Sheets через сервисный аккаунт

---

## 📊 Пример модели в базе данных

```json
{
  "id": 1,
  "text": "Не приходит SMS-код",
  "status": "open",
  "timestamp": "2025-07-06T12:33:48",
  "sentiment": "negative",
  "category": "техническая"
}
```

---

## 📊 Зависимости

Файл `requirements.txt` содержит:

```
fastapi
uvicorn
sqlalchemy
transformers
torch
httpx
python-dotenv
openai
```

---

## 🔧 TODO / Дополнительно
* [ ] Docker-обёртка
