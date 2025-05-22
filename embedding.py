from transformers import AutoTokenizer, AutoModel
import torch

# ひとつの文章を埋め込みベクトル(数値の配列)に変換するモジュール

# モデル
model_name = "BAAI/bge-m3"

# モデルとトークナイザーのロード
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 埋め込み取得関数
def get_embedding(text, model=model, tokenizer=tokenizer):
    # "passage:" のprefixが重要
    text = "passage: " + text

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = model(**inputs)

    # 平均プーリング
    embeddings = output.last_hidden_state
    attention_mask = inputs['attention_mask']
    mask = attention_mask.unsqueeze(-1).expand(embeddings.size()).float()
    masked_embeddings = embeddings * mask
    summed = torch.sum(masked_embeddings, 1)
    counts = torch.clamp(mask.sum(1), min = 1e-9)
    mean_pooled = summed/ counts

    return mean_pooled[0].numpy()

