# Potential Waves and Ice Cream Shop: Examining Oahu Temperature Trends in June and December
Module 9 Challenge

## Project Overview
A potential stakeholder for a posible surf and ice cream shop in Oahu, Hawaii is interested in understanding temperature trends to determine the viability of the business. Specifically, the potential stakeholder would like to review temperature data for the months of June and December. The purpose of this project is to gather and analyze June and December temperature data in order for the stakeholder to make a more informed investment decision.

## Software & Resources
- Python 3.8.8
- SQLAlchemy 1.4.7
- SQLite database: hawaii.sqlite (stored weather data)

## Results
- The average temperature in June is 3.9 degrees warmer than December. 
- The lowest temperature in December is 8 degrees cooler than the lowest temperature in June.
- June has a higher max temperature than December, revealing a difference of 2 degrees.
- There are 11.3% less data points in December (June: 1700, December: 1517).

#### Summary statistics for June temperatures
![fig1](https://github.com/retroxsky06/surfs_up/blob/main/Resources/June_temps.png)

#### Summary statistics for Decemeber temperatures
![fig2](https://github.com/retroxsky06/surfs_up/blob/main/Resources/Dec_Temps.png)


## Summary
Based on the findings of the above analysis, there could be a possibility of having a lesser number of customers in the month of December due to cooler temperatures; however further analysis is needed.  As shown above, the difference in average temperature is 3.9 degrees Fahrenheit between June and December, which may not be enough information to guide the stakeholder. To provide additional weather data that can inform the stakeholder's decision, I would perform two queries to gather and analyze precipitation data for the months of June and December.

To run the query that would obtain June precipitation data, I would use the code below:
```
june_prcp = []
june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
```
For the June precipitation summary statistics, [view here](https://github.com/retroxsky06/surfs_up/blob/main/Resources/june_prcp.png).

To run the query that would obtain December precipitation data, I would use the code below:
``` 
dec_prcp = []
dec_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()
```
For the December precipitation summary statistics, [view here](https://github.com/retroxsky06/surfs_up/blob/main/Resources/dec_prcp.png).

still viable, possibly query on precipitation for June and December


