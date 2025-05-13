# Service LLM

### Docker

* **Création d'une image docker en locale**
  * Microservice LLM : llm_app

````sh
docker build -t llm_app .  
````

### Teste en local
* **lancer le service :** ``docker run -p 5001:5001 llm_app``

![teste_llm](/IMAGES/teste_llm.png)

# Docker Hub

* **Tag l'image docker :** ``docker tag 789dea9b87ae sofiane212/llm_app:01``
 
* **se connecter vers DockerHub :** ``docker login``

* **Pousser l'image vers DockerHub :** ``docker push sofiane212/llm_app:01``
  
# Déploiment

### le Secret Kubernetes pour le webhook du LLM
````sh
  apiVersion: v1
  kind: Secret
  metadata:
    name: llm-secret
  type: Opaque
  stringData:
    WEBHOOK_URL: "https://hook.us2.make.com/n1d2bkjxvlsyk26t3wrs2sr1ie4b73ma"


````
car l’URL du **webhook Make.com** est une donnée sensible.

* ``kubectl apply -f llm-secret.yaml``

### déploiment du service
* Ligne **69 -> 119** du fichier [deploiment.yml](/deploiment.yml)

* **Verifier les pods**

``kubectl get pods | grep "llm" ``

![pods_llm](/IMAGES/pods_llm.png)

* **le lancer** : ``minikube service llm-service ``
````
|-----------|-------------|-------------|---------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL            |
|-----------|-------------|-------------|---------------------------|
| default   | llm-service |          80 | http://192.168.49.2:30309 |
|-----------|-------------|-------------|---------------------------|
````

![llm_teste](/IMAGES/teste_llm.png)