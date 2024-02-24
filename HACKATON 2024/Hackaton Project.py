##imitation of a JSON DATA transformed into a Key and Values
UserData={
  "User":"John Doe", "Age": 30,"City": "New York", "Anual Debt": 5000, "Anual Income": 40000, "Average expenses": 10000, "Savings": 8000, "Loans": 3000, "Credit": 6000, "Investments": 7000, "Balance": 40000, "Montly Expenses": , "Monthly Income": 10000, "Monthly Savings": 8000, "Monthly Loans": 3000
}


##Filtrates de info and calculates how much money is left after eliminating the money that is compromised.
def UserInfoFiltration(data):
  dict={"Usable money":0, "Left Money":0, "Used week":""}
  for k,v in data.items():
    if(k=="User"):
      dict[k]=v
    if(k=="Age"):
      dict[k]=v
    if(k=="City"):
      dict[k]=v
    if(k=="Anual Income"):
      
      dict[k]=v
    if(k=="Average expenses"):
      dict[k]=v
    if(k=="Savings"):
      dict[k]=v


# UserInfoFiltration(UserData)

def TripDays(option, filteredData):
  if(option=="Weekends"):
    filteredData["Used week"]= "Weekends"
  elif(option=="Weekdays"):
    
    
    
    


