"""
    Fichier : gestion_equipes_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp

class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    civilite_regexp = ""
    civilite_wtf = StringField("Clavioter la civilité ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(civilite_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])


    nom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_wtf = StringField("Clavioter le nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    #prenom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_regexp = ""
    prenom_wtf = StringField("Clavioter le prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(prenom_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    # prenom_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nationnalite_regexp = ""
    nationnalite_wtf = StringField("Clavioter la nationnalité ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(nationnalite_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                    ])

    date_naissance_regexp = ""
    date_naissance_wtf = StringField("Clavioter la date de naissance ",
                                   validators=[Length(min=2, max=20, message="min 2 max 20"),
                                               Regexp(date_naissance_regexp,
                                                      message="Pas de chiffres, de caractères "
                                                              "spéciaux, "
                                                              "d'espace à double, de double "
                                                              "apostrophe, de double trait union")
                                               ])

    courriel_regexp = ""
    courriel_wtf = StringField("Clavioter l'E-Mail ",
                                     validators=[Length(min=2, max=40, message="min 2 max 40"),
                                                 Regexp(courriel_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])

    telephone_regexp = ""
    telephone_wtf = StringField("Clavioter le numéro de téléphone ",
                               validators=[Length(min=2, max=20, message="min 2 max 20"),
                                           Regexp(telephone_regexp,
                                                  message="Pas de chiffres, de caractères "
                                                          "spéciaux, "
                                                          "d'espace à double, de double "
                                                          "apostrophe, de double trait union")
                                           ])

    FK_equipes_regexp = ""
    FK_equipes_wtf = StringField("Clavioter le numéro correspondant à l'équipe ",
                                validators=[Length(min=1, max=20, message="min 1 max 20"),
                                            Regexp(FK_equipes_regexp,
                                                   message="Pas de chiffres, de caractères "
                                                           "spéciaux, "
                                                           "d'espace à double, de double "
                                                           "apostrophe, de double trait union")
                                            ])

    FK_cotisations_regexp = ""
    FK_cotisations_wtf = StringField("Clavioter le numéro correspondant à la cotisation ",
                                 validators=[Length(min=1, max=20, message="min 1 max 20"),
                                             Regexp(FK_cotisations_regexp,
                                                    message="Pas de chiffres, de caractères "
                                                            "spéciaux, "
                                                            "d'espace à double, de double "
                                                            "apostrophe, de double trait union")
                                             ])

    FK_passeport_regexp = ""
    FK_passeport_wtf = StringField("Clavioter le numéro correspondant au passeport ",
                                     validators=[Length(min=1, max=20, message="min 1 max 20"),
                                                 Regexp(FK_passeport_regexp,
                                                        message="Pas de chiffres, de caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait union")
                                                 ])



    submit = SubmitField("Enregistrer joueur")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    civilite_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    civilite_update_wtf = StringField("Clavioter la civilité ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(civilite_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    nom_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_update_wtf = StringField("Clavioter le nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                         Regexp(nom_update_regexp,
                                                                                message="Pas de chiffres, de "
                                                                                        "caractères "
                                                                                        "spéciaux, "
                                                                                        "d'espace à double, de double "
                                                                                        "apostrophe, de double trait "
                                                                                        "union")
                                                                         ])

    prenom_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_update_wtf = StringField("Clavioter le prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                        Regexp(prenom_update_regexp,
                                                                               message="Pas de chiffres, de "
                                                                                       "caractères "
                                                                                       "spéciaux, "
                                                                                       "d'espace à double, de double "
                                                                                       "apostrophe, de double trait "
                                                                                       "union")
                                                                        ])

    date_naissance_update_regexp = ""
    date_naissance_update_wtf = StringField("Clavioter la date de naissance",
                                            validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(date_naissance_update_regexp,
                                                               message="Pas de chiffres, de "
                                                                       "caractères "
                                                                       "spéciaux, "
                                                                       "d'espace à double, de double "
                                                                       "apostrophe, de double trait "
                                                                       "union")
                                                        ])

    nationnalite_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nationnalite_update_wtf = StringField("Clavioter la nationnalité ",
                                            validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(nationnalite_update_regexp,
                                                               message="Pas de chiffres, de "
                                                                       "caractères "
                                                                       "spéciaux, "
                                                                       "d'espace à double, de double "
                                                                       "apostrophe, de double trait "
                                                                       "union")
                                                        ])

    courriel_update_regexp = ""
    courriel_update_wtf = StringField("Clavioter le courriel ",
                                          validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                      Regexp(courriel_update_regexp,
                                                             message="Pas de chiffres, de "
                                                                     "caractères "
                                                                     "spéciaux, "
                                                                     "d'espace à double, de double "
                                                                     "apostrophe, de double trait "
                                                                     "union")
                                                      ])

    telephone_update_regexp = ""
    telephone_update_wtf = StringField("Clavioter le téléphone ",
                                      validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                  Regexp(telephone_update_regexp,
                                                         message="Pas de chiffres, de "
                                                                 "caractères "
                                                                 "spéciaux, "
                                                                 "d'espace à double, de double "
                                                                 "apostrophe, de double trait "
                                                                 "union")
                                                  ])

    FK_equipes_update_regexp = ""
    FK_equipes_update_wtf = StringField("Clavioter le numéro correspondant à l'équipe ",
                                       validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                   Regexp(FK_equipes_update_regexp,
                                                          message="Pas de chiffres, de "
                                                                  "caractères "
                                                                  "spéciaux, "
                                                                  "d'espace à double, de double "
                                                                  "apostrophe, de double trait "
                                                                  "union")
                                                   ])

    FK_cotisations_update_regexp = ""
    FK_cotisations_update_wtf = StringField("Clavioter le numéro correspondant à la cotisation ",
                                        validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                    Regexp(FK_cotisations_update_regexp,
                                                           message="Pas de chiffres, de "
                                                                   "caractères "
                                                                   "spéciaux, "
                                                                   "d'espace à double, de double "
                                                                   "apostrophe, de double trait "
                                                                   "union")
                                                    ])

    FK_passeport_update_regexp = ""
    FK_passeport_update_wtf = StringField("Clavioter le numéro correspondant au passeport ",
                                            validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(FK_passeport_update_regexp,
                                                               message="Pas de chiffres, de "
                                                                       "caractères "
                                                                       "spéciaux, "
                                                                       "d'espace à double, de double "
                                                                       "apostrophe, de double trait "
                                                                       "union")
                                                        ])


    # date_genre_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
    #                                                          DataRequired("Date non valide")])
    submit = SubmitField("Update joueur")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "equipes_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce joueur")
    submit_btn_del = SubmitField("Effacer joueur")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
