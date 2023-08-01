# Estimating Test Scores from Educational Spending: Project Overview
- Investigated the relationship between statewide educational spending and outcome on standardized tests
- Combined data from multiple sources into single dataframe, reconciling differences in formatting
- Compared two forms of regression (linear and polynomial) to model the relationship between spending and test scores
- Visualized results using choropleth maps, showing state-by-state outcomes

### Code and Resources Used
**Python Version**: 3.11.4
**Packages**: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn

### Website blog post
https://www.nolaneley.com/educational-spending

### Data sources
- Public education spending data was taken from the National Education Resource Database on schools (https://edunomicslab.org/nerds/)
- Data on standardized test scores were taken from the Nation's Report Card (https://www.nationsreportcard.gov/profiles/stateprofile)

### Data cleaning
- Removed "flagged" (potentially problematic) and NA values from each state's data
- Combined spending and test scores data into single dataframe
- Reconciled state abbreviation and full state names as keys in two separate data sources
- Removed non-state entries (DoDEA, Washington D.C., etc.)

### EDA
- Looked at histograms of data to ensure distributions were somewhat normal and that there were no unexpected values
- Plotted linear and polynomial regressions to get a sense of relationship between variables

![mathScatter](/images/spending_math.png)

### Modeling
I tried both linear and polynomial regression and measured their performance using the mean absolute error (MAE).
- **Linear regression**: MAE = 4.59 (math), 3.49 (reading)
- **Polynomial regression**: MAE = 4.51 (math), 3.36 (reading)

I also tested the significance of the correlation of these two variables by calculating the Pearon correlation coefficient (*r*) and its associated *p*-value.
- ***r***: 0.27 (for both math and reading)
- ***p*-values**: .062 (math), .057 (reading) 

### Choropleth maps
In addition to histograms and scatter plots, I also created choropleth maps to visualize different metrics on a map of the United States.

![math](/images/math_choropleth.png)