# Miss America Web Scraping Project

## Project Goal

The goal of this project was to brush up on skills learned in my MS. MIS program while simultaneously displaying my home-state's statistical dominance in the Miss America Pageants. I scraped historical Miss America data from wikipedia, took census data from census.gov to get state populations (2019), used SQL to combine the data, and finally used Tableau to visualize the results. 



## Scraping With Python

To start, I used python's pandas, lxml and requests modules to scrape and clean the data. To retrieve the data, I wrote the following code:

![ScrapingCode_MissAmerica](https://user-images.githubusercontent.com/94634170/219900938-375f6912-b27b-44d0-9cbc-b9a6df59024f.png)

This resulted in fairly clean output, as seen below:

![ScrapingOutput_MissAmerica](https://user-images.githubusercontent.com/94634170/219900957-4aaf7c85-2aa1-4269-9d1b-0f38e62b069f.png)

However, there were a few things to correct. Namely, the mismatched list lengths, town names in the state list and missing values and /n in the age list. First off, I cleaned the /n from the age column, filled empty age strings and replaced the city names with the state, which was a problem when representatives from a single state won in succession, as shown below with New York:

![MultipleLines_OneState_Issue](https://user-images.githubusercontent.com/94634170/219901247-21c2d90f-d5f5-4348-ac26-eb1d80228dab.png)

The code used to fix the age and state columns is below:

![CleaningCode_Age State_MissAmerica](https://user-images.githubusercontent.com/94634170/219901250-4aa066a2-363f-4c8f-bd26-295a63a02f9e.png)

Due to a scandal taking place in 1984 with the reiging Miss America, the runner up was awarded the title late in the year, so there were two winners in 1984. My scraping only pulled 1984 once, so I had to add 1984 once more using its index in the list, which fixed the mismatched list lengths. See below: 

![CleaningCode_Year_MissAmerica](https://user-images.githubusercontent.com/94634170/219901686-1e5b7a0a-9d18-4bc8-a31d-6e96f6caa408.png)

Now with each column clean, the output was as seen below:

![CleaningOutput_MissAmerica](https://user-images.githubusercontent.com/94634170/219901956-42c7301b-047c-4600-bcd7-c12e1bd8406c.png)

Afterwards, I was ready to create a dataframe using the cleaned lists and export to a csv:

![CreatingDF Exporting_MissAmerica](https://user-images.githubusercontent.com/94634170/219901759-5b651397-f5c6-495d-a438-7aa29116b292.png)



## Combining Tables Using SQL

After importing the census csv file and the cleaned Miss America data into SQL Server Management Studio, I joined the file on the shared value (state) so that I could have the associated population for each state. The code for doing this and querying the data is seen below:

![SQL_Code_Image](https://user-images.githubusercontent.com/94634170/219902667-7f781731-1d77-4f6e-9c1c-817a6c35fd53.png)

The query output:

![SQL_Output_Image](https://user-images.githubusercontent.com/94634170/219902685-cca900b5-4754-45d0-b7f3-0d1ac4523830.png)

This output gave me a good idea for the data and how I could visualize it using Tableau.



## Visualization With Tableau

For creating a Tableau dashboard, I decided to go with three graphs:
* Miss America winner's age over time
* States with the most wins
* States with the lowest population to winner ratios

![Screenshot_20230218_063033](https://user-images.githubusercontent.com/94634170/219904074-79035533-d229-4b29-817d-b58246017bfb.png)







