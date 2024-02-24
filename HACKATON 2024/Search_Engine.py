from googleapiclient.discovery import build

#function that gives us the links
def google_search(api_key, search_engine_id, query):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query,       
    cx=search_engine_id).execute()
    return res['items']

# information that makes us search in google(search engine)
api_key = 'AIzaSyB9Pb1pVGt5n1o0i6DIqMWqcaQl80uEF5s'
search_engine_id = '360a3807299d24b9e'
query = 'Google Travel'

#each link
results = google_search(api_key, search_engine_id, query)
for result in results:
    print(result['title'], result['link'])
    
#####################################################################################