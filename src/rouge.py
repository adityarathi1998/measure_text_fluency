
import os,sys
import time
import itertools

def _split_into_words(sentences):
  # print(sentences)
  """Create list of words from given list of sentences"""
  words = list()
  for tok in sentences:
    lines = tok.split(" ")
    words = [*words,*lines]
  
  # print(len(words))
  # print(words)
  return words

def _get_word_ngrams(n,len_of_sent, sentences):
  """Calculates word n-grams for multiple sentences.
  """
  if len_of_sent <= 0:
    print("Len of sentence is invalid")
  if n <= 0:
    print("N is invalid")

  words = _split_into_words(sentences)
  len_of_text = len(words)
  return _get_ngrams(n, words, len_of_text)

#supporting function
def _get_ngrams(n, text, len_of_text):
  """Calcualtes n-grams.
  Args:
    n: which n-grams to calculate
    text: An array of tokens
  Returns:
    A set of n-grams
  """
  ngram_set = set()
  # text_length = len(text)
  max_index_ngram_start = len_of_text - n
  for i in range(max_index_ngram_start + 1):
    ngram_set.add(tuple(text[i:i + n]))
  return ngram_set

def rouge_n(reference_sentences, evaluated_sentences, n=2):
  """
  Computes ROUGE-N of two text collections of sentences.
  
  Args:
    evaluated_sentences: The sentences that have been picked by the summarizer
    reference_sentences: The sentences from the referene set
    n: Size of ngram.  Defaults to 2.
  Returns:
    recall rouge score(float)
  Raises:
    ValueError: raises exception if a param has len <= 0
  """
  len_of_eval_sent = len(evaluated_sentences)
  len_of_ref_sent = len(reference_sentences)

  assert len_of_eval_sent > 0 , "Length of evaluated sentences is less 0."
  assert len_of_ref_sent  > 0 , "Length of reference sentences is less 0."


  # if len_of_eval_sent <= 0 or len_of_ref_sent <= 0:
  #   raise ValueError("Collections must contain at least 1 sentence.")

  evaluated_ngrams = _get_word_ngrams(n, len_of_eval_sent, evaluated_sentences)
  reference_ngrams = _get_word_ngrams(n, len_of_ref_sent, reference_sentences)
  reference_count = len(reference_ngrams)
  evaluated_count = len(evaluated_ngrams)

  # Gets the overlapping ngrams between evaluated and reference
  overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
  overlapping_count = len(overlapping_ngrams)

  # Handle edge case. This isn't mathematically correct, but it's good enough
  if evaluated_count == 0:
    precision = 0.0
  else:
    precision = overlapping_count / evaluated_count

  if reference_count == 0:
    recall = 0.0
  else:
    recall = overlapping_count / reference_count
  num1 = (precision * recall)
  den1 = (precision + recall + 1e-8)
  f1_score = 2.0 * ( num1 / den1)

  #just returning recall count in rouge, useful for our purpose
  return f1_score,recall


###############################
def main():
  ar = sys.argv[1:]
  # print(ar)
  ref_file_path = ar[0]
  gen_file_path = ar[1]

  file_ref = open(ref_file_path, 'r')
  ref = file_ref.readlines()

  file_gen = open(gen_file_path, 'r')
  gen = file_gen.readlines()

  for i,l in enumerate(gen):
      gen[i] = l.strip()

  for i,l in enumerate(ref):
      ref[i] = l.strip()


  # ref = 'When I was in my 20s, I saw my very first psychotherapy client.'
  # can = 'When I had twenty, I saw my first customers like a psychotherapist.'
  start = time.time()
  _,rouge_score = rouge_n(ref, gen, n=2)
  end = time.time()
  print("Time taken: ", end-start)
  print("Rouge Score: ", rouge_score)

if __name__ == "__main__":
  main()