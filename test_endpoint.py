import json

def classify_deployed(file_name, classes):
    payload = None
    with open(file_name, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)
    runtime_client = boto3.client('runtime.sagemaker')
    response = runtime_client.invoke_endpoint(EndpointName = "image-classification-2020-12-14-00-17-31-761",ContentType = 'application/x-image',Body = payload)
    result = json.loads(response['Body'].read())
    print(f"Image is {classes[np.argmax(result)]}")

classify_deployed("./pearl-5.jpg",["mona-lisa","pearl"])