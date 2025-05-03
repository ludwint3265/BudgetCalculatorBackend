import sys

#need a way to sanitize user input before actually sending to AI
#this step in the actual program will be pure user input, which will 
catValid = False
budgetValid = False
budgetValue = 0
category = ""
def main():
   global catValid, budgetValid, budgetValue, category, budget_value
   budget = input("Tell us your budget - we'll show you smart, personalized ideas powered by AI" )
   try:
      budget_value = float(budget)
      if budget_value > 0:
         budgetValid = True
      else:
         print("Please enter a budget greater than 0.")
         return
   except ValueError:
      print("This is not a valid budget price. Please enter a non-zero dollar amount, without '$' or any other characters.")
      return
   
   #...santization/checking... before getting sent to AI

   #category will be text, can simply choose from options given in frontend to match with these in future
   catDict = {
      "Travel": 1,
      "Food": 2, 
      "Education / Courses": 3, 
      "Housing / Rent Rate": 4,
      "Save & Grow It": 5, 
      "Fitness and Wellness": 6, 
      "Social Impact & Charity": 7, 
      "Entertainment": 8, 
      "Emergency Fund": 9, 
      "Subscriptions and Memberships": 10
   }

   #in future implementation, this section won't be user-text input, but simply chosen from the clickable options on the frontend, which will be sent here;
   #this line is simply testing the inputs to the API

   category = input("Which category would you like?" )
   while (catValid == False):
      if (category in catDict):
         catValid = True
         print("Now preparing possible plans...")
      else:
         print("That is not a valid category. Please try again.\n")
         category = input("Which category would you like")

if __name__ == "__main__":
   main()
      