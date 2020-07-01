'''
将句子中的中文和英文分开，使用huggingface/tokenizers

https://github.com/huggingface/tokenizers/blob/master/bindings/python/tests/bindings/test_normalizers.py
'''

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.normalizers import BertNormalizer

text = "薛定谔的猫（英文名称：Erwin Schrödinger's Cat）是奥地利著名物理学家薛定谔"

tokenizer = Tokenizer(BPE())
tokenizer.normalizer = BertNormalizer(
    strip_accents=False, lowercase=False, handle_chinese_chars=True, clean_text=False
)

output = tokenizer.normalize(txt)
print(output)
