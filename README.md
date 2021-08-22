# Waves and Ice Cream: Examining Oahu Temperature Trends in June and December
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
Base on the findings of the analysis, the differences are by a at 2-3 degrees.

only 3.9 degrees difference on average, 2 degree difference for max.  there could possibly be less customers in December, however more analysis is needed to determine.  In addition to temperatures, it would be best to perform another analysis that gathers precipitation data for June and December.  It's not conclusive to say that it is statistically significant.

```
june_prcp = []
june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
```
June precipitation summary statistics, [view here](https://github.com/retroxsky06/surfs_up/blob/main/Resources/june_prcp.png).

December precipitation summary statistics, [view here](https://github.com/retroxsky06/surfs_up/blob/main/Resources/dec_prcp.png).

still viable, possibly query on precipitation for June and December

For this part of the Challenge, write a report that describes the key differences in weather between June and December and two recommendations for further analysis.

Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.



