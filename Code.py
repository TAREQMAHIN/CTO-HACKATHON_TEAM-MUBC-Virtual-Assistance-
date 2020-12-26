import os
import io
import boto3
import csv
import json
ENDPOINT_NAME = os.environ['chatbot']
runtime = boto3.client('runtime.sagemaker')
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(even))
    payload = data['data']
    print(payload)
    
    response = runtime.invoke_endpoint(EndpintName=ENDPOINT_NAME,
                                        ContentType='text/csv',
                                        Body = payload)
    
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)
    pred = int(result['predictions'][0]['score'])
    predicted_label = 'M' if pred == 1 else 'B'
    # TODO implement
    return predicted_label
