import json
from jsondiff import diff

json1 = json.dumps("{'current_status': {'time': '70:25'}, 'dashboard_coefs': {'command_right': {'ATTACKS': '114'}}, 'table_coefs': {'Asian Handicap': {'Handiсap Tensung (+1.75)': '4.97', 'Handiсap Ugyen Academy (-1.75)': '1.15', 'Handiсap Tensung (+3.75)': '1.09', 'Handiсap Ugyen Academy (-3.75)': '6.41'}, 'Total 1': {'Individual Total 1 Over 2': '11.6', 'Individual Total 1 Under 2': '1.02'}, 'European Handicap': {'European Handicap 2:0 Tensung': '5.7', 'European Handicap 2:0 X': '2.44', 'European Handicap 2:0 Ugyen Academy': '1.93', 'European Handicap 4:0 Tensung': '1.16', 'European Handicap 4:0 X': '6.25', 'European Handicap 4:0 Ugyen Academy': '11.7'}, 'Individual Total 1 Even/Odd': {'Tensung Total Even': '3.4', 'Tensung Total Odd': '1.27'}, 'Individual Total 2 Even/Odd': {'Ugyen Academy Total Even': '2.16', 'Ugyen Academy Total Odd': '1.616'}, 'Any Team To Win By': {'Any Team To Win With Difference Of 1 Goal(s) - Yes': '6.55', 'Any Team To Win With Difference Of 1 Goal(s) - No': '1.075', 'Any Team To Win With Difference Of 2 Goal(s) - Yes': '2.44', 'Any Team To Win With Difference Of 2 Goal(s) - No': '1.49', 'Any Team To Win With Difference Of 3 Goal(s) - Yes': '2.93', 'Any Team To Win With Difference Of 3 Goal(s) - No': '1.35', 'Any Team To Win With Difference Of 4 Goal(s) - Yes': '5.9', 'Any Team To Win With Difference Of 4 Goal(s) - No': '1.096'}, 'Win By': {'Ugyen Academy To Win By 1 Goals - Yes': '6.65', 'Ugyen Academy To Win By 1 Goals - No': '1.075', 'Ugyen Academy To Win By 2 Goals - Yes': '2.44', 'Ugyen Academy To Win By 2 Goals - No': '1.49', 'Ugyen Academy To Win By 3 Goals - Yes': '2.93', 'Ugyen Academy To Win By 3 Goals - No': '1.35', 'Ugyen Academy To Win By 4 Goals - Yes': '5.9', 'Ugyen Academy To Win By 4 Goals - No': '1.096'}, 'Team 2 To Win Both Halves': {'Ugyen Academy To Win Both Halves - Yes': '1.1', 'Ugyen Academy To Win Both Halves - No': '5.75'}, 'Double Chance. 2 Half': {'Tensung Or X': '6.18', 'Tensung Or Ugyen Academy': '1.025'}, 'Total 1. 2 Half': {'Individual Total 1 Over 2': '11.6', 'Individual Total 1 Under 2': '1.02'}, 'Correct Score. 2 Half': {'Correct Score 2-2': '7.77', 'Correct Score 1-2': '3.33', 'Correct Score - Any Other Score': '1.285'}, 'Remaining Time Outcome. 2 Half': {'W Tensung After Score 1-2': '6.35', 'X After Score 1-2': '2.448', 'W Ugyen Academy After Score 1-2': '1.94'}, 'Remaining Time Double Chance. 2 Half': {'Tensung X After Score 1-2': '1.768', 'Tensung Ugyen Academy After Score 1-2': '1.488', 'Ugyen Academy X After Score 1-2': '1.08'}, 'Team 1 To Score N Goals. 2 Half': {'Tensung Will Score 2 - 3 Goals - Yes': '3.04', 'Tensung Will Score 2 - 3 Goals - No': '1.34'}, 'Team 2 To Score N Goals. 2 Half': {'Ugyen Academy Will Score 2 - 3 Goals - Yes': '1.21', 'Ugyen Academy Will Score 2 - 3 Goals - No': '3.99', 'Ugyen Academy Will Score 3 - 4 Goals - Yes': '1.73', 'Ugyen Academy Will Score 3 - 4 Goals - No': '2.008', 'Ugyen Academy Will Score 4 - 5 Goals - Yes': '4.21', 'Ugyen Academy Will Score 4 - 5 Goals - No': '1.192', 'Ugyen Academy Will Score 5 - 6 Goals - Yes': '14.6', 'Ugyen Academy Will Score 5 - 6 Goals - No': '1.001'}, 'Individual Total 1 Exact Number Of Goals. 2 Half': {'Individual Total Tensung 1 - Yes': '1.37', 'Individual Total Tensung 1 - No': '2.98', 'Individual Total Tensung 2 - Yes': '3.61', 'Individual Total Tensung 2 - No': '1.25'}, 'Individual Total 2 Exact Number Of Goals. 2 Half': {'Individual Total Ugyen Academy 2 - Yes': '2.36', 'Individual Total Ugyen Academy 2 - No': '1.55', 'Individual Total Ugyen Academy 3 - Yes': '2.53', 'Individual Total Ugyen Academy 3 - No': '1.47', 'Individual Total Ugyen Academy 4 - Yes': '5.5', 'Individual Total Ugyen Academy 4 - No': '1.12', 'Individual Total Ugyen Academy 5 - Yes': '17'}, 'Correct Score - Group Bet.... 2 Half': {'Any Other Score - Yes': '1.21', 'Any Other Score - No': '3.94', 'Correct Score 2-2 Or 3-3 - Yes': '7.66', 'Correct Score 2-2 Or 3-3 - No': '1.05', 'Correct Score 2-3 Or 3-2 - Yes': '8.11', 'Correct Score 2-3 Or 3-2 - No': '1.045'}, 'Multi Goal. 2 Half': {'Multi Goal 4-5': '1.52', 'Multi Goal 4-10': '1.296', 'Multi Goal 5-10': '2.544', 'Multi Goal 6-10': '6.76'}, 'Team 1, Multi Goal. 2 Half': {'Team Tensung, Multi Goal 2-4': '2.9'}, 'Team 2, Multi Goal. 2 Half': {'Team Ugyen Academy, Multi Goal 3-4': '1.66', 'Team Ugyen Academy, Multi Goal 3-6': '1.536', 'Team Ugyen Academy, Multi Goal 4-6': '3.89'}, 'Interval Outcome (5m). Quick events': {'W Ugyen Academy In The Interval From 75:00 To 79:59 Minute': '5.44', 'W Ugyen Academy In The Interval From 80:00 To 84:59 Minute': '5.44', 'W Ugyen Academy In The Interval From 85:00 To 89:59 Minute': '5.44'}, 'Double Outcome (5m). Quick events': {'Tensung Ugyen Academy In The Interval From 75:00 To 79:59 Minute': '4.07', 'Tensung Ugyen Academy In The Interval From 80:00 To 84:59 Minute': '4.07', 'Tensung Ugyen Academy In The Interval From 85:00 To 89:59 Minute': '4.07'}, 'Total In The Interval (5m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 79:59 Minute': '3.97', 'Total Over 0.5 In The Interval From 80:00 To 84:59 Minute': '3.97', 'Total Over 0.5 In The Interval From 85:00 To 89:59 Minute': '3.97'}, 'Handicap Interval (5m). Quick events': {'Handicap Ugyen Academy 0 In The Interval From 85:00 To 89:59 Minute': '1.235', 'Handicap Ugyen Academy 0 In The Interval From 80:00 To 84:59 Minute': '1.235', 'Handicap Ugyen Academy 0 In The Interval From 75:00 To 79:59 Minute': '1.235'}, 'Interval Outcome (10m). Quick events': {'W Tensung In The Interval From 75:00 To 84:59 Minute': '9.61', 'X In The Interval From 75:00 To 84:59 Minute': '1.512', 'W Ugyen Academy In The Interval From 75:00 To 84:59 Minute': '3.155', 'W Tensung In The Interval From 80:00 To 89:59 Minute': '9.61', 'X In The Interval From 80:00 To 89:59 Minute': '1.512', 'W Ugyen Academy In The Interval From 80:00 To 89:59 Minute': '3.155'}, 'Double Outcome (10m). Quick events': {'Tensung X In The Interval From 75:00 To 84:59 Minute': '1.305', 'Tensung Ugyen Academy In The Interval From 75:00 To 84:59 Minute': '2.375', 'Tensung X In The Interval From 80:00 To 89:59 Minute': '1.305', 'Tensung Ugyen Academy In The Interval From 80:00 To 89:59 Minute': '2.375'}, 'Total In The Interval (10m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 84:59 Minute': '2.24', 'Total Over 0.5 In The Interval From 80:00 To 89:59 Minute': '2.24', 'Total Over 1.5 In The Interval From 75:00 To 84:59 Minute': '9.31', 'Total Over 1.5 In The Interval From 80:00 To 89:59 Minute': '9.31'}, 'Handicap Interval (10m). Quick events': {'Handicap Ugyen Academy -1 In The Interval From 75:00 To 84:59 Minute': '13', 'Handicap Ugyen Academy -1 In The Interval From 80:00 To 89:59 Minute': '13', 'Handicap Ugyen Academy -1.5 In The Interval From 75:00 To 84:59 Minute': '17.1', 'Handicap Ugyen Academy -1.5 In The Interval From 80:00 To 89:59 Minute': '17.1'}, 'Interval Outcome (15m). Quick events': {'W Tensung In The Interval From 75:00 To 89:59 Minute': '7.88', 'X In The Interval From 75:00 To 89:59 Minute': '1.85', 'W Ugyen Academy In The Interval From 75:00 To 89:59 Minute': '2.416'}, 'Double Outcome (15m). Quick events': {'Tensung X In The Interval From 75:00 To 89:59 Minute': '1.5', 'Tensung Ugyen Academy In The Interval From 75:00 To 89:59 Minute': '1.85'}, 'Total In The Interval (15m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 89:59 Minute': '1.675', 'Total Under 0.5 In The Interval From 75:00 To 89:59 Minute': '2.07', 'Total Over 1.5 In The Interval From 75:00 To 89:59 Minute': '4.82'}, 'Handicap Interval (15m). Quick events': {'Handicap Ugyen Academy -1 In The Interval From 75:00 To 89:59 Minute': '6.65', 'Handicap Ugyen Academy -1.5 In The Interval From 75:00 To 89:59 Minute': '9.27'}, 'Draw In At Least One Half': {'Draw In At Least One Half - Yes': '6.6', 'Draw In At Least One Half - No': '1.075'}, 'Individual 3Way Total 1': {'Tensung Total (3Way) Over 2': '13.5', 'Tensung Total (3Way) Exact 2': '3.9', 'Tensung Total (3Way) Under 2': '1.37'}}}")
json2 = json.dumps("{'current_status': {'time': '70:23'}, 'dashboard_coefs': {'command_right': {'ATTACKS': '114'}}, 'table_coefs': {'Asian Handicap': {'Handiсap Tensung (+1.75)': '4.97', 'Handiсap Ugyen Academy (-1.75)': '1.15', 'Handiсap Tensung (+3.75)': '1.09', 'Handiсap Ugyen Academy (-3.75)': '6.41'}, 'Total 1': {'Individual Total 1 Over 2': '11.6', 'Individual Total 1 Under 2': '1.02'}, 'European Handicap': {'European Handicap 2:0 Tensung': '5.7', 'European Handicap 2:0 X': '2.44', 'European Handicap 2:0 Ugyen Academy': '1.93', 'European Handicap 4:0 Tensung': '1.16', 'European Handicap 4:0 X': '6.25', 'European Handicap 4:0 Ugyen Academy': '11.7'}, 'Individual Total 1 Even/Odd': {'Tensung Total Even': '3.4', 'Tensung Total Odd': '1.27'}, 'Individual Total 2 Even/Odd': {'Ugyen Academy Total Even': '2.16', 'Ugyen Academy Total Odd': '1.616'}, 'Any Team To Win By': {'Any Team To Win With Difference Of 1 Goal(s) - Yes': '6.55', 'Any Team To Win With Difference Of 1 Goal(s) - No': '1.075', 'Any Team To Win With Difference Of 2 Goal(s) - Yes': '2.44', 'Any Team To Win With Difference Of 2 Goal(s) - No': '1.49', 'Any Team To Win With Difference Of 3 Goal(s) - Yes': '2.93', 'Any Team To Win With Difference Of 3 Goal(s) - No': '1.35', 'Any Team To Win With Difference Of 4 Goal(s) - Yes': '5.9', 'Any Team To Win With Difference Of 4 Goal(s) - No': '1.096'}, 'Win By': {'Ugyen Academy To Win By 1 Goals - Yes': '6.65', 'Ugyen Academy To Win By 1 Goals - No': '1.075', 'Ugyen Academy To Win By 2 Goals - Yes': '2.44', 'Ugyen Academy To Win By 2 Goals - No': '1.49', 'Ugyen Academy To Win By 3 Goals - Yes': '2.93', 'Ugyen Academy To Win By 3 Goals - No': '1.35', 'Ugyen Academy To Win By 4 Goals - Yes': '5.9', 'Ugyen Academy To Win By 4 Goals - No': '1.096'}, 'Team 2 To Win Both Halves': {'Ugyen Academy To Win Both Halves - Yes': '1.1', 'Ugyen Academy To Win Both Halves - No': '5.75'}, 'Double Chance. 2 Half': {'Tensung Or X': '6.18', 'Tensung Or Ugyen Academy': '1.025'}, 'Total 1. 2 Half': {'Individual Total 1 Over 2': '11.6', 'Individual Total 1 Under 2': '1.02'}, 'Correct Score. 2 Half': {'Correct Score 2-2': '7.77', 'Correct Score 1-2': '3.33', 'Correct Score - Any Other Score': '1.285'}, 'Remaining Time Outcome. 2 Half': {'W Tensung After Score 1-2': '6.35', 'X After Score 1-2': '2.448', 'W Ugyen Academy After Score 1-2': '1.94'}, 'Remaining Time Double Chance. 2 Half': {'Tensung X After Score 1-2': '1.768', 'Tensung Ugyen Academy After Score 1-2': '1.488', 'Ugyen Academy X After Score 1-2': '1.08'}, 'Team 1 To Score N Goals. 2 Half': {'Tensung Will Score 2 - 3 Goals - Yes': '3.04', 'Tensung Will Score 2 - 3 Goals - No': '1.34'}, 'Team 2 To Score N Goals. 2 Half': {'Ugyen Academy Will Score 2 - 3 Goals - Yes': '1.21', 'Ugyen Academy Will Score 2 - 3 Goals - No': '3.99', 'Ugyen Academy Will Score 3 - 4 Goals - Yes': '1.73', 'Ugyen Academy Will Score 3 - 4 Goals - No': '2.008', 'Ugyen Academy Will Score 4 - 5 Goals - Yes': '4.21', 'Ugyen Academy Will Score 4 - 5 Goals - No': '1.192', 'Ugyen Academy Will Score 5 - 6 Goals - Yes': '14.6', 'Ugyen Academy Will Score 5 - 6 Goals - No': '1.001'}, 'Individual Total 1 Exact Number Of Goals. 2 Half': {'Individual Total Tensung 1 - Yes': '1.37', 'Individual Total Tensung 1 - No': '2.98', 'Individual Total Tensung 2 - Yes': '3.61', 'Individual Total Tensung 2 - No': '1.25'}, 'Individual Total 2 Exact Number Of Goals. 2 Half': {'Individual Total Ugyen Academy 2 - Yes': '2.36', 'Individual Total Ugyen Academy 2 - No': '1.55', 'Individual Total Ugyen Academy 3 - Yes': '2.53', 'Individual Total Ugyen Academy 3 - No': '1.47', 'Individual Total Ugyen Academy 4 - Yes': '5.5', 'Individual Total Ugyen Academy 4 - No': '1.12', 'Individual Total Ugyen Academy 5 - Yes': '17'}, 'Correct Score - Group Bet.... 2 Half': {'Any Other Score - Yes': '1.21', 'Any Other Score - No': '3.94', 'Correct Score 2-2 Or 3-3 - Yes': '7.66', 'Correct Score 2-2 Or 3-3 - No': '1.05', 'Correct Score 2-3 Or 3-2 - Yes': '8.11', 'Correct Score 2-3 Or 3-2 - No': '1.045'}, 'Multi Goal. 2 Half': {'Multi Goal 4-5': '1.52', 'Multi Goal 4-10': '1.296', 'Multi Goal 5-10': '2.544', 'Multi Goal 6-10': '6.76'}, 'Team 1, Multi Goal. 2 Half': {'Team Tensung, Multi Goal 2-4': '2.9'}, 'Team 2, Multi Goal. 2 Half': {'Team Ugyen Academy, Multi Goal 3-4': '1.66', 'Team Ugyen Academy, Multi Goal 3-6': '1.536', 'Team Ugyen Academy, Multi Goal 4-6': '3.89'}, 'Interval Outcome (5m). Quick events': {'W Ugyen Academy In The Interval From 75:00 To 79:59 Minute': '5.44', 'W Ugyen Academy In The Interval From 80:00 To 84:59 Minute': '5.44', 'W Ugyen Academy In The Interval From 85:00 To 89:59 Minute': '5.44'}, 'Double Outcome (5m). Quick events': {'Tensung Ugyen Academy In The Interval From 75:00 To 79:59 Minute': '4.07', 'Tensung Ugyen Academy In The Interval From 80:00 To 84:59 Minute': '4.07', 'Tensung Ugyen Academy In The Interval From 85:00 To 89:59 Minute': '4.07'}, 'Total In The Interval (5m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 79:59 Minute': '3.97', 'Total Over 0.5 In The Interval From 80:00 To 84:59 Minute': '3.97', 'Total Over 0.5 In The Interval From 85:00 To 89:59 Minute': '3.97'}, 'Handicap Interval (5m). Quick events': {'Handicap Ugyen Academy 0 In The Interval From 85:00 To 89:59 Minute': '1.235', 'Handicap Ugyen Academy 0 In The Interval From 80:00 To 84:59 Minute': '1.235', 'Handicap Ugyen Academy 0 In The Interval From 75:00 To 79:59 Minute': '1.235'}, 'Interval Outcome (10m). Quick events': {'W Tensung In The Interval From 75:00 To 84:59 Minute': '9.61', 'X In The Interval From 75:00 To 84:59 Minute': '1.512', 'W Ugyen Academy In The Interval From 75:00 To 84:59 Minute': '3.155', 'W Tensung In The Interval From 80:00 To 89:59 Minute': '9.61', 'X In The Interval From 80:00 To 89:59 Minute': '1.512', 'W Ugyen Academy In The Interval From 80:00 To 89:59 Minute': '3.155'}, 'Double Outcome (10m). Quick events': {'Tensung X In The Interval From 75:00 To 84:59 Minute': '1.305', 'Tensung Ugyen Academy In The Interval From 75:00 To 84:59 Minute': '2.375', 'Tensung X In The Interval From 80:00 To 89:59 Minute': '1.305', 'Tensung Ugyen Academy In The Interval From 80:00 To 89:59 Minute': '2.375'}, 'Total In The Interval (10m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 84:59 Minute': '2.24', 'Total Over 0.5 In The Interval From 80:00 To 89:59 Minute': '2.24', 'Total Over 1.5 In The Interval From 75:00 To 84:59 Minute': '9.31', 'Total Over 1.5 In The Interval From 80:00 To 89:59 Minute': '9.31'}, 'Handicap Interval (10m). Quick events': {'Handicap Ugyen Academy -1 In The Interval From 75:00 To 84:59 Minute': '13', 'Handicap Ugyen Academy -1 In The Interval From 80:00 To 89:59 Minute': '13', 'Handicap Ugyen Academy -1.5 In The Interval From 75:00 To 84:59 Minute': '17.1', 'Handicap Ugyen Academy -1.5 In The Interval From 80:00 To 89:59 Minute': '17.1'}, 'Interval Outcome (15m). Quick events': {'W Tensung In The Interval From 75:00 To 89:59 Minute': '7.88', 'X In The Interval From 75:00 To 89:59 Minute': '1.85', 'W Ugyen Academy In The Interval From 75:00 To 89:59 Minute': '2.416'}, 'Double Outcome (15m). Quick events': {'Tensung X In The Interval From 75:00 To 89:59 Minute': '1.5', 'Tensung Ugyen Academy In The Interval From 75:00 To 89:59 Minute': '1.85'}, 'Total In The Interval (15m). Quick events': {'Total Over 0.5 In The Interval From 75:00 To 89:59 Minute': '1.675', 'Total Under 0.5 In The Interval From 75:00 To 89:59 Minute': '2.07', 'Total Over 1.5 In The Interval From 75:00 To 89:59 Minute': '4.82'}, 'Handicap Interval (15m). Quick events': {'Handicap Ugyen Academy -1 In The Interval From 75:00 To 89:59 Minute': '6.65', 'Handicap Ugyen Academy -1.5 In The Interval From 75:00 To 89:59 Minute': '9.27'}, 'Draw In At Least One Half': {'Draw In At Least One Half - Yes': '6.6', 'Draw In At Least One Half - No': '1.075'}, 'Individual 3Way Total 1': {'Tensung Total (3Way) Over 2': '13.5', 'Tensung Total (3Way) Exact 2': '3.9', 'Tensung Total (3Way) Under 2': '1.37'}}}")

changes = json.loads(diff(json2, json1, load=True, dump=True))
# print(time_to_create_task.strftime('%y-%m-%d %H:%M'))
print(changes)
