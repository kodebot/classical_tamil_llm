# Classical Tamil LLM - Literature Review

## Papers reviewed

### 1. [Tamil-Llama: A New Tamil Language Model Based on Llama 2](https://arxiv.org/abs/2311.05845)

LLaMa 2 model that supports Tamil language

#### Methodology

* LLaMA 2 model enhanced with additional 16,000 Tamil tokens (combination of root/lemma and suffixes)
* LoRA for model training
* SentencePiece for tokenization
* Dataset: Tamil translated version of Alpaca dataset and OpenOrca (collection of instruction following data for LLM fine-tuning)
  * Alpaca dataset: instruction-response dataset from researchers from Stanford University
  * OpenOrca: Open source version of Orca to replicate the capabilities of proprietary models like OpenAI's GPT-4.

#### Key Findings

* The enhanced LLaMA model with additional Tamil tokens showed improved performance in understanding and generating Tamil text.
* The use of LoRA for model training proved to be effective in fine-tuning the model with limited computational resources.
* The translated Alpaca dataset and OpenOrca data significantly contributed to the model's ability to follow instructions and generate coherent responses in Tamil.
* The model demonstrated capabilities comparable to proprietary models like GPT-4 in specific tasks.
* Emphasized the potential of smaller, fine-tuned models to achieve high performance with targeted training data. - **THIS IS IMPORTANT IDEA THAT WE ARE EXPANDING ON WITH OUR WORK**

#### Important limitations or insights

* The model's performance is highly dependent on the quality and quantity of the additional Tamil tokens - 16,000 tokens may not be sufficient for all tasks - especially for classical Tamil.
* Availability of high-quality, Tamil datasets for training and evaluation in various domains
* LoRA in fine-tuning may not be the best with different datasets and tasks
* The model may struggle with complex linguistic nuances and idiomatic expressions in Tamil
* Portability of this idea to other models like Google's Gemma 2B

#### Evaluation Methods

GPT-4 is used to assign grade on a 10-point scale, supplemented with manual reviews

#### Result models

Tamil LlaMa 7b and 13b for both base and instruct versions

#### Other useful

Orca approach (Orca paper from Microsoft Research) - fine-tuning smaller language model using data distilled from more advanced teacher model - focusing on explanation and reasoning

### 2. Cited By [Towards building first persian LLM](https://arxiv.org/abs/2312.15713)

Very Similar to #1 but for Persian language. Introduces PersianLLaMA - trained on diverse Persian text dataset

#### Methodology

1. Training approaches - two methods
    1. Training from scratch
    2. Training as adapter on pre-trained English LLaMA 2
2. Data preprocessing using Hazm library
3. Tokenizer
    1. Mono-lingual tokenizer used for model from scratch
    2. Multilingual tokenizer used for adapter model (English LLaMA 2)
4. DeepSpeed and TencentPretrain for optimization
5. LoRA for training of adapter model

#### Key Findings

First Persian LLM based on LLaMA 2 model that can generate coherent Persian text

#### Important limitations or insights

Limitations including the scope of the training data, ethical considerations and lack of a specific Persian evaluation dataset.

### 3. Cited By [sphinx: Sample efficient multilingual instruction fine-tuning through n-shot guided prompting](https://arxiv.org/abs/2407.09879)

Highlights the performance gap of LLMs in non-English languages
Introduces novel recipe for creating a multilingual synthetic instruction tuning dataset - SPHINIX

#### Methodology

* Comprises 1.8M instruction response pairs in 51 languages (selectively translating Orac instruction fine-tuning dataset)
  * Tamil was one of the 51 languages
* Tested by fine tuning PHI-3-SMALL and MISTRAL-7B models

#### Key Findings / Outcomes

* Novel approach to generate synthetic data for multi-lingual instruction fine-tuning by selectively translating Orca instruction fine-tuning dataset

* Language Specific N-shot Guided instruction fine tuning (LANG) strategy

* experiments showed both Mistral 7B and Phi-3-Small performed better with SPHINIX dataset
* experiments showed that the LANG strategy outperformed the baseline strategy

#### Limitations

* Required significant use of computational resources (GPU hours) for experiments so it may be expensive option to fully fine-tune a model

* Experiments are done on a model with max parameter of 7B
  * however authors believe that it is suitable for whenever LoRA or PEFT is used for fine-tuning using smaller dataset

* Evaluation is mainly on reasoning tasks - no evaluation is done on generation tasks like summarisation

## 4. Cited By [Egalitarian Language Representation in Language Models: It All Begins with Tokenizers](https://arxiv.org/abs/2409.11501)

Introduces new Tokenizer called Grapheme Pair Encoding based on Byte Pair Encoding to tokenize languages like Tamil, Hindi and Sinhala better

Highlights unequal treatment of languages begins at the tokenizer level.

All popular tokenizers breaks Tamil (Sinhala and Hindi) tokens into smaller tokens unnecessarily - leading to large context windows and increased computational cost.

Byte Pair Encoding (BPE) is not ideal for languages like Tamil, Hindi and Sinhala. Introduces Grapheme Pair Encoding (GPE) as a better alternative.

#### Methodology

* Proposes to introduce pre-tokenization step to break input text into smaller manageable chunks (pre-tokens)
* Introduces a concept called Graphemes as the smallest unit of a language rather than unicode points - unicode points usually divides single Tamil character into multiple tokens whereas graphemes will keep them as single token.
  * Grapheme Pair Encoding is exactly same as Byte Pair Encoding but uses graphemes as the smallest unit rather than bytes
* Uses Compression Ratio (CR) and Tokenization Parity (TP) as metrics to evaluate tokenizers

#### Key Findings

* GPT-2 performs poorly on Tamil, Hindi and Sinhala languages with respect to tokenization and evaluated using CR and TP metrics 
* FLAN-T5 and Gemma 2 are suitable for adaptation to new languages
* GPE outperforms BPE in terms of CR and TP metrics for Tamil, Hindi and Sinhala languages

#### Limitations

* Suitability of GPE for training LLMs from scratch/adapter layer is not evaluated
* Hardwares used for experiments are not mentioned

## 5. Cited By [Chitranuvad: Adapting Multi-lingual LLMs for Multimodal Translation](https://aclanthology.org/2024.wmt-1.80/)

Introduces Chiranuvad system - a multimodal translation model based on multi-lingual LLMs
Focus is on image/text to multi-lingual translation for non-English language pairs

#### Methodology

* Chitranuvad model architecture is inspired by LLaVA like model (not LLaMA, it is LLaVA) and used Krutrim LLM as multilingual backbone

* Uses three stage pipeline 
  1. Pre-training for Feature Alignment
  2. Instruction tuning
  3. Task specific fine-tuning

* uses LLaVA pre-train and instruct datasets

#### Key Findings

* Able to achieve SOTA (State of the art) on Hindi and Malayalam language
* Able to do image captioning in all three languages - Hindi, Malayalam and Bengali

#### Limitations

* Evaluation is done on only three languages - Hindi, Malayalam and Bengali
* Vision modality did not have significant impact on the translation quality
* Future work is needed for better visual representation learning

## 6. Cited By [How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?](https://arxiv.org/abs/2406.11477)

Explores the use of Cross lingual vocabulary adaption (CVA) for non-English languages (for both vocabulary expansion and replacement) in low-resource settings

#### Methodology

* Build an adapted tokenizer for the target language, initialise embedding for the new token then adapting the LLM to the current target language

* Training - two approaches
  * LoRA applied to all linear layers
  * two-stage tuning process where only embedding and LM heads are updated first then LoRA - this minimises the risk of overfitting

* Models used - LLaMA2 (7B), LLaMA3 (8B) and Gemma2 (9B)

* Uses 10 topologically different languages for evaluation wiht only 30K sentences (0.01GB for each) - Tamil is not one of them (Telugu and Sinhala are the closest but they are still significantly different from Tamil)

* Metrics 
* chrF (character F-score) for machine translation


#### Key Findings

* 3 English centric models are adapted with vocabulary expansion technique in low resource settings (only 0.01GB of target language text is used) for machine translation and summarization tasks

* popular vocabulary expansion techniques used in high resource settings are not always optimal in low resource settings

* vocabulary initialisation approach (using heuristics from the source and target tokenizer) is more effective than vocabulary expansion approach in low resource settings

* fine-tuning top and bottom 2 layers of the model is more effective than fine-tuning all layers (using multi-token predictive objective)

* short input sequence length by splitting longer text into multiple sentences allows for a larger number of model updates - helps to avoid underfitting [THIS IS IMPORTANT AND WORTH TRYING FOR THIS PROJECT]

#### Limitations

* BPE is assumed to be the tokenizer for base models - models with other tokenizers are not evaluated

* Tamil is not one of the languages evaluated

* model size used are 7B, 8B and 9B - smaller/larger models are not evaluated

* only translation and summarization tasks are evaluated - other tasks like question answering, text generation are not evaluated

## 7. Cited By [Exploring Pretraining via Active Forgetting for Improving Cross Lingual Transfer for Decoder Language Models](https://arxiv.org/abs/2410.16168)

Pretraining autoregressive LLMs (decoder only) using active forgetting to improve cross-lingual transfer ability.
Based on https://scholar.google.com/scholar_url?url=https://arxiv.org/abs/2307.04507&hl=en&sa=T&oi=gsr-r&ct=res&cd=0&d=15145699747692781975&ei=CZVVZ9XEILiC6rQP5ZaquAE&scisig=AFWwaeaApuqgzyejfJ46SVqjIaDd for encoder only model

#### Methodology

* Active forgetting where token embeddings are reset after every 'k' steps
* New vocabulary is merged with the original vocabulary and new LM Head is added to the model

#### Key Findings

* common method of adapting LLMs to a new language leads to performance degradation in the original language
* LLMs pretrained with active forgetting lead to better cross-lingual transfer performance

#### Limitations

* Scope is limited to pretaining of multilingual LLMs so cannot be applied to existing models
* Model size used are 10B or less


## 8. Cited By [BongLLaMA: LLaMA for Bangla Language](https://arxiv.org/abs/2410.21200)

Exact replica of Tamil LLaMA but for Bangla (Bengali) language - NOT MUCH TO LEARN FROM THIS PAPER IN OUR CONTEXT

## 9. Cited By [Pretraining Data and Tokenizer for Indic LLM](https://arxiv.org/abs/2407.12481)

Focus is on Pre-training Data and Tokenizer - proposes data preparation approach for pre-training LLMs for Indic languages

#### Methodology

* among other sources - Tesseract OCR is used to extract text from images
* tokenization is done using BPE rather than SentencePiece (and token to word ratio is used as quality metric)
* first dummy tokenizer is created and manually removed gibberish tokens then a new and final tokenizer is trained using cleaned tokens

#### Key Findings

* better performance when using cleaned data and new tokenizer in 11 indic languages - Tamil is one of them

#### Limitations

* presented from the context of pretraining but model size requirements were not discussed
* data cleaning and tokenization process is manual and time consuming - systematic approach is needed


## 10. Cited By [Fine Tuning LLMs for Low Resource Languages](https://ieeexplore.ieee.org/abstract/document/10660753)

Presents language specific modelling techniques for low resource languages - PEFT methods (LoRA and QLoRA), instruction tuning and and ReFT (Representation Fine Tuning) to address performance gaps in low resource languages

Highlights the need for language specific benchmark techniques for low resource languages

#### Limitations

Only the challenges and techniques are discussed - no evaluation or proposed solutions are presented

## 11. [LLMs Are Few-Shot In-Context Low-Resource Language Learners](https://arxiv.org/abs/2403.16512)

* Explores the effectiveness of LLMs as few-shot learners for low-resource languages
* Highlights shortcomings of in-context label alignment of low-res languages and proposes alternative - query alignment

#### Methodology

* cross lingual in-context learning (X-ICL)
  * cross lingual alignment that provides labels in source and target languages (in context label alignment)
  * query alignment that provides translation of queries in source and target languages but keeping the labels the same
* cross lingual prompting and retrieval

* models - XGLM-7.5B and BLOOM-7B
* 25 low resource languages are evaluated

#### Key Findings

* in-context label alignment is effective for low resource languages
* in-context query alignment can be used as substitute or complement to X-=ICL

#### Limitations

* coverage of low res languages are limited - Tamil is not one of them
* limited task coverage
* Due to hardware limitations, larger models are not explored

## 12. [ProverbEval: Exploring LLM Evaluation Challenges for Low-resource Language Understanding](https://arxiv.org/abs/2411.05049)

Highlights the challenges in evaluating LLMs for low resource languages

New ProverbEval dataset is introduced to evaluate LLMs for low resource languages (only 5 languages are evaluated - Tamil is not one of them)

#### Methodology

* Manual construction of ProverbEval dataset
* Three tasks are used for benchmarking 
  * multiple choice (task 1)
  * fill in the blank (task 2)
  * generation (task 3)
* Both closed and open source models are evaluated
  * LLaMA
  * Gemma
  * Aya-101
  * GPT-4o

#### Key Findings

* in zero shot evaluation of multiple choice task, model size matters, the bigger the model the better the performance
* few shot prompting has limited impact on task 2
* models performed better at generating proverbs if instructions are given in the same language

#### Limitations

* scope is limited to handful of languages
* limited LLMs are evaluated
* only three tasks are evaluated

## 13. [On Limitations of LLM as Annotator for Low Resource Languages](https://arxiv.org/abs/2411.17637)

Explores the limitations of LLMs as annotators for low resource languages


#### Methodology

* Marathi is evaluated using GTP-4o and Gemini 1.0 Pro, Gemma 2 (2B and 9B) and LLaMA 3.1 (8B) on classification, sentiment analysis and hate speech detection tasks

* Few shot and zero shot learning methods are used for annotation

#### Key Findings

* LLMs are not effective as annotators for low resource languages (Marathi in this case)

* GPT-4o achieved the best result

#### Limitations

* only one language is evaluated
* no details on evaluation metrics are provided
* hardware used for experiments are not mentioned

## 14. [Low-Resource Machine Translation through Retrieval-Augmented LLM Prompting: A Study on the Mambai Language](https://arxiv.org/abs/2404.04809)

Focus on Machine Translation for low resource languages using RAG and LLMs

#### Methodology

* Extracted nearly 2000 parallel English-Mambai sentences from a language manual using OCR and alignment techniques, along with a bilingual dictionary.
* Incorporated parallel sentences and dictionary entries in LLM prompts to optimize translation accuracy (using RAG).
* Tested the approach using a mix of manual and model-driven Mambai translations across diverse domains.

#### Key Findings

* Retrieval-augmented LLM prompting effectively handles low-resource translation.
* Domain-specific data significantly improves translation quality.
* Combining dictionary and sentence-level data enhances performance.

#### Limitations

* Results may not generalize well due to limited corpus size.
* Relies heavily on the availability of high-quality bilingual data.
