import numpy as np
import pandas as pd

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

def createnewdf():
    df = pd.DataFrame(
        {
            "Time": '',
            "Location": '',
            "Action": '',
            "Duration": '',
        },
        index=[0],
    )
    return df   

def cleanpatrolplan(df):
    cleanplan_df = df.dropna()
    cleanplan_df = combine_patrol_data(cleanplan_df)
    cleanplan_df['Time'] = pd.to_datetime(cleanplan_df['Time'])
    cleanplan_df['Time'] = pd.DatetimeIndex(cleanplan_df['Time']).time
    last_row = cleanplan_df.iloc[-1]
    if last_row["Action"] in ["End Patrol", "Start Patrol"]:
        pass
    if last_row["Action"] == "Patrolling":
        # Add a row at the end with action of End Patrol with same Time, and Location.
        new_row = pd.DataFrame(
            {
                "Time": last_row["Time"],
                "Location": last_row["Location"],
                "Action": "End Patrol",
                "Duration": "-",
            },
            index=[0],
        )

        # Add the new row to the patrol plan data.
        cleanplan_df = pd.concat([cleanplan_df, new_row], ignore_index=True)

    cleanplan_df = cleanplan_df.dropna(ignore_index=True)
    
    FinalPatrolPlan = createnewdf()
    Standdowntime = ''
    for i in range(len(cleanplan_df)- 1):
        row = cleanplan_df.iloc[i]
        row2 = cleanplan_df.iloc[i+1]
        if row["Action"] == "Start Patrol":
            new_row = pd.DataFrame(
            {
                "Time": row["Time"] ,
                "Location": row["Location"],
                "Action": row["Action"],
                "Duration": row["Duration"],
            },
            index=[0],
            )
            FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)
            if row2["Action"] == "Patrolling":
                newtiming = str(row["Time"]) + " - " + str(row2["Time"])
                new_row = pd.DataFrame(
                {
                    "Time": newtiming ,
                    "Location": row["Location"],
                    "Action": "Patrol",
                    "Duration": row2["Duration"],
                },
                index=[0],
                )
                FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)
        if row["Action"] == "End Patrol":
            pass
        if row["Action"] == "Start travelling":
            if row2["Action"] == "End travelling":
                newtiming = str(row["Time"]) + " - " + str(row2["Time"])
                newlocation = "To " + row2["Location"]
                new_row = pd.DataFrame(
                {
                    "Time": newtiming ,
                    "Location": newlocation,
                    "Action": "Travelling",
                    "Duration": row["Duration"],
                },
                index=[0],
                )
                FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)
        if row["Action"] == "End travelling":
            if row2["Action"] == "Patrolling":
                newtiming = str(row["Time"]) + " - " + str(row2["Time"])
                new_row = pd.DataFrame(
                {
                    "Time": newtiming ,
                    "Location": row2["Location"],
                    "Action": "Patrol",
                    "Duration": row2["Duration"],
                },
                index=[0],
                )
                FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)                               
        if row["Action"] == "Start Break":
            if row2["Action"] == "End Break":
                if int(row["Duration"]) == 30:
                    newaction = "Short Break"
                if int(row["Duration"]) == 60:
                    newaction = "Official Ease"
                newtiming = str(row["Time"]) + " - " + str(row2["Time"])
                new_row = pd.DataFrame(
                {
                    "Time": newtiming ,
                    "Location": row["Location"],
                    "Action": newaction,
                    "Duration": row["Duration"],
                },
                index=[0],
                )
                FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)
        if i == (len(cleanplan_df) - 2):
            Standdowntime = str(row["Time"]) 

    new_row = pd.DataFrame(
    {
        "Time": Standdowntime,
        "Location": "To Base",
        "Action": "Stand Down",
        "Duration": "-",
    },
    index=[0],
    )
                                          
    FinalPatrolPlan = pd.concat([FinalPatrolPlan, new_row], ignore_index=True)
    FinalPatrolPlan = FinalPatrolPlan.drop(index=0)
    return FinalPatrolPlan

##Logic
clean_roster = []
def cleanroster(roster):
    for team in roster:
        cleanteam = cleanpatrolplan(team)
        clean_roster.append(cleanteam)
    return clean_roster
