import requests
from datetime import datetime



today =datetime.now()

USER = "fepop"
TOKEN = "bruhmomento"
graph_config = {

    "quantity":"9"
}


header = {
    "X-USER-TOKEN":TOKEN
}

#direct link is https://pixe.la/v1/users/fepop/graphs/bruhz1.html


pixela = f"https://pixe.la/v1/users"
endpoint = f"{pixela}/{USER}/graphs/bruhz1/{today.strftime('%Y%m%d')}"

pixel_response = requests.put(url=endpoint,headers=header,json=graph_config)




print(pixel_response.text)
