import argparse

global matrics_order 
matrics_order = ["bleu", "rouge", "meteor"]

def bleu(candidate, reference):
    pass
def meteor(candidate, reference):
    pass
def rouge(candidate, reference):
    pass

"""
    Function to calculate the scores for a (cadidate, reference) pair for the given matrics.
    Input:
        - candidate: sentence
        - reference: sentence
        - matrcs: specific matrics or all
"""
def sentence_evaluation_helper(candidate, reference, matrics):
    pass


"""
    Helper function to evaluate the files
    Input:
        - candidate_file_path
        - reference_file_path
        - matrics
    Output:
        - File with the metrics scores.
"""
def file_evaluation_helper(candidate_file_path, reference_file_path,matrics):
    pass
            
"""
    driver code.
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t","--input_type", help="specifies type of input", choices=["file", "cmd"], default="cmd", required=True)
    parser.add_argument("-em","--evaluation_matrix", help="specifies the evaluation matrix or all.", choices=["bleu", "rouge", "meteor", "all"], default="bleu", required=True)
    parser.add_argument("-rf","--reference_file_path", help="reference file path")
    parser.add_argument("-cf","--candidate_file_path", help="candidate file path")
    args = parser.parse_args()

    input_type = args.input_type
    if input_type == "cmd":
        candidate = input("Candidat sentence :")
        reference = input("Reference sentence :")
    else:
        reference_file_path = args.reference_file_path
        candidate_file_path = args.candidate_file_path

        # if os.path.isfile(reference_file_path):
        # print(reference_file_path)


        # #     fp = open(reference_file_path, "r")
        # #     sys.exit("Invalid reference file path")
        
        # if os.path.isfile(candidate_file_path):
        #     sys.exit("Invalid candidate file path")

    if input_type == "cmd":
        results = sentence_evaluation_helper(candidate, reference, args.evaluation_matrix)
        if args.evaluation_matrix =="all":
            print("{} score : {}, {} score : {}, {} score : {}\n ".format(matrics_order[0], results[0], matrics_order[1], results[1], matrics_order[2], results[2]))    
        else:
            print("{} score : {}\n".format(args.evaluation_matrix, results[0]))
    else:
        file_evaluation_helper(candidate_file_path, reference_file_path,args.evaluation_matrix)