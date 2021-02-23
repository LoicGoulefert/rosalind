# rosalind

Solutions for Rosalind problems (http://rosalind.info/problems/list-view/)


## Repository structure

Code for each problem is located in the `src` folder. Corresponding data is in the `data` folder.
Each solution and its associated data is named after the problem's ID given on Rosalind:

- `src/{ID}.py`
- `data/{ID}.txt`


## Run the code

Clone this repository, create a virtual env and install dependencies.

```
git clone git@github.com:LoicGoulefert/rosalind.git
cd rosalind
python3.7 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Run a solution:

```
python src/GC.py 
```
