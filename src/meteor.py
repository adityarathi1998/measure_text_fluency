import collections
import itertools


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


def calculate_penalty(candidate_unigrams, reference_unigrams):
    pass


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


def calculate_unigram_precision_recall(candidate_unigrams, reference_unigrams):
    pass


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

    penalty = calculate_penalty(candidate_unigrams, reference_unigrams)
    f_score =  calculate_harmonic_mean(Precision, Recall)
    penalty_val = penalty[0]
    meteor_score = calculate_meteor_score(f_score, penalty_val)

    return meteor_score
