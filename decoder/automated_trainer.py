import imp
import optuna
import pycnbi.decoder.trainer as tn
import sys
import os
import random
import plotly.graph_objects as go


REF_FILE_NAME = "/Users/apple/Desktop/Me/ENSTA/PFE/EEG_ECoG_decoder/pycnbi/pycnbi/config_files/config_trainer_mi_ref.py"

cfg = None


def replaceAllValues(filename_in, filename_out, params):
    f = open(filename_in,'r')
    filedata = f.read()
    f.close()

    ref_indicator = "r_{}"
    for param in params:
        old_data = ref_indicator.format(param)
        new_data = str(params[param])
        filedata = filedata.replace(old_data, new_data)

    f = open(filename_out,'w')
    f.write(filedata)
    f.close()




def objective(trial):
    params = {}

    gen = (item for item in dir(cfg) if not item.startswith("__"))

    for item in gen:
        print(eval('cfg.'+item))

        if eval('cfg.'+item)['type']=='float':
            if 'step' in eval('cfg.'+item):
                params[eval('cfg.'+item)['name']] = trial.suggest_float(eval('cfg.'+item)['name'], eval('cfg.'+item)['values'][0], eval('cfg.'+item)['values'][1], step=eval('cfg.'+item)['step'])
            else:
                params[eval('cfg.'+item)['name']] = trial.suggest_float(eval('cfg.'+item)['name'], eval('cfg.'+item)['values'][0], eval('cfg.'+item)['values'][1])
        
        if eval('cfg.'+item)['type']=='int':
            if 'step' in eval('cfg.'+item):
                params[eval('cfg.'+item)['name']] = trial.suggest_int(eval('cfg.'+item)['name'], eval('cfg.'+item)['values'][0], eval('cfg.'+item)['values'][1], step=eval('cfg.'+item)['step'])
            else:
                params[eval('cfg.'+item)['name']] = trial.suggest_int(eval('cfg.'+item)['name'], eval('cfg.'+item)['values'][0], eval('cfg.'+item)['values'][1])
            
        if eval('cfg.'+item)['type']=='categorical':
            params[eval('cfg.'+item)['name']] = trial.suggest_categorical(eval('cfg.'+item)['name'], eval('cfg.'+item)['values'])
    
    params['REPORT_NAME'] = trial.number
    config_name = REF_FILE_NAME[:-7] + "_{}.py"
    config_name = config_name.format(trial.number)
    replaceAllValues(REF_FILE_NAME,config_name, params)

    try:
        acc, f1 = tn.batch_run(config_name)
        return acc, f1

    except:
        acc,f1 = 0.0, 0.0
        return acc, f1

    # 2) create configuration file
    # 3) launch trainer with the created config file
    # 4) evaluate peformance after reading the performance file
    

if __name__ == '__main__':
    # Load parameters
    if len(sys.argv) < 2:
        cfg_file = input('Config file name? ')
    else:
        cfg_file = sys.argv[1]
    
    cfg = imp.load_source(cfg_file, cfg_file)
    study = optuna.create_study(directions=["maximize", "maximize"])
    study.optimize(objective, n_trials=1000)

    fig = optuna.visualization.plot_pareto_front(study, target_names=["accuracy", "f1 score"])
    fig.show()

    fig2 = optuna.visualization.plot_param_importances(study, target=lambda t: t.values[0])
    fig2.show()

    fig4 = optuna.visualization.plot_param_importances(study, target=lambda t: t.values[1])
    fig4.show()

    fig3 = optuna.visualization.plot_slice(study, params=["LEPOCH", "HEPOCH"], target=lambda t: t.values[0])
    fig3.show()

    fig5 = optuna.visualization.plot_slice(study, params=["PSDFMIN", "PSDFMAX"], target=lambda t: t.values[0])
    fig5.show()

