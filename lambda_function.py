#  write a lambda function to use sagemaker inference endpoint
import boto3
import json
import ast

def lambda_handler(event,  context):
  
    runtime_client =  boto3.client('runtime.sagemaker')
  
    endpoint_name = 'xgboost-2024-05-02-21-51-28-886'
  
    #sample = '7.0,3.2,4.7,1.4'
    sample = '{},{},{},{}'.format(ast.literal_eval(event['body'])['x1'],
                                  ast.literal_eval(event['body'])['x2'],
                                  ast.literal_eval(event['body'])['x3'],
                                  ast.literal_eval(event['body'])['x4'])
  
    response = runtime_client.invoke_endpoint(EndpointName=endpoint_name,
                                              ContentType='text/csv',
                                              Body=sample )
    result =  int(float(response['Body'].read().decode('ascii')))
  
    print(result)
  
    return{
           'statusCode': 200,
           'body': json.dumps({'Prediction': result})
           #'body': "Hello"
          }
  
