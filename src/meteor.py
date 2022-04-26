import collections
import itertools
from meteor_helper import Point, Line

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

def find_intersections(lines):
    pass


def calculate_allignments():
    pass


def calculate_chunks(candidate_unigrams, reference_unigrams):
    pass
    

"""
    Function to calculate the chunk penalty
    Input:
        - candidate_unigrams
        - reference_unigrams
    Output:
        - chunk penalty
"""
def calculate_chunk_penalty(candidate_unigrams, reference_unigrams):
    no_of_chunks = calculate_chunks(candidate_unigrams, reference_unigrams)
    candidate_unigrams = len(set(candidate_unigrams))
    chunk_penalty = 0.5*(no_of_chunks/candidate_unigrams)**3
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

    if (set(candidate_unigrams).intersection(set(reference_unigrams)) == 0):
        return score
    
    # Calculate precision adn recall
    Precision, Recall = calculate_unigram_precision_recall(candidate_unigrams, reference_unigrams)

    penalty = calculate_chunk_penalty(candidate_unigrams, reference_unigrams)
    f_score =  calculate_harmonic_mean(Precision, Recall)
    penalty_val = penalty[0]
    meteor_score = calculate_meteor_score(f_score, penalty_val)

    return meteor_score
