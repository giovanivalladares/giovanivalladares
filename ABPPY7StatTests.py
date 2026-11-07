0#StatTests.py
"""
Created on Tue Oct 29 2019
This module compares two or more means and performs regression
@author: Kellie Keeling
"""
import matplotlib.pyplot as plt
from scipy import stats 
import numpy as np

def MeansTest(df,GroupCol,MeanCol):
    """This function allows you to compare either two or multiple means. 
    The output is a boxplot with appropriate
    Assumes matplotlib, statsmodels, scipy has been installed

    Keyword arguments:
    df -- a dataframe with at least one quantitative variable for means
          and one qualitative variable with categories for comparison
    GroupCol -- a name of a column in the dataframe with categories
    MeanCol -- a name of a column in the dataframe with quantatitive values
               this will be used to calculate the means to compare across Groups
    """
    
    #Determine number of Groups of Group Names
    GrpNames = df[GroupCol].unique()
    NumGrps = len(GrpNames)
    alpha = .05
    if NumGrps == 2:
        #if only 2 groups
        #First do t test for equal variances
        dfGrp1 = df.loc[df[GroupCol]==GrpNames[0],MeanCol]
        dfGrp2 = df.loc[df[GroupCol]==GrpNames[1],MeanCol]

        tvar, p_valvar = stats.bartlett(dfGrp1,dfGrp2)
        print(f"The groups are {GrpNames[0]} and {GrpNames[1]}")
        print("")
        print("This is a test of equal variances with Ho: The variances are equal")
        print(f"The t test statistic is {round(tvar,3)} and the p-value is {round(p_valvar,4)}")
        if p_valvar < alpha:
            print("Conclusion: Reject Ho: The variances are not equal")
            tEqVar=False
            ttype='Welch (unequal variances) Two-Sample t test'
        else:
            print("Conclusion: Fail to Reject Ho: We can't reject that the variances are the same")
            tEqVar=True
            ttype='Two-Sample t test (assuming equal variances)'

        #Second do the t test for equal means
        tmean, p_valmean = stats.ttest_ind(dfGrp1,dfGrp2,equal_var=tEqVar)
        print("")
        print("This is a " + ttype + " of equal means with Ho: The group means are equal")
        print(f"The t test statistic is {round(tmean,3)} and the p-value is {round(p_valmean,4)}")
        if p_valmean < alpha:
            print("Conclusion: Reject Ho: The means are not equal")
        else:
            print("Conclusion: Fail to Reject Ho: We can't reject that the means are the same")

        # Create the boxplot
        y=[dfGrp1,dfGrp2]
        plt.boxplot(y)
        plt.title(f't: {round(tmean,3)}, p-val: {round(p_valmean,4)}',size=10)
        plt.suptitle(ttype,size=10)
        plt.xticks(range(1,3),[f"{GrpNames[0]}: {round(dfGrp1.mean(),2)}",
                                   f"{GrpNames[1]}: {round(dfGrp2.mean(),2)}"])
        plt.ylabel(MeanCol)
        plt.savefig('ttest.png', bbox_inches='tight')
        plt.show()
    elif NumGrps in [3,4,5]:
        dfGrp1 = df.loc[df[GroupCol]==GrpNames[0],MeanCol]
        dfGrp2 = df.loc[df[GroupCol]==GrpNames[1],MeanCol]
        dfGrp3 = df.loc[df[GroupCol]==GrpNames[2],MeanCol]
        if NumGrps == 3:
            print(f"The groups are {GrpNames[0]} and {GrpNames[1]} and {GrpNames[2]}")
            y = (dfGrp1, dfGrp2, dfGrp3)
            f, p_val = stats.f_oneway(dfGrp1, dfGrp2, dfGrp3) 
            xticklabels = [f"{GrpNames[0]}: {round(dfGrp1.mean(),2)}",
                                   f"{GrpNames[1]}: {round(dfGrp2.mean(),2)}",
                                   f"{GrpNames[2]}: {round(dfGrp3.mean(),2)}"]
        elif NumGrps == 4:
            print(f"The groups are {GrpNames[0]} and {GrpNames[1]} and {GrpNames[2]} and {GrpNames[3]}")
            dfGrp4 = df.loc[df[GroupCol]==GrpNames[3],MeanCol]
            y = [dfGrp1, dfGrp2, dfGrp3, dfGrp4]
            f, p_val = stats.f_oneway(dfGrp1, dfGrp2, dfGrp3, dfGrp4) 
            xticklabels = [f"{GrpNames[0]}: {round(dfGrp1.mean(),2)}",
                                   f"{GrpNames[1]}: {round(dfGrp2.mean(),2)}",
                                   f"{GrpNames[2]}: {round(dfGrp3.mean(),2)}",
                                   f"{GrpNames[3]}: {round(dfGrp4.mean(),2)}"]
        elif NumGrps == 5:
            print(f"The groups are {GrpNames[0]} and {GrpNames[1]} and {GrpNames[2]} and {GrpNames[3]} and {GrpNames[4]}")
            dfGrp4 = df.loc[df[GroupCol]==GrpNames[3],MeanCol]
            dfGrp5 = df.loc[df[GroupCol]==GrpNames[4],MeanCol]
            y = [dfGrp1, dfGrp2, dfGrp3, dfGrp4, dfGrp5]
            f, p_val = stats.f_oneway(dfGrp1, dfGrp2, dfGrp3, dfGrp4, dfGrp5) 
            xticklabels = [f"{GrpNames[0]}: {round(dfGrp1.mean(),2)}",
                                   f"{GrpNames[1]}: {round(dfGrp2.mean(),2)}",
                                   f"{GrpNames[2]}: {round(dfGrp3.mean(),2)}",
                                   f"{GrpNames[3]}: {round(dfGrp4.mean(),2)}",
                                   f"{GrpNames[4]}: {round(dfGrp5.mean(),2)}"]
        print("This is a test of equal means with Ho: The means of all groups are equal/Ha: At least one group mean is different")
        print(f"The F test statistic is {round(f,3)} and the p-value is {round(p_val,4)}")
        if p_val < alpha:
            print("Conclusion: Reject Ho: At least one group mean is different")
            ANOVAtype = "ANOVA: At least one group mean different"
        else:
            print("Conclusion: Fail to Reject Ho: We can't reject that the means are the same")
            ANOVAtype = "ANOVA: Group Means are the same" 
        
   
    
        # Create the boxplot
        plt.boxplot(y)
        plt.title(f'F: {round(f,3)}, p-val: {round(p_val,4)}',size=10)
        plt.suptitle(ANOVAtype,size=10)
        plt.savefig('ANOVA.png', bbox_inches='tight')
        plt.xticks(range(1,NumGrps+1),xticklabels)
        plt.ylabel(MeanCol)
        plt.savefig('ANOVA.png', bbox_inches='tight')
        plt.show()

        #Creating Multiple Comparisions Analysis from ANOVA when p-value < alpha
        from statsmodels.stats.multicomp import pairwise_tukeyhsd

        tukey = pairwise_tukeyhsd(endog=df[MeanCol],     # Data (endogenous,response variable)
                                  groups=df[GroupCol],   # Groups
                                  alpha=0.05)          # Significance level

        print('Ho: The group means are equal')
        print(tukey.summary() )
        tukey.plot_simultaneous()    # Plot group confidence intervals
        plt.vlines(x=df[MeanCol].mean(),ymin=-0.5,ymax=NumGrps-.5, color="red")
        plt.show()
    else:
        print("This only works with 2-5 groups")
        
        
def mult_reg(model, ydata, actvspredplot=True, residplot=True,capture=False):
    """This function allows you to perform regression with one
    Response Variable (Y) and one or more Predictor (X) variables. 
    Assumes matplotlib, statsmodels has been installed
    Assumes you run from statsmodels.formula.api import ols

    Keyword arguments:
    model -- a regression model from ols using the format
    ols("Y ~ X1 + X2",data=df).fit()
    ydata -- a dataframe with the data
    actvspredplot -- return the plot or not showing actual vs predicted values
    residplot -- return the plot of residuals vs predicted Y
    capture -- return the adjusted r-square, p-value, regression equation
    """
    r2adj = round(model.rsquared_adj,2) #use for multiple regression
    reg_p_val = round(model.f_pvalue,4)
    coefs = model.params
    coefsindex = coefs.index #one person needed coefs.index.values to get to work
    regeq = round(coefs.iloc[0],3) #first get intercept
    cnt = 1
    for i in coefs[1:]:
        regeq=f"{regeq} + {round(i,3)} {coefsindex[cnt]}"
        cnt = cnt + 1
    miny=ydata.min()
    maxy=ydata.max()
    if actvspredplot==True:
        #Scatterplot for Multiple Regression - y vs predicted y
        predict_y = model.predict()
        plt.scatter(ydata,predict_y)
        diag = np.arange(miny,maxy,(maxy-miny)/50)
        plt.scatter(diag,diag,color='red',label='perfect prediction')
        plt.suptitle(regeq)
        plt.title(f' with adjR2: {r2adj}, F p-val {reg_p_val}',size=10)
        plt.xlabel(ydata.name)
        plt.ylabel('Predicted ' + ydata.name)
        plt.legend(loc='best')
        plt.show()
    if residplot==True:
        #Scatterplot residuals 'errors' vs predicted values
        resid = model.resid
        predict_y = model.predict()
        plt.scatter(predict_y, resid)
        plt.suptitle(regeq)
        plt.hlines(0,miny,maxy) #horizontal line at 0 error
        plt.ylabel('Residuals')
        plt.xlabel('Predicted ' + ydata.name)
        plt.show()
    if capture==False:
        return
    else:
        return(r2adj, reg_p_val, regeq)