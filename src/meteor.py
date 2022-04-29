import collections
import itertools
from math import comb
from meteor_helper import Point, Line, count_intersections
from collections import defaultdict
from itertools import product, combinations

"""
    Calculate the harmonic mean.
    Input:
        - P : Unigram precision
        - R : Unigram Recall
    Output:
        - harmonic mean
"""
def calculate_harmonic_mean(P, R):
    if R == 0 or P ==0:
        return 0
    hm = (10*P*R)
    hm = hm/float(R + 9*P)
    return hm


"""
    Function to find the alignments.
    Input:
        - candidate_unigrams
        - reference_unigrams
    Output:
        - alignments
"""
def calculate_alignments(candidate_unigrams, reference_unigrams):
    reference_len = len(reference_unigrams)
    candidate_len = len(candidate_unigrams)

    mapping = defaultdict(list)

    for r,c in product(range(reference_len), range(candidate_len)):
        if candidate_unigrams[c] == reference_unigrams[r]:
            mapping[r].append(c)

    keys = tuple(mapping.keys())
    values = tuple(mapping.values())

    alignments = []

    for v in product(*values):
        per_alignment = []
        for item in list(dict(zip(keys, v)).items()):
            line = Line(Point(item[0],0), Point(item[1],1))
            per_alignment.append(line)
        alignments.append(per_alignment)

    return alignments

"""
    Function to calculate the # of chunks among the reference and candidate.
    Input:
        - candidate_unigrams
        - reference_unigrams
    Output:
        - chunks
        - mappings
"""
def calculate_chunks(candidate_unigrams, reference_unigrams):
    min_alignments = None
    alignments = calculate_alignments(candidate_unigrams, reference_unigrams)
    len_alignment_map = map(len, alignments)
    min_len = min(len_alignment_map)
    min_alignments = []
    for alignment in alignments:
        if min_len ==len(alignment):
            min_alignments.append(alignment)
    
    len_min_alignments = len(min_alignments)

    if len_min_alignments ==1:
        min_alignment = min_alignments[0]
    elif len_min_alignments ==0:
        return 0,0
    else:
        min_alignment = min(min_alignments, key=count_intersections)
    
    
    alignment_iter = iter(min_alignment)
    next(alignment_iter)

    chunks = 1  
    for prev, curr in zip(min_alignment, alignment_iter):
        if prev.point2.x + 1 != curr.point2.x:
            chunks +=1
    
    mappings = len(min_alignment)
    return chunks, mappings
    

"""
    Function to calculate the chunk penalty
    Input:
        - candidate_unigrams
        - reference_unigrams
    Output:
        - chunk penalty
"""
def calculate_chunk_penalty(candidate_unigrams, reference_unigrams):
    no_of_chunks, mappings = calculate_chunks(candidate_unigrams, reference_unigrams)
    # print("No_of_chunks:",no_of_chunks)
    candidate_unigrams_len = len(set(candidate_unigrams))
    # print("candidate_unigrams_len:",candidate_unigrams_len)
    chunk_penalty = 0.5*(no_of_chunks/candidate_unigrams_len)**3
    return chunk_penalty


"""
    Function to calculate the meteor score.
    Input:
        - f_score
        - penalty_val
    Output:
        - meteor score
"""
def calculate_meteor_score(f_score, penalty_val):
    meteor_score = f_score*(1-penalty_val)
    return meteor_score


"""
    Finds the unigram precision and recall
    Input:
        - candidate_unigrams
        - reference_unigrams
    Output:
        - Precision
        - Recall
"""
def calculate_unigram_precision_recall(candidate_unigrams, reference_unigrams):
    reference_set = set(reference_unigrams)
    candidate_set = set(candidate_unigrams)

    match = len(candidate_set.intersection(reference_set))
    # candidate unigram count
    wt = len(candidate_unigrams)
    # reference unigram count
    wr = len(reference_unigrams)

    # Find precision and recall
    recall_score = match/wr
    precision_score = match/wt

    return precision_score, recall_score
    

"""
    Function to convert a sentence into its unigrams.
    Input:
        - sentence
    Output:
        - List of unigrams.
"""
def get_unigrams(sentence):
    return sentence.split()


"""
    Function to compute meteor score.
    Input:
        - candidate: sentenece
        - reference: sentence
    Output:
        - Meteor Score
"""
def meteor(candidate, reference):
    score = 0.0
    candidate_unigrams = get_unigrams(candidate)
    reference_unigrams = get_unigrams(reference)
    # print("candidate_unigrams:", candidate_unigrams)
    # print("reference_unigrams:", reference_unigrams)
    if (len(set(candidate_unigrams).intersection(set(reference_unigrams))) == 0):
        return score
    
    # Calculate precision adn recall
    Precision, Recall = calculate_unigram_precision_recall(candidate_unigrams, reference_unigrams)

    penalty = calculate_chunk_penalty(candidate_unigrams, reference_unigrams)
    f_score =  calculate_harmonic_mean(Precision, Recall)
    penalty_val = penalty
    meteor_score = calculate_meteor_score(f_score, penalty_val)

    return meteor_score
