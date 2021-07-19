import sys
sys.path.insert(1, '/Users/apple/Desktop/Me/ENSTA/PFE/EEG_ECoG_decoder/pycnbi')

import pycnbi
#from pycnbi.pycnbi_config import CAP
#from pycnbi.triggers.trigger_def import trigger_def

#-------------------------------------------
# Data 
#-------------------------------------------
DATA_PATH = r'/Users/apple/Desktop/Me/ENSTA/PFE/NSGA-II/nsga2code/data'
EPOCH = [r_LEPOCH, r_HEPOCH]
#EPOCH = [-0.3, 0.5]
#EPOCH = [-0.9,0]
#-------------------------------------------
# Trigger
#-------------------------------------------
TRIGGER_FILE = r'triggerdef_upperLimb_P18.ini'
TRIGGER_DEF = ['P5', 'P11']
LOAD_EVENTS = {'selected':'False', 'False':None, 'True':'C:'}

#-------------------------------------------
# Channels specification
#-------------------------------------------
PICKED_CHANNELS = None
#PICKED_CHANNELS= ['ch3','ch4','ch5','ch6','ch7','ch8']
EXCLUDED_CHANNELS = []

REF_CHANNELS_OLD = []
REF_CHANNELS_NEW = []
REREFERENCE = {'selected':'False', 'False':None, 'True':dict(new=[], old=[])}

#-------------------------------------------
# Filters
#-------------------------------------------
SP_FILTER = r_SP_FILTER #'car' or None

SP_FILTER = None
SP_CHANNELS = PICKED_CHANNELS
TP_FILTER = {'selected':'True', 'False':None, 'True':r_TP_FILTER}
NOTCH_FILTER = {'selected':'False', 'False':None, 'True':[50]}

#-------------------------------------------
# Unit conversion
#-------------------------------------------
MULTIPLIER = 1

#-------------------------------------------
# PSD 
#-----FEATURES = {'selected':'PSD','PSD':dict(fmin=1, fmax=40, wlen=0.5, wstep=10, decim=1)}
FEATURES = {'selected':'PSD','PSD':dict(fmin=r_PSDFMIN, fmax=r_PSDFMAX, wlen=0.5, wstep=r_PSDWSTEP, decim=1)}
EXPORT_GOOD_FEATURES = True
FEAT_TOPN = 100

#-------------------------------------------
# Feature types
#-------------------------------------------

CLASSIFIER =    {'selected': 'RF', \
                'GB': dict(trees=1000, learning_rate=0.01, depth=7, seed=666), \
                'RF': dict(trees=r_NBTREESRF, depth=r_DEPTHRF, seed=666), \
                'rLDA': dict(r_coeff=0.3), \
                'LDA': dict()}

EXPORT_CLS = False

#-------------------------------------------
# Cross-Validation & testing
#-------------------------------------------
CV_PERFORM =   {'selected':'StratifiedShuffleSplit', \
                'False':None, \
                'StratifiedShuffleSplit': dict(test_ratio=0.3, folds=3, seed=0, export_result=True), \
                'LeaveOneOut': dict(seed=0,export_result=True)}

REPORT_NAME = r_REPORT_NAME
#-------------------------------------------
# Parallel processing
#-------------------------------------------
N_JOBS = None
