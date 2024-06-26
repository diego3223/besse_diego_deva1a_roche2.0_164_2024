"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterPasseport(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    numero_passeport_regexp = ""
    numero_passeport_wtf = StringField("Clavioter le numéro de passeport ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(numero_passeport_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    date_photo_passeport_regexp = ""
    date_photo_passeport_wtf = StringField("Clavioter la date de la photo passeport ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(date_photo_passeport_regexp,
                                                                    message="Pas de chiffres, de caractères "
                                                                            "spéciaux, "
                                                                            "d'espace à double, de double "
                                                                            "apostrophe, de double trait union")
                                                             ])

    date_qualification_regexp = ""
    date_qualification_wtf = StringField("Clavioter la date de qualification ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(date_qualification_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])




    submit = SubmitField("Enregistrer passeport")


class FormWTFUpdatePasseport(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    numero_passeport_update_regexp = ""
    numero_passeport_update_wtf = StringField("Clavioter le numéro de passeport ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(numero_passeport_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    date_photo_passeport_update_regexp = ""
    date_photo_passeport_update_wtf = StringField("Clavioter la date de la photo passeport ",
                                              validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                          Regexp(date_photo_passeport_update_regexp,
                                                                 message="Pas de chiffres, de "
                                                                         "caractères "
                                                                         "spéciaux, "
                                                                         "d'espace à double, de double "
                                                                         "apostrophe, de double trait "
                                                                         "union")
                                                          ])

    date_qualification_update_regexp = ""
    date_qualification_update_wtf = StringField("Clavioter la date de qualification ",
                                                  validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                              Regexp(date_qualification_update_regexp,
                                                                     message="Pas de chiffres, de "
                                                                             "caractères "
                                                                             "spéciaux, "
                                                                             "d'espace à double, de double "
                                                                             "apostrophe, de double trait "
                                                                             "union")
                                                              ])

    # date_genre_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                              # DataRequired("Date non valide")])
    submit = SubmitField("Update passeport")


class FormWTFDeletePasseport(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce passeport")
    submit_btn_del = SubmitField("Effacer passeport")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
