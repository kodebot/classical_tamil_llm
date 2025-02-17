
# Notes

literature review

## things to explore

data collection - low resource languages

few shot learning or more data

try to use LLM to see mapping

data generation try different models - do qualitative study


## Meeting with Dr. Abbas

1. Find the context window of LLaMA 2
2. Contact Balachandran to see if the new model is available


## Notes

1. use correct prompt template for LLAMA

## Steps - Data set preparation
     1. Dataset need to validated and verified by the native speaker (Human)
       a. there is no hallucinated
       b. quality is high
     2. using automatic one like GPT

## Chunking - experiment with different chunking sizes

1. use human feedback to validate the data
2. use GPT to provide rank of the data


## Fine tune - with different models - see if that improves

Golden dataset - 

1. Get questions and ground truth answers - 

## RAGus evaluation library - use it to evaluate the model
    1. Does it support non-English languages?  



## Plots loss

Weights and Biases
Pheonix
LangWatch

## Evaluation

BERT Score
CHRF
Explore all similarity score evaluation metrics
GPT-4 for scoring
Human verification


## Review

### Title

1. Pick a better title (few title)
2. Dataset is novel

### Introduction

1. Citation for Tamil language - wikipedia (why important)
2. Should address the problem being solved - low resource language
3. Tamil models are OK but not good enough
4. Hence what you are doing is important

Avoid butllet points and numbered list

Last paragraph - this work curates new dataset, models are fine-tuned and evaluated

### Related Work

1. add all papers
2. lot more info on important paper
3. why human evaluation
4. why text generation
5. why few shot learning

### Methodology

No need for the figure

3.2 measure the size of the data set in numeer of tokens

Move the augumented dataset to the experiment section or in a subsection

Include 3.3.1 as model hyper parameters and also introduce inference hyper parameters. Also explain why these values like other reseachrs or recommended by library

include performance metrics - include the formula as well

try line graph

check if there is a pattern of unnecessary text







## More notes

### Intro
1. Introduction - need more citation
2. include does not convey we have a problem
3. include no precense of data in digital media
4. look for Tamil info citations from other pages
5. Repharse the flow of the introduction
6. Use GenAI for rephrasing
7.

### Related Work
1. the study conducted by - should start with like this
2. No need for separate heading - may just one both models (LLM Fine tuned on Tamil)
3. Expand on the paper

### Design Methodology
  1. remove the instruction set box
  2. change curated to web - ask GPT
  3. try to simplify the diagram

  3.1. Dataset
  1. Go through all the refrerences and make sure first one mention is refreenced
  2. more penality to be next to F thing so it will on the same line
  3. move everything to springer template

 ### Experimental results

Start with Colab and computational info

explain the why even when more data why the quality is low for augmented data

Add some qualitative analysis - explain with an example - explain the difference between the two
human eval and 


### Limitatioins

dont' down play
think about limitatins again - in postive way
use Further research - metrics  and line by line

Remove Grapheme Pair encoding - very negative

put all the things we did not do as futher work - how others have used and what they recommended


### Cleanup (data)

[a-zA-Z]{1,40}\s+
[a-zA-Z]{1,40}, 
'[a-zA-Z]{1,40}' 
&nbsp; - replace with space
\\t
\\n
\\r
\\
[ ]{2,100} - replace with single space


