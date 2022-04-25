import collections
import itertools

def calculate_harmonic_mean(P, R):
    pass


def calculate_penalty(candidate_unigrams, reference_unigrams):
    pass


def calculate_meteor_score(f_mean, penalty):
    pass


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
