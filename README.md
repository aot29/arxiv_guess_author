# ArXiv: Guess Author
Is double blind peer review really anonymous? Try to guess the author(s) of a paper by looking at its metadata. 

## Using Conda
```
conda create -n arxiv_exp python=3.12.2
conda activate arxiv_exp
pip install -r requirements.txt
```

```
conda activate arxiv_exp
jupyter lab
```

## Using plain Python
```
python -m venv arxiv_exp
source arxiv_exp/bin/activate
cd workspace/arxiv_exploratory/
pip install -r requirements.txt
```

```
source arxiv_exp/bin/activate
cd workspace/arxiv_exploratory/
jupyter lab
```
