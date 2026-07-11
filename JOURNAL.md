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