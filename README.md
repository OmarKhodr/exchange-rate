# Currency Exchange Rate
EECE 430L Project developed for Web, Desktop and iOS.
Supervised by Dr. Mohamad Chehab.
Developed by:
- Hussein Jaber
- Maria Mattar
- Charbel Chucri
- Omar Khodr.

## Functional Documentation

These are the features supported by our platforms (Web, Desktop and iOS). Their ordering or visual representation differs slightly between the platforms to accomodate for their particularities.

### User Accounts
The app supports performing transactions anonymously or through an account which can be created and logged into through the app by assigning to each user a unique username.

### Recording a Transaction
Adding a transaction is done by specifying the USD and LBP amounts, the direction of the transaction as well as if it is directed to a specific user (this option is only available when the user is logged in).

### Exchange Rates
See the USD/LBP exchange rates (how much LBP to buy/sell 1 USD) averaged over the last *N* days where *N* is specified by the user (it is 3 by default).

### Statistics
The statistics section displays a graph that plots the daily average exchange USD/LBP rates over variable ranges (30, 60 or 90 days) as well as detailed statistics which display the max, average and standard devitation of both exchange rates from the last 30/60/90 days as well as a prediction of the next transaction's value.
A table that lists all past transactions is also displayed. The table can be filtered to only show transactions done between users. The backend also predicts using 
Linear Regression the rate of the next USD->LBP and LBP->USD transaction (Note that this idea (and not the implementation) was taken from another team (Simon, Karim, and Karim) with consent)

### Exchange Rate Calculator
The calculator allows the user to convert a specific amount of a given currency (LBP or USD) to the other at the exchange rate shown on the main view (USD/LBP exchange rates averaged over the last *N* days).

### Architecture
Below is a simple diagram that shows that whole system architecture. Feel free to read more about every platform used in their corresponding Readme.md file

![alt text](https://github.com/OmarKhodr/exchange-rate/blob/main/Archi.PNG?raw=true)
