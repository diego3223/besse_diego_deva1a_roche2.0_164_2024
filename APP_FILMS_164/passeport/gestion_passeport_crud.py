"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.passeport.gestion_passeport_wtf_forms import FormWTFAjouterPasseport
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.passeport.gestion_passeport_wtf_forms import FormWTFDeletePasseport
from APP_FILMS_164.passeport.gestion_passeport_wtf_forms import FormWTFUpdatePasseport

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""



@app.route("/passeport_afficher/<string:order_by>/<int:ID_passeport_sel>", methods=['GET', 'POST'])
def passeport_afficher(order_by, ID_passeport_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and ID_passeport_sel == 0:
                    strsql_passeport_afficher = """SELECT * FROM t_passeport"""
                    mc_afficher.execute(strsql_passeport_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_ID_passeport_selected_dictionnaire = {"value_id_genre_selected": ID_passeport_sel}
                    strsql_passeport_afficher = """SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport WHERE ID_passeport = %(value_ID_passeport)s, %(value_numero_passeport)s, %(value_date_photo_passeport)s, %(value_date_qualification)s """

                    mc_afficher.execute(strsql_passeport_afficher, valeur_ID_passeport_selected_dictionnaire)
                else:
                    strsql_passeport_afficher = """SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport ORDER BY ID_passeport DESC"""

                    mc_afficher.execute(strsql_passeport_afficher)

                data_passeport = mc_afficher.fetchall()

                print("data_genres ", data_passeport, " Type : ", type(data_passeport))

                # Différencier les messages si la table est vide.
                if not data_passeport and ID_passeport_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_passeport and ID_passeport_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le passeport demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données passeport affichées !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{passeport_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("passeport/passeport_afficher.html", data=data_passeport)


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


@app.route("/passeport_ajouter", methods=['GET', 'POST'])
def passeport_ajouter_wtf():
    form = FormWTFAjouterPasseport()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                numero_passeport_wtf = form.numero_passeport_wtf.data
                date_photo_passeport_wtf = form.date_photo_passeport_wtf.data
                date_qualification_wtf = form.date_qualification_wtf.data
                valeurs_insertion_dictionnaire = {"value_numero_passeport": numero_passeport_wtf,
                                                  "value_date_photo_passeport": date_photo_passeport_wtf,
                                                  "value_date_qualification": date_qualification_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_passeport = """INSERT INTO t_passeport (ID_passeport, numero_passeport, date_photo_passeport, date_qualification) VALUES (NULL,%(value_numero_passeport)s, %(value_date_photo_passeport)s, %(value_date_qualification)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_passeport, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('passeport_afficher', order_by='DESC', ID_passeport_sel=0))

        except Exception as Exception_passeport_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{passeport_ajouter_wtf.__name__} ; "
                                            f"{Exception_passeport_ajouter_wtf}")

    return render_template("passeport/passeport_ajouter_wtf.html", form=form)


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


@app.route("/passeport_update", methods=['GET', 'POST'])
def passeport_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    ID_passeport_update = request.values['ID_passeport_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_passeport_update = FormWTFUpdatePasseport()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_passeport_update.submit.data:
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            numero_passeport_update_wtf = form_passeport_update.numero_passeport_update_wtf.data
            date_photo_passeport_update_wtf = form_passeport_update.date_photo_passeport_update_wtf.data
            date_qualification_update_wtf = form_passeport_update.date_qualification_update_wtf.data


            valeur_update_dictionnaire = {"value_ID_passeport": ID_passeport_update,
                                          "value_numero_passeport": numero_passeport_update_wtf,
                                          "value_date_photo_passeport": date_photo_passeport_update_wtf,
                                          "value_date_qualification": date_qualification_update_wtf
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_passeport SET numero_passeport = %(value_numero_passeport)s, date_photo_passeport = %(value_date_photo_passeport)s, date_qualification = %(value_date_qualification)s WHERE ID_passeport = %(value_ID_passeport)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('passeport_afficher', order_by="DESC", ID_passeport_sel=ID_passeport_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_genre = "SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport " \
                               "WHERE ID_passeport = %(value_ID_passeport)s"
            valeur_select_dictionnaire = {"value_ID_passeport": ID_passeport_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_numero_passeport = mybd_conn.fetchone()
            print("data_numero_passeport ", data_numero_passeport, " type ", type(data_numero_passeport), " genre ",
                  data_numero_passeport["numero_passeport"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "genre_update_wtf.html"
            form_passeport_update.numero_passeport_update_wtf.data = data_numero_passeport["numero_passeport"]
            form_passeport_update.date_photo_passeport_update_wtf.data = data_numero_passeport["date_photo_passeport"]
            form_passeport_update.date_qualification_update_wtf.data = data_numero_passeport["date_qualification"]




    except Exception as Exception_genre_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{passeport_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("passeport/passeport_update_wtf.html", form_update=form_passeport_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/passeport_delete", methods=['GET', 'POST'])
def passeport_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    ID_passeport_delete = request.values['ID_passeport_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_passeport_delete = FormWTFDeletePasseport()
    try:
        print(" on submit ", form_passeport_delete.validate_on_submit())
        if request.method == "POST" and form_passeport_delete.validate_on_submit():

            if form_passeport_delete.submit_btn_annuler.data:
                return redirect(url_for("passeport_afficher", order_by="ASC", id_genre_sel=0))

            if form_passeport_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer le passeport de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_passeport_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_ID_passeport": ID_passeport_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_passeport WHERE ID_passeport = %(value_ID_passeport)s"""
                str_sql_delete_idgenre = """DELETE FROM t_passeport WHERE ID_passeport = %(value_ID_passeport)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idgenre, valeur_delete_dictionnaire)

                flash(f"Passeport définitivement effacé !!", "success")
                print(f"Passeport définitivement effacé !!")

                # afficher les données
                return redirect(url_for('passeport_afficher', order_by="ASC", ID_passeport_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_ID_passeport": ID_passeport_delete}
            print(ID_passeport_delete, type(ID_passeport_delete))

            # Requête qui affiche tous les films_genres qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT * FROM t_passeport WHERE ID_passeport = %(value_ID_passeport)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_genre = "SELECT * FROM t_passeport WHERE ID_passeport = %(value_ID_passeport)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_numero_passeport = mydb_conn.fetchone()
                # print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      # data_nom_genre["intitule_genre"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "genre_delete_wtf.html"
            form_passeport_delete.nom_genre_delete_wtf.data = data_numero_passeport["numero_passeport"]

            # Le bouton pour l'action "DELETE" dans le form. "genre_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_passeport_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{passeport_delete_wtf.__name__} ; "
                                      f"{Exception_passeport_delete_wtf}")

    return render_template("passeport/passeport_delete_wtf.html",
                           form_delete=form_passeport_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)
