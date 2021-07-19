# pycnbi_optuna
 A fully automated EEG/ECoG decoding pipeline (feature + model engineering), using pycnbi and Optuna hyperparameter optimization framework.

## Installation and Setup
1) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install optuna and the plotly package for visualization.

```bash
pip install optuna plotly
```
2) Install [pycnbi](https://github.com/aizmeng/pycnbi) if you didn't.

3) Replace the trainer.py default file with the trainer.py file provided in this repo, and add all other files from the [/decoder](https://github.com/icaresakr/pycnbi_optuna/tree/main/decoder) folder of this repo in the pycnbi decoder folder.

4) Place the reference configuration file [config_trainer_mi_ref.py](https://github.com/icaresakr/pycnbi_optuna/blob/main/config_files/config_trainer_mi_ref.py) in the config_files folder of pycnbi.

## Run the automated trainer
1) ### The optimizer configuration file [optimization_config.py](https://github.com/icaresakr/pycnbi_optuna/blob/main/decoder/optimization_config.py)
Define the parameters to optimize as a python dictionary, containing the name of the parameter, the type (float, int or categorical), the possible values to take, and the step (optional) between consecutive values (for int and float types only).
```python 
PARAM_float = {
    'name':'PARAM_float',
    'type':'float',
    'values':[-1, 0.2],
    'step':0.05
}

PARAM_int = {
    'name':'PARAM_int',
    'type':'int',
    'values':[1, 50],
}

PARAM_categorical = {
    'name':'PARAM_categorical',
    'type':'categorical',
    'values':["None", "[None, r_TP_FMAX]", "[r_TP_FMIN, r_TP_FMAX]", "[r_TP_FMIN, None]"],

}
```
2) ### The pycnbi reference configuration file [config_trainer_mi_ref.py](https://github.com/icaresakr/pycnbi_optuna/blob/main/config_files/config_trainer_mi_ref.py).
For the parameters you want to explore (as specified in the optimizer configuration file), put a reference word instead of the value in config_trainer_mi_ref.py, so that the automated trainer can detect the word and replace it with the value to evaluate it.
The reference word starts with an "r_" followed by the parameter name as specified in the optimizer configuration file. For example, if you call the epoch lower bound parameter "LEPOCH" in the optimizer configuration file, then the reference should be "r_LEPOCH" in the reference configuration file.
For parameters you wish to fix, assign default value (remove the refernce if exists).

3) ### Run the automated trainer as follow:
```bash
python /path/to/automated_trainer.py /path/to/optimization_config.py
```

4) ### Do something else and get great decoding results once the execution is done


