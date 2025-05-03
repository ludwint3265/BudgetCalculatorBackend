from google import genai
from google.genai import types
import getBudgetInfo as bi
import privconfig as p

client = genai.Client(api_key=p.API_Key)

if (bi.catValid == True):
   price = bi.budget_value
   area = bi.category
   response = client.models.generate_content(
      model="gemini-2.0-flash", 
      config=types.GenerateContentConfig(
         system_instruction="You are a caring financial advisor, who wants to help people plan out how they can spend their budget, given a dollar amount and category/area they would like to spend it on"),
      contents="What are three ways I can spend a budget of " << bi.budget_value << " on " << bi.category << ", in a way that will stay within my means of living?"
   )
   print(response.text)
else:
   print("Your entered category was not valid. Please try again.")