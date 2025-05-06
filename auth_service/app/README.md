# Service Authentification

### Docker
* **Création de deux images docker en locale**
  * BDD : Postgresql
  * Microservice : app_web

````sh
docker-compose up --build
````

![images_docker](/IMAGES/images.png)

### BDD
* **Les migrations**

````sh
flask db init
flask db migrate -m "Create users table"
````
* **Verification de la creation de la Table : users**

````sh
docker exec -it postgres_container psql -U postgres -d auth_db -c "\d users"
````

### Teste en local
* **Afficher les container**

![docker_ps](/IMAGES/docker_ps.png)

* **Acceder au service** : Lien 👉 [localhost:5000/](http://127.0.0.1:5000/)
  
* **Se connecter avec un compte qui n'existe pas encore**

![login1](/IMAGES/login1.png)

* **Creer un compte et s'y connecter**

![login2](/IMAGES/login2.png)

* **Dans la table users**
  * ``docker exec -it postgres_container psql -U postgres -d auth_db -c "SELECT * FROM users;"``

![users](/IMAGES/users.png)

# Docker Hub
* **Tag l'image docker :** ``docker tag 9d997cc3acfb aghilasob/auth_app:01 ``
 
* **se connecter vers DockerHub :** ``docker login``

* **Pousser l'image vers DockerHub :** ``docker push aghilasob/auth_app:01``

****

## Deploiment
* **Lancement de minikube :** ``minikube start --driver=docker`` via docker.
* **Tableau de bord minikube :** ``minikube dashboard``
### PostgreSQL
* **Déploiement d'un conteneur Postgres dans un cluster Kubernetes :**
  * **Espace de stockage persistant :**``kubectl apply -f postgres-pvc.yaml``
  * **Définir le mot de passe qui sera utilisé lors de la connexion au serveur Postgres :** ``kubectl apply -f postgres-secret.yaml``

  * **Deployer PostgreSQL :**``kubectl apply -f postgres-statefulset.yaml``
  * **Exposer PostgreSQL :**``kubectl apply -f postgres-service.yaml``
  * 
###### Verification
````sh
kubectl get secrets
kubectl get PersistentVolumes
kubectl get deployment
kubectl get service
kubectl get pod
kubectl describe pod postgres-XXXXXXXXXXXXX # avoir plus d'infos 
````

![dep_psql](/IMAGES/Psql.png)

### Auth_service

👉 [deploiment.yml](/deploiment.yml)
* **Deployer le service authentification :**
````sh
kubectl apply -f deploiment.yml
````

![dep_auth](/IMAGES/dep_auth.png)

![dep_info](/IMAGES/info_dep.png)

### Teste
* **Récupérer l'adresse du service :** ``minikube service auth-service --url``
  
![ip](/IMAGES/ip.png)

* **Lancer le service avec minikube :** ``minikube service auth-service``
* 
````
|-----------|--------------|-------------|---------------------------|
| NAMESPACE |     NAME     | TARGET PORT |            URL            |
|-----------|--------------|-------------|---------------------------|
| default   | auth-service |          80 | http://192.168.49.2:32447 |
|-----------|--------------|-------------|---------------------------|
````

![teste](/IMAGES/teste_01.png)

****
