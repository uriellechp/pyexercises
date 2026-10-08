# Journal de conversation — Assistance IA (Devoirs 3, 4 et 5)

## Exercices 3.0 & 3.1 — Arithmétique de base et Parité

### Prompt Étudiant :
> Dois-je faire des tests ou pas ?

### Explications & Contexte :
*Clarification sur la méthodologie de test. L'objectif était de comprendre comment valider la section "Check it yourself" et vérifier le comportement des structures conditionnelles sur différents types d'entrées (valeurs limites et invalides).*

### Réponse IA :
Oui, absolument. Il faut exécuter les tests dans le terminal pour compléter la section *Check it yourself* des fichiers `.py`.

Tests à exécuter pour `3.1_odd_or_even.py` :
1. Test avec `6` : valide 3 nombres impairs et 3 nombres pairs.
2. Test avec `0` : affiche le message d'erreur.
3. Test avec `-4` : affiche le message d'erreur.
4. Test avec `5000` : affiche le message d'avertissement.

---

### Prompt Étudiant :
> OK, parce que du coup, j'ai fait le premier test avec enter a positive number number six et du coup ensuite qu'est-ce qu'il faut que je fasse ? Il faut que je remette Python 3.0 basic arithmetic py et ensuite que je fasse encore ça ? Comment est-ce que je suis censé refaire ?

### Explications & Contexte :
*Prise en main des commandes du terminal sous VS Code / Codespaces pour enchaîner l'exécution de plusieurs scripts Python et réexécuter un programme avec des arguments différents.*

### Réponse IA :
Pour re-tester :
1. Réexécuter la commande `python 3.1_odd_or_even.py` pour tester `0`, `-4` et `5000`.
2. Pour tester `3.0_basic_arithmetic.py`, lancer `python 3.0_basic_arithmetic.py`.
Astuce : utiliser la flèche du haut dans le terminal pour rappeler les commandes précédentes.

---

### Prompt Étudiant :
> Bah, j'ai fait 0 après ça m'a fait please write a number greater than 0.

### Explications & Contexte :
*Vérification du traitement des cas limites. Confirmation que le filtre d'instruction conditionnelle détecte correctement la valeur 0 et renvoie l'avertissement demandé.*

### Réponse IA :
C'est le comportement attendu. Le programme a correctement détecté que 0 n'est pas strictement supérieur à 0 et a levé le message d'erreur approprié.

---

## Devoir 4 — Listes et Dictionnaires

### Prompt Étudiant :
> la je compte faire les excercice 4 [Consignes fournies pour 4.0, 4.1 et 4.2]

### Explications & Contexte :
*Application des notions de structures de données en Python (listes et dictionnaires) appliquées à un cas d'usage marketing (budgets de coûts d'acquisition client - CAC). Implémentation du tri non destructif et manipulation sécurisée de clés.*

### Réponse IA :
Génération du code et des commentaires pour :
- `4.0_list_manipulation.py` : manipulation d'une liste de budgets CAC (coûts d'acquisition client) marketing.
- `4.1_list_reverse_sort.py` : réordonnancement sans altération de la liste originale (utilisation de `sorted()`, `reversed()`, et `.copy()`).
- `4.2_dictionaries.py` : création d'un dictionnaire décrivant une campagne marketing digital avec test sécurisé `.get()`.

---

## Devoir 5 — Boucles (`for` & `while`)

### Prompt Étudiant :
> 5 : Loops [Consignes fournies pour 5.1 et 5.2]

### Explications & Contexte :
*Implémentation des itérations. Utilisation d'une boucle `for` avec `enumerate()` pour calculer les ratios budgétaires, et d'une boucle `while` sécurisée avec limite d'essais et nettoyage de chaîne (`.strip().lower()`).*

### Réponse IA :
Génération des scripts :
- `5.1_for_loops.py` : boucle `for` avec `enumerate()` calculant la part en pourcentage de chaque budget sur le total.
- `5.2_while_loops.py` : boucle `while` de validation avec arrêt au bout de 3 tentatives et nettoyage d'entrée (`.strip().lower()`).

---

### Prompt Étudiant :
> pour le 5.2 je n'arrive pas a mettre en messsage peut etre parce que j'ai deja fais avec le 5.1

### Explications & Contexte :
*Résolution d'un blocage d'exécution dans le terminal lié à un processus en attente de saisie utilisateur (`input()`).*

### Réponse IA :
Le terminal est bloqué par le processus précédent.
Solution : Utiliser `Ctrl + C` dans le terminal pour interrompre le programme en cours, puis relancer `python 5.2_while_loops.py`.