# Introduction to NLP - Team 6
## Measure Text Fluency

### Team Members
    - Aditya Rathi (2020201041)
    - Prashant Raj (2020201057)
    - Jayant Ingle (2020201019)

### Directory Structure
* src - Contains the python scripts files.
* dataset - Contains the dataset used.
* analysis - Containers the notebook file. 
* requirements.txt - Specifies the required python modules.
* figure - Containes the saved figures.
* output - COntains the output files.
* report.pdf
* presentation.pdf
* README.md


### Requirements
* python3.7 +

### Getting Started
* Istall the modules
```
    pip3 install -r requirements.txt
```

* cd to the src directory
```
    cd src
```

* How to run
```
    NLP_Project$ python3 main.py --help
    usage: main.py [-h] -t {file,cmd} -em {bleu,rouge,meteor,all}
                [-rf REFERENCE_FILE_PATH] [-cf CANDIDATE_FILE_PATH]
                [-of OUTPUT_FILE_PATH]

    optional arguments:
    -h, --help            show this help message and exit
    -t {file,cmd}, --input_type {file,cmd}
                            specifies type of input
    -em {bleu,rouge,meteor,all}, --evaluation_matrix {bleu,rouge,meteor,all}
                            specifies the evaluation matrix or all.
    -rf REFERENCE_FILE_PATH, --reference_file_path REFERENCE_FILE_PATH
                            reference file path
    -cf CANDIDATE_FILE_PATH, --candidate_file_path CANDIDATE_FILE_PATH
                            candidate file path
    -of OUTPUT_FILE_PATH, --output_file_path OUTPUT_FILE_PATH
                            output file name
```

* Command to run for a single statement.
```
    time python3 main.py -t cmd -em all
    
    Candidat sentence :That was when I realized that this sort of benign neglect was a real problem, and it had real consequences, not just for Alex and her love life but for the careers and the families and the futures of twentysomethings everywhere.
    
    Reference sentence :It was at this moment that I understood that this harmless negligence was a real problem and that he had real consequences, not only for Alex and his sentimental life but for careers, families and the future of all the people in their twenties.
    
    bleu score : 0.1649662542496744
    rouge score : 0.7637795275590551
    meteor score : 0.37272787203232266
```

* Command to run for a complete file.
```
    time python3 main.py -t file -em <evaluation_metrics> -rf <reference_file_path> -cf <candidate_file_path> -of <output_file_name>
    
```

```
    # Example
    time python3 main.py -t file -em all -rf ../dataset/reference.en -cf ../dataset/test.en -of output.txt
    
    real    2m29.310s
    user    2m28.586s
    sys     0m1.828s
```


### Links 
* dataset : [link](https://drive.google.com/drive/folders/1Bbdg7uS3FWGGJ8J7pTtRpls_eA5oR5c6?usp=sharing)
* Presentation : [link](https://docs.google.com/presentation/d/1S16xE295dZiKsScLo_a07KHvRqu5mmot3gUOzG5jJEM/edit?usp=sharing)
* Report : [link](https://www.notion.so/Project-Report-Team-6-be7d2387f6fd4822a692094ec83c9ccd)



