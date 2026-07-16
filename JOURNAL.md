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

Okay i have an idea, I need to create another page, in this page 
I can use a column charts to show how every year the average 
temperature changes.

* *8:16 PM* Created `yearly_temperature.ipynb` which creates a 
dataset(`temperature_yearly_summary.csv`) with the mean
temperature of all the mean temperatures of each year

# July 13th

* *9:35 AM* Okay so I honestly forgot to Journal the couple of 
commits before, so I'll explain them now.

Firstly, I tried creating a plot firectly in the streamlit app. 
The app kept crashing no matter what I did, in the way i figured 
out that the meme image in the introduction is actually a jpg
file not a png file. 

So instead of plotting the graph using streamlit, I used the
jupyter notebook and made the graph and saved it as a PNG, and 
I'll display the PNG in streamlit. I hope this works

*Update* I wanna kms. The erorr was never with the plot. It was 
with importing multiple datasets.. Did all that for nothing. Oh 
well it looks cleaner in my opinion

* *3:03 PM* Okay I've finally completed the regression plot. I created the file `Yearly Temperatures.py`. 
I included the image with some information 

* Okay time for another graph, This time I'm thinking of creating a Daily Temperature Range 
Area chart. For this i would need to get the minimum and maximum, so i'll add them to the
dataset 

# July 14th

* *11:19 AM* Alright so I've added the graph to the streamlit page, I've also added explanations to the graph
interpreting the results.

* *12:43 PM* Okay so time for another sub-section, this time I want to compare rainfall
and temperature. Specifically the hypothesis that heave rainfall correlates with lower
maximum temperatures

* *1:24 PM* Created the graphs!

I'll document this in the streamlit app

DONE!

* *2:15 PM* Up next, i want to compare Rainfall vs Wind Speed. This would follow similar procedures as the Rainfall vs Temperature.

DONE!

* *2:55 PM* Okayy, added the graph to streamlit

Okay now i'm just really fricking bored from all this, I want to do something 
different. How about... idk how hard this will be but make a sort of predictive model
or smth that predicts stuff????? Lemme research a lil n see what i find 

Okay so it's not thaaat hard, I'll create another page for this: `predicting temperature`.

I am so sleepy rn omds, anywho I DID IT! that look alot of research online but I 
finally managed to make a model and save it locally! 

# July 15th 

* *9:29 AM* okie soo, wow the 17th deadline is getting pretty near huh. 

Anywho now that i have the mode, I have an idea, what if we make a page where
the user can like select all the features and based off of that it gives a prediction
of the weather, does that not sound like the coolest thing ever?

Finally done! The user can now choose the features and the model makes a prediction

* *3:33 PM* Okay so I've completed another page called "prediction" showcasing how the model actually works. I loved making this page cause i actually explained stuff. 

I honestly want to do this to the other pages too, instead of some 1-2 sentences,
actually explain the stuff.

I changed up the "Predicted Temperatures" page to make it more cleaner

Cleaned up Rainfall vs Wind Speed.

Cleaned up Rainfall vs Temperature.

Okay now finally I think I def need to re order the pages:

1. Yearly Temperatures
2. Rainfall vs Temperature
3. Rainfall vs Wind Speed
4. Prediction Introduction
5. Prediction Temperature

Okay so one more step to making this much better is to use **interactive** graphs
using plotly. So I looked up how to do that and created one for the
rainfall vs temperature.

Did the same for Yearly temperatures.

Same for Rainfall vs Wind Speed

# July 16th 

Okay now finally, All i have left to do is edit out the `Introduction.py` file. I'm gonna make it alot better
now

So I've changed the "Data at a glance" section to include extremes from every year cause only 2019 doesn't
really make any sense tbh

Finally fixed up Introduction, made it alot better and cleaner

I think after all this time, I can finally, finally do the readme and ship the project 🥹 BUUT before that
I need to upload the project on streamlit cloud. I'll do it now.

Okay so setting it up was actually pretty simple. However I do see some errors. The issue is plotly is not
installed as a package so all the pages where I need it jst fails. So the solution is to create a requirements.
txt file. Let me do that now and try it. 

Okay this is taking soo long to load, I think I should remove some of the requirements.

IT WORKS!!!!!!