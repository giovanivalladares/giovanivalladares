# This script contains instructions for R Mini-Task 1
# Please follow the prompts and add your code directly beneath each prompt as appropriate
# Once finished, please update the file name to "R Mini-Task 1 FIRSTNAME LASTNAME"
# Once you've updated the file name, upload/submit your script to Canvas
# Add a comment to your Canvas submission describing, e.g., challenges, errors, victories

# Step 1. Run the code below to add this new data frame to your R environment 
df <- data.frame(var1 = 1:50,
                 var2 = rep(c("Male", "Female", "Non-Binary"), each = 17, length.out = 50),
                 var3 = rep(c("Yes", "No"), 25),
                 var4 = runif(50,10000,120000))

# Step 2. Rename the columns of this new data frame to "subjectid", "gender", "collegedegree", and "income"

colnames(df) <- c("subjectid", "gender", "collegedegree","income")


# Step 3. Print the incomes of all participants

print(df$income)

# Step 4. Find the mean income for all participants 

mean(df$income)

# Step 5. Print the incomes of only female participants

print(subset(df, gender == "Female", select = income))

# Step 6. Find the mean income for only female participants

mean(df$income[df$gender == "Female"])

# Step 7. Find the mean income for only non-binary participants with a college degree

mean(df$income[df$gender == "Non-Binary" & df$collegedegree == "Yes"])

# Step 8. Find the mean income for only male participants without a college degree

mean(df$income[df$gender == "Male" & df$collegedegree == "No"])
