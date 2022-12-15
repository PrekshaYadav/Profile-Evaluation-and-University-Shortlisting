import os

from cffi.setuptools_ext import execfile

#import Connector

#execfile('Connector.py')
os.system('python Connector.py')
os.system('python Importing_Dataset.py')
os.system('python YMGrad_Scraper.py')
os.system('python Visualization.py')
os.system('python Prediction_model.py')
os.system('python app.py')


print("Main endddd")
