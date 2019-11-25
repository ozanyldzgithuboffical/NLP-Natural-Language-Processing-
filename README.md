# NLP-Natural-Language-Processing-
- This repo contains sub-branch of artificial intelligence for natural language processing basis and some examples
- Natural Language Processing, usually shortened as NLP, is a branch of artificial intelligence that deals with the interaction between computers and humans using the natural language.

  1. **Natural Language Processing (NLP)**
  - **Enterance to DDI World**
  - **Sparce Matrix & Spelling Signs**
  - **Big &.Small Letters**
  - **Stop Words**
  - **Stemmer**
  - **CounterVectorizer**
  - **Classification**
  
  - **NLP** consists of some core approaches which help the machines to understand the language and generate it in return
  1.**Linguistic Approach**
  2.**Statistical Approach** 
  3.**Hybrid Approach**
  
  - **Linguistic Approach** is dealt by linguistics and has sub-branches which is about the structure of the sentences
  1. **Morphology** => Looks for roots and words of the sentences and their different meanings changing in the sentence
  2. **Syntax** => Determines the exact place of the usage of these words by taking consideration of their meanings
  3. **Semantics** => Understanding the meaning of the word for the sentence
  4. **Pragmatics** => Understanding the sense of the word usage in the sentence or for whole sentence
  
  - **Statistical Approach** is about the pre-processing and feature extraction of the NLP where machines can understand.
  1.**N-gram**
  2.**TFIDF**
  3.**Word Grow**
  4.**Bag of Words (BOW)**
  
  
 - **Some Usage Fields of Natural Language Processing**
 
  - 1.**Emotion Analysis**
  - 2.**Text Classification**
  - 3.**Text Summarization**
  - 4.**Question Answering**
  - 5.**Tag Clouds & Extracting Keywords**
  
 - **Some Language Libraries**
 1. **NLTK**
 2. **SpacCY**
 3. **Standford NLP**
 4. **Open NLP**
 5. **Amueller Word Cloud**
 6. **Tensorflow**
 7. **Rapid Automatic Keyword Extraction (RAKE)**
 
 - **Steps of NLP**
 
 **Data Source For NLP** ----> **Preprocessing (Stop Words,BOW)** ---> **Feature Engineering(N-gram,TF-IDF)**--->**ML**----->**Results**
 
 ## Sparse Matrix & Spelling Sign
- Consider the following sentences:
  
  **Mary, is hungry for apples.**

  **John is happy he is not hungry for apples.**
  
- **Step 1: Get rid of all punctuation marks.**

> Mary is hungry for apples
> John is happy he is not hungry for apples
- **Step 2: Make all letters lowercase. Computers distinguish between uppercase and lowercase and as such will treat ‘A’ and ‘a’ differently.**

> mary is hungry for apples
> john is happy he is not hungry for apples

- **Step 3: Separate each word in each sentence so that it becomes its own entity. This is a process known as tokenization and the resultant individual words are known as tokens**

> [mary], [is], [hungry], [for], [apples]
> [john], [is], [happy], [he], [is], [not], [hungry], [for], [apples]

- **Step 4: Get all the unique words in both sentences and assign a particular position (index) to them.**

> [mary], [is], [hungry], [for], [apples], [john], [happy], [he], [not]

- **Step 5: Convert each word to a number. For each word in each sentence, assign the assign the number of times the word occurs in that sentence to the word in question. This is a process known as count vectorization.**

