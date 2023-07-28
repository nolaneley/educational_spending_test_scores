import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Verbose flag to print out troubleshooting messages
verbose = 0

# Load state dictionary for matching between two tables
state_dict = pd.read_csv('state_names.csv')

# --- Go through each file in spending ---
spending_dir = os.getcwd() + '/spending/FY18-19'
all_files = os.listdir(spending_dir)
states, med_spending, valid_rows_pct, states_abbrev = [], [], [], []

for filename in all_files:
    if filename == '.DS_Store':
        continue
    file_path = os.path.join(spending_dir, filename)
    
    df = pd.read_excel(file_path,sheet_name='FY 2018-19')
    cur_state_abbrev = filename[0:2]
    states_abbrev.append(cur_state_abbrev)
    cur_state_full = state_dict['state'][state_dict['code']==cur_state_abbrev].iloc[0]
    states.append(cur_state_full)
    
    # Get some attributes
    og_len = df.shape[0]
    f33_sum = sum(df['flag_f33'])
    
    if verbose:
        # Print current state
        print("\nCurrent state: " + cur_state_abbrev)
        
        # Print number of records    
        print("Total # records: " + str(og_len))
        
        # Print number of records with flag_f33
        print("Total # records with flag_f33: " + str(f33_sum))  
        
        # Print percentage of records with flag_f33
        print("Percentage of flagged records: " + str(round(f33_sum/og_len,2)))   
        
        # Print number of records without flag_f33
        print("Total # records without flag: " + str(og_len-f33_sum))
    
    # Remove rows with NAs or flags
    df = df.dropna(subset=['pp_total_norm_NERDS'])
    df = df[df.flag_f33!=1]
    df = df[df.flag_nerds!=1]
    new_len = df.shape[0]
    
    # Plot histogram of normalized spending
    sns.displot(df.pp_total_norm_NERDS, kde=True)
    plt.title(cur_state_abbrev + ' Educational Spending')
    plt.xlabel('Spending ($)')
    plt.savefig(cur_state_abbrev + '_spending_hist.png', dpi=300)
        
    # Get median per pupil spending for current state
    med_spending.append(np.median(df['pp_total_norm_NERDS']))
    
    # Get valid rows left out of total original rows
    valid_rows_pct.append(new_len/og_len)
    
# Create table of state spending
spending_data = {'Jurisdiction': states,
                 'states_abbrev': states_abbrev,
                  'spending': med_spending,
                  'pct_valid': valid_rows_pct}
spending = pd.DataFrame(spending_data)

# Load outcomes
outcomes_math = pd.read_csv(os.getcwd() + '/outcome/g8_math_2019.csv')
outcomes_reading = pd.read_csv(os.getcwd() + '/outcome/g8_reading_2019.csv')

data = pd.merge(spending, outcomes_math[['Jurisdiction','MN']], on='Jurisdiction')
data = data.rename(columns={'MN' : 'math'})
data = pd.merge(data, outcomes_reading[['Jurisdiction','MN']], on='Jurisdiction')
data = data.rename(columns={'MN' : 'reading'})
data.reading = data.reading.astype(float)
data = data.rename(columns={'Jurisdiction' : 'state'})

#data.to_csv('school_spending_outcome.csv', index=False)




    