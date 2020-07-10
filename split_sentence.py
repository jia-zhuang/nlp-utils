import re
# 将 content_field 的段落拆成句子
SPLIT_PATTERN = re.compile(r'(。|！|？?!)')
def split_text_to_sentences(text, max_seq_length=192):
    res = []
    if isinstance(text, str):
        sentences = SPLIT_PATTERN.split(text)
        for i in range(len(sentences) // 2):
            sent = sentences[2*i] + sentences[2*i + 1]
            res.append(sent.strip()[:max_seq_length])
    return res
