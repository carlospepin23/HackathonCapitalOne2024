UserData = {
  "User": "John Doe",
  "Age": 30,
  "City": "New York",
  "Anual Debt": 5000,
  "Anual Income": 80000,
  "Average expenses of Needs": 10000,
  "Average Savings": 8000,
  "Loans": 3000,
  "Credit": 6000,
  "Investments": 7000,
  "Balance": 40000,
  "Montly Expenses": 0,
  "Monthly Income": 10000,
  "Monthly Savings": 8000,
  "Monthly Loans": 3000
}

def UserPercentageFiltration(data):
  result = {"Travel Budget": 0, "Left Money": 0, "Used week": "", "Vacation Itinerary Percentage": 0}
  for k, v in data.items():
      if k == "Anual Income":
          result["Travel Budget"] = v
  
          if v >= 50000 and v<= 100000:
            vacation_percentage = 0.15
            result["Travel Budget"] = v * vacation_percentage
  
          elif v >= 25000 and v< 50000:
            vacation_percentage = 0.10
            result["Travel Budget"] = v * vacation_percentage
            
          elif v < 25000:
            vacation_percentage = 0.5
            result["Travel Budget"] = v * vacation_percentage

          result["Vacation Itinerary Percentage"] = vacation_percentage
  result["Left Money"] = data["Anual Income"] - result["Travel Budget"]
  result["Vacation Itinerary Percentage"]= vacation_percentage *100
  result["City"] = data["City"]
  return result


# result = UserPercentageFiltration(UserData)
# print(result)



def TripDays(option, filteredData):
  if(option=="Weekends"):
    filteredData["Used week"]= "Weekends"
  elif(option=="Weekdays"):
    filteredData["Used week"]= "Weekdays"
  elif (option=="Seasonal"):
    filteredData["Used Week"]="Seasonal"
  return filteredData

# res=UserPercentageFiltration(UserData)
# print(TripDays("Weekends",res))