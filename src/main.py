import os
import sys
import argparse
from meteor import meteor

global matrics_order 
matrics_order = ["bleu", "rouge", "meteor"]

def bleu(candidate, reference):
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
    scores = []
    if matrics == all or matrics == "bleu":
        bleu_score = bleu(candidate, reference)
        scores.append(bleu_score)
    if matrics == all or matrics == "rouge":
        rouge_score = rouge(candidate, reference)
        scores.append(rouge_score)
    if matrics == all or matrics == "meteor":
        meteor_score = meteor(candidate, reference)
        scores.append(meteor_score)
    return scores


"""
    Helper function to evaluate the files
    Input:
        - candidate_file_path
        - reference_file_path
        - matrics
    Output:
        - File with the metrics scores.
"""
def file_evaluation_helper(candidate_file_path, reference_file_path, output_file_path,matrics):
    avg_blue = 0
    avg_rouge = 0
    avg_meteor = 0
    avg_score = 0
    count = 0
    temp_count = 0
    ouput_fp =  open(output_file_path, "w+")
    if matrics == "all":
        ouput_fp.write("{:<15} {:<15} {:<15}\n".format(matrics_order[0] + " score", matrics_order[1] + " score",matrics_order[2] + " score"))
    else:
        ouput_fp.write("{:<15}\n".format(matrics + " score"))


    with open(candidate_file_path,"r") as candidates_fp, open(reference_file_path,"r") as references_fp:
        candidates = candidates_fp.readlines()
        references = references_fp.readlines()
        for candidate, reference in zip(candidates, references):
            temp_count +=1
            if (len(reference) > 160):
                ouput_fp.write("Too long sentence. Index : {}\n".format(temp_count))
                continue
            count +=1
            scores = sentence_evaluation_helper(candidate, reference, matrics)
            
            if matrics == "all":
                ouput_fp.write("{:<15} {:<15} {:<15}\n".format(scores[0],scores[1],scores[2]))
                avg_blue += scores[0]
                avg_rouge +=scores[1]
                avg_meteor +=scores[2]
            else:
                ouput_fp.write("{:<15}\n".format(scores[0]))
                avg_score +=scores[0]


    if matrics == "all":
        ouput_fp.write("Average {} score : {}\n".format(matrics_order[0], avg_blue/count))
        ouput_fp.write("Average {} score : {}\n".format(matrics_order[1], avg_rouge/count))
        ouput_fp.write("Average {} score : {}\n".format(matrics_order[2], avg_meteor/count))
    else:
        ouput_fp.write("Average {} score : {}\n".format(matrics, avg_score/count))

            
"""
    driver code.
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t","--input_type", help="specifies type of input", choices=["file", "cmd"], default="cmd", required=True)
    parser.add_argument("-em","--evaluation_matrix", help="specifies the evaluation matrix or all.", choices=["bleu", "rouge", "meteor", "all"], default="bleu", required=True)
    parser.add_argument("-rf","--reference_file_path", help="reference file path")
    parser.add_argument("-cf","--candidate_file_path", help="candidate file path")
    parser.add_argument("-of","--output_file_path", help="output file name")
    args = parser.parse_args()

    input_type = args.input_type
    if input_type == "cmd":
        candidate = input("Candidate sentence :")
        reference = input("Reference sentence :")
    else:
        reference_file_path = args.reference_file_path
        candidate_file_path = args.candidate_file_path
        output_dir = "../output/"
        output_file_path = output_dir + args.output_file_path

        if not os.path.isfile(reference_file_path):
            sys.exit("Invalid reference file path")

        if not os.path.isfile(candidate_file_path):
            sys.exit("Invalid candidate file path")

        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        

    if input_type == "cmd":
        results = sentence_evaluation_helper(candidate, reference, args.evaluation_matrix)
        if args.evaluation_matrix =="all":
            print("{} score : {}, {} score : {}, {} score : {}\n ".format(matrics_order[0], results[0], matrics_order[1], results[1], matrics_order[2], results[2]))    
        else:
            print("{} score : {}\n".format(args.evaluation_matrix, results[0]))
    else:
        file_evaluation_helper(candidate_file_path, reference_file_path, output_file_path,args.evaluation_matrix)