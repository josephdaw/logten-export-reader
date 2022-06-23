import pandas as pd

logbook_file = '~/Desktop/flights_2022-06-22.csv'
# se_dual_day = 0

df_logbook_import = pd.read_csv(logbook_file, low_memory=False)
df_logbook_import[' flight_night'].fillna(0, inplace=True)

# print(type(df_logbook_import.loc[1][' flight_selectedCrewRelief']))


# rego = df_logbook_import['Aircraft ID']
# pic = df_logbook_import['PIC/P1 Crew']
route = df_logbook_import[' flight_from'] + '-' + df_logbook_import[' flight_to']

df_new_logbook = df_logbook_import[['flight_flightDate', ' aircraft_aircraftID', ' aircraftType_type', ' aircraftType_selectedCategory', ' flight_selectedCrewPIC', ' flight_selectedCrewSIC', ' flight_remarks']].copy()

# df_new_logbook.insert(1,"Rego", rego)
# df_new_logbook.insert(3,"Pilot in Command", pic)

# hard coded aeroplane as the aircraft category
# df_new_logbook.insert(3,"Aircraft Category", "Aeroplane")
df_new_logbook.insert(7,"Airports Visited", route)

# CALCULATING FLIGHT TIMES

# SINGLE ENGINE TIMES
 # aircraftType_selectedAircraftClass = 'Single-Engine'
 
# ICUS DAY
df_new_logbook.loc[(pd.isna(df_logbook_import[' flight_night']) &  (df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land')), 'SE ICUS Day'] = df_logbook_import[' flight_p1us']

# ICUS NIGHT
df_new_logbook.loc[((df_logbook_import[' flight_night'] > 0) &  (df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land')), 'SE ICUS Night'] = df_logbook_import[' flight_p1us']

# DUAL DAY
df_new_logbook.loc[((df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land') & (df_logbook_import[' flight_dualReceived'] > 0)), 'SE Dual Day'] = (df_logbook_import[' flight_dualReceived'] - (df_logbook_import[' flight_night'])) 

# DUAL NIGHT
df_new_logbook.loc[((df_logbook_import[' flight_night'] > 0) &  (df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land') & (df_logbook_import[' flight_dualReceived'] > 0)), 'SE Dual Night'] = df_logbook_import[' flight_night']

# PIC DAY
df_new_logbook.loc[(pd.isna(df_logbook_import[' flight_night']) &  (df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land')), 'SE PIC Day'] = df_logbook_import[' flight_pic']

# PIC NIGHT
df_new_logbook.loc[((df_logbook_import[' flight_night'] > 0) &  (df_logbook_import[' aircraftType_selectedAircraftClass'] == 'Single-Engine Land')), 'SE PIC Night'] = df_logbook_import[' flight_pic']

# CO-PILOT DAY
# df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'SE Copilot Day'] = df_logbook_import['SIC']
# co_pilot_day = 

# CO-PILOT NIGHT
# df_new_logbook.loc[df_logbook_import['Night'] > 0, 'SE Copilot Night'] = df_logbook_import['SIC']

# MULTI ENGINE TIMES
# ICUS DAY
# df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'ME ICUS Day'] = df_logbook_import['P1u/s']

# ICUS NIGHT
# DUAL DAY
# DUAL NIGHT
# PIC DAY
# PIC NIGHT
# CO-PILOT DAY
# CO-PILOT NIGHT


# df_new_logbook.insert(8,"SE Dual Day", se_dual_day)

sum_se_day_icus = df_new_logbook['SE ICUS Day'].sum(axis=0)
sum_se_night_icus = df_new_logbook['SE ICUS Night'].sum(axis=0)
sum_se_day_dual = df_new_logbook['SE Dual Day'].sum(axis=0)     #missing 0.6 from when night was entered in same line
sum_se_night_dual = df_new_logbook['SE Dual Night'].sum(axis=0) #printing correctly
sum_se_day_pic = df_new_logbook['SE PIC Day'].sum(axis=0)
sum_se_night_pic = df_new_logbook['SE PIC Night'].sum(axis=0)

sum_me_day_icus = 0
sum_me_night_icus = 0

# print("SE ICUS Day", round(sum_se_day_icus,2))
# print("SE ICUS Night", round(sum_se_night_icus,2))
# print("SE Dual Day", round(sum_se_day_dual,2))
# print("SE Dual Night", round(sum_se_night_dual,2))

hours = {
    "single_engine": {
        "ICUS Day": round(sum_se_day_icus,2),
        "ICUS Night": round(sum_se_night_icus,2),
        "Dual Day": round(sum_se_day_dual,2),
        "Dual Night": round(sum_se_night_dual,2),
        "PIC Day": round(sum_se_day_pic,2),
        "PIC Night": round(sum_se_night_pic,2),
        },
    "multi_engine":{
        "ICUS Day": round(sum_me_day_icus,2),
        "ICUS Night": round(sum_me_night_icus,2),
        }
        }

print(hours)

