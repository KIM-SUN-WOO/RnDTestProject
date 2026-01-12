import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

class ExampleData:
    df = pd.DataFrame()  # original file
    dff = pd.DataFrame() # filtered file
    m = []               # local minima indices
    WS = 1               # window size
    OD = 1               # order for local minima

    def __init__(self, filename, WindowSize=20, Order=12):
        self.df = pd.DataFrame()
        self.df = pd.read_excel('../data/'+filename)
        self.df = self.df.dropna()

        pd.set_option('mode.chained_assignment', None)

        self.set_data(self.df)

        self.WS = WindowSize
        self.dff = self.df.rolling(window=WindowSize).mean()
        self.set_data(self.dff)

        self.OD = Order
        minima_indices = argrelextrema(self.dff['torso_y'].values, np.less,order = Order)
        self.m = minima_indices[0]


    def set_data(self,df):

        df['l_tibia_x'] = df['l_knee_x'] - df['l_ankle_x']
        df['l_tibia_y'] = df['l_knee_y'] - df['l_ankle_y']
        df['l_tibia_z'] = df['l_knee_z'] - df['l_ankle_z']
        df['l_femur_x'] = df['l_hip_x']  - df['l_knee_x']
        df['l_femur_y'] = df['l_hip_y']  - df['l_knee_y']
        df['r_tibia_x'] = df['r_knee_x'] - df['r_ankle_x']
        df['r_tibia_y'] = df['r_knee_y'] - df['r_ankle_y']
        df['r_tibia_z'] = df['r_knee_z'] - df['r_ankle_z']
        df['r_femur_x'] = df['r_hip_x']  - df['r_knee_x']
        df['r_femur_y'] = df['r_hip_y']  - df['r_knee_y']

        df['tor_wai_y'] = df['torso_y'] - df['waist_y']
        df['tor_wai_z'] = df['torso_z'] - df['waist_z']
        df['l_hip_wai_y'] = df['waist_y'] - df['l_hip_y']
        df['l_hip_wai_z'] = df['waist_z'] - df['l_hip_z']
        df['l_tibia_y'] = df['l_knee_y'] - df['l_ankle_y']
