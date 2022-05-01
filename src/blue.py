from collections import Counter
import numpy as np
import nltk.translate.bleu_score as nltk_bleu_impl
import warnings
warnings.filterwarnings("ignore")

lower_n_split = lambda x: x.lower().split()

def make_ngrams(sentence, n):
    words = lower_n_split(sentence)
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(" ".join(words[i:i+n]))
    return ngrams

def modified_precision(ca, refs, n):
    ngrams = make_ngrams(ca, n)
    ngram_counts = Counter(ngrams)
    total_count = 0
    for ngram in set(ngrams):
        max_count = 0
        for ref in refs:
            max_count = max(max_count, Counter(make_ngrams(ref, n)).get(ngram, 0))
        total_count += min(max_count, ngram_counts[ngram])
    return total_count / len(ngrams)

# To penalize for very short length candidate sentences.
def brevity_penalty(ca, refs):
    ca_len = len(ca)
    if ca_len == 0:
        return 0
    cleaned_refs = (lower_n_split(ref) for ref in refs)
    ref_lens = (len(ref) for ref in cleaned_refs)
    closest_ref_len = min(ref_lens, key=lambda ref_len: abs(ca_len - ref_len))
    return 1 if ca_len > closest_ref_len else np.exp(1 - closest_ref_len / ca_len)

def bleu_helper(ca, refs, weights, n_start, n_end):
    assert n_end >= n_start > 0
    bp = brevity_penalty(ca, refs)
    p_n = [modified_precision(ca, refs, n) for n in range(n_start, n_end + 1)]
    res = 0
    try:
        res = bp * np.exp(sum([w * np.log(p) for w, p in zip(weights, p_n)]))
        return res
    except:
        return res

def nltk_bleu(ca, refs, weights):
    res = 0
    try:
        res = nltk_bleu_impl.sentence_bleu(list(map(lambda ref: lower_n_split(ref), refs)), lower_n_split(ca), weights = weights)
        return res
    except:
        return res

def bleu(candidate, reference):
    ref = []
    ref.append(reference)

    n_val = 4
    weights = [1/n_val] * n_val

    result_scratch = bleu_helper(candidate, ref, weights, 1, n_val)
    result_nltk = nltk_bleu(candidate, ref, weights)

    return(result_scratch, result_nltk)