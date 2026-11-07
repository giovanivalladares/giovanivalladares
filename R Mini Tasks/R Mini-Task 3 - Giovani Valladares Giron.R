# This script contains instructions for R Mini-Task 3
# Please follow the prompts and add your code directly beneath each prompt as appropriate
# Once finished, please update the file name to "R Mini-Task 3 FIRSTNAME LASTNAME"
# Once you've updated the file name, upload/submit your script to Canvas
# Add a comment to your Canvas submission describing, e.g., challenges, errors, victories

# Before beginning this task, download "R Mini-Task 3 Dataset.csv" from Canvas 
# Then import the dataset into R, label it df and enable headings

# Step 1. Run the following line of code to produce a plot using base R graphics. 
plot(df$age, df$sexism,
     main = "Relationship Between Age and Sexism",
     xlab = "Age",
     ylab = "Sexism",
     pch = 16,
     col = "brown1")

# Step 2. Use ggplot2 to create a plot as similar as possible to the one from Step 1. 
# It's okay if you can't match it exactly, but try to get as close as you can! 
install.packages("ggplot2")

library("ggplot2")

ggplot(data = df, aes(x = age, y = sexism)) +
  geom_point(col = "red") + 
  ggtitle("Relationship between Age and Sexism") + 
  xlab ("Age") + 
  ylab("Sexism") + theme_bw() +
  scale_x_continuous(breaks=18:26) +
  scale_y_continuous(breaks=1:10)

# Step 3. Create a visualization of your own using any combination of variables in df
ggplot(data = df, aes(x = sexism)) + 
  geom_boxplot(aes(fill = gender)) +
  coord_flip() + xlab("") +
  theme_bw() +
  scale_x_continuous(breaks=1:10) + 
  ggtitle("Distribution of Sexism Scores by Gender") + 
  xlab("Sexism Scores") +
  scale_y_continuous(breaks = NULL) + facet_grid(~gender)

# scale_y_discrete()# You can use base R or ggplot2, but try to make it as nice and customized as you can! 
# After your code, please add a comment with a quick interpretation of the plot you made
