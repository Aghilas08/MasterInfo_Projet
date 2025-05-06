
# Microservices Cloud Native

## Une architecture moderne pour vos besoins d'authentification et de traitement de données

Notre plateforme, basée sur une architecture microservices avec Kubernetes, offre trois services sécurisés :

### Service d'Authentification

Le service d'authentification vous permet de gérer l'accès à vos applications en toute sécurité.

**Fonctionnalités principales :**
- Création de compte utilisateur simplifiée
- Connexion sécurisée avec mots de passe cryptés
- Persistance des données avec PostgreSQL
- Interface web intuitive

**Comment l'utiliser :**
1. Accédez à l'URL du service : https://api.m1info.com/
2. Créez un compte via la page d'inscription
3. Connectez-vous avec vos identifiants
4. Une fois authentifié, accédez aux autres services depuis le tableau de bord

### 🤖 Service LLM (Large Language Model)

Exploitez la puissance de l'IA pour générer du code Python avec des explications détaillées.

**Fonctionnalités principales :**
- Interface simple pour soumettre des problèmes à résoudre
- Génération de code Python via l'intégration à Make.com
- Extraction automatique des explications textuelles
- Résultats formatés et prêts à l'emploi

**Comment l'utiliser :**
1. Authentifiez-vous via le service d'authentification
2. Cliquez sur le bouton "Python" depuis votre tableau de bord
3. Décrivez le problème que vous souhaitez résoudre
4. Recevez instantanément du code Python fonctionnel avec explications

### 📄 Service OCR (LaTeX/PDF)

Convertissez vos documents PDF(manuscrit) en code LaTeX structuré et compilable.

**Fonctionnalités principales :**
- Upload facile de documents PDF
- Conversion intelligente via l'API Gemini AI de Google
- Extraction de formules mathématiques et structure du document
- Code LaTeX prêt à être compilé (compatible avec Overleaf)

**Comment l'utiliser :**
1. Authentifiez-vous via le service d'authentification
2. Cliquez sur le bouton "LaTeX-PDF" depuis votre tableau de bord
3. Téléversez votre document PDF
4. Obtenez instantanément le code LaTeX correspondant

## 🛡️ Sécurité et Performance

- Communication sécurisée par HTTPS
- Authentification requise pour accéder aux services
- Architecture containerisée et orchestrée par Kubernetes
- Haute disponibilité avec réplication des services
- Monitoring intégré via Istio et Kiali

## 📊 Monitoring en temps réel

Visualisez les performances et interactions entre vos services grâce à notre dashboard Kiali intégré, offrant une visibilité complète sur l'architecture microservices.

---

**Accès unifié** via notre domaine sécurisé : https://api.m1info.com/

*Une solution Cloud Native complète pour vos besoins de développement et de traitement documentaire.*
