import numpy as np
import pandas as pd
import math as math
from datetime import datetime, timedelta
import glob
from zipfile import ZipFile

def identify_problem(df):  #checks both coords are valid as well as whether the movements are plausible
    df['X'] = df['X'].astype(int)
    df['Y'] = df['Y'].astype(int)
    checklist = df['X'].values.tolist()
    checklist2 = df['Y'].values.tolist()
    checklist.extend(checklist2)
    for count in range(len(df)):
        if checklist[count]<0 or checklist[count]>100:
            return False
    df = df.sort_values(by=['id', 'Timestamp'])
    df = df.drop(columns=['type'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    checklist = df.values.tolist()
    problem_id = []
    for count in range(len(checklist)-1):
        if checklist[count][1] == checklist[count+1][1]:
            dist = distance(checklist, count)
            time = abs(checklist[count+1][0] - checklist[count][0])
            time = time.total_seconds()
            if time == 0.0 and dist > 0.0:
                speed = "infinite"  
                if checklist[count][1] not in problem_id:
                    problem_id.append(checklist[count][1])
            if time == 0.0 and dist == 0.0:
                speed = 0
            if time > 0.0 and dist > 0.0:
                speed = dist / time
                if speed > 1.0: #this number come from avverage speed and tested data with fri and sat
                    if checklist[count][1] not in problem_id:
                        problem_id.append(checklist[count][1])
    return(problem_id)

def clean_data(df, list):
    clean_df = df[~df['id'].isin(list)]
    clean_df = clean_df.reset_index(drop=True)
    date = df.iloc[0]['Timestamp']
    date = date[0:9]
    return clean_df

def distance(list, a):
    Px = list[a][2]
    Py = list[a][3]
    Qx = list[a+1][2]
    Qy = list[a+1][3]
    dist = math.dist([Px, Py], [Qx, Qy])
    return dist

combinedcleandata_datetime = pd.DataFrame()
combinedcleandata_time = pd.DataFrame()

def process(all_files):

    #load all zip files in folder
    container = []

    all_files= glob.glob(all_files + "/*.zip")

    for filename in all_files:
         zip_file = ZipFile(filename)
    for text_file in zip_file.infolist():
        if text_file.filename.endswith('.csv'):
            df = pd.read_csv(zip_file.open(text_file.filename))
            container.append(df)

    cleandata = []
    for name in container:
        id = identify_problem(name)
        clean = clean_data(name, id)
        cleandata.append(clean)
    
    combinedcleandata_datetime = pd.concat(cleandata, ignore_index =True)
    combinedcleandata_datetime['Timestamp'] = pd.to_datetime(combinedcleandata_datetime['Timestamp'])

    combinedcleandata_time = pd.concat(cleandata, ignore_index =True)
    combinedcleandata_time['Timestamp'] = pd.to_datetime(combinedcleandata_time['Timestamp'])
    combinedcleandata_time['Timestamp'] = pd.to_datetime(combinedcleandata_time['Timestamp']).apply(lambda x: x.replace(year=2023, month=1, day=1))

    return combinedcleandata_datetime, combinedcleandata_time
