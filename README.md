# 🚀🤖　RAGチャットボット　-総務省　情報通信白書2023 対応
このリポジトリは、総務省「情報通信白書2023 (第一部 第三章~第五章)」を知識ベースとした、RAG構成のチャットボットです！
Streamlitで動作し、FAISSベースのベクトル検索＋生成AIによる回答を行います。

## 情報通信白書のAIチャットボット  
[🌐 アプリを試す](https://ai-chatbot-kefhgtbmroq76vbujaijtn.streamlit.app/)

## 🔧 構成
- 言語モデル：intfloat/multilingual-e5-small
- ベクトル検索：FAISS
- UI：Streamlit
- デプロイ：Streamlit Cloud
- 生成モデル：OpenAI GPT-3.5 API

## 💡機能概要
- 質問に対して関連文書をベクトル検索で取得
- 検索結果＋質問をもとにLLMで回答を生成(RAG)
- 検索チャンクの表示機能
- 利用回数制限(一日五回まで)
