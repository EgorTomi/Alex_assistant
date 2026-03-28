import requests
def Ai_responce():
    API_KEY = "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"  # ключ OpenRouter


    url = "https://openrouter.ai/api/v1/chat/completions"



    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # необязательно:
        # "HTTP-Referer": "https://your-site.com",
        # "X-Title": "My Test Bot",
    }

    data = {
        "model": "openrouter/free",
        "messages": [
            {"role": "system", "content": "Ты полезный помощник, который кратно отвечает на вопросы."},
            {"role": "user", "content": "ответь мне"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()

        result = response.json()
        print(result["choices"][0]["message"]["content"])
        print("Какая модель ответила:", result.get("model"))

    except requests.exceptions.HTTPError:
        print("HTTP ошибка:", response.status_code)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)

    except KeyError:
        print("Неожиданный формат ответа:")
        print(response.text)