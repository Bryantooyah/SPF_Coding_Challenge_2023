import Combineandcleandata
import Generatemintraveltime
import Generatepatrolplan
import Cleanpatrolplan
import Generatetableofsummary
import pandas as pd


def getrosters(file_path, yesorno):
    combinedcleandata_datetime = Combineandcleandata.process(file_path)[0]
    combinedcleandata_time = Combineandcleandata.process(file_path)[1]
    combinedcleandata_datetime = pd.read_csv('combinedcleandatainDatetime.csv')
    print('Cleaned')
    print(yesorno)
    if yesorno == "yes":
        mintimes = pd.read_csv('Minimum Travel Times.csv')
        print('It doenst work')
    else:
        mintimes = Generatemintraveltime.minspeeddf(combinedcleandata_datetime)
        print('It works')
    unclean_roster = Generatepatrolplan.uncleanpatrol(mintimes, combinedcleandata_time)
    print('Generated')
    clean_roster = Cleanpatrolplan.cleanroster(unclean_roster)
    Table_of_summary = Generatetableofsummary.generatesummary(clean_roster)[0]
    Teams_traveltime = Generatetableofsummary.generatesummary(clean_roster)[1]
    clean_roster.append(Table_of_summary)
    clean_roster.append(Teams_traveltime)
    print(clean_roster)
    # teama = pd.read_csv('Patrol Plan for Team A.csv')
    # teamb = pd.read_csv('Patrol Plan for Team B.csv')
    # teamc = pd.read_csv('Patrol Plan for Team C.csv')
    # teamd = pd.read_csv('Patrol Plan for Team D.csv')
    # teame = pd.read_csv('Patrol Plan for Team E.csv')
    # teamf = pd.read_csv('Patrol Plan for Team F.csv')
    # table = pd.read_csv('Table of Summary.csv')
    # traveltime = pd.read_csv('Teams Travel Time.csv')
    # clean_roster = [teama,teamb,teamc,teamd,teame,teamf,table,traveltime]
    return clean_roster
