from googleapiclient.discovery import build
import time
import requests
from bs4 import BeautifulSoup
import re



def google_search(api_key, search_engine_id, query):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=search_engine_id).execute()
    return res['items']



def scrape_expedia_deal(url):


  # Extracting hotel name
  # hotel_name = soup.find('h1', class_='uitk-type-heading-500').text.strip()
  hotel_name="Dominican Fiesta Hotel"

  budget=392
  stay_duration="Weekend"

  things_to_do=["Pool","Restaurants","Bars"]

  # Building dictionary with scraped information
  expedia_deal_info = {
      'Destination': url,
      'hotel': hotel_name,
      'budget': budget,
      'stay_duration': stay_duration,
      'things_to_do': things_to_do[:3]  # Limiting to the first 3 things to do
  }
  return expedia_deal_info


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



def Itinerary_Trip(dic, TripCost,TripLocation):
  print("Itinerary:")
  print(f'{dic["City"]} to {TripLocation}')
  print(f'Stay: {dic["Used week"]}')
  dic["Travel Budget"]=TripCost
  print(f'Travel Cost: {dic["Travel Budget"]}')


def main():
  #Imitation of a JSON Data transformed into a dictionary
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
  #####Extract User Data##########################################
  
  res=UserPercentageFiltration(UserData)
  
  ###Search for posible Trips##########################################
  
  # Info that lets us search in google, searching terms and searched data
  api_key = 'AIzaSyB9Pb1pVGt5n1o0i6DIqMWqcaQl80uEF5s'
  search_engine_id = '360a3807299d24b9e'
  query_terms = ['All_inclusive','Expedia','Weekend']
  results = google_search(api_key, search_engine_id, query_terms)

  # Procesar los resultados de la búsqueda
  for result in results:
      title = result['title']
      url = result['link']
      print(title,url)
      print()
      time.sleep(2)
  
  results=TripDays("Weekends",res)
  print()
  print()
  Itinerary_Trip(results,392,"Dominican Fiesta Hotel")
  print()
  x=input("Do you want to save this trip? ")
  print()
  if(x=="yes"):
    try:
      deal_info = scrape_expedia_deal(url)
      print(deal_info)
    except Exception as e:
      print(f"Error scraping {url}: {str(e)}")
    print()
    print("This info has been sent to mail")
    print("Thank you for using our service")
  else:
    print("Thank you for using our service")
main()




