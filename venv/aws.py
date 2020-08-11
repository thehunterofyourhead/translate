import boto3
import pandas as pd

data = pd.read_csv('data1.csv')

client = boto3.client('translate', region_name="us-east-1")
