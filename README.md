![Banner](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/CreditCardBanner.png)

## Customer Segmentation
 Our stakeholder is a Credit Card Company that wants to market new credit cards.  They have asked us to segment their potential customers to determine how and what kind of cards they should market to each group.
- The credit cards they want to market are:
  - Platinum. It's considered a High End product offering benefits like:
    - Rewards on spending: The introductory offer can take the travel further: Earn 100,000 Membership Rewards® Points after spending $6,000 on purchases on the Card in the first 6 months of Card Membership.
    - Up to $300 in annual credit for airline incidental fees.
    - Up to $200 in Uber cash for rides.
    - Up to $200 in annual hotel credit.
    - Money-saving perks for stays booked through The Hotel Collection.
    - And more.
  - Gold. This product has the intention to give special status for customers beyond the average, offering:
    - Upgrade to Hilton Honors Gold status.
    - Low fares through the International Airline Program.
    - Up to $100 in annual credit for airline incidental fees.
    - Up to $100 in Uber cash for rides.
    - Acces to Global Dining Collection.
    - And more.


<img src="https://raw.githubusercontent.com/matiassingers/awesome-readme/master/icon.png" align="right" />

## Author
#### Name: Eduardo Galindez.
#### Date: Octuber 2022.

<img alt="GitHub followers" src="https://img.shields.io/github/followers/edleafvirtual?style=social"> <img alt="GitHub User's stars" src="https://img.shields.io/github/stars/edleafvirtual?style=social"> <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/edleafvirtual/sales_predictions2023?style=social">

## Project Information

#### General Objective:
- Xxxxxx.
#### Specific Objectives:
- Xxxx.
- Xxxxx.
- Xxxx.
- Xxxx.

#### Scope:
- Our study consists of two parts:
   - [Part A:](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Part_A--Exploratory_Analysis.ipynb "Part A:") Xxxxxxx.
   - [Part B:](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Part_B--ML_Modeling.ipynb "Part B:") Xxxxxxx.

#### General Description
A [Licensed Vendor](https://abd.iowa.gov/licensing/licensepermit-fees "Licensed Vendor") sells alcoholic liquor to a store, being responsible for paying to Iowa State the fee per bottle sold (column 'State Bottle Retail' in our dataset). The State wants to agile administrative checkpoints, whose counties are more profitable. Part of the new procedures could be extending the deadline to pay the fees.

Xxxxxxxxxx


## Outcome
#### [Part A:](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Part_A--Exploratory_Analysis.ipynb "Part A:") Data Insights.
1.- According to Iowa State data, the Top 10 counties with the highest volume sale (gallons) were identified. Using the bar chart below, we can see that the highest volume of sales occurs in the last quarter of the year. As we are in August 2022, if the Iowa Alcoholic Beverages Division wants to make improvements, it must be careful not to affect the highest volumes reported by the end of the year.

![Top 10](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Top%2010%20volume%20sold.png "Top 10")


2.- By evaluating profit performance by county, our stakeholder (Iowa Alcoholic Beverages Division) hoped to have a better idea of the focus point, thus reducing checkpoint downtime. In Part A of the study, we developed coding to determine which counties account for 80% of the volume sold, and which counties account for 80% of the state's profit. Using both lists, we identified 22 counties, as shown in the graph below.

![22 counties](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/PROFIT%20pareto%20location.png "22 counties")

According to the packed bubbles graph below, these are the top ten counties in terms of profit and volume sold in 2019, 2020, and 2021.

![Top 10](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Iowa%20Top%2010%20volume%20sold%20profit.png "Top 10")

#### [Part B:](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/Part_B--ML_Modeling.ipynb "Part B:") Predictive Model.
1.- This part of the project produced the best results for each regression model tested. Below are the graphs showing the best results for each model. Based on the results, Random Forest is the model of choice. It has a lower MAE, meaning that is more accurate, and the highest R2 Score meaning is the most precise.   

![ML Metrics](https://github.com/edleafvirtual/Iowa_Liquor_Sales/blob/main/ML%20metrics.png "ML Metrics")

## Recomendations
1.- Select 1% of the data per year (2012 - 2021), concatenate them in order to re-do the Part B of the project. The model should learn from yearly behavior.

2.- Tune the hyperparameters of the predictive model selected, using multiple [cross-validation](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74 "cross-validation") methods. 

3.- Once the model is tuned, we would use its predictive values in order to plot more insights and also to show what our predictions look like. Subsequently in January 2023 when real data from 2022 were available in the data [source](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy "source"), we will be able to compare our model. This analysis would deliver some insights about the approach to be done by Data Engineering, to then enrich our Machine Learning process in order to deliver a product that could predict more precise and accurate future scenarios.

## Limitations
- Splitting the data for Visual Exploration considering only 2019, 2020, and 2021 because of technical limitations (RAM/memory), is something that could have affected the final result. Trying to use some [ETL tools](https://www.geeksforgeeks.org/top-7-python-etl-tools-to-learn/?ref=gcse "ETL tools") or a cloud environment like AWS sounds to be a great solution.

- By tuning our chosen predictive model, we should find the best environment for this task without burning time because of RAM\memory issues. It's true that Data Engineering could have a better effect on our model than just tuning, but selecting the right hyperparameter is very important.


## Credits
### Eduardo Galindez
<p>
  <a href="https://www.linkedin.com/in/eduardogalindez/" rel="nofollow noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin">
  </a> &nbsp; 
  <a href="https://github.com/edleafvirtual" rel="nofollow noreferrer">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="github">
  </a>
</p>
