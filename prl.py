import requests

#-------------Core requests-------------
def rawGet(URL, PARAMS = None):
    response = requests.get(URL, params=PARAMS)
    return response

def rawPost(URL, DATA = None):
    response = requests.post(url=URL, data=DATA)
    return response

def rawPut(URL, DATA = None):
    response = requests.post(URL, data=DATA)
    return response
#-------------Core requests-------------
baseURL = "https://pbell97.pythonanywhere.com/"

def get(endpoint):
    """Gets data from Patrick's REST serve with the provided enpoint

    Arguments:
        endpoint {string} -- The endpoint to be reached

    Raises:
        Exception -- Throws exception if a successful get wan't accomplished (status code 200)

    Returns:
        string -- Returns a string of the received data
    """

    endpoint = endpoint.strip("/")
    fullURL = baseURL + endpoint + "/"
    response = rawGet(fullURL)
    if (response.status_code != 200):
        raise Exception("Expecting response code of 200, received " + str(response.status_code) + ". Attempted URL: " + fullURL)
    else:
        return str(response.text)


def post(endpoint, data):
    """Posts data to Patrick's REST api with the provided endpoint
    
    Arguments:
        endpoint {string} -- The endpoint to be reached
        data {dict} -- The dictionary object of data to be posted
    
    Raises:
        Exception -- Throws exception if the data isn't a dictionary object
        Exception -- Throws exception if the post wasn't successfull (status code 201)
    
    Returns:
        string -- Returns a string of the received data
    """

    endpoint = endpoint.strip("/")
    fullURL = baseURL + endpoint + "/"

    if(type(data) != dict):
        raise Exception("Data parameter must be of type 'dict'")

    response = rawPost(fullURL, DATA=data)
    if (response.status_code != 201):
        raise Exception("Expecting response code of 201, received " + str(response.status_code) + ". Attempted URL: " + fullURL)
    else:
        return str(response.text)