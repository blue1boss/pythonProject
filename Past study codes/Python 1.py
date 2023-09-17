'''
Let's take this ammusement park data from online.
Suppose we are working for the ammusement park company
and that was recently opened and to get a
better idea about things we sent out a survey.
We will use the survey data to try and get an idea
of how consumer satisfactions has varied.
Idealy, we would have been with the team designing the survey,
 but we weren't, and so we'll do the best with what we've got.
'''


# Here, we just change some options to help with display.
%config InlineBackend.figure_format = 'svg'
import pandas as pd  #Important ones, the last three lines are effect how things are gonna be displayed.
# bringing extra library in the python system.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 70)



#Load data
#We are getting the data from online, so hopefully they didn't change the link!
import pandas as pd #type pd whenever wanna use pandas
# import numpy as np  # numpy using will be np calling
sat_df = pd.read_csv('http://bit.ly/PMR-ch7') #changing into a dataframe , created a name called sat
sat_df.head()

#Produce outcome below , take the dataframe to use a function and see the head of the dataframe
#waittime of the park - high points maybe the people was not very much for riding etc reason
#overall rating of the park itself.

sat_df.describe().round(2) #소수점 2번째자리까지 만들기

# We change a few options in seaborn to draw correlation charts and preform graphical analysis of the data.
# We are looking for linear relationship between the dependent and indipendent variables and and distributions with long tails (look at distance distribution!).
import seaborn as sns
sns.set_context('paper')
import matplotlib.pyplot as plt
# Create a pairgrid plot and store it in varible "g". We use the replace function here to change the True/False varibles to numerical varibles so we can graph them.
# The height and aspect object just let us create a prettier output.
g = sns.PairGrid(sat_df.replace({False: 0, True: 1}),
                 height=1.2, aspect=1.0)
# Use the map_upper function on g to define what we will see on the upper diagonal. In this case, we want a scatterplot.
g.map_upper(sns.scatterplot, linewidths=1, edgecolor="w", s=10,
            alpha=0.5)  # upper: Put the upper triangle of G , scatter plot or other options
# On the diagonal, we want histograms.
g.map_diag(plt.hist) # histogram
# On the lower part, we will get density plots.
g.map_lower(sns.kdeplot)

#data has a upward direction shape to them, positive correlation from it : one thing higher score, the rest of them also could be given a higher score
#Cleaness is the best scored data, wait/ ride / games have to be improved overall

#Correct for the distance distribution by taking the logarithm.
sat_df['log_dist'] = sat_df.distance.apply(np.log)

#Display the log(distance) by using the hist function and check that the problems is corrected.
# Looks close to normal so we have done a good job!
sat_df.log_dist.hist()
plt.xlabel('log distance')
plt.ylabel('Count')
#long right tail= everything is pushed to the left side.

#Check the correlations between our variables. This will give us an idea of where we might get low p-values because of multicolliniarity.
#Have a positive or negative relationship with each other? / correlation =1 perfectly straight line related to each other  (Clean and rides are tightly related to each other)
# Games on the weekends are not happy with (having a negative relationship number)
sat_df.corr()

# It can be simpler to look at the correlations with color to immidiatly direct our eyes to correlated variables (like rides and clean).
# This will also give us numbers to go with the visual analysis.
sat_df_corr = sat_df.corr()
sns.heatmap(sat_df_corr, annot=True, fmt=".2f",
            mask=~np.tri(sat_df_corr.shape[0], k=-1, dtype=bool),
            cbar=False)


# If we would like to get more details on a relationship, we can use the plot function to get a scatterplot.
# For example, here we see the relationship between rides and overall satisfaction.  It seems like they are highly coorelated.
sat_df.plot(kind='scatter', x='rides', y='overall')
# Setting the options for the function, what type and kind is it = it is a scatterplot (dataframe scatterplot)
plt.xlabel('Satisfaction with rides')
plt.ylabel('Satisfaction overall')


'''
Important part for ols
'''
 Let's try a very simple linear regression with rides as our only x variable.
# It seems like the effect is very strong! When the guest gave one more point to rides, they were likely to give about 1.3 more points to overall satisfaction!
import statsmodels.formula.api as smf
smf.ols('overall ~ rides', data=sat_df).fit().summary()

#overall은 여러개의 항목 variable중에 1개를 선택해서 진행한 것을 의미
# Result: Intercept / coeffiencit = expect the satisfication is -28
# Rides coefficent : each adding point satisifaction +1, more generall happy for the 1.2887, so it is very important when consdiering the individual section .
# R square = 0.407 rides alone back up how the satisfication to the park (one variable called ride is taking 40% of the general satisification- rather very important side)
# std error for ride is low 0,070 (add 2 std error and subtract to get the range of the coefficient)
# P>|1| rides and satisifaction are connected, less possibility of having errors with the relationship


# Here lets save our regression in variable name m1.
m1 = smf.ols('overall ~ rides', data=sat_df).fit()

# This plot and the one below it are identical
sat_df.plot(kind='scatter', x='rides', y='overall')
plt.plot(sat_df.rides, m1.predict(sat_df.rides))

#Now lets do a more in-depth survey analysis to get a better idea
# of the which variable will be more important in determining satisfaction for our amusement park.

m2 = smf.ols('overall ~ rides + games + wait + clean',
             data=sat_df).fit()
m2.summary()

#regression ols function using able to do this
#multiple x variables having here has 4 variables : intercept is lower than before
#just by looking at the coefficient = P value same 0, all of them influencial of the result in some sense take care - bigger coeffient = bigger influence
#clean / rides / wait / games . might not care games so much - easily increase as the same cost, maybe in order of importance
#R squared : how accurated / clean back up strongly how much 4 factors explain satisfaction about 60%