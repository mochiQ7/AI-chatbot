import pickle
import faiss
import numpy as np
from embedding import get_embedding

# ユーザーの質問をベクトルに変換し、FAISSを使って似たチャンクを検索するスクリプト

#(チャンク, ベクトル)
with open('C:/Users/omoch/Downloads/AI_cahtbot/embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)


# ベクトルだけ取り出して、numpy配列に変換
vectors = np.array([vec for _, vec in embeddings]).astype('float32')

# FAISSインデックスを作成(内積ベース:Dot Product)
# 意味が近いベクトルほどスコアが高くなる
index = faiss.IndexFlatIP(vectors.shape[1]) # ベクトル検索用のインデックス
index.add(vectors)

# チャンクとの紐付け用リスト
# 元のテキストも保存→ここから文章を取り出す
chunk_texts = [chunk for chunk, _ in embeddings]

# 検索関数
def search(query, top_k=3): # query(質問文)をベクトルにして、似ている文章をtop_k件(3件)返す

    query_vector = get_embedding(query).astype('float32').reshape(1, -1) # 入力されたqueryをベクトルに変換
    D, I = index.search(query_vector, top_k) # FAISSで検索　D:類似度, I:一番近いチャンクのインデックス一覧

    return [chunk_texts[i] for i in I[0]] # 類似度の高い上位のtop_k件の文章を返す


if __name__ == "__main__":
    results = search("日本のAI政策の動向について教えて", top_k=3)
    for i, res in enumerate(results):
        print(f"\n🔍 Top {i+1}:\n{res}")


