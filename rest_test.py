import requests
import base64

b64_ims = []
im_paths = [
      './testimage.jpg' 
]
for im_path in im_paths:
    with open(im_path, 'rb') as f:
        im_b64 = base64.encodebytes(f.read()).decode('utf-8')
        b64_ims.append(im_b64)

#payload = {"images": b64_ims, "ids" : [1,2,3,4,5,6]}
#resp = requests.post('http://127.0.0.1:5000/validate', data=payload)
#print(resp.status_code)
#print(resp.content)

#payload = {"images": b64_ims, "ids" : [1,2,3], "db_id" : 1}
#resp = requests.post('https://demo2020-app.herokuapp.com/detect', json=payload)
#print(resp.status_code)
#print(resp.content)


payload = {"image": b64_ims[0], "ids" : [1], "db_id" : 'demo'}
resp = requests.post('http://localhost:5000/predict', json=payload)
print(resp.status_code)
print(resp.content)
#myobj = {'id': 1}
#resp = requests.post('https://demo2020-app.herokuapp.com/train', data=myobj)
#print(resp.status_code)
#print(resp.content)

#resp = requests.post("http://127.0.0.1:5000/predict",
#                     files={"file": open('/home/axd170033/face_recognition/dataset/images_cropped/Aaron_Peirsol/Aaron_Peirsol_0004.jpg','rb')})
#print(resp.status_code)
#print(resp.json())
