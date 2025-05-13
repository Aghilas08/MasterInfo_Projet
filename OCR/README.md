# Service OCR

### Docker

* **Création d'une image docker en locale**
  * Microservice OCR : ocr_app

````sh
docker build -t ocr_app .  
````

### Teste en local
* **lancer le service :** ``docker run -p 5002:5002 ocr_app``

![teste_ocr](/IMAGES/test_local_ocr.png)

# Docker Hub

* **Tag l'image docker :** ``docker tag 9248086ac62f sofiane212/ocr_app:1``
 
* **se connecter vers DockerHub :** ``docker login``

* **Pousser l'image vers DockerHub :** ``docker push sofiane212/ocr_app:1 ``
  
## Déploiment

### le Secret pour la clé API OCR
````sh
apiVersion: v1
kind: Secret
metadata:
  name: ocr-secret
type: Opaque
stringData:
  GEMINI_AI_API_KEY: "AIzaSyBXfxG0C2YwZHMv9fcxoDm9Pr6rAt4EIJc"


````
à chaque fois que Kubernets démarre un conteneur de **ocr-service** il injecte la clé API Gemini comme variable d’envronnement ``GEMINI_AI_API_KEY``

* ``kubectl apply -f ocr-secret.yaml``

### déploiment du service
* Ligne **122 -> 177** du fichier [deploiment.yml](/deploiment.yml)

* **Verifier les pods**

``kubectl get pods | grep "ocr" ``

![pods_ocr](/IMAGES/pods_ocr.png)

* **le lancer** : ``minikube service ocr-service ``
````
|-----------|-------------|-------------|---------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL            |
|-----------|-------------|-------------|---------------------------|
| default   | ocr-service |          80 | http://192.168.49.2:32667 |
|-----------|-------------|-------------|---------------------------|
````

![ocr_teste_kb](/IMAGES/ocr_kb.png)