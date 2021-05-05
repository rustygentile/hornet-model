# Hornet Model

This project models and simulates the outbreak of Asian giant hornets in the northwest. For a more detailed writeup, see also: https://my-hornet-model.readthedocs.io/

## Setup

### 1. Installation

From a fresh Python3 environment, first install geopandas:

```
conda install geopandas
```

Then the rest of the dependencies:

```
pip install -r requirements.txt
```

In case there are issues, see [also](https://github.com/geopandas/geopandas/issues/1812).

### 2. Download Data Files

You will need:
* '2021MCMProblemC_DataSet.xlsx'
* 'USA_Canada_ShapefileMerge'

See [also](./data/README.md).

### 3. Running

Run the files in this order:

```
python run_models.py
python run_plots.py
```
