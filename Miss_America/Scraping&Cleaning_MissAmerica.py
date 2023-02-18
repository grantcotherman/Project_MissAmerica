#Read in relevant Libraries
import pandas as pd
from lxml import html
from lxml import etree
import requests
import os


# Set working directory
os.chdir("C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Miss_America")

#SetUp
wikiurl = "https://en.wikipedia.org/wiki/List_of_Miss_America_titleholders" 
resp = requests.get(wikiurl)
tagtree = html.fromstring(resp.content)


# Year Column
xp_year = "//div[@id='bodyContent']/div[@id='mw-content-text']/div[@class='mw-parser-output']/table[1]/tbody/tr/td[1]/a/text()"
year_list = tagtree.xpath(xp_year)


# State Column
xp_state = "//div[@id='bodyContent']/div[@id='mw-content-text']/div[@class='mw-parser-output']/table[1]/tbody/tr/td[4]/a/text()"
state_list = tagtree.xpath(xp_state)

# Age Column
xp_age = "//div[@id='bodyContent']/div[@id='mw-content-text']/div[@class='mw-parser-output']/table[1]/tbody/tr/td[6]/text()"
age_list = tagtree.xpath(xp_age)


####################################
#Part Two - Cleaning Scraped Data
####################################
 
#Clean the Age List (remove \n)
age_list2 = []
for i in age_list:
    i = i.strip("\n")
    age_list2.append(i)

age_list2.insert(2,"17") #Compensate for the 2nd winner, who won twice
age_list2.insert(-9,"24")
age_list2.insert(-9,"23")
age_list2.insert(-17,"20")
age_list2.insert(32,"20")
del age_list2[33]
del age_list2[-19]
del age_list2[-8] #delete empty string
del age_list2[-8]# delete empty string

age_list3 = []
for age in age_list2: # Make a for loop to get the last empty age in middle of data
    if age == '':
        age = "21"
    age_list3.append(age)

print()
print(age_list3)
print("\nThe length of the age list is:",(len(age_list3)),"\n")

#Clean the State List -- Insert States where town names are
state_list2 = []
for state in state_list:
    if state == "Fayetteville":
        state = "New York"
    if state == "Manhattan":
        state = "New York"
    if state == "Lawton":
        state = "Oklahoma"
    if state == "Natchez":
        state = "Mississippi"
    if state == "Mays Landing":
        state = "New Jersey"
    state_list2.append(state)


state_list2.insert(2, "Ohio")
state_list2.insert(8, "Pennsylvania")  
print(state_list2)
print("\nThe length of the state list is:",(len(state_list2)),"\n")


#Clean the Year List

year_list.insert(57,"1984") # 2 Miss Americas held title in 1984 due to photo scandal
print(year_list)
print("\nThe length of the year list is:",(len(year_list)),"\n")



###################################
#Part Three - Creating a Dataframe
###################################

#Save as a dataframe
miss_america_df = pd.DataFrame(
    {'Year': year_list,
     'State': state_list2,
     'Age': age_list3})

#export to csv
#miss_america_csv = miss_america_df.to_csv('Miss_America.csv', index = True)


