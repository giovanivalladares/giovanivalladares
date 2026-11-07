# This script contains instructions for R Mini-Task 2
# Please follow the prompts and add your code directly beneath each prompt as appropriate
# Once finished, please update the file name to "R Mini-Task 2 FIRSTNAME LASTNAME"
# Once you've updated the file name, upload/submit your script to Canvas
# Add a comment to your Canvas submission describing, e.g., challenges, errors, victories

# Before beginning this task, download "R Mini-Task 2 Dataset.csv" from Canvas 
# Then import the dataset into R, label it df and enable headings

# Step 1. Print the column headings and first 6 rows of the data frame

head(taskdf)

# Step 2. Reorder the rows by condition (A, then B, then C); print but don't save

taskdf[order(taskdf$condition),]

# Step 3. Reorder the rows by condition AND opinion; print but don't save

View(taskdf[order(taskdf$condition, taskdf$opinion),])

# Step 4. Use subset() to print data for participants in condition A with a gpa over 3.50

subset(taskdf, taskdf$condition == "A" & taskdf$gpa > 3.5)

# Step 5. Repeat Step 4, but only print the subjectid and gpa columns

subset(taskdf, taskdf$condition == "A" & taskdf$gpa > 3.5, select = -c(condition:opinion))

# Step 6. Repeat Step 4, but print all columns EXCEPT condition

subset(taskdf, taskdf$condition == "A" & taskdf$gpa > 3.5, select = -c(condition))

# Step 7. Use table() to display a frequency table for condition AND opinion

table(taskdf$condition,taskdf$opinion)

# Step 8. Use aggregate() to compute the mean gpa for each condition

aggregate(gpa ~ condition, taskdf, mean)
