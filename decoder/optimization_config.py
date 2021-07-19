###
# Parameters defintions for the automated hyperparameters optimization trainer
#
# 2021
###


LEPOCH = {
    'name':'LEPOCH',
    'type':'float',
    'values':[-1, 0.2],
    'step':0.05
}

HEPOCH = {
    'name':'HEPOCH',
    'type':'float',
    'values':[0.35, 1.1],
    'step':0.05
}

SP_FILTER = {
    'name':'SP_FILTER',
    'type':'categorical',
    'values':["None", "'car'"]
}

TP_FILTER = {
    'name':'TP_FILTER',
    'type':'categorical',
    'values':["None", "[None, r_TP_FMAX]", "[r_TP_FMIN, r_TP_FMAX]", "[r_TP_FMIN, None]"]
}

TP_FMIN = {
    'name':'TP_FMIN',
    'type':'float',
    'values':[0,3]
}

TP_FMAX = {
    'name':'TP_FMAX',
    'type':'float',
    'values':[35,65]
}

PSDFMIN = {
    'name':'PSDFMIN',
    'type':'float',
    'values':[0,3]
}

PSDFMAX = {
    'name':'PSDFMAX',
    'type':'float',
    'values':[35,75]
}

PSDWSTEP = {
    'name':'PSDWSTEP',
    'type':'int',
    'values':[1,20]
}

NBTREESRF = {
    'name':'NBTREESRF',
    'type':'int',
    'values':[1,1000]
}

DEPTHRF = {
    'name':'DEPTHRF',
    'type':'int',
    'values':[1,20]
}



