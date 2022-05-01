import os
import sys
import argparse
from meteor import meteor
from blue import bleu
from rouge import rouge_n as rouge
import time

global metrics_order 
metrics_order = ["bleu", "rouge", "meteor"]


"""
    Function to calculate the scores for a (cadidate, reference) pair for the given metrics.
    Input:
        - candidate: sentence
        - reference: sentence
        - matrcs: specific metrics or all
"""
def sentence_evaluation_helper(candidate, reference, metrics):
    scores = []
    times = []

    if metrics == "all" or metrics == "bleu":
        bleu_st = time.time()
        bleu_score_scratch, bleu_score_nltk = bleu(candidate, reference)
        bleu_ed = time.time()
        if bleu_score_scratch == 0:
            scores.append(bleu_score_nltk)
        else:
            scores.append(bleu_score_scratch)
        times.append(bleu_ed - bleu_st)
    
    if metrics == "all" or metrics == "rouge":
        rouge_st = time.time()
        rouge_score = rouge(candidate, reference)
        rouge_ed = time.time()
        scores.append(rouge_score)
        times.append(rouge_ed - rouge_st)

    if metrics == "all" or metrics == "meteor":
        meteor_st = time.time()
        meteor_score = meteor(candidate, reference)
        meteor_ed = time.time()
        times.append(meteor_ed - meteor_st)
        scores.append(meteor_score)

    return scores, times


"""
    Helper function to evaluate the files
    Input:
        - candidate_file_path
        - reference_file_path
        - metrics
    Output:
        - File with the metrics scores.
"""
def file_evaluation_helper(candidate_file_path, reference_file_path, output_file_path,metrics):
    avg_blue = 0
    avg_rouge = 0
    avg_meteor = 0
    avg_score = 0
    count = 0
    temp_count = 0
    bleu_time = 0 
    rouge_time = 0 
    meteor_time = 0
    avg_time = 0
    ouput_fp =  open(output_file_path, "w+")
    if metrics == "all":
        ouput_fp.write("{:<15}\t{:<15}\t{:<15}\n".format(metrics_order[0] + " score", metrics_order[1] + " score",metrics_order[2] + " score"))
    else:
        ouput_fp.write("{:<15}\n".format(metrics + " score"))


    with open(candidate_file_path,"r") as candidates_fp, open(reference_file_path,"r") as references_fp:
        candidates = candidates_fp.readlines()
        references = references_fp.readlines()
        for candidate, reference in zip(candidates, references):
            temp_count +=1
            if (len(reference) > 160):
                continue
            count +=1
            scores, time_array = sentence_evaluation_helper(candidate, reference, metrics)
            
            if metrics == "all":
                ouput_fp.write("{:<15}\t{:<15}\t{:<15}\n".format(scores[0],scores[1],scores[2]))
                avg_blue += scores[0]
                avg_rouge +=scores[1]
                avg_meteor +=scores[2]

                bleu_time +=time_array[0]
                rouge_time += time_array[1]
                meteor_time += time_array[2]
                
            else:
                ouput_fp.write("{:<15}\n".format(scores[0]))
                avg_score +=scores[0]
                avg_time +=time_array[0]
                


    if metrics == "all":
        ouput_fp.write("Average {} score : {}\n".format(metrics_order[0], avg_blue/count))
        ouput_fp.write("Average {} score : {}\n".format(metrics_order[1], avg_rouge/count))
        ouput_fp.write("Average {} score : {}\n".format(metrics_order[2], avg_meteor/count))

        ouput_fp.write("Total {} time : {}\n".format(metrics_order[0], bleu_time))
        ouput_fp.write("Total {} time : {}\n".format(metrics_order[1], rouge_time))
        ouput_fp.write("Total {} time : {}\n".format(metrics_order[2], meteor_time))

    else:
        ouput_fp.write("Average {} score : {}\n".format(metrics, avg_score/count))
        ouput_fp.write("Total {} time : {}\n".format(metrics, avg_time))

            
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
        results, _ = sentence_evaluation_helper(candidate, reference, args.evaluation_matrix)
        if args.evaluation_matrix =="all":
            print("{} score : {}\n {} score : {}\n {} score : {}\n ".format(metrics_order[0], results[0], metrics_order[1], results[1], metrics_order[2], results[2]))    
        else:
            print("{} score : {}\n".format(args.evaluation_matrix, results[0]))
    else:
        file_evaluation_helper(candidate_file_path, reference_file_path, output_file_path,args.evaluation_matrix)