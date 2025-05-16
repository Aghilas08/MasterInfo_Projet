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

#### Microservice LLM
Ce microservice expose une API Flask permettant l’envoi de messages à un **LLM via un webhook Make.com** et retourne une réponse contenant du code Python et une explication extraite de la réponse textuelle.
  * **Fonctionnalités principales :**

    * **Interface web** (HTML form ou API) pour envoyer une requête textuelle.
    * Appel à **un webhook** externe (**Make.com**) contenant **un LLM**.
    * Extraction du **code Python** depuis la réponse du **LLM**.
    * Extraction de **l’explication textuelle associée**.
    * Réponse **JSON** contenant **le code extrait** et **son explication**.

  * **Environnement technique :**
    * Framework : Flask (Python)
    * Conteneurisation via **Docker** et déploiment avec **Kubernetes**.
    * Variables sensibles (comme le WEBHOOK_URL) sécurisées avec Kubernetes Secrets.
    * Service exposé via un **LoadBalancer** pour accès depuis l’extérieur.
  
  ````
  Make.com — Plateforme d’Automatisation Visuelle :
  -------------------------------------------------

  Make.com est une plateforme d’automatisation visuelle qui permet de connecter facilement des applications,
    services et API sans écrire de code.

  Elle permet de créer des scénarios (workflows) complexes grâce à une interface glisser-déposer, idéale pour automatiser 
    des processus métiers, envoyer des données entre outils ou intégrer des services externes comme des LLM.
  ````
#### Microservice OCR

Ce microservice permet l’extraction de contenu **LaTeX** à partir de **documents PDF** en utilisant l’API **Gemini AI de Google**.

  * **Fonctionnalités principales :**
  
    * **Interface web** pour **uploader un fichier PDF**.
    * Upload du fichier sur l’API **Gemini AI**.
    * Génération d’un document **LaTeX structuré**, compilable à partir du PDF.
    * Affichage du **code LaTeX généré**.

  * **Environnement technique :**

    * Framework : Flask (Python)
    * Librairie utilisée : **google.generativeai**
    * Clé API protégée via Kubernetes Secrets (GEMINI_AI_API_KEY).
    * Conteneurisé avec Docker et déploiment avec **Kubernetes**.
    * Fichiers uploadés localement dans un dossier.
    * Service exposé via **LoadBalancer** pour utilisation depuis une interface externe

****
# Structure du Projet

![schema](/IMAGES/schema.png)

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
  - Monte un volume persistant à ``/var/lib/postgresql/data`` pour stocker les données durablement.
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

**b. creation d'un utilisateur qui existe déja :** ❌

![teste](/IMAGES/Psql/teste3.png)


**c. se connecter avec un utilisateur qui n'existe pas :** ❌ 

![teste](/IMAGES/Psql/teste1.png)

###### Améloiration future

* **Protection** : protéger les formulaires.
* **Meilleure gestion des erreurs** : retourner des messages HTML ou redirections au lieu de simples chaînes.
* **Déconnexion** : Ajout une route **/logout** pour vider la session.


# 2 -  Microservice LLM

###### Fonctionnalités principales :

  * **Interface utilisateur** (/) :
    * Affiche une page HTML (via render_template) permettant à l’utilisateur de soumettre un message texte.

  * **Envoi de message au LLM** (/send) :

    * Reçoit une requête JSON contenant un champ message.
    * Transmet ce message à un webhook externe Make.com (via **requests.post()**).

    * Extrait de la réponse :
      - Un bloc de code Python (entre python ... ).
      - Une explication textuelle identifiée par le marqueur **"Explication:"**.
      -Renvoie une réponse JSON contenant :

          - **code** : le code Python extrait.

          - **explanation** : l’explication extraite, ou un message par défaut si non trouvée.

###### Les codes d’erreur courants

  * **400 Bad Request :**

      * Signification : **Aucun message** n’a été fourni dans la requête.
      * Ce que le client doit faire : Fournir un probléme a résoudre dans le champ message.

  * **Erreur Make.com ou exception réseau :**
      * En cas d'échec du webhook ou de problème de connexion, le service retourne une erreur avec le message d’exception ou le code HTTP (status_code).

###### Déploiment

Le service LLM est conteneurisé via **Docker** et exposé sur **le port 5001**. En production, il est déployé avec **Kubernetes** à l’aide de **2 réplicas** et un Service de type **LoadBalancer** pour permettre un accès externe. L’URL du webhook externe (**WEBHOOK_URL**) est stockée de manière sécurisée dans un Secret Kubernetes. L’image Docker utilisée est **aghilasob/llm_app:01**.

###### Teste

**a. ecrire une requete :** ✅

![teste](/IMAGES/test_llm.png)

**b. aucun message par l'utilisateur :** ❌

![teste](/IMAGES/llm_erreur.png)

# 3 -  Microservice OCR

###### Fonctionnalités principales :

  * **Téléversement de fichier** (/) :

      - Permet à l’utilisateur de uploader un fichier PDF via une interface web.
      - Le fichier est enregistré localement dans un dossier **uploads/**.
      - Le nom du fichier est sécurisé via **secure_filename**.

  * **Extraction de LaTeX via Gemini AI :**

      - Utilise l’API **Gemini de Google** pour analyser le contenu du PDF.
      - Envoie **un prompt** très précis pour structurer le document en LaTeX compilable.
      - Récupère uniquement le code source LaTeX.

  * **Affichage du résultat :**

      - Le code LaTeX extrait est affiché directement dans la page web.
      - Aucun fichier LaTeX n’est généré sur disque, tout est traité en mémoire.

###### Sécurité :
La clé API Gemini est lue depuis la variable d’environnement **GEMINI_AI_API_KEY**.

##### Prompt :
````python

prompt = (
"""Tu dois convertir ce document PDF en un fichier LaTeX complet, structuré et compilable.

Voici les consignes précises :

1. Génère le texte du document en **français** comme il est écrit (ne pas traduire s'il est déjà en français).
2. Toutes les **formules et expressions mathématiques** doivent être converties correctement en **LaTeX**, avec les bons environnements (`equation`, `align`, etc.).
3. Utilise des balises comme `\section`, `\subsection`, etc. pour structurer le document.
4. Fournis un **document LaTeX complet**, avec le `\documentclass`, l'import des packages nécessaires (ex. `amsmath`, `amssymb`, `geometry`, `babel`, etc.).
5. Le fichier doit pouvoir être compilé sans erreur (par exemple sur Overleaf).
6. N'ajoute aucun commentaire ou explication en dehors du contenu du document original.
7. mettre chaque question a ligne c'est a dire de l'exercice a ligne c'est a dire quand c'est une question il faut laisser une ligne puis passer la suivante

Retourne uniquement le **code source LaTeX** complet, sans aucune explication.
"""
````

* **Consignes :**

  * **Langue** : garder le texte en français, sans le traduire.

  * **Maths** : convertir toutes les formules en vrai LaTeX avec les bons environnements (equation, align, etc.).

  * **Structure** : utiliser les balises LaTeX comme \section, \subsection, etc. pour organiser le document.

  * **Complet** : produire un document LaTeX entier (avec \documentclass, \begin{document}, etc.).

  * **Compilable** : s'assurer que le fichier fonctionne directement sur Overleaf (pas d'erreurs).

  * **Pas de blabla** : ne pas ajouter de commentaires ou d’explications, juste le contenu.

  * **Saut de ligne entre questions** : bien espacer chaque question pour une bonne lisibilité.

##### Déploiment :

* Une exposition via **un LoadBalancer** pour permettre un accès depuis l’extérieur.

* L’image Docker : **aghilasob/ocr_app:01**.

* Le dossier **uploads** est monté dans le conteneur, **emptyDir** : répertoire temporaire pour stocker les PDF uploadés..

* Les variables sensibles (clé Gemini API) sont injectées via un Secret Kubernetes.

* Le service écoute sur **le port 5002**, redirigé depuis le port 80 pour l’accès web.

###### Teste

![ocr_teste_kb](/IMAGES/ocr_kb.png)

# Limitation des ressources
###### IMPORTANT : vu que tous les services tournent en locale avec "minikube" on a du limiter les ressources (CPU , RAM) pour le déploiment des services.
````sh
        resources:
          limits:
            cpu: "500m"
            memory: "512Mi"
          requests:
            cpu: "200m"
            memory: "256Mi"
````
# Minikube dashbord

![ts_les_services_dep](/IMAGES/dashboard.png)

****
* sert a vérifier si le code source fonctionne et que les images Docker  des services peuvent être construites correctement.
* Il agit comme un test de validation pour éviter d’intégrer du code qui peut eroné le build Docker.

* **Déclenchement :**
````yaml
on:
  - pull_request

````

![teste_pipline](/IMAGES/pipline.png)

****
# Gateway via istio
````yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: api-gateway
  namespace: istio-system     
spec:
  selector:
    istio: ingressgateway       # pod istio ingress
  servers:
  - port:
      number: 80      # accept que le trafic HTTP sur le port 80
      name: http
      protocol: HTTP
    hosts:
    - "*"            # accepte les requetes pour ts les hote
````
* **le but** : ouvrir un point d’entrée unique **ingress** sur le cluster pour tout le trafic HTTP externe.

![infos_gateway](/IMAGES/info-gw.png)

# Le VirtualService
````yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: services-routing
  namespace: default
spec:
  hosts:
  - "*"
  gateways:
  - istio-system/api-gateway
  http:
  - match:
    - uri:
        prefix: /
    rewrite:
      uri: /
    route:
    - destination:
        host: auth-service
        port:
          number: 80
          .
          .
          .
````
* **Le but** : une fois le trafic entré via le Gateway ; router chaque requete vers les back‑end (auth-service, llm-service, ocr-service).

* **Comment ça marche :**

  * Le client envoie une requête HTTP..
  * Istio Ingress Gateway capte cette requête (via la gateway).
  * VirtualService examine l’URI et applique :

    - une réécriture si besoin,
    - une règle de routage vers auth-service, llm-service ou ocr-service .
  
  * le pod de destination reçoit la requête et la transmet à ton conteneur.
  
![virtual_service](/IMAGES/VS.png)

# Teste les trois services
* **Mise a jour home.html du service "authentification"** :
````html
        <div class="choices">
            <a href="http://localhost:8081/"><button>Python</button></a>
            <a href="http://localhost:8082/"><button>LateX-PDF</button></a>
        </div>
````
* **rediréction** :
  * 8080:80  pour accéder à auth-service via http://localhost:8080, qui redirige vers le port 80 du service dans le cluster.

  * 8081:80 pour accder à llm-service sur http://localhost:8081.

  * 8082:80 pour l'accès à ocr-service sur http://localhost:8082.

````shell
kubectl -n default port-forward svc/auth-service 8080:80 &
kubectl -n default port-forward svc/llm-service 8081:80 &
kubectl -n default port-forward svc/ocr-service 8082:80 &
````

![service_auth](/IMAGES/service3.png)

![service_llm](/IMAGES/service2.png)

![service_ocr](/IMAGES/service1.png)

****

# Sécuriser le cluster
### RBAC Kubernetes

**1. ServiceAccounts :** Les ServiceAccounts **auth-sacc, llm-sacc et ocr-sacc** ont pour but de donner à chacun des services une identité distincte dans le cluster, sur laquelle on pourras appliquer des politiques RBAC.
````yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: auth-sacc
  namespace: default
    .
    .
    .
````

![service_account](/IMAGES/seracc.png)


* **no** : signifie simplement que **ServiceAccount n’a aucun droit sur la ressource pods** tant que il n y’as pas de Role/RoleBinding

* il faut les ajouter dans le deploiment.
 
**2. Roles** :

* **get** : Récupérer un objet unique (exp : ``kubectl get pod <nom-pod>``)
* **list** : Lister tous les objets d’un type (exp: ``kubectl get pods``).
  
* ``kubectl apply -f serviceaccount.yml``
* ``kubectl apply -f deploiment.yml``
* ``kubectl apply -f roles.yml ``

![roles](/IMAGES/test_role.png)

### HTTPS
* **Générer un certificat TLS**
  * **Créeation du répertoire et génération d'une paire clé / certificat auto‑signé** :
    ````sh
    #  le dossier
      mkdir -p certs

    # Générer une clé privée et un certificat auto‑signé valable 1 an
      openssl req -x509 \
        -nodes \
        -newkey rsa:2048 \
        -keyout tls.key \
        -out tls.crt \
        -days 365 \
        -subj "/CN=api.m1info.com/O=upc"

    ````

  * **Créeation du Secret Kubernetes TLS**
  ````sh
  kubectl -n istio-system create secret tls tls-secret \
    --cert=./certs/tls.crt \
    --key=./certs/tls.key

  ````

* **Mettre à jour le Gateway Istio & Virtalservice** :

  * **Redirection automatique HTTP → HTTPS** :
  ````yaml
    tls:
      httpsRedirect: true
  ````

  * **Définition d’un VirtualService multi-routes avec filtrage par URI** : les routes sont bien définies par match pour ``/auth, /llm, /ocr``, avec des redirections explicites vers les bons services et cela permet une gestion centralisée du routage via un unique point d’entrée ``api.m1info.com`` (scalable).
  
  * **Route par défaut vers auth-service** : route '/' pour rediriger les accès vers le service d’authentification, utile si quelqu’un accède à https://api.m1info.com/ sans chemin explicite.



* **teste** :
````bash
# certificat :

kubectl -n istio-system get secret

NAME              TYPE                DATA   AGE
istio-ca-secret   istio.io/ca-root    5      37h
tls-secret        kubernetes.io/tls   2      27m   # <--


# IP externe

kubectl get svc istio-ingressgateway -n istio-system
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)                                                                      AGE
istio-ingressgateway   LoadBalancer   10.107.115.196   10.107.115.196   15021:31132/TCP,80:32580/TCP,443:32690/TCP,31400:32403/TCP,15443:31283/TCP   37h

# resolution de nom de domaine en locale :

nano /etc/hosts

127.0.0.1       localhost
127.0.1.1       ARCADIA
10.107.115.196  api.m1info.com  # <--

````

![test_https](/IMAGES/cert.png)
****
# Service Mesh
````bash
# Proxy :

kubectl label namespace default istio-injection=enabled --overwrite

kubectl get namespace default --show-labels

NAME      STATUS   AGE   LABELS
default   Active   44h   istio-injection=enabled,kubernetes.io/metadata.name=default

# redeploiment des pods :

kubectl rollout restart deployment auth-service
kubectl rollout restart deployment llm-service
kubectl rollout restart deployment ocr-service
````

* **Vérifier l'injection des sidecars proxy** :

![inection_istio_proxy](/IMAGES/injction_proxy.png)

* **Appliquer une DestinationRule** :
````yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: default-destination-rule
  namespace: default
spec:
  host: '*.default.svc.cluster.local'
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
````
c'est pour pour activer la communication chiffrée (mTLS) entre les services du namespace default en utilisant Istio Mutual TLS.

### Kiali
````bash
# installation et l'ajouts les pluggins
istioctl install --set profile=demo -y

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/prometheus.yaml


kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/grafana.yaml

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.22/samples/addons/kiali.yaml

# lancer kiali :

istioctl dashboard kiali

````

Pour tester on va juste s'authentifier et choisir le service ocr.

![kiali](/IMAGES/kiali.png)

****

# Au finale :

* **En python je veux un programme qui fait la moyenne entre deux notes**

![notes_py](/IMAGES/notes.png)

* **le contenu du pdf c'est des images contenant des maths**
[PDF TESTE](/OCR/uploads/final_image.pdf)

![ocr_resltat](/IMAGES/math_ocr.png)

![overleaf](/IMAGES/des_math.png)

# GOOGLE LAB

* **Aghilas OULD BRAHAM**

![aghilas](/IMAGES/aghilas.png)

* **Sofiane AGOUNI KACI**

![sofiane](/IMAGES/sofiane.png)

# Amélioration future :
* **Améliorer la securité :**
  * Sécuriser les images docker
  * l'authentification
  * la communication entre les services
* Rendre le graphisme des sites web (plus attractives : chargement des fichiers dans le service OCR ...)

* Elargir le nombre de rquetes dans le service llm (ici max 1000)

* Si l'API est deployée dans un univers éducatif (univercité...) au lieu de faire une inscription (register), c'est a l'admin d'ajouter tous les etudiants (pour une premier connexion login : num etudian + date de naissance comme mot de passe , avec la possibilité de le changer).

* Deploiment chez un cloud provider (solution cloud)
