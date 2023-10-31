import numpy as np
import pandas as pd

Teams = ["Team A travel time:", "Team B travel time:", "Team C travel time:", "Team D travel time:", "Team E travel time:", "Team F travel time:", "Total travel time:"]
def tableofsummary(list_df):
    summary = pd.DataFrame(
        {
            "Location" : '',
            "Number of Times Patrolled" : '',
            "Total Duration" : '',
        },
        index=[0],
    )
    traveltime = []
    for team in list_df:
        team_traveltime = 0
        for i in range(len(team)):
            row_team = team.iloc[i]
            if row_team['Action'] == 'Patrol':
                location = row_team['Location']
                duration = int(row_team['Duration'])
                occured = False
                for j in range(len(summary)):
                    row_summary = summary.iloc[j]
                    if row_summary['Location'] == location:
                        new_times = row_summary['Number of Times Patrolled'] + 1
                        new_duration = row_summary['Total Duration'] + duration
                        summary.loc[[j],'Number of Times Patrolled'] = new_times
                        summary.loc[[j],'Total Duration'] = new_duration
                        occured = True
                if occured == False:
                    new_row = pd.DataFrame(
                        {
                            "Location" : location,
                            "Number of Times Patrolled" : 1,
                            "Total Duration" : duration,
                        },
                        index=[0],
                    )                    
                    summary = pd.concat([summary, new_row], ignore_index=True)
            if row_team['Action'] == 'Travelling':
                team_traveltime += int(row_team['Duration'])
        traveltime.append(team_traveltime)
        
    summary = summary.drop(index=0)
    summary = summary.sort_values(by=['Total Duration'], ascending=False)
    summary = summary.reset_index(drop=True)
    totaltraveltime = sum(traveltime)
    traveltime.append(totaltraveltime)
    teams_traveltime = {"Teams": Teams, "Travel_Time": traveltime}
    traveltime_df = pd.DataFrame.from_dict(teams_traveltime)
    return summary, traveltime_df


def generatesummary(roster):
    Table_of_summary = tableofsummary(roster)[0]
    Teams_traveltime = tableofsummary(roster)[1]
    return Table_of_summary, Teams_traveltime



                        

