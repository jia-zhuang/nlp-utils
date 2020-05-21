'''
实现原始文本与tokenize后的文本的对齐功能
原理：通过映射

huggingface/tokenizers 已经实现了tokenize后的token对应原始文本的idx，
这里只要实现反过来的映射，即原始文本中每个char对应token的idx即可
'''


from tokenizers import BertWordPieceTokenizer


def get_char_token_idx(offsets, sentence_len):
    '''获得 char 的 token_idx, 以数组形式返回'''
    token_idx = [None] * sentence_len
    for i, offset in enumerate(offsets):
        start, end = offset
        token_idx[start: end] = [i] * (end - start)
    
    return token_idx


def get_token_span(token_idx):
    '''寻找第一个和最后一个不为None的数'''
    i = 0
    while token_idx[i] is None:
        i += 1
    start = token_idx[i]
    
    i = -1
    while token_idx[i] is None:
        i -= 1
    end = token_idx[i]
    
    return start, end

