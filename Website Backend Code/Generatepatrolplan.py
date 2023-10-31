import numpy as np
import pandas as pd
import math as math
from datetime import datetime, timedelta
import string
import itertools
import time
import random


## Global variable
avgspeed = 7.26
coord_list = [[0, 67], [6, 43], [16, 49], [16, 66], [17, 43], [17, 67], [23, 54], [26, 59], [27, 15], [28, 66], [32, 33], [34, 68], [38, 90], [42, 37], [43, 78], [43, 56], [45, 24], [47, 11], [48, 87], [50, 57], [60, 37], [63, 99], [67, 37], [69, 44], [73, 84], [73, 79], [76, 88], [76, 22], [78, 48], [78, 37], [79, 89], [79, 87], [81, 77], [82, 80], [83, 88], [85, 86], [86, 44], [87, 81], [87, 63], [87, 48], [92, 81], [99, 77]]
key_list = ['0067', '0643', '1649', '1666', '1743', '1767', '2354', '2659', '2715', '2866', '3233', '3468', '3890', '4237', '4378', '4356', '4524', '4711', '4887', '5057', '6037', '6399', '6737', '6944', '7384', '7379', '7688', '7622', '7848', '7837', '7989', '7987', '8177', '8280', '8388', '8586', '8644', '8781', '8763', '8748', '9281', '9977']
atn_list = ['West Entrance', 'Scholtz Express', 'Rhynasaurus Rampage', 'Wendisaurus Chase', 'Firefall', 'Jurassic Road', 'Eberlesaurus Roundup', 'Maiasaurus Madness', 'Galactosaurus Rage', 'Kristanodon Kaper', 'Creighton Pavilion', 'Paleocarrie Carousel', 'Auvilotops Express', 'Central Park Entrance 1', 'Raptor Race', "Kauf's Lost Canyon Escape", 'Atmosfear', 'Wrightiraptor Mountain', 'Squidosaur', 'Liggement Fix-Me-Up', 'Central Park Entrance 2', 'North Entrance', 'Central Park Entrance 3', 'Flight of the Swingodon', 'Flying TyrAndrienkos', 'Sauroma Bumpers', 'Beelzebufo', 'Mary Anning Beer Garden/Grinosaurus Stage', 'TerrorSaur', 'Ichthyoroberts Rapids', 'Enchanted Toadstools', 'Cyndisaurus Asteroid', 'Jeredactyl Jump', 'Stegocycles', 'Blue Iguanodon', 'Wild Jungle Cruise', 'Keimosaurus Big Spin', 'Stone Cups', 'SabreTooth Theatre', 'Dykesadactyl Thrill', 'North Line', 'East Entrance']
coord_name = {'0067': 'West Entrance', '0643': 'Scholtz Express', '1649': 'Rhynasaurus Rampage', '1666': 'Wendisaurus Chase', '1743': 'Firefall', '1767': 'Jurassic Road', '2354': 'Eberlesaurus Roundup', '2659': 'Maiasaurus Madness', '2715': 'Galactosaurus Rage', '2866': 'Kristanodon Kaper', '3233': 'Creighton Pavilion', '3468': 'Paleocarrie Carousel', '3890': 'Auvilotops Express', '4237': 'Central Park Entrance 1', '4378': 'Raptor Race', '4356': "Kauf's Lost Canyon Escape", '4524': 'Atmosfear', '4711': 'Wrightiraptor Mountain', '4887': 'Squidosaur', '5057': 'Liggement Fix-Me-Up', '6037': 'Central Park Entrance 2', '6399': 'North Entrance', '6737': 'Central Park Entrance 3', '6944': 'Flight of the Swingodon', '7384': 'Flying TyrAndrienkos', '7379': 'Sauroma Bumpers', '7688': 'Beelzebufo', '7622': 'Mary Anning Beer Garden/Grinosaurus Stage', '7848': 'TerrorSaur', '7837': 'Ichthyoroberts Rapids', '7989': 'Enchanted Toadstools', '7987': 'Cyndisaurus Asteroid', '8177': 'Jeredactyl Jump', '8280': 'Stegocycles', '8388': 'Blue Iguanodon', '8586': 'Wild Jungle Cruise', '8644': 'Keimosaurus Big Spin', '8781': 'Stone Cups', '8763': 'SabreTooth Theatre', '8748': 'Dykesadactyl Thrill', '9281': 'North Line', '9977': 'East Entrance'}
coorddict = {'West Entrance': [0, 67], 'Scholtz Express': [6, 43], 'Rhynasaurus Rampage': [16, 49], 'Wendisaurus Chase': [16, 66], 'Firefall': [17, 43], 'Jurassic Road': [17, 67], 'Eberlesaurus Roundup': [23, 54], 'Maiasaurus Madness': [26, 59], 'Galactosaurus Rage': [27, 15], 'Kristanodon Kaper': [28, 66], 'Creighton Pavilion': [32, 33], 'Paleocarrie Carousel': [34, 68], 'Auvilotops Express': [38, 90], 'Central Park Entrance 1': [42, 37], 'Raptor Race': [43, 78], "Kauf's Lost Canyon Escape": [43, 56], 'Atmosfear': [45, 24], 'Wrightiraptor Mountain': [47, 11], 'Squidosaur': [48, 87], 'Liggement Fix-Me-Up': [50, 57], 'Central Park Entrance 2': [60, 37], 'North Entrance': [63, 99], 'Central Park Entrance 3': [67, 37], 'Flight of the Swingodon': [69, 44], 'Flying TyrAndrienkos': [73, 84], 'Sauroma Bumpers': [73, 79], 'Beelzebufo': [76, 88], 'Mary Anning Beer Garden/Grinosaurus Stage': [76, 22], 'TerrorSaur': [78, 48], 'Ichthyoroberts Rapids': [78, 37], 'Enchanted Toadstools': [79, 89], 'Cyndisaurus Asteroid': [79, 87], 'Jeredactyl Jump': [81, 77], 'Stegocycles': [82, 80], 'Blue Iguanodon': [83, 88], 'Wild Jungle Cruise': [85, 86], 'Keimosaurus Big Spin': [86, 44], 'Stone Cups': [87, 81], 'SabreTooth Theatre': [87, 63], 'Dykesadactyl Thrill': [87, 48], 'North Line': [92, 81], 'East Entrance': [99, 77]}
HeadCount = 15
Manpower = HeadCount * 0.8
shift_numbers = int(Manpower // 2)
shift_teams = int(shift_numbers // 2)
alphs = list(string.ascii_uppercase)
teams = []
shift1start = 8
shift1end = 17
shift2start = 15
shift2end = 24
teamnames = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F"]
breaktime, traveltime = 0, 0
sortingruntime = 10

# All functions
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

# Function to create the popularity of each attraction
def popularity_checkin(df, time):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    if time == "day":
        checkin = df[df["type"].str.contains("movement") == False]
        checkin = checkin.groupby(['X', 'Y']).size().reset_index(name='count')
        checkin = checkin.sort_values(by=['count'], ascending=False)
        checkin = checkin.reset_index(drop=True)
        checkin = addnamedf(checkin, coord_name)
        checkin['percentage'] = checkin['count'].apply(lambda x: x / checkin['count'].sum())
        return(checkin)
    
    if (type(time) is pd.Timestamp) == True:
        checkin = df[df["type"].str.contains("movement") == False]
        checkin = checkin[(checkin['Timestamp'] >= time) & (checkin['Timestamp'] < time + pd.Timedelta(minutes=60))]
        checkin = checkin.groupby(['X', 'Y']).size().reset_index(name='count')
        checkin = checkin.sort_values(by=['count'], ascending=False)
        checkin = checkin.reset_index(drop=True)
        checkin = addnamedf(checkin, coord_name)
        checkin['percentage'] = checkin['count'].apply(lambda x: x / checkin['count'].sum())
        return(checkin)

def checkout_entrances(df, time):
    entrances = [[0, 67], [99, 77], [63, 99]]
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    if (type(time) is pd.Timestamp) == True:
        movement = df[df["type"].str.contains("movement") == True]
        movement = movement[(movement['Timestamp'] >= time) & (movement['Timestamp'] < time + pd.Timedelta(minutes=60))]
        movement = movement.groupby(['X', 'Y']).size().reset_index(name='count')
        movement = movement[movement.apply(lambda row: [row['X'], row['Y']] in entrances, axis=1)]
        movement = movement.sort_values(by=['count'], ascending=False)
        movement = movement.reset_index(drop=True)
        movement = addnamedf(movement, coord_name)
        movement['percentage'] = movement['count'].apply(lambda x: x / movement['count'].sum())
        return(movement)

def teamsonshift(dthour):
    timing = int(dthour.strftime('%H'))
    if shift1start <= timing < shift2start:
        teams = [0, 1, 2]
    if shift2start <= timing < shift1end:
        teams = [0, 1, 2, 3, 4, 5]
    if shift1end<= timing <= shift2end:
        teams = [3, 4, 5]
    return teams

def time_gen(df, measurementoftime):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    time_min = df['Timestamp'].min()
    time_max = df['Timestamp'].max()
    time_min = time_min.replace(minute=0, second=0, microsecond=0)
    time_max = time_max.replace(minute=0, second=0, microsecond=0)
    time_range = pd.date_range(time_min, time_max, freq= measurementoftime) 
    return(time_range)   

#creating two new variables patrol and leftovers
def gencleandf(daycheckin):
    df = daycheckin
    df = df.drop(columns=['count', 'percentage'])
    df = df.assign(manhours = 0)
    return df

def createroster(first_hour, numofteams, teams): #gen list of whole day teams df
    act, dur, entr, hour = ['Start Patrol'], ['-'], ['North Entrance', 'West Entrance', 'East Entrance'], first_hour
    for i in range(numofteams):
        if numofteams/(i+1)<2:
            hour = first_hour + timedelta(hours=7)
        loc = [entr[i%3]]
        team = pd.DataFrame({'Time':hour, 'Location':loc, 'Action':act, 'Duration':dur})
        teams.append(team)
    return teams

def travelling(start, end):
    start_coord, end_coord = coorddict[start], coorddict[end]
    xcoord = [start_coord[0], end_coord[0]]
    ycoord = [start_coord[1], end_coord[1]]
    dist = math.dist(xcoord, ycoord)
    if dist == 0.0:
        return 0
    trvtime = dist / avgspeed + 5.0
    return trvtime
def new_travelling(start, end, mintimes):
    for count in range(len(mintimes['Min Time'])):
        if mintimes['Start'][count] == start and mintimes['End'][count] == end:
            trvtime = mintimes['Min Time'][count]
            if trvtime < 5:
                return 5
            elif trvtime > 20:
                return travelling(start, end)
            else:
                return trvtime
    return travelling(start, end)

def split_list_into_sublists(list_to_split, separator_list):
  sublists = []
  for size in separator_list:
    sublist = []
    for i in range(size):
      sublist.append(list_to_split[0])
      list_to_split = list_to_split[1:]
    sublists.append(sublist)
  return sublists

def combine_patrol_data(patrolplan):
    combinepatrol = pd.DataFrame(
        {
            "Time": '',
            "Location": '',
            "Action": '',
            "Duration": '',
        },
        index=[0],
    )
    if len(patrolplan) == 1:
        return patrolplan
    combined = False
    for i in range(len(patrolplan) - 1):
        combined_duration = 0
        row = patrolplan.iloc[i]
        row2 = patrolplan.iloc[i+1]
        if (row["Action"] == "Patrolling") and (row2["Action"] == "Patrolling") and (row["Location"] == row2["Location"] and combined == False):
            combined = True
            combined_duration = int(row["Duration"]) + int(row2["Duration"])
            while True:
                i += 1
                if i >= (len(patrolplan) - 1):
                    new_row = pd.DataFrame(
                    {
                        "Time": row2["Time"],
                        "Location": row2["Location"],
                        "Action": row2["Action"],
                        "Duration": combined_duration,
                    },
                    index=[0],
                    )
                    combinepatrol = pd.concat([combinepatrol, new_row], ignore_index=True)
                    return combinepatrol
                row = patrolplan.iloc[i]
                row2 = patrolplan.iloc[i+1]
                if (row["Action"] == "Patrolling") and (row2["Action"] == "Patrolling") and (row["Location"] == row2["Location"]):
                    combined_duration += int(row2["Duration"])
                else:
                    break
            new_row = pd.DataFrame(
            {
                "Time": row["Time"],
                "Location": row["Location"],
                "Action": row["Action"],
                "Duration": combined_duration,
            },
            index=[0],
            )
            combinepatrol = pd.concat([combinepatrol, new_row], ignore_index=True)
        elif combined == False:
            new_row = pd.DataFrame(
            {
                "Time": row["Time"],
                "Location": row["Location"],
                "Action": row["Action"],
                "Duration": row["Duration"],
            },
            index=[0],
            )
            combinepatrol = pd.concat([combinepatrol, new_row], ignore_index=True)
        elif row2["Action"] == "End Patrol":
            combined = False

    last_row = patrolplan.iloc[-1]
    combinepatrollast = combinepatrol.iloc[-1]
    if last_row["Location"] == combinepatrollast["Location"] and last_row["Action"] == combinepatrollast["Action"]:
        pass
    else:
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": last_row["Action"],
            "Duration": last_row["Duration"],
        },
        index=[0],
        )
    combinepatrol = pd.concat([combinepatrol, new_row], ignore_index=True)

    return combinepatrol            
                            
def sortingalgo(df, no_teams, teams_dfs, teamspatroltiming, timing, mintimes):
    df = df.dropna().reset_index(drop=True)
    df = df[df.manhours != 0]
    df['manhours (in 15min)'] = df['manhours'].apply(lambda x: x / 15)
    df['manhours (in 15min)'] = df['manhours (in 15min)'].astype('int')
    attractions = df['Attraction'].tolist()
    attraction_list = []
    for attraction in attractions:
        attraction_list.extend([attraction] * df['manhours (in 15min)'][df['Attraction'] == attraction].values[0])
    timing = timing.strftime('%Y-%m-%d %H:%M:%S')
    timing = timing[10:]
    timing = timing[:3]
    timing = int(timing)
    if shift1start <= timing < shift2start:
        teams = [0, 1, 2]
    if shift2start <= timing < shift1end:
        teams = [0, 1, 2, 3, 4, 5]
    if shift1end<= timing < shift2end:
        teams = [3, 4, 5]
    patrol = []
    for i in teams:
        patrol.append(teams_dfs[i])
    teamname = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F" }
    startpoints = []
    for a in range(len(teams)):
        lastpoint = patrol[a].tail(1)['Location'].iloc[-1]
        startpoints.append(lastpoint)

    temp_attraction = []
    for j in range(len(startpoints)):
        for k in range(len(attraction_list)):
                if startpoints[j] == attraction_list[k]:
                    if teamspatroltiming[j] != 0:
                        teamspatroltiming[j] = teamspatroltiming[j] - 1
                        team = teams[j]
                        new_time = teams_dfs[team].tail(1)['Time'].iloc[-1] + pd.Timedelta(minutes=15)
                        new_row = {'Time': new_time, 'Location':attraction_list[k], 'Action':'Patrolling', 'Duration':15}
                        teams_dfs[team] = pd.concat([teams_dfs[team], pd.DataFrame([new_row])], ignore_index=True)
                    else:
                        temp_attraction.append(attraction_list[k])
                else:
                    temp_attraction.append(attraction_list[k])
        attraction_list = temp_attraction
        temp_attraction = []
    for count, patrolplan in enumerate(teams_dfs):
        patrolplan = combine_patrol_data(patrolplan)
        teams_dfs[count] = patrolplan

    # Calculate the total number of slots needed
    total_slots = sum(teamspatroltiming)
    # Initialize variables to track the best plan and its minimum traveling time
    best_patrol_plan = None
    min_total_travel_time = float('inf')
    if total_slots < 7:
        # Create a list of all possible permutations for each team
        all_permutations = []
        working_permutation = list(itertools.permutations(attraction_list))
        for working in working_permutation:
            start_index = 0
            all_permutations.append([])
            for slots in teamspatroltiming:
                all_permutations[-1].append(list(working[start_index:start_index+slots]))
                start_index += slots
        patrol_plans_with_startpoints = []
        for patrol_plan in all_permutations:
            patrol_plan_with_startpoint = []
            for team_patrol,startpoint in zip(patrol_plan,startpoints):
                # Include the starting point for the team
                if len(team_patrol) == 0:
                    patrol_plan_with_startpoint.append([])
                else:
                    team_patrol.insert(0,startpoint)
                    patrol_plan_with_startpoint.append(team_patrol)
            patrol_plans_with_startpoints.append(patrol_plan_with_startpoint)

        for permutation in patrol_plans_with_startpoints:
            total_travel_time = 0
        
            # Calculate traveling time for each team's assigned attractions
            for team_attractions in permutation:
                
                # Calculate traveling time between attractions for the current team
                for i in range(len(team_attractions) - 1):
                    total_travel_time += new_travelling(team_attractions[i], team_attractions[i + 1], mintimes)
            
            # Update the best plan if this plan has a lower total traveling time
            if total_travel_time < min_total_travel_time:
                min_total_travel_time = total_travel_time
                best_patrol_plan = permutation

        ##print("Best Patrol Plan:", best_patrol_plan)
        ##print("Min Total Travel Time:", min_total_travel_time)
    else:
        start_time = time.time()
        seconds = sortingruntime #the timing of running the code Actual generating of csv will be 3 min

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time > seconds:
                print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
                break
            else:
                random.shuffle(attraction_list)
                start_index = 0
                onepermutation = []
                for slots in teamspatroltiming:
                    if slots == 0:
                        onepermutation.append([])
                    else:
                        onepermutation.append(list(attraction_list[start_index:start_index+slots]))
                        start_index += slots

                patrol_plan_with_startpoint = []
                for team_patrol,startpoint in zip(onepermutation,startpoints):
                    # Include the starting point for the team
                    if len(team_patrol) > 0:
                        team_patrol.insert(0,startpoint)
                        patrol_plan_with_startpoint.append(team_patrol)
                    else:
                        patrol_plan_with_startpoint.append([])

                total_travel_time = 0
                
                # Calculate traveling time for each team's assigned attractions
                for team_attractions in patrol_plan_with_startpoint:

                    if(len(team_attractions) == 0):
                        pass
                    else:    
                        # Calculate traveling time between attractions for the current team
                        for i in range(len(team_attractions) - 1):
                            total_travel_time += new_travelling(team_attractions[i], team_attractions[i + 1], mintimes)
                        
                        # Update the best plan if this plan has a lower total traveling time
                        if total_travel_time < min_total_travel_time:
                            min_total_travel_time = total_travel_time
                            best_patrol_plan = patrol_plan_with_startpoint

    return best_patrol_plan, teams_dfs

def breaktimeroster(teamsdf, timing):
    timing = timing.strftime('%Y-%m-%d %H:%M:%S')
    timing = timing[10:]
    timing = timing[:3]
    timing = int(timing) 
    if timing == 9 : # Team A 30 min Break
        duration = 30
        team = 0
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)

    elif timing == 10 : # Team B 30 min Break
        duration = 30
        team = 1
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )        
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)

    elif timing == 11 : # Team C 30 min Break
        duration = 30
        team = 2
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )        
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)

    elif timing == 12: # Team A 60 min Break
        duration = 60
        team = 0
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )        
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 13 : # Team B 60 min Break
        duration = 60
        team = 1
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 14 : # Team C 60 min Break
        duration = 60
        team = 2
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 17: # Team D 60 min Break
        duration = 60
        team = 3
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)

    elif timing == 18: # Team E 60 min Break
        duration = 60
        team = 4
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 19: # Team F 60 min Break
        duration = 60
        team = 5
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 20: # Team D 30 min Break
        duration = 30
        team = 3
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)

    elif timing == 21: # Team E 30 min Break
        duration = 30
        team = 4
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    

    elif timing == 22: # Team F 30 min Break
        duration = 30
        team = 5
        last_row = teamsdf[team].iloc[-1]
        first_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "End Patrol",
            "Duration": "-",
        },
        index=[0],
        )
        new_row = pd.DataFrame(
        {
            "Time": last_row["Time"],
            "Location": last_row["Location"],
            "Action": "Start Break",
            "Duration": duration,
        },
        index=[0],
        )
        new_row2 = pd.DataFrame(
        {
            "Time": (last_row["Time"] + pd.Timedelta(minutes=duration)),
            "Location": last_row["Location"],
            "Action": "End Break",
            "Duration": "-",
        },
        index=[0],
        )
        teamsdf[team] = pd.concat([teamsdf[team], first_row, new_row, new_row2], ignore_index=True)    
    
    else :
        duration = 0
    
    return teamsdf, duration
    
def simplerounding(x):
    if x > 0:
        x = math.floor(x)
    else:
        x = 0
    return x

def allocatetime(teams, dthour, numof15mins): #dthour is in datetime format
    allocation, timesleft= [], []
    teams_indexes = teamsonshift(dthour)
    numofteams = len(teams_indexes)
    for team_index in teams_indexes:
        time = teams[team_index]['Time'][len(teams[team_index]['Time'])-1]
        print(time)
        prev_min = int(time.strftime('%M'))
        if time < dthour:
            leftover = prev_min - 60
        else:
            leftover = prev_min
        timesleft.append(leftover)
    for count in range(len(timesleft)):
        i = timesleft[count]
        counter = math.floor(abs(i/15))
        if i < 0:
            allocation.append(counter)
            counter = -counter
        else:
            allocation.append(-counter)
        timesleft[count] -= counter*15
        numof15mins += counter
    num15mins = math.floor(numof15mins/numofteams)
    remaining = numof15mins - num15mins * numofteams
    for count in range(numofteams):
        allocation[count] += num15mins
        timesleft[count] += num15mins * 15
    for count in range(remaining):
        minpos = timesleft.index(min(timesleft))
        allocation[minpos] += 1
        timesleft[minpos] += 15    
    for count in range(len(allocation)):
        while allocation[count] < 0:
            timesleft[count] = -999
            maxpos = timesleft.index(max(timesleft))
            allocation[maxpos] -= 1
            timesleft[maxpos] -= 15
            allocation[count] += 1
    return allocation

def addtoroster(teams, best_patrol_plan, dthour, mintimes):
    teams_indexes, totaltrvttime = teamsonshift(dthour), 0
    for count in range(len(best_patrol_plan)):
        if len(best_patrol_plan[count]) == 0:
            continue
        team_index = teams_indexes[count]
        for i in range(len(best_patrol_plan[count])-1):
            team = teams[team_index]
            start = best_patrol_plan[count][i]
            end = best_patrol_plan[count][i+1]
            if start != end:
                prev_time, prev_action = team['Time'][len(team['Time'])-1], team['Action'][len(team['Time'])-1]
                if prev_action == 'Patrolling':
                    teams[team_index].loc[len(teams[team_index])] = {'Time': prev_time, 'Location': start, 'Action': 'End Patrol', 'Duration': '-'}
                traveltime = math.ceil(new_travelling(start, end, mintimes))
                totaltrvttime += traveltime
                team.loc[len(team)] = {'Time': prev_time, 'Location': start, 'Action': 'Start travelling', 'Duration': traveltime}
                team.loc[len(team)] = {'Time': prev_time+timedelta(minutes=traveltime), 'Location': end, 'Action': 'End travelling', 'Duration': '-'}
                teams[team_index] = team
            prev_time = team['Time'][len(team['Time'])-1]
            teams[team_index].loc[len(teams[team_index])] = {'Time': prev_time+timedelta(minutes=15), 'Location': end, 'Action': 'Patrolling', 'Duration': 15}
        prev_time = team['Time'][len(team['Time'])-1]
        teams[count] = combine_patrol_data(teams[count])
    return teams, totaltrvttime

## Logic
def uncleanpatrol(mintimes, combinedata):
    combinedata['Timestamp'] = pd.to_datetime(combinedata['Timestamp'])
    start_hour = time_gen(combinedata, 'H')
    daycheckin = popularity_checkin(combinedata, "day")
    patroltiming_df =gencleandf(daycheckin)
    leftovers_df = gencleandf(daycheckin)
    fri_roster = createroster(start_hour[0], shift_numbers, teams) 
    roster_day = fri_roster
    traveltime = 0
    for i in range(len(start_hour)):
        rosteringwithbreak =breaktimeroster(roster_day,start_hour[i])
        roster_day = rosteringwithbreak[0]
        breaktime = rosteringwithbreak[1]
        if 7 <= i < 9:
            noofteam = Manpower / 2
        else: 
            noofteam = Manpower / 4
        checkinhour_df = popularity_checkin(combinedata, start_hour[i])
        manhours = 60 * noofteam - breaktime - traveltime
        noof15min = math.floor(manhours / 15)
        manhours_15min = noof15min * 15
        ##to add last checkout for last hour
        if start_hour[i] == start_hour[-1]:
            entranceslasthour = checkout_entrances(combinedata, start_hour[i])
            combined_df = pd.concat([checkinhour_df, entranceslasthour], ignore_index=True)
            combined_df.drop(columns=['percentage'])
            combined_df['percentage'] = combined_df['count'].apply(lambda x: x / combined_df['count'].sum())
        else:
            combined_df = checkinhour_df

        combined_df['manhours'] = combined_df['percentage'].apply(lambda x: x * manhours_15min)
        patroltiming_df = gencleandf(daycheckin)
        timing_df = gencleandf(daycheckin)
        timing_df['manhours'] = timing_df['Attraction'].map(combined_df.set_index('Attraction')['manhours'])
        timing_df = timing_df.fillna(0)
        ##map the previous leftover manhours
        timing_df['manhours (leftovers)'] = timing_df['Attraction'].map(leftovers_df.set_index('Attraction')['manhours'])
        timing_df['manhours (final)'] = timing_df.apply(lambda x: x['manhours'] + x['manhours (leftovers)'], axis=1)
        timing_df['manhours'] = timing_df['manhours (final)']
        timing_df = timing_df.drop(["manhours (leftovers)", "manhours (final)"], axis='columns')
        timing_df = timing_df.fillna(0)
        leftovers_df = gencleandf(daycheckin)

        timing_df['manhours (in 15min)'] = timing_df['manhours'].apply(lambda x: x / 15)
        timing_df['manhours (denominator)'] = timing_df['manhours (in 15min)'].apply(lambda x: simplerounding(x))
        timing_df['manhours (remainder)'] = timing_df.apply(lambda x: x['manhours (in 15min)'] - x['manhours (denominator)'] , axis=1)
        timing_df = timing_df.sort_values(by=['manhours (remainder)'], ascending=False)
        timing_df = timing_df.reset_index(drop=True)
        noof15minleft = noof15min - timing_df['manhours (denominator)'].sum()
        for j in range(noof15minleft):
            timing_df.at[j, 'manhours (denominator)'] = timing_df.iloc[j]['manhours (denominator)'] + 1
            timing_df.at[j, 'manhours (remainder)'] = timing_df.iloc[j]['manhours (remainder)'] - 1
        print(timing_df)
        timing_df['manhours (timeowed/repay)'] = timing_df['manhours (remainder)'].apply(lambda x: x * 15)
        timing_df['manhours (to patrol)'] = timing_df['manhours (denominator)'].apply(lambda x: x * 15)
        patroltiming_df['manhours (temporary)'] = patroltiming_df['Attraction'].map(timing_df.set_index('Attraction')['manhours (to patrol)'])
        patroltiming_df['manhours (final)'] = patroltiming_df.apply(lambda x: x['manhours'] + x['manhours (temporary)'], axis=1)
        patroltiming_df['manhours'] = patroltiming_df['manhours (final)']
        patroltiming_df = patroltiming_df.drop(["manhours (temporary)", "manhours (final)"], axis='columns')
        patroltiming_df = patroltiming_df.fillna(0)
        leftovers_df['manhours (temporary)'] = leftovers_df['Attraction'].map(timing_df.set_index('Attraction')['manhours (timeowed/repay)'])
        leftovers_df['manhours (final)'] = leftovers_df.apply(lambda x: x['manhours'] + x['manhours (temporary)'], axis=1)
        leftovers_df['manhours'] = leftovers_df['manhours (final)']
        leftovers_df = leftovers_df.drop(["manhours (temporary)", "manhours (final)"], axis='columns')
        leftovers_df = leftovers_df.fillna(0)
        print(leftovers_df)
        teampatroltiming = allocatetime(fri_roster, start_hour[i], noof15min)
        print(start_hour[i])
        print(noof15min)
        print(teampatroltiming)
        patrolteamsplit = sortingalgo(patroltiming_df, noofteam, fri_roster, teampatroltiming, start_hour[i], mintimes)
        bestpatrolplanforthehour = patrolteamsplit[0]
        fri_roster =patrolteamsplit[1]
        finaliserosterforhour = addtoroster(fri_roster, bestpatrolplanforthehour, start_hour[i], mintimes)
        roster_day = finaliserosterforhour[0]
        traveltime = finaliserosterforhour[1]

        print(bestpatrolplanforthehour)
    print(roster_day)
    return roster_day

