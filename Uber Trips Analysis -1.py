#!/usr/bin/env python
# coding: utf-8

# ### Uber Pickups Analysis Quiz
# 
# The question set is based on the August dataset, `uber-raw-data-aug14.csv`.
# 
# #### Keeping the dataset ready before questions

# In[1]:


import pandas as pd

df = pd.read_csv(r"E:\power bi\DevasahayamBondalapati\Uber Trips Analysis\Uber Trips Analysis\data\uber-raw-data-aug14.csv")
df.head()


# In[2]:


df.info()


# In[3]:


df.isnull().sum()


# #### Q1. On what date did we see the most number of Uber pickups?
# 
# **Skill Test:** Grouping & Counting

# In[4]:


# Convert the 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])


df["Date"] = df["Date/Time"].dt.date
df["Time"] = df["Date/Time"].dt.time
#df.head()
# Group by date and count the number of pickups
total_pickup = df.groupby(df["Date"]).size().sort_values(ascending=False)


# Find the date with the highest number of pickups
max_pickup_date = total_pickup.idxmax()
max_pickup = total_pickup.max()
print("the highest number of pickups is",max_pickup, "on date" ,max_pickup_date )



# ANS : the highest number of pickups is 32759 on date 2014-08-07

# #### Q.2 How many Uber pickups were made on the date with the highest number of pickups?
# 
# **Skill Test:** Indexing and filtering

# In[5]:


# Get the count of pickups on the highest date
total_pickup[0]



# ANS : 32759 Uber pickups were made on the date as the highest number of pickups
# 

# #### Q.3 How many unique TLC base companies are affiliated with the Uber pickups in the dataset?
# 
# **Skill Test:** Counting unique values

# In[6]:


# Count the number of unique TLC base companies
unique_TLC = df["Base"].nunique()
print("Total unique TLC base companies are ",unique_TLC)



# ANS: Total unique TLC base companies are  5

# #### Q.4 Which TLC base company had the highest number of pickups?
# 
# **Skill Test:** Grouping, counting, and finding the maximum

# In[7]:


# Group by TLC base company and count the number of pickups

total_pickup_Basewise=df.groupby("Base").Base.count().sort_values(ascending = False)
print(total_pickup_Basewise)


# Find the TLC base company with the highest number of pickups

print("TLC base company with the highest number of pickups is",total_pickup_Basewise.idxmax())


# ANS: TLC base company with the highest number of pickups is B02617

# #### Q.5 How many Uber pickups were made at each unique TLC base company?
# 
# **Skill Test:** Grouping and counting

# In[8]:


# Group by TLC base company and count the number of pickups

total_pickup_Basewise=df.groupby("Base").Base.count().sort_values(ascending = False)
print("Uber pickups were made at each unique TLC base company are given below:-\n",total_pickup_Basewise)



# #### Q.6 Can you determine the busiest time of day for Uber pickups based on the date/time column?
# 
# **Skill Test:** Extracting time components, grouping, counting, and finding the maximum

# In[9]:


# Convert the 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Extract the hour from the 'Date/Time' column
df["hour"] = df["Date/Time"].dt.hour

# Group by hour and count the number of pickups
total_pickup_hourwise = df.groupby("hour").size().sort_values(ascending = False)
print(total_pickup_hourwise)
# Find the hour with the highest number of pickups
print("The hour with the highest number of pickups: ",total_pickup_hourwise.idxmax())





# Ans: the busiest time of day for Uber pickups based on the date/time column is 17(in hour)

# #### Q.7 Can you create a visualization (e.g., a bar chart or line plot) to represent the number of Uber pickups over time?
# 
# **Skill Test:** Data Visualization using Plotting function 

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by date and count the number of pickups

pickup_count_datewise=df.groupby("Date").size()
pickup_count_datewise

# Create a line plot to visualize the number of pickups over time

x= pickup_count_datewise.index.tolist()
y= pickup_count_datewise.values.tolist()

plt.figure(figsize=(10,5))
plt.xlabel("Pickup Date")
plt.ylabel("Pickup Count")
plt.title("Pickup count for each date")
plt.bar(x,y,color="blue")
sns.despine()



# Insights based on above graph
# The maximum pickups were done on 2014-08-07
# The minimum pickups were done in 2014-08-10

# #### Q8. Can you create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude?
# 
# **Skill Test:** Scatter Plot

# In[11]:


# Create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude


plt.figure(figsize=(10,5))
plt.xlabel("latitude")
plt.ylabel("longitude")
plt.title("Distribution of Uber pickups based on latitude and longitude")
plt.scatter(x=df["Lat"],y=df["Lon"],color= "blue")


# #### Q9. Can you create a bar chart to compare the number of Uber pickups for each TLC base company?
# 
# **Skill Test:** Bar Chart

# In[12]:


# Create a bar chart to compare the number of Uber pickups for each TLC base company

base_count = df["Base"].value_counts()
x = base_count.index.tolist()
y= base_count.values.tolist()
plt.figure(figsize=(5,5))
plt.xlabel("TLC base company")
plt.ylabel("Base_count")
plt.title("Number of pickup by TLC base company")
plt.bar(x,y,color= "orange")
sns.despine()


# Insights based on above graph
# TLC base company with highest base count is B02617
# TLC base company with lowest base count is B02512

# #### Q10. Can you create a pie chart to display the percentage distribution of Uber pickups for each day of the week?
# 
# **Skill Test:** Pie Chart

# In[13]:


# Group by day of the week and count the number of pickups
pickups_daywise = df["Date/Time"].dt.day_name().value_counts()
print(pickups_daywise)

# Create a pie chart to display the percentage distribution of Uber pickups for each day of the week
pickups_daywise.plot(kind="pie",autopct = '%1.1f%%', title = "Percentage distribution of Uber pickups for each day of the week")


# In[ ]:




