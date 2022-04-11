## 7 April 2022 
1. Took referance from velotio's blog to create thee tier application in kuberneted on GKE ( i am doing in minikube ) 
2. Undestood how the Deployment finds the pod it wants to control. Following Selector and Label syntax in manifests 
            
           Selector: 
               MatchLabels 
                <kay> : <Value>
		
           Metadata:
                labels 
                <key>	: <value>
3. It took some time to port the Flask Script ( midleware ) from python 2.7 to Python 3.
4. Built the image after modifying the source code in app.py and updated the image tag in deployment manifest of app. 
5. There are some issues while connecting to database ( username , password ) 
6. Understood how mysql service ( DNS ) is used as DB host inside app.y  (  mysql-service.default ). ## default since it is in default workspace. 
7. Used Kubectl port forward to access the webpage from Host machine 

TODO for 8th April 
1. Use Confgmap to keep database username and password 
2. Do Database writes ( Insert Command ) from app.py 
3. Use Ingress controller to access the services 
4. Please ADD if you feel anything should be done


## 8 April 
1. Added ingress to Test App service 
2. No Success in inserting data into mysql due to credential issue. 
3. TODO : 
    Identify the username and password for mysql image and try to connnect 
    Try out Statefulset 
