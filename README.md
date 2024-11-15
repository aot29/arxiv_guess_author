# ArXiv: Guess Author
Is double blind peer review really anonymous? Try to guess the author(s) of a paper. 

## Installation

### Using Conda
```
conda create -n arxiv_exp python=3.12.2
conda activate arxiv_exp
pip install -r requirements.txt
```

```
conda activate arxiv_exp
cd workspace/arxiv_guess_author/
jupyter lab
```

### Using plain Python
```
python -m venv arxiv_exp
source arxiv_exp/bin/activate
cd workspace/arxiv_guess_author/
pip install -r requirements.txt
```

```
source arxiv_exp/bin/activate
cd workspace/arxiv_guess_author/
jupyter lab
```

## Notebooks

### Attempt 01
* Guess the corresponding author (first attempt, keep it simple)
* Based on the topics discovered in the abstract of the paper

00 process_snapshot
 * Download a snapshop of arXiv [arXiv.org submitters, 2024] manually, put it in folder data.
 * Load the snapshot into a dataframe
 * Add columns for date and general categories
 * Save it in CSV format

01_prepare_data
* Load the data prepared in ../00_process_snapshot.ipynb
* Filter by year and subject, count the number of authors
* Split data into train/validate/test
* Apply pre-processing filters
* Apply lemmatization
* Save tokenized corpus, one for each train/validate/test dataset on NLP

02_fit_topic_model
* Load the tokenized corpus created in 00_load_data
* Fit the LDA model on the train corpus, evaluate it on the validate corpus
* Save the fitted model

03_assign_topics
* Load the train/validate/test tokenized article abstracts
* Load the model
* Use the model to assign topics probability to all articles
* Save the topic assignments

