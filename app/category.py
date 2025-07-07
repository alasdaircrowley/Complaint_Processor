import openai
import re
from openai import OpenAIError
from .config import OPENAI_API_KEY
from .config import PROXY_URL
import httpx

proxy_client = httpx.AsyncClient(proxy="your_proxy") # Прокси может быть установлен так же через .env-file
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY, http_client=proxy_client)

async def classify_category(text: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Ты — ИИ, который определяет тип жалобы. Всегда выбирай одно из слов: техническая, оплата, другое. Ответ только одним словом."
                },
                {
                    "role": "user",
                    "content": f'Определи категорию жалобы: "{text}".'
                }
            ],
            temperature=0
        )

        raw = response.choices[0].message.content
        print("GPT raw category:", raw)

        clean = re.sub(r"[^\wа-яё]+", "", raw.strip().lower())
        print("GPT cleaned category:", clean)

        return clean if clean in ["техническая", "оплата"] else "другое"

    except OpenAIError as e:
        print("OpenAI error:", e)
        return "другое"
