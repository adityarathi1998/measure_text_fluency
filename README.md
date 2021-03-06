# Introduction to NLP - Team 6
## Measure Text Fluency

### Team Members
    - Aditya Rathi (2020201041)
    - Prashant Raj (2020201057)
    - Jayant Ingle (2020201019)

### Introduction to Text Fluency


### Directory Structure
* src - Contains the scripts files.
* data - Contains the dataset used for train, test and validate.
* report.pdf
* presentation.pdf
* README.md
* requirements.txt - Specifies the required python modules.
* figure - Containes the saved tsne plots.


### Requirements
* python3.7 +

### Getting Started
* Command to run for a single statement.
```
    pip3 install requirements.txt
    time python3 <changed_name>.py -t cmd -em meteor
    
    Candidat sentence :That was when I realized that this sort of benign neglect was a real problem, and it had real consequences, not just for Alex and her love life but for the careers and the families and the futures of twentysomethings everywhere.
    
    Reference sentence :It was at this moment that I understood that this harmless negligence was a real problem and that he had real consequences, not only for Alex and his sentimental life but for careers, families and the future of all the people in their twenties.
    
    meteor score : 0.5803974382853132
```
* Command to run for a complete file.
```
    time python3 meteor.py -t file -em meteor -rf ./dataset/reference.en -cf ./dataset/test.en
    
    real    3m29.846s
    user    3m27.247s
    sys     0m2.048s
```


### Links 
* dataset : [link](https://drive.google.com/drive/folders/1Bbdg7uS3FWGGJ8J7pTtRpls_eA5oR5c6?usp=sharing)
* model checkpoints
* Presentation : [link](https://docs.google.com/presentation/d/1S16xE295dZiKsScLo_a07KHvRqu5mmot3gUOzG5jJEM/edit?usp=sharing)
* Report : [link](https://www.notion.so/Project-Report-Team-6-be7d2387f6fd4822a692094ec83c9ccd)



