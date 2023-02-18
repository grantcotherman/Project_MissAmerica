# Miss America Web Scraping Project

## Project Goal

The goal of this project was to brush up on skills learned in my MS. MIS program while simultaneously displaying my home-state's statistical dominance in the Miss America Pageants. I scraped historical Miss America data from wikipedia, took census data from census.gov to get state populations (2019), used SQL to combine the data, and finally used Tableau to visualize the results. 

## Scraping With Python

To start, I used python's pandas, lxml and requests modules to scrape and clean the data. To retrive the data, I wrote the following code:

![ScrapingCode_MissAmerica](https://user-images.githubusercontent.com/94634170/219900938-375f6912-b27b-44d0-9cbc-b9a6df59024f.png)


This Resulted in fairly clean output, as seen below:

![ScrapingOutput_MissAmerica](https://user-images.githubusercontent.com/94634170/219900957-4aaf7c85-2aa1-4269-9d1b-0f38e62b069f.png)

Unfortunately, there were a few things to correct.  First off, I cleaned the /n from the age column and replaced the city names with the state, which was a problem when representatives from a single state won in succession, as shown below:

![MultipleLines_OneState_Issue](https://user-images.githubusercontent.com/94634170/219901247-21c2d90f-d5f5-4348-ac26-eb1d80228dab.png)

The code used to fix the age and state columns are below:
![CleaningCode_Age State_MissAmerica](https://user-images.githubusercontent.com/94634170/219901250-4aa066a2-363f-4c8f-bd26-295a63a02f9e.png)

## Combining Tables Using SQL



## Visualization With Tableau






