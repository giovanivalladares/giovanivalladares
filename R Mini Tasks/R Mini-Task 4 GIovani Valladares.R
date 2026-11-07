# This script contains solutions for R Mini-Task 4
# Please follow the prompts and add your code directly beneath each prompt as appropriate
# Once finished, please update the file name to "R Mini-Task 4 FIRSTNAME LASTNAME"
# Once you've updated the file name, upload/submit your script to Canvas
# Add a comment to your Canvas submission describing, e.g., challenges, errors, victories

# Before beginning this task, download "R Mini-Task 4 Dataset.csv" from Canvas 
# Then import the dataset into R, label it df and enable headings
# Note that this is the same dataset that we used in R Mini-Task 2

# I encourage you to think through the results and consider what conclusions you would make
# For example, which effects/differences are significant (p < .05)? Which aren't (p > .05)? 

# Step 1. Conduct an independent-samples t-test on the GPAs of people who agree vs. disagree
# Hint: You'll need to use bracket notation when specifying "x" and "y" in t.test()
# Hint: Don't conduct a Welch's t-test by accident! Assume homogeneity of variances 

t.test(x = df$gpa[df$opinion == "Agree"],
       y = df$gpa[df$opinion == "Disagree"], var.equal = TRUE)

# Step 2. Use aggregate() to calculate mean GPAs for participants in each of the three conditions
# Hint: If it's been a while since you've used aggregate(), you can always run ?aggregate for help/examples

aggregate(df,gpa~condition,mean)

# Step 3. Test whether there are significant differences among those means using a one-factor ANOVA
# Hint: Remember to summarize your model with summary() to see the p-values
# Hint: Your ANOVA should report only one main effect

model1 <- aov(gpa~condition, df)

summary(model1)

# Step 4. Use aggregate() to calculate the mean GPAs for each combination of condition and opinion
# Hint: You can aggregate by an additional variable using + (again, see the help documentation for examples)

aggregate(df,gpa~condition+opinion,mean)

# Step 5. Conduct a factorial ANOVA to test the main effects of and interaction between condition and opinion on GPA
# Hint: Your factorial ANOVA should report two main effects (one for each factor) and an interaction

model2 <- aov(gpa~condition * opinion, df)

summary(model2)
