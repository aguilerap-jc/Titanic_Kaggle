import pandas as pd
import os

class Dataset:
    def __init__(self):
        self.dataset_folder = "../Datasets"
        self.src_folder = "../src"
        self.train = self.dataset_folder+"/train.csv"
        self.test = self.dataset_folder+"/test.csv"
    
    def get_train_df(self):
        return pd.read_csv(self.train)    

    def get_test_df(self):
        return pd.read_csv(self.test)    
    

if __name__=="__main__":
    ds = Dataset()
    print(ds.train)