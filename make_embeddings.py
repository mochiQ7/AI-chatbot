from splitter import load_and_split_text
from embedding import get_embedding
import pickle
import os

# 全文をチャンクに分けて、全部をベクトル化して保存する

# テキストのパス
file_path = "C:/Users/omoch/Downloads/AI_cahtbot/soumu_whitepaper.txt"
save_path = "C:/Users/omoch/Downloads/AI_cahtbot/embeddings.pkl"

# チャンク作成前に、テキスト中身を少しだけ出力
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()


# チャンクを作成
chunks = load_and_split_text(file_path)
print(f"チャンク数: {len(chunks)}")

print("✅ テキスト一部（改行・空白チェック）:")
print(repr(chunks[0]))  # repr を使うと不可視文字が見える！

# チャンクごとにベクトル化
embeddings = []
for chunk in chunks:
    vec = get_embedding(chunk)
    embeddings.append((chunk, vec))

# 保存
# 保存
with open(save_path, "wb") as f:
    pickle.dump(embeddings, f)

print(f"{len(embeddings)}件の埋め込みを保存しました!")
print("✅ 最初のチャンク:", repr(embeddings[0][0]))
print("✅ 保存先:", os.path.abspath(save_path))
