import re

# 長文を3文単位でチャンクに分ける機能を提供するモジュール

# 改行、空白を統一する
def preprocess_text(text):
    text = text.replace("\u3000", " ")            # 全角スペースを半角に
    text = re.sub(r'[\r\n]+', ' ', text)          # 改行文字（\n, \r）をスペースに
    text = re.sub(r'\s+', ' ', text)              # 連続スペースを1つに
    return text.strip()


# 文ごとに分割する
def sentence_split(text):
    sentence = re.split(r'(?<=[。])', text)
    return [s.strip() for s in sentence if s.strip()]

# 5文ずつまとめて1チャンクにする
def chunk_by_sentences(text, chunk_size=5):
    sentences = sentence_split(text)
    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = "".join(sentences[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

# テキストファイルを読み込んでチャンクに変換する
def load_and_split_text(file_path, chunk_size=5):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = preprocess_text(text)
    return chunk_by_sentences(text, chunk_size,)