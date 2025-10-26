import streamlit as st
from openai import OpenAI

# StreamlitのSecretsからAPIキーを取得
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# prompt:GPTに送る質問文
def generate_answer(context, question):
    prompt = f"""
以下の情報をもとに、質問に対して簡潔に答えてください

【情報】
{context}

【質問】
{question}

【回答】
"""
    # promptをGPTに送信
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # GPTの返事を取り出す
    return response.choices[0].message.content

# テスト実行
if __name__ == "__main__":
    from faiss_search import search

    while True:
        question = input("\n 😼質問をどうぞ！(終了するには、exitと入力)")
        if question.lower() == "exit":
            print("終了します。お疲れ様！😼")
            break

        chunks = search(question)
        context = "\n".join(chunks) # 検索結果をひとつの文字列にまとめる
    
        answer = generate_answer(context, question)
        print("回答:\n", answer)