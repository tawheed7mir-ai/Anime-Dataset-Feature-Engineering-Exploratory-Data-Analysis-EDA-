import numpy as np
import pandas as pd


df = pd.read_csv(r"C:\Users\DELL\Downloads\anime.csv")
# print(df.head(5))
# EXTRACT NUMBER OF EPISODES FROM TITLE 
def extract_episodes(text):
    check = False
    data = ""
    for i in text:
        if i ==")":
            check = False
            return data
        if check == True:
            data+=i
        if i == "(":
            check = True
       
    
df["Episodes"]=df["Title"].apply(extract_episodes)
df["Episodes"]=df["Episodes"].str.replace(" eps","")
df["Episodes"]=df["Episodes"].astype(int)

# EXTRACT TIME FROM TITLE
def extract_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] ==")":
            for j in range(i+1,i+20):
                data+=txt[j]
    return data
df["Total Time"]=df["Title"].apply(extract_time)



# EXTRACT NUMBER OF MONTHS 

# Split into start and end
df[['start', 'end']] = df['Total Time'].str.split(' - ', expand=True)

# Convert to datetime
df['start'] = pd.to_datetime(df['start'], format='%b %Y')
df['end'] = pd.to_datetime(df['end'], format='%b %Y')

# Calculate months
df['months'] = (
    (df['end'].dt.year - df['start'].dt.year) * 12 +
    (df['end'].dt.month - df['start'].dt.month)
)





# WHICH ANIME HAS THE HIGHEST SCORE

# print(df[df["Score"]==df["Score"].max()]["Title"])

# GIVE ME TOP 5 SCORING ANIME
# print(df["Title"].head())


# WHICH ANIME HAS THE HIGHEST EPISODE COUNT

# print(df[df["Episodes"]==df["Episodes"].max()])

# ANIMES WITH TOP 5 EPISODE COUNT
df.sort_values(by="Episodes" ,ascending=False,inplace=True)
# print(df.head()["Title"])



# WHICH IS THE LONGEST RUNNING ANIME
print(df.sort_values(by="months", ascending=False).head(1))