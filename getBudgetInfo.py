#need a way to sanitize user input before actually sending to API
#this step in the actual program will be pure user input, which will 
budget = input("Tell us your budget - we'll show you a smart, personalized ideas powered by AI")
try:
   budget_value = float(budget)
except ValueError:
   print("This is not a valid budget price. Please enter a non-zero dollar amount, without '$' or any other characters.")
#...santization/checking... before getting sent to API

#category will be text, can simply choose from options given in frontend to 
catDict = {"Travel":1, "Food":2, "Education / Courses":3, 
           "Housing / Rent Rate":4, "Save & Grow It":5, "Fitness and Wellness":6, 
            "Social Impact & Charity":7, "Entertainment":8, "Emergency Fund":9, 
            "Subscriptions and Memberships":10}

#in future implementation, this section won't be user-text input, but simply chosen from the clickable options on the frontend, which will be sent here;
#this line is simply testing the inputs to the API
category = catDict.get(input("Which category would you like?"))
catValid = False
if (category in catDict):
   catValid = True

else:
   print("That is not a valid category. Please try again.")