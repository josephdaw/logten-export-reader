import pandas as pd

logbook_file = '~/Desktop/flights_2022-06-22.csv'
# se_dual_day = 0

df_logbook_import = pd.read_csv(logbook_file)

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
# and  df_logbook_import['aircraftType_selectedAircraftClass']
df_new_logbook.loc[(pd.isna(df_logbook_import[' flight_night']) and  df_logbook_import['aircraftType_selectedAircraftClass']), 'SE ICUS Day'] = df_logbook_import[' flight_p1us']

# ICUS NIGHT
df_new_logbook.loc[df_logbook_import['Night'] > 0, 'SE ICUS Night'] = df_logbook_import['P1u/s']

# DUAL DAY
df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'SE Dual Day'] = df_logbook_import['flight_dualReceived']

# DUAL NIGHT
df_new_logbook.loc[df_logbook_import['Night'] > 0, 'SE Dual Night'] = df_logbook_import['flight_dualReceived']

# PIC DAY
df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'SE PIC Day'] = df_logbook_import['PIC']

# PIC NIGHT
df_new_logbook.loc[df_logbook_import['Night'] > 0, 'SE PIC Night'] = df_logbook_import['PIC']

# CO-PILOT DAY
df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'SE Copilot Day'] = df_logbook_import['SIC']

# CO-PILOT NIGHT
df_new_logbook.loc[df_logbook_import['Night'] > 0, 'SE Copilot Night'] = df_logbook_import['SIC']

# MULTI ENGINE TIMES
# ICUS DAY
df_new_logbook.loc[pd.isna(df_logbook_import['Night']), 'ME ICUS Day'] = df_logbook_import['P1u/s']

# ICUS NIGHT
# DUAL DAY
# DUAL NIGHT
# PIC DAY
# PIC NIGHT
# CO-PILOT DAY
# CO-PILOT NIGHT


# df_new_logbook.insert(8,"SE Dual Day", se_dual_day)