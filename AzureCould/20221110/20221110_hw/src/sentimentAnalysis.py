from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    secret_key = "83ceeeea471c4fd5968a9db479da27b1"
    endpoint = "https://sentimentanalysis-20221110.cognitiveservices.azure.com/"

    ta_credential = AzureKeyCredential(secret_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(client):
    documents = [
        {
            "id": "1",
            "language": "zh-hant",
            "text": "我今天好快樂"
        },
    ]

    response = client.analyze_sentiment(documents=documents)

    for document in response:
        print("Document Id: ", document.id)
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for idx, sentence in enumerate(document.sentences):
            print("Sentence: {}".format(sentence.text))
            print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))


client = authenticate_client()
sentiment_analysis_example(client)