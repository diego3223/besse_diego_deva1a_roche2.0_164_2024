"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_equipes_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * from t_joueurs"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_ID_joueurs_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * from t_joueurs WHERE ID_joueurs = %(value_ID_joueurs_selected)s"""

                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * from t_joueurs ORDER BY ID_joueurs DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le joueur demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données joueurs affichées !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                civilite_wtf = form.civilite_wtf.data
                nom_wtf = form.nom_wtf.data
                prenom_wtf = form.prenom_wtf.data
                nationnalite_wtf = form.nationnalite_wtf.data
                date_naissance_wtf = form.date_naissance_wtf.data
                courriel_wtf = form.courriel_wtf.data
                telephone_wtf = form.telephone_wtf.data
                FK_equipes_wtf = form.FK_equipes_wtf.data
                FK_cotisations_wtf = form.FK_cotisations_wtf.data
                FK_passeport_wtf = form.FK_passeport_wtf.data
                valeurs_insertion_dictionnaire = {"value_civilite": civilite_wtf,
                                                  "value_nom": nom_wtf,
                                                  "value_prenom": prenom_wtf,
                                                  "value_nationnalite": nationnalite_wtf,
                                                  "value_date_naissance": date_naissance_wtf,
                                                  "value_courriel": courriel_wtf,
                                                  "value_telephone": telephone_wtf,
                                                  "value_FK_equipes": FK_equipes_wtf,
                                                  "value_FK_cotisations": FK_cotisations_wtf,
                                                  "value_FK_passeport": FK_passeport_wtf,
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_joueurs (ID_joueurs, civilite, nom, prenom, nationnalite, date_naissance, courriel, telephone, FK_equipes, FK_cotisations, FK_passeport) VALUES (NULL,%(value_civilite)s, %(value_nom)s, %(value_prenom)s, %(value_nationnalite)s, %(value_date_naissance)s, %(value_courriel)s, %(value_telephone)s, %(value_FK_equipes)s, %(value_FK_cotisations)s, %(value_FK_passeport)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    ID_joueurs_update = request.values['ID_joueurs_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateGenre()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            civilite_update_wtf = form_update.civilite_update_wtf.data
            nom_update_wtf = form_update.nom_update_wtf.data
            prenom_update_wtf = form_update.prenom_update_wtf.data
            date_naissance_update_wtf = form_update.date_naissance_update_wtf.data
            nationnalite_update_wtf = form_update.nationnalite_update_wtf.data
            courriel_update_wtf = form_update.courriel_update_wtf.data
            telephone_update_wtf = form_update.telephone_update_wtf.data
            FK_equipes_update_wtf = form_update.FK_equipes_update_wtf.data
            FK_cotisations_update_wtf = form_update.FK_cotisations_update_wtf.data
            FK_passeport_update_wtf = form_update.FK_passeport_update_wtf.data

            valeur_update_dictionnaire = {"value_ID_joueurs": ID_joueurs_update,
                                          "value_civilite": civilite_update_wtf,
                                          "value_nom": nom_update_wtf,
                                          "value_prenom": prenom_update_wtf,
                                          "value_date_naissance": date_naissance_update_wtf,
                                          "value_nationnalite": nationnalite_update_wtf,
                                          "value_courriel": courriel_update_wtf,
                                          "value_telephone": telephone_update_wtf,
                                          "value_FK_equipes": FK_equipes_update_wtf,
                                          "value_FK_cotisations": FK_cotisations_update_wtf,
                                          "value_FK_passeport": FK_passeport_update_wtf
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_joueurs SET civilite = %(value_civilite)s, 
            nom = %(value_nom)s, prenom = %(value_prenom)s, date_naissance = %(value_date_naissance)s, nationnalite = %(value_nationnalite)s, courriel = %(value_courriel)s, telephone = %(value_telephone)s, FK_equipes = %(value_FK_equipes)s, FK_cotisations = %(value_FK_cotisations)s, FK_passeport = %(value_FK_passeport)s WHERE ID_joueurs = %(value_ID_joueurs)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=ID_joueurs_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_genre = "SELECT ID_joueurs, civilite, nom, prenom, date_naissance, nationnalite, courriel, telephone, FK_equipes, FK_cotisations, FK_passeport FROM t_joueurs " \
                               "WHERE ID_joueurs = %(value_ID_joueurs)s"
            valeur_select_dictionnaire = {"value_ID_joueurs": ID_joueurs_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_civilite = mybd_conn.fetchone()
            print("data_civilite ", data_civilite, " type ", type(data_civilite), " genre ",
                  data_civilite["civilite"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "genre_update_wtf.html"
            form_update.civilite_update_wtf.data = data_civilite["civilite"]
            form_update.nom_update_wtf.data = data_civilite["nom"]
            form_update.prenom_update_wtf.data = data_civilite["prenom"]
            form_update.date_naissance_update_wtf.data = data_civilite["date_naissance"]
            form_update.nationnalite_update_wtf.data = data_civilite["nationnalite"]
            form_update.courriel_update_wtf.data = data_civilite["courriel"]
            form_update.telephone_update_wtf.data = data_civilite["telephone"]
            form_update.FK_equipes_update_wtf.data = data_civilite["FK_equipes"]
            form_update.FK_cotisations_update_wtf.data = data_civilite["FK_cotisations"]
            form_update.FK_passeport_update_wtf.data = data_civilite["FK_passeport"]



    except Exception as Exception_genre_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/equipes_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    ID_joueurs_delete = request.values['ID_joueurs_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteGenre()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/equipes_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer le joueur de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": ID_joueurs_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_habiter WHERE FK_joueurs = %(value_id_genre)s"""
                str_sql_delete_idgenre = """DELETE FROM t_joueurs WHERE ID_joueurs = %(value_id_genre)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idgenre, valeur_delete_dictionnaire)

                flash(f"Joueur définitivement effacé !!", "success")
                print(f"Joueur définitivement effacé !!")

                # afficher les données
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_ID_joueurs": ID_joueurs_delete}
            print(ID_joueurs_delete, type(ID_joueurs_delete))

            # Requête qui affiche tous les films_genres qui ont le genre que l'utilisateur veut effacer
            strsql_joueur_selected = """SELECT ID_joueurs, civilite, nom, prenom, numero_rue FROM t_habiter
                                                    INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                    INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                    WHERE ID_joueurs = %(value_ID_joueurs)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(strsql_joueur_selected, valeur_select_dictionnaire)
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "genres/equipes_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_genre = "SELECT * FROM t_joueurs WHERE ID_joueurs = %(value_ID_joueurs)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_genre = mydb_conn.fetchone()
                #print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      #data_nom_genre["intitule_genre"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "equipes_delete_wtf.html"
            form_delete.nom_genre_delete_wtf.data = data_nom_genre["nom"]

            # Le bouton pour l'action "DELETE" dans le form. "equipes_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_genre_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_delete_wtf.__name__} ; "
                                      f"{Exception_genre_delete_wtf}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)
