import numpy as np
import pandas as pd

avgspeed = 7.26
coord_list = [[0, 67], [6, 43], [16, 49], [16, 66], [17, 43], [17, 67], [23, 54], [26, 59], [27, 15], [28, 66], [32, 33], [34, 68], [38, 90], [42, 37], [43, 78], [43, 56], [45, 24], [47, 11], [48, 87], [50, 57], [60, 37], [63, 99], [67, 37], [69, 44], [73, 84], [73, 79], [76, 88], [76, 22], [78, 48], [78, 37], [79, 89], [79, 87], [81, 77], [82, 80], [83, 88], [85, 86], [86, 44], [87, 81], [87, 63], [87, 48], [92, 81], [99, 77]]
key_list = ['0067', '0643', '1649', '1666', '1743', '1767', '2354', '2659', '2715', '2866', '3233', '3468', '3890', '4237', '4378', '4356', '4524', '4711', '4887', '5057', '6037', '6399', '6737', '6944', '7384', '7379', '7688', '7622', '7848', '7837', '7989', '7987', '8177', '8280', '8388', '8586', '8644', '8781', '8763', '8748', '9281', '9977']
atn_list = ['West Entrance', 'Scholtz Express', 'Rhynasaurus Rampage', 'Wendisaurus Chase', 'Firefall', 'Jurassic Road', 'Eberlesaurus Roundup', 'Maiasaurus Madness', 'Galactosaurus Rage', 'Kristanodon Kaper', 'Creighton Pavilion', 'Paleocarrie Carousel', 'Auvilotops Express', 'Central Park Entrance 1', 'Raptor Race', "Kauf's Lost Canyon Escape", 'Atmosfear', 'Wrightiraptor Mountain', 'Squidosaur', 'Liggement Fix-Me-Up', 'Central Park Entrance 2', 'North Entrance', 'Central Park Entrance 3', 'Flight of the Swingodon', 'Flying TyrAndrienkos', 'Sauroma Bumpers', 'Beelzebufo', 'Mary Anning Beer Garden/Grinosaurus Stage', 'TerrorSaur', 'Ichthyoroberts Rapids', 'Enchanted Toadstools', 'Cyndisaurus Asteroid', 'Jeredactyl Jump', 'Stegocycles', 'Blue Iguanodon', 'Wild Jungle Cruise', 'Keimosaurus Big Spin', 'Stone Cups', 'SabreTooth Theatre', 'Dykesadactyl Thrill', 'North Line', 'East Entrance']
coord_name = {'0067': 'West Entrance', '0643': 'Scholtz Express', '1649': 'Rhynasaurus Rampage', '1666': 'Wendisaurus Chase', '1743': 'Firefall', '1767': 'Jurassic Road', '2354': 'Eberlesaurus Roundup', '2659': 'Maiasaurus Madness', '2715': 'Galactosaurus Rage', '2866': 'Kristanodon Kaper', '3233': 'Creighton Pavilion', '3468': 'Paleocarrie Carousel', '3890': 'Auvilotops Express', '4237': 'Central Park Entrance 1', '4378': 'Raptor Race', '4356': "Kauf's Lost Canyon Escape", '4524': 'Atmosfear', '4711': 'Wrightiraptor Mountain', '4887': 'Squidosaur', '5057': 'Liggement Fix-Me-Up', '6037': 'Central Park Entrance 2', '6399': 'North Entrance', '6737': 'Central Park Entrance 3', '6944': 'Flight of the Swingodon', '7384': 'Flying TyrAndrienkos', '7379': 'Sauroma Bumpers', '7688': 'Beelzebufo', '7622': 'Mary Anning Beer Garden/Grinosaurus Stage', '7848': 'TerrorSaur', '7837': 'Ichthyoroberts Rapids', '7989': 'Enchanted Toadstools', '7987': 'Cyndisaurus Asteroid', '8177': 'Jeredactyl Jump', '8280': 'Stegocycles', '8388': 'Blue Iguanodon', '8586': 'Wild Jungle Cruise', '8644': 'Keimosaurus Big Spin', '8781': 'Stone Cups', '8763': 'SabreTooth Theatre', '8748': 'Dykesadactyl Thrill', '9281': 'North Line', '9977': 'East Entrance'}
coorddict = {'West Entrance': [0, 67], 'Scholtz Express': [6, 43], 'Rhynasaurus Rampage': [16, 49], 'Wendisaurus Chase': [16, 66], 'Firefall': [17, 43], 'Jurassic Road': [17, 67], 'Eberlesaurus Roundup': [23, 54], 'Maiasaurus Madness': [26, 59], 'Galactosaurus Rage': [27, 15], 'Kristanodon Kaper': [28, 66], 'Creighton Pavilion': [32, 33], 'Paleocarrie Carousel': [34, 68], 'Auvilotops Express': [38, 90], 'Central Park Entrance 1': [42, 37], 'Raptor Race': [43, 78], "Kauf's Lost Canyon Escape": [43, 56], 'Atmosfear': [45, 24], 'Wrightiraptor Mountain': [47, 11], 'Squidosaur': [48, 87], 'Liggement Fix-Me-Up': [50, 57], 'Central Park Entrance 2': [60, 37], 'North Entrance': [63, 99], 'Central Park Entrance 3': [67, 37], 'Flight of the Swingodon': [69, 44], 'Flying TyrAndrienkos': [73, 84], 'Sauroma Bumpers': [73, 79], 'Beelzebufo': [76, 88], 'Mary Anning Beer Garden/Grinosaurus Stage': [76, 22], 'TerrorSaur': [78, 48], 'Ichthyoroberts Rapids': [78, 37], 'Enchanted Toadstools': [79, 89], 'Cyndisaurus Asteroid': [79, 87], 'Jeredactyl Jump': [81, 77], 'Stegocycles': [82, 80], 'Blue Iguanodon': [83, 88], 'Wild Jungle Cruise': [85, 86], 'Keimosaurus Big Spin': [86, 44], 'Stone Cups': [87, 81], 'SabreTooth Theatre': [87, 63], 'Dykesadactyl Thrill': [87, 48], 'North Line': [92, 81], 'East Entrance': [99, 77]}
def retrieve(keylist, namedict):
    result = []
    for i in keylist:
        if i in namedict:
            result.append(namedict[i])
    return result
def addnamedf(df, namedict):
    checklistx, checklisty, keylist = df['X'].values.tolist(), df['Y'].values.tolist(), []
    check = df.columns.get_loc("Y")+1
    for count in range(len(checklistx)):
        tempx, tempy = str(checklistx[count]), str(checklisty[count])
        if checklistx[count]<10:
            tempx = '0' + tempx
        if checklisty[count]<10:
            tempy = '0' + tempy
        keylist.append(tempx+tempy)
    namelist = retrieve(keylist, namedict)
    df.insert(loc=check, column='Attraction', value=namelist)
    return df

def minspeeddf(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df[df["type"].str.contains("movement") == False]
    df = df.sort_values(by=['id', 'Timestamp']).reset_index(drop=True)
    df = addnamedf(df, coord_name)
    result, mindf = pd.DataFrame({'Start':['-'], 'End':['-'], 'Time': [0]}), pd.DataFrame({'Start':['-'], 'End':['-'], 'Min Time': [0]})
    for count in range(len(df['id'])-1):
        if df['id'][count] == df['id'][count+1] and df['Attraction'][count] != df['Attraction'][count+1]:
            time1 = df['Timestamp'][count]
            time2 = df['Timestamp'][count+1]
            time = (time2 - time1).total_seconds() / 60
            result.loc[len(result)] = {'Start':df['Attraction'][count], 'End':df['Attraction'][count+1], 'Time':time}
    result = result.drop([0]).reset_index(drop=True)
    result = result.sort_values(by=['Start', 'End']).reset_index(drop=True)
    minvalue = 1000
    templist = [result['Start'][0], result['End'][0]]
    for count in range(len(result['Start'])):
        if [result['Start'][count], result['End'][count]] == templist:
            if result['Time'][count] < minvalue:
                minvalue = result['Time'][count]
        else:
            mindf.loc[len(mindf)] = {'Start':result['Start'][count-1], 'End':result['End'][count-1], 'Min Time':minvalue}
            templist = [result['Start'][count], result['End'][count]]
            minvalue = 1000
    mindf = mindf.drop([0]).reset_index(drop=True)
    for count in range(len(mindf['Start'])):
        mintime1, start, end, check = mindf['Min Time'][count], mindf['Start'][count], mindf['End'][count], False
        for i in range(len(mindf['Start'])):
            if mindf['Start'][i] == end and mindf['End'][i] == start:
                check = True
                tempindex = i
                break
        if check == True:
            mintime2 = mindf['Min Time'][tempindex]
            if mintime1 < mintime2:
                mindf.iloc[tempindex] = {'Start':end, 'End':start, 'Min Time':mintime1}
                mindf = mindf.reset_index(drop=True)
            else:
                mindf.iloc[count] = {'Start':start, 'End':end, 'Min Time':mintime2}
                mindf = mindf.reset_index(drop=True)
        else:
            mindf.loc[len(mindf)] = {'Start':end, 'End':start, 'Min Time':mintime1}
    return mindf

