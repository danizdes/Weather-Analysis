# July 11th

* *2:40 PM* Alrighty so i've imported the NOAA GHCN Dataset for 2026 
aaand woaaah lol thats alot of data! I asked ChatGPT what all the 
data means and I finally get it!

I need to get the specific country code, I'm thinking of a small 
country like hmm singapore(horizons reference), and only analyze the TMAX readings

okay update I can't find any singaporean stations in the database :(. I think I'll just go with the official records singapore themselves release(data.gov.sg). 

Nevermind I found a better dataset on this cool [Github repo](https://raw.githubusercontent.com/chuachinhon/weather_singapore_cch/refs/heads/master/data/weather_clean.csv)
cutoff year is 2019 but this is honestly the best that i found.

I'll start of with 2019 (the latest year in the dataset).
I'll create a file called `2019.ipynb` where i'll look at that 
years data, and then maybe expand to other years

* *3:21 PM* Okay so i imported the csv file successfully and it 
works great! the python version and installing pandas was giving 
me such a big headache it was so fricking annoying, thankfully i 
managed to figure out a solution by downgrading the python version

* *4:46* Filtered out the 2019 years only, added max and minimum wind temperature / speeds respectfully. Basic stuff works perfectly. But now to actually get this up and running;I need
to create a streamlit app `app.py`

# July 12th

* *5:39 AM* Okay so I created a streamlit app at `app.py`. 
Imported the csv file, filtered the data to only get 2019 at the 
moment. Created a usable navigation with a Home button. 

* *5:48* I've come to the realization that maybe i should 
organize things cleanly. Here is what I'll do:

1. Create a streamlit directory (This is gonna hold only the streamlit application stuff, not the pandas data manipulation)
2. Create a notebook folder (This is where we will actually do the data manipulation)
3. Include the dataset in a "dataset" folder

In addition in the streamlit directory i can include multiple pages in a sub-directory.

* *6:08 AM* Alright so I've written all the introductory stuff for the streamlit root app

* *10:19 AM* Added a "Data at a glance" showing Hottest Temperatures & Windiest speeds with their date