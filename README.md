![Banner](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Images/CreditCardBanner.png)

## Purpose
Use K-Means (Unsupervised Machine Learning Model) to identify clusters in the data and determine which group of customers is aligned with each credit card. Create a dashboard that allows stakeholders to determine more insights per cluster through an interactive interface.

<img src="https://raw.githubusercontent.com/matiassingers/awesome-readme/master/icon.png" align="right" />

## Author
#### Name: Eduardo Galindez.
#### Date: Octuber 2022.

<img alt="GitHub followers" src="https://img.shields.io/github/followers/edleafvirtual?style=social"> <img alt="GitHub User's stars" src="https://img.shields.io/github/stars/edleafvirtual?style=social"> <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/edleafvirtual/sales_predictions2023?style=social">

## General Information

Our stakeholder is a Financial Company that wants to market new credit cards.  They have asked us to segment their potential customers to determine how and what kind of cards they should market to each group.
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

#### Main Objective:
Identify the groups (clusters) that should be targeted for marketing by credit card type.

#### Specific Objectives:
- Use a clustering algorithm to find groups which have not been explicitly labeled in the data.
- Develop a scoring method to profile the customers.
- Recommend how to market each group per credit card type.
- Deploy a web app (Dashboard) for future research.

#### Scope:
- The code of the project was developed in three parts:
   - [Part A:](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Part_A_KMeans.ipynb) Unsupervised Machine Learning Model ([KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)).
   - [Part B:](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Part_B_AB_Testing.ipynb) A/B Testing.
   - [Dashboard:](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/app.py) Streamlit App.


## Outcome
### Part A: Unsupervised Machine Learning Model (KMeans).
1.- The Machine Learning model helped us to identify three groups to be marketed: Cluster A, Cluster B & Cluster C. The graph below shows:
  - There is not significant different in age, between Cluster A and C.
  - Cluster B is the highest in income, education level and years employeed.

![KPI 1](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Images/KPI%20-%20Income%20hued%20by%20Age.png)

2.- Plotting the relationship between income, debt and debt income ratio we identified how risky is Cluster B. In fact, in [Part A](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Part_A_KMeans.ipynb) we described which financial product should be marketed to this group, instead of a credit card.

![KPI 2](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Images/KPI%20-%20Income%20hued%20by%20Debt%20%26%20Debt%20Income%20Ratio.png)


### Part B: A/B Testing.
The code was developed to determine income vs debt focus points in the marketing strategy. Based on the model developed, we concluded that Platinum Credit Card should be marketed to Cluster A using an income performance-based strategy.

In the [notebook](https://github.com/edleafvirtual/Project-4-How_to_Market_New_Cards/blob/main/Part_B_AB_Testing.ipynb), we described why using a debt performance-based strategy could boost Gold Credit Card's conversion rate.


### Dashboard: Streamlit App.
We created a [web application](https://edleafvirtualproject4.streamlitapp.com/) with dynamic filters to interact with all variables of the database using the streamlit library and Python. By using the app, our stakeholders can go deeper into research per group (Cluster).


## Recomendations
1.- Xxxxx.

2.- Xxxxxxx. 

3.- Xxxxxx.

## Limitations
- Xxxxxxx.


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
