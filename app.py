import streamlit as st
import datetime
from faiss_search import search
from generate_answer import generate_answer




# 設定
st.set_page_config(page_title="AIチャットボット", layout="centered")
st.title("🤖 情報通信白書のAI ChatBot🔍")
st.markdown("生成AI・AI政策に関する質問をどうぞ！😼(※１日５回まで)")

# 定数定義
USER = "😺"
ASSISTANT = "🤖"

# セッションステート初期化
today = datetime.date.today().isoformat() # 日付でリセットするためのキー

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

if "usage" not in st.session_state or st.session_state.usage.get("date") != today:
    st.session_state.usage = {"date": today, "count": 0}

# チャット表示
for chat in st.session_state.chat_log:
    with st.chat_message(chat["role"], avatar=USER if chat["role"] == "user" else ASSISTANT):
        st.markdown(chat["content"])
        if chat.get("chunks"):
            with st.expander("🔍 参照されたチャンク（検索結果）"):
                for i, chunk in enumerate(chat["chunks"]):
                    st.markdown(f"**Top {i+1}**:\n{chunk}")

# 質問入力
if st.session_state.usage["count"] >= 5:
    st.warning("本日の利用回数制限に達しました😿")
else:
    question = st.chat_input("❓ 質問を入力してください")
    if question:
        # ユーザーの発言の保存
        st.session_state.chat_log.append({"role": "user", "content": question})
        with st.chat_message("user", avatar=USER):
            st.markdown(question)

        with st.spinner("検索中..."):
            chunks = search(question)
            context = "\n".join(chunks)

        with st.spinner("回答を生成中..."):
            answer = generate_answer(context, question)

        # アシスタント発言の保存(チャンク付き)
        st.session_state.chat_log.append({
            "role": "assistant",
            "content": answer,
            "chunks": chunks
        })

        with st.chat_message("assistant", avatar=ASSISTANT):
            st.markdown(answer)
            with st.expander("🔍 参照されたチャンク（検索結果）"):
                for i, chunk in enumerate(chunks):
                    st.markdown(f"**Top {i+1}**:\n{chunk}")
        
        # 実行ブロックの中でカウント
        st.session_state.usage["count"] += 1


