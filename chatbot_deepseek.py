import os
import requests

# 配置 DeepSeek API（官方接口）
DEEPSEEK_API_KEY = "sk-1c8aaef2d52743879acb52b059e7a21a"
API_BASE_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL_NAME = "deepseek-chat"

def deepseek_chat(user_message: str) -> str:
    os.environ['NO_PROXY'] = '*'  # 绕过系统代理
    
    if not DEEPSEEK_API_KEY:
        return "错误：请先配置有效的DeepSeek API Key！"
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(
            API_BASE_URL,
            headers=headers,
            json=payload,
            timeout=30,
            proxies={"http": None, "https": None}
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.Timeout:
        return "错误：请求超时，请检查网络或稍后重试！"
    except requests.exceptions.RequestException as e:
        return f"请求失败：{str(e)}"
    except KeyError:
        return f"响应解析失败：{response.text}"

def interactive_chat():
    print("=== DeepSeek Chatbot 启动成功（输入 'quit' 退出）===")
    while True:
        user_input = input("你：").strip()
        if user_input.lower() in ["quit", "exit", "退出"]:
            print("Chatbot：再见！")
            break
        if not user_input:
            print("Chatbot：请输入有效内容！")
            continue
        print("Chatbot：正在思考...")
        answer = deepseek_chat(user_input)
        print(f"Chatbot：{answer}\n")

if __name__ == "__main__":
    interactive_chat()