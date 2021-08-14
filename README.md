# surfs_up

## Overview of the Analysis
This analysis was designed to introduce us to SQLite, SQLAlchemy and Flask. We were tasked with pulling weather information for Oahu that would be used to determine whether opening a Surf and Ice Cream shop was a good idea (based on weather trends year around).

This information would be presented to investors, as capital for the business was being raised.

## Results
The question this analysis was trying to address was: were the temperature trends consistent year around in order to determine if the surf and ice cream shop business is sustainable.

In order to do this, we pulled information for the months of June and December from 2010 to 2017. A summary of the June temperature dataframe can be found below:

<img width="133" alt="Screen Shot 2021-08-14 at 2 06 16 PM" src="https://user-images.githubusercontent.com/46773181/129459987-2604d030-9bc0-4de0-bc71-dd0a8261bcde.png">

You may find a screenshot of the December temperature dataframe found below:

<img width="161" alt="Screen Shot 2021-08-14 at 2 06 59 PM" src="https://user-images.githubusercontent.com/46773181/129459999-159b9297-0ee3-4596-8a13-b63b44d7e675.png">

Comparing the two, we see that:
- The mean and median temperatures for the two months are very similar
- December does tend to be slightly colder, as we see by comparing the min and looking at the percentiles
- December has a slightly smaller sample size that June

This suggests that the temperature in Oahu remains relatively steady throughout the year. We can safely assume this trend has existed since 2010, as we have used plenty of data from 2010 to 2017. 

## Summary
By looking at these two dataframes, the data suggests that the temperature in Oahu is ideal year-round for an ice cream / surf shop. However, there are other things that I would suggest looking at before rushing to pitch investors, these are:
- What are the other seasons like? Are they also consistent with June / December?
- If we are checking for seasonality (outside of weather data), perhaps we should investigate seasonality on tourism -- how do locals compare to tourists when thinking about revenue / orders? Are tourist numbers just as consistent as the temperature year around? What impact would that have on the business if so?
- Perhaps we also want to check precipitation vs. simply analyzing temperature, as this may have an impact on sales
