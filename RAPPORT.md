**Auteurs**  
- **Auteur 1** : Sofiane AGOUNI KACI
- **Auteur 2** : Aghilas OULD BRAHAM
  
**Date** : 2024 - 2025

**Groupe** : M1-RSA

****
<h3 align="center">Projet : Microservices</h3>

<p align="center"><i>LLM & OCR</i></p>
<p align="center"
    <a href="https://www.u-paris.fr/">
       <img alt="Université Paris Cité" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Logo_Universit%C3%A9_Paris-Cit%C3%A9_%28partenariat_Wikim%C3%A9dia%29.svg/1024px-Logo_Universit%C3%A9_Paris-Cit%C3%A9_%28partenariat_Wikim%C3%A9dia%29.svg.png" width="100">
    </a>
</p>
<p align="center">
    <a href="https://docs.pypots.com/en/latest/install.html#reasons-of-version-limitations-on-dependencies">
       <img alt="Python version" src="https://img.shields.io/badge/Python-v3.11+-E97040?logo=python&logoColor=white">
    </a>
    <a href="https://flask.palletsprojects.com/">
       <img alt="Flask version" src="https://img.shields.io/badge/Flask-v2.0.3+-FF1493?logo=flask&logoColor=white">
    </a>
    <a href="https://www.docker.com/">
       <img alt="Docker version" src="https://img.shields.io/badge/Docker-v26.1.3+-2496ED?logo=docker&logoColor=white">
    </a>
    <a href="https://kubernetes.io/">
       <img alt="Kubernetes version" src="https://img.shields.io/badge/Kubernetes-v1.21+-326CE5?logo=kubernetes&logoColor=white">
    </a>
    <a href="https://www.postgresql.org/" title="PostgreSQL v14">
   <img
    alt="PostgreSQL version"
    src="https://img.shields.io/badge/PostgreSQL-v14-4169E1?logo=postgresql&logoColor=white"
  >
  </a>
  <a href="https://istio.io/" title="Istio v1.19">
  <img
    alt="Istio version"
    src="https://img.shields.io/badge/Istio-v1.19-505A5F?logo=istio&logoColor=white"
   >
  </a>
</p>

****

# Description des microservices

#### Microservice Flask avec PostgreSQL
Ce microservice d’authentification d’utilisateurs développé avec **Flask** et connecté à une base de données **PostgreSQL**. Il permet la gestion sécurisée des comptes utilisateurs via une API REST, avec les fonctionnalités suivantes :
  * **Fonctionnalités principales :**
    * **Inscription d’un nouvel utilisateur** avec vérification des données
    * **Connexion sécurisée** avec gestion de mot de passe haché
    * Base de données relationnelle **PostgreSQL**pour stocker les utilisateurs
    * Migration de la base avec **Flask-Migrate**


  * **Environnement technique :**

    * Conteneurisation avec **Docker** et **orchestration** via **Docker Compose** ou **Kubernetes (Minikube)**
    * Utilisation de **Secrets Kubernetes** pour sécuriser les variables sensibles (DB user, password…)
    * **Service exposé** via un **LoadBalancer** (pour accès depuis l’extérieur)

#### M2

service LLM (sof)

#### M3

Service OCR (sof)

****
# Structure du Projet

****
# Etapes : Conception de l’application selon les 15 facteurs

### Virtualize microservices → Containers (CaaS – Containers as a Service)

* Emballage des microservices dans des conteneurs Docker pour :

    - Assurer l’isolation
    - Garantir la portabilité entre environnements
    - Permettre un déploiement rapide et fiable

### Manage containers in a cluster → Kubernetes Gateway

* Utilisation de Kubernetes comme orchestrateur pour :

    - Le déploiement,le redémarrage automatique...
    - L’exposition des services via des gateways et ingress

### The gateway to the cloud → API Management / API Gateway

* Utilisation d’un API Gateway (comme **Istio**, ou NGINX Ingress) pour :

    - Centraliser les appels API
    - Gérer les routes, la sécurité et les logs

### Monitoring and Control pane → Service Mesh

* Mise en œuvre d’un Service Mesh (comme Istio ou Linkerd) pour :

    - Observer les services (tracing, métriques, logs)
    - Gérer le trafic entre microservices

### Deploy from scratch → Infrastructure as Code (IaC) *Facultative*

* Mise en place automatisée de l'infrastructure via des outils comme **Terraform** ou **Ansible**, assurant une configuration cohérente et reproductible.

****

# 1 -  Microservice Authentification

### 1.1 Déployer PostgreSQL dans Kubernetes avec stockage persistant et secrets
* **Deploiment** (postgres) :

  - Lance un pod avec un conteneur PostgreSQL (postgres:14).
  - Configure les variables d’environnement :
  ````
  # POSTGRES_USER, POSTGRES_DB en clair
  # POSTGRES_PASSWORD via un Secret Kubernetes sécurisé.
  ````
  - Monte un volume persistant à /var/lib/postgresql/data pour stocker les données durablement.
  - Numéro de port : ``5432``


* **Secret** (postgres-secret) :

  - Contient les identifiants sensibles :
  ````
  # postgresql-password :  utilisé par le container.
  (Contient aussi les champs postgresql-user et postgresql-db)
  ````

* **PersistentVolumeClaim** (postgres-pvc) :

  - Alloue 10 Go de stockage persistant.
  - Monté dans le pod PostgreSQL pour assurer que les données survivent aux redémarrages.

**a. Informations**

![pods](/IMAGES/Psql/pod.png)

![desc](/IMAGES/Psql/desc.png)

**b. Ouvrire un terminal dans le pod**
**c. s'y conncter**
**d. Afficher les BDD**

![teste_dep_psql](/IMAGES/Psql/teste_psql.png)

<span style="color:red">Remarque :
- Toujours déployer le service PostgeSQL en premier.
- Pour l'instant on ne trouve pas notre base de données qui vas contenir les utilisateurs et leurs mot de passes vu qu'on a pas encore lancer le service authentification.
</span>


### 1.2 Service Authentification
###### Fonctionnalités principales :

* **Inscription** (/register) :

  - Permet à un nouvel utilisateur de créer un compte avec un nom d'utilisateur et un mot de passe.
  - Vérifie si l'utilisateur existe déjà dans la base de données.
  - Stocke le mot de passe de manière sécurisée via **user.set_password()**.

* **Connexion** (/) **ou** (/login) :

  - Permet à un utilisateur de se connecter en validant les informations contre la base de données.
  - Enregistre le nom d'utilisateur dans la session en cas de succès.

* **Accueil protégé** (/home) :

  - Accessible uniquement si l'utilisateur est connecté (vérifie session **['username']**).
  - Affiche une page personnalisée avec le nom d'utilisateur.

###### Les codes 401 et 409

* **401 Unauthorized** : 
  - Signification : L'utilisateur **n'est pas authentifié**.
  - Ce que le client doit faire : Fournir des identifiants valides.
* **409 Conflict** :
  - Signification : Il y a **un conflit** avec l'état actuel du serveur.
  - Ce que le client doit faire : Choisir un autre nom d'utilisateur.

###### Déploiment

Le déploiment du service d'authentification (auth-service) avec **2 réplicas**, connectée à une base PostgreSQL via des variables d’environnement sécurisées issues d’un Secret. Elle expose le service sur le port **80** (redirection vers le port 5000 de l’application) avec un type **LoadBalancer**, ce qui permet un accès externe. L’image Docker utilisée est **aghilasob/auth_app:01**. Des ressources CPU et mémoire sont également réservées.

![deploimet_dashbord](/IMAGES/Psql/dashbord.png)

###### Teste

**a. creation d'un nouvel utilisateur :** ✅

![teste](/IMAGES/Psql/teste2.png)

**a. creation d'un utilisateur qui existe déja :** ❌

![teste](/IMAGES/Psql/teste3.png)


**c. se connecter avec un utilisateur qui n'existe pas :** ❌ 

![teste](/IMAGES/Psql/teste1.png)

###### Améloiration future

* **Protection** : protéger les formulaires.
* **Meilleure gestion des erreurs** : retourner des messages HTML ou redirections au lieu de simples chaînes.
* **Déconnexion** : Ajout une route **/logout** pour vider la session.


# 2 -  Microservice LLM
(sof)

# 3 -  Microservice OCR
(sof)
****
