import json, argparse, os

import pprint as pp
import numpy as np
import pandas as pd

from sklearn import metrics, datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score, r2_score

from models.NNeighClassifier import NNeighClassifier
from util import vis, dataIn
from util.helpers import playlistToSparseMatrixEntry




class TestTracks():
    def __init__(self):
        """self.readData(idx=idx,
            numFiles=numFiles,
            shouldProcess=parseFiles)"""
        pass
    
        """def testPlaylist(self):
            self.NNC = NNeighClassifier(
                sparsePlaylists=self.playlistSparse,
                songs=self.songs,
                playlists=self.playlists,
                reTrain=True)

            self.predictRandomNeighbour(self.playlists.iloc[10])"""
