files = [
    "C:/Users/omoch/Downloads/AI_cahtbot/whitepaper_3.txt",
    "C:/Users/omoch/Downloads/AI_cahtbot/whitepaper_4.txt",
    "C:/Users/omoch/Downloads/AI_cahtbot/whitepaper_5.txt"
    ]
output_file = "C:/Users/omoch/Downloads/AI_cahtbot/soumu_whitepaper.txt"

with open(output_file, "w", encoding="utf-8") as out_f:
    for file in files:
        with open(file, "r", encoding="utf-8") as in_f:
            out_f.write(in_f.read())
            out_f.write("\n") # セクションの区切りの改行

print(f"結合完了")