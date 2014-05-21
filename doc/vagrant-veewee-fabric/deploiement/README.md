# Déploiement

Nous utilisons fabric pour gérer le déploiement automatisé de la pile Virtualbox, Vagrant et Veewee.

Virtualbox sera donc notre environnement de virtualisation chargé d'éxecuter nos machines virtuelles de test.

Vagrant est une solution permettant de rapidement déployer des vm de test (ou de développement) et cela de manière répétitive.

Veewee est un outil permetant de facilement générer des modèle d'environements pour Vagrant (BOX).

**Note : L'ensemble des exemples et scripts porte sur l'utilisation d'une distribution Ubuntu ou Debian**

Les seuls prérequis d'installation sont Python (> 2.6) et le module fabric. L'insallation de fabric se fait très simplement vias la commande easy_install ou la commande pip. Si easy_install n'est pas installé, il suffit d'utiliser le gestionnaire de paquet de la distribution.

Commençon par installer les outils qui permetront de déployer le module fabric.

    sudo apt-get install python-setuptools

Il ne reste plus qu'à executer la commande suivante pour installer fabric.

    sudo pip install fabric
