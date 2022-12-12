import re
import requests
import uuid
from utils import AzureTranslateConfig
from utils import Logger


@Logger
def translate(text, resource, to, outputFilePath):
    # Add your key and endpoint
    key = AzureTranslateConfig.subscription_key.value.decode('utf-8')
    endpoint = AzureTranslateConfig.endpoint.value.decode('utf-8')

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = AzureTranslateConfig.region.value.decode('utf-8')

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': resource,
        'to': to
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    response = requests.post(
        constructed_url,
        params=params,
        headers=headers,
        json=body
    ).json()

    with open(outputFilePath, 'w', encoding='utf-8') as f:
        lines=response[0]['translations'][0]['text'].split('\n')
        result=[]
        for line in lines:
            if re.search('^\d+：\d+：\d+，\d+ --> \d+：\d+：\d+，\d+$',line):
                line = line.replace('：', ':')
                line = line.replace('，', ',')
            result.append(line)
        f.write('\n'.join(result))
