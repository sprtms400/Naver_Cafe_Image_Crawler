#%%
import requests
import json
import time
import pika

IMAGE_PATH = 'images'
MAPFILE_NAME = 'map.json'

def extract_artworks(nodes):
    artworks = []
    for node in nodes:
        if node['nodeType'] == 'artwork':
            artworks.append(node)
    return artworks

def quque_uploader(project_path):
    with open(project_path+'/'+ MAPFILE_NAME) as f:
        mapfile = json.load(f)
    artworks = extract_artworks(mapfile)
    rabbitmq = 'localhost'
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq))
    channel = connection.channel()
    channel.queue_declare(queue='analyzingQueueNumberPlate', durable=True)
    channel.queue_declare(queue='analyzingQueueAppearance', durable=True)
    
    photoIds = [artwork['nodeId'] for artwork in artworks]
    for photoId in photoIds:
        photoId_bytes = photoId.encode()
        response_a = channel.basic_publish(exchange='', routing_key='analyzingQueueNumberPlate', body=photoId_bytes)
        response_b = channel.basic_publish(exchange='', routing_key='analyzingQueueAppearance', body=photoId_bytes)
        print('response_a:', response_a, 'response_b:', response_b)

def upload_project(project_path):
    meters = 0
    responses = []
    mapfile = None
    with open(project_path+'/'+ MAPFILE_NAME) as f:
        mapfile = json.load(f)
    print('mapfile:', len(mapfile))
    artworks = extract_artworks(mapfile)
    print('Artworks:', len(artworks))
    
    for artwork in artworks:
        time.sleep(0.2)
        print('Uploading', artwork['nodeId'], '... meters:', meters)
        image_path = project_path+'/'+IMAGE_PATH+'/'+artwork['nodeId']
        print('image_path:', image_path)
        data = {
            'photoId': artwork['nodeId'],
            'competition': '2023상주그란폰도',
            'author': '굼디바이크',
            'photographedTime': '2024-03-08T18:52:33.101580',
            'srcLink': artwork['url'],
            'accessUserId': 'demo'
        }
        files = None
        with open(image_path, 'rb') as file:
            files = {'file': (image_path, file)}
            response = requests.post('http://localhost:3000/photo/upload', files=files, data=data)
            meters += 1
            print('response:', response.status_code, response.text)
            responses.append(response)
    
    print('Upload complete')
    print('Total requests:', len(responses))
    print('success:', len([response for response in responses if response.status_code == 200]))

upload_project('../kumdibike_2023_상주그란폰도_2024-03-08_18:33')
# quque_uploader('../kumdibike_2023_상주그란폰도_2024-03-08_18:33')