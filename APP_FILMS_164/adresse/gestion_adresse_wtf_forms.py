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


class FormWTFAjouterAdresse(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    pays_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_wtf = StringField("Clavioter le pays ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(pays_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    canton_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    canton_wtf = StringField("Clavioter le canton ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(canton_regexp,
                                                                    message="Pas de chiffres, de caractères "
                                                                            "spéciaux, "
                                                                            "d'espace à double, de double "
                                                                            "apostrophe, de double trait union")
                                                             ])

    code_postal_regexp = ""
    code_postal_wtf = StringField("Clavioter le NPA ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(code_postal_regexp,
                                                                        message="Pas de chiffres, de caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait union")
                                                                 ])

    ville_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_wtf = StringField("Clavioter la ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(ville_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    nom_rue_regexp = ""
    nom_rue_wtf = StringField("Clavioter le nom de la rue ", validators=[Length(min=1, max=40, message="min 2 max 40"),
                                                               Regexp(nom_rue_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])


    numero_rue_regexp = ""
    numero_rue_wtf = StringField("Clavioter le numéro de la rue ", validators=[Length(min=1, max=20, message="min 1 max 20"),
                                                               Regexp(numero_rue_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])


    submit = SubmitField("Enregistrer adresse")


class FormWTFUpdateAdresse(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    pays_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_update_wtf = StringField("Clavioter le pays ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(pays_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    canton_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    canton_update_wtf = StringField("Clavioter le canton ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                    Regexp(canton_update_regexp,
                                                                           message="Pas de chiffres, de "
                                                                                   "caractères "
                                                                                   "spéciaux, "
                                                                                   "d'espace à double, de double "
                                                                                   "apostrophe, de double trait "
                                                                                   "union")
                                                                    ])

    code_postal_update_regexp = ""
    code_postal_update_wtf = StringField("Clavioter le NPA ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(code_postal_update_regexp,
                                                                             message="Pas de chiffres, de "
                                                                                     "caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait "
                                                                                     "union")
                                                                      ])

    ville_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_update_wtf = StringField("Clavioter la ville ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(ville_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])

    nom_rue_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_rue_update_wtf = StringField("Clavioter le nom de rue ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                      Regexp(nom_rue_update_regexp,
                                                                             message="Pas de chiffres, de "
                                                                                     "caractères "
                                                                                     "spéciaux, "
                                                                                     "d'espace à double, de double "
                                                                                     "apostrophe, de double trait "
                                                                                     "union")
                                                                      ])

    numero_rue_update_regexp = ""
    numero_rue_update_wtf = StringField("Clavioter le numéro de rue ",
                                     validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                 Regexp(numero_rue_update_regexp,
                                                        message="Pas de chiffres, de "
                                                                "caractères "
                                                                "spéciaux, "
                                                                "d'espace à double, de double "
                                                                "apostrophe, de double trait "
                                                                "union")
                                                 ])

    # date_genre_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                              # DataRequired("Date non valide")])
    submit = SubmitField("Update adresse")


class FormWTFDeleteAdresse(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer cette adresse")
    submit_btn_del = SubmitField("Effacer adresse")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
