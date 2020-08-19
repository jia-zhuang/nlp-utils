import re
import math
# 将 content_field 的段落拆成句子
SPLIT_PATTERN = re.compile(r'(。|！|？?!)')
def split_text_to_sentences(text, max_seq_length=192):
    res = []
    if isinstance(text, str):
        sentences = SPLIT_PATTERN.split(text)
        for i in range(math.ceil(len(sentences) / 2)):
            sent = ''.join(sentences[(2*i):(2*i + 2)])
            if sent:
                res.append(sent.strip()[:max_seq_length])
    return res
