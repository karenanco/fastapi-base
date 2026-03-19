import requests 


def buscar_noticias(query):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q":query,
        "apiKey":"5b86a818f6a1425db9f7380ca054b441"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    return data.get("totalResults" , [])
    print(datafil)
