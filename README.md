# citation-context-summarization
Citation Context based scientific summarization algorithm based on C-LexRank (http://www-personal.umich.edu/~vahed/c-lexrank.html)

## Modified summarization algorithm (/summaryModAlgo):

* The dataset is present in /contextFiles as <paperName>.txt
* The factoids for the dataset required for evaluation is present in /facts as <paperName>.ann
* The log for the runs is present in the file log.txt
* To execute the algorithm over the whole dataset and calculate the evaluation score for a feature index

### Current list of features
* 1 - Unigrams
* 2 - Bigrams
* 3 - Number of citations

```
python executeAndEvaluate.py <featureIndex> <comments>

```


