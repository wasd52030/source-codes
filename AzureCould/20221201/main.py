import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "Inputs": {
        "WebServiceInput0": [
            {
                "symboling": 3,
                "normalized-losses": 1.0,
                "make": "alfa-romero",
                "fuel-type": "gas",
                "aspiration": "std",
                "num-of-doors": "two",
                "body-style": "convertible",
                "drive-wheels": "rwd",
                "engine-location": "front",
                "wheel-base": 88.6,
                "length": 168.8,
                "width": 64.1,
                "height": 48.8,
                "curb-weight": 2548,
                "engine-type": "dohc",
                "num-of-cylinders": "four",
                "engine-size": 130,
                "fuel-system": "mpfi",
                "bore": 3.47,
                "stroke": 2.68,
                "compression-ratio": 1.0,
                "horsepower": 1.0,
                "peak-rpm": 1.0,
                "city-mpg": 21,
                "highway-mpg": 27,
                "price": 1.0
            },
            {
                "symboling": 3,
                "normalized-losses": 1.0,
                "make": "alfa-romero",
                "fuel-type": "gas",
                "aspiration": "std",
                "num-of-doors": "two",
                "body-style": "convertible",
                "drive-wheels": "rwd",
                "engine-location": "front",
                "wheel-base": 88.6,
                "length": 168.8,
                "width": 64.1,
                "height": 48.8,
                "curb-weight": 2548,
                "engine-type": "dohc",
                "num-of-cylinders": "four",
                "engine-size": 130,
                "fuel-system": "mpfi",
                "bore": 3.47,
                "stroke": 2.68,
                "compression-ratio": 1.0,
                "horsepower": 1.0,
                "peak-rpm": 1.0,
                "city-mpg": 21,
                "highway-mpg": 27,
                "price": 1.0
            },
            {
                "symboling": 1,
                "normalized-losses": 1.0,
                "make": "alfa-romero",
                "fuel-type": "gas",
                "aspiration": "std",
                "num-of-doors": "two",
                "body-style": "hatchback",
                "drive-wheels": "rwd",
                "engine-location": "front",
                "wheel-base": 94.5,
                "length": 171.2,
                "width": 65.5,
                "height": 52.4,
                "curb-weight": 2823,
                "engine-type": "ohcv",
                "num-of-cylinders": "six",
                "engine-size": 152,
                "fuel-system": "mpfi",
                "bore": 2.68,
                "stroke": 3.47,
                "compression-ratio": 1.0,
                "horsepower": 1.0,
                "peak-rpm": 1.0,
                "city-mpg": 19,
                "highway-mpg": 26,
                "price": 1.0
            },
            {
                "symboling": 2,
                "normalized-losses": 1.0,
                "make": "audi",
                "fuel-type": "gas",
                "aspiration": "std",
                "num-of-doors": "four",
                "body-style": "sedan",
                "drive-wheels": "fwd",
                "engine-location": "front",
                "wheel-base": 99.8,
                "length": 176.6,
                "width": 66.2,
                "height": 54.3,
                "curb-weight": 2337,
                "engine-type": "ohc",
                "num-of-cylinders": "four",
                "engine-size": 109,
                "fuel-system": "mpfi",
                "bore": 3.19,
                "stroke": 3.4,
                "compression-ratio": 1.0,
                "horsepower": 1.0,
                "peak-rpm": 1.0,
                "city-mpg": 24,
                "highway-mpg": 30,
                "price": 1.0
            },
            {
                "symboling": 2,
                "normalized-losses": 1.0,
                "make": "audi",
                "fuel-type": "gas",
                "aspiration": "std",
                "num-of-doors": "four",
                "body-style": "sedan",
                "drive-wheels": "4wd",
                "engine-location": "front",
                "wheel-base": 99.4,
                "length": 176.6,
                "width": 66.4,
                "height": 54.3,
                "curb-weight": 2824,
                "engine-type": "ohc",
                "num-of-cylinders": "five",
                "engine-size": 136,
                "fuel-system": "mpfi",
                "bore": 3.19,
                "stroke": 3.4,
                "compression-ratio": 1.0,
                "horsepower": 1.0,
                "peak-rpm": 1.0,
                "city-mpg": 18,
                "highway-mpg": 22,
                "price": 1.0
            }
        ]
    },
    "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

url = 'http://20.27.45.147:80/api/v1/service/api/score'
# Replace this with the API key for the web service
api_key = 'Va0Z3p64WlyguAax7qcV5NEzKJTqeEC0'

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
