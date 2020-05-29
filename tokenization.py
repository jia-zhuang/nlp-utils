'''
实现原始文本与tokenize后的文本的对齐功能
原理：通过映射

huggingface/tokenizers 已经实现了tokenize后的token对应原始文本的idx，
这里只要实现反过来的映射，即原始文本中每个char对应token的idx即可
'''


from tokenizers import BertWordPieceTokenizer


def get_char_token_indexes(offsets, sentence_len):
    '''获得一句话中所有 char 的 token_idx, 以数组形式返回'''
    token_indexes = [None] * sentence_len
    for i, offset in enumerate(offsets):
        start, end = offset
        token_indexes[start: end] = [i] * (end - start)
    
    return token_indexes


def get_token_span(span_token_indexes):
    '''寻找第一个和最后一个不为None的数, 返回一个有效区间'''
    i = 0
    while span_token_indexes[i] is None:
        i += 1
    start = span_token_indexes[i]
    
    i = -1
    while span_token_indexes[i] is None:
        i -= 1
    end = span_token_indexes[i]
    
    return start, end + 1  # [start, end)

