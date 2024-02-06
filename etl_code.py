import glob
import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET 

log_file = 'log_file.txt'
target_file = 'transformed_data.csv'

def extract_from_csv(data_file):
    df = pd.read_csv(data_file)
    return df

def extract_from_json(data_file):
    df = pd.read_json(data_file, lines = True)
    return df

def extract_from_xml(data_file):
    df = pd.DataFrame(columns = ['name','height','weight'])
    tree = ET.parse(data_file)
    root = tree.getroot()
    
    for i in root:
        name = i.find('name').text
        height = float(i.find('height').text)
        weight = float(i.find('weight').text)
        df = pd.concat([df,pd.DataFrame([{'name':name,'height':height,'weight':weight}])], ignore_index = True)
        return df

def extract():
    extracted_data = pd.DataFrame(columns = ['name','height','weight'])   

    for csv in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csv))], ignore_index = True)

    for jsonf in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data,pd.DataFrame(extract_from_json(jsonf))],ignore_index = True)

    for xml in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xml))],ignore_index = True)

    return extracted_data

def transform(data):
    data['height'] = round(data.height * 0.0254,2)
    data['weight'] = round(data.weight * 0.45359237,2)
    return data

def load_data(target_file, data):
    data.to_csv(target_file)

def log_process(msg):
    timestamp_format = '%Y-%h-%d-%H-%M-%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as lfile:
        lfile.write(timestamp+','+msg+'\n')

log_process("ETL process start")

log_process("Extraction start")

extracted_data = extract()

log_process("Extraction done")

log_process("Transformation start")

transformed_data = transform(extracted_data)

print("Transformed Data is as follows")
print(transformed_data)

log_process("Transformation done")

log_process("Loading start")

load_data(target_file, transformed_data)

log_process("Loading done")

log_process("ETL process done")