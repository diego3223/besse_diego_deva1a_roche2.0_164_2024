/* Requetes */ 

/* Les requetes ci-dessous sont issues des Crud */

    /* Joueurs */
        /* Afficher*/
            /* Sélection de tous les joueurs */
                SELECT * from t_joueurs;
            /* Sélection d'un joueur spécifique (ID_joueurs = 1) */
                SELECT * from t_joueurs WHERE ID_joueurs = 1;
            /* Sélection de tous les joueurs par ordre décroissant de leur ID */
                SELECT * from t_joueurs ORDER BY ID_joueurs DESC;
        /*Ajouter*/
            /* Ajout d'un nouveau joueur */
                INSERT INTO t_joueurs (ID_joueurs, civilite, nom, prenom, nationnalite, date_naissance, courriel, telephone, FK_equipes, FK_cotisations, FK_passeport) VALUES (NULL, 'Monsieur', 'Maccaud', 'Patrick', 'Suisse', '2007-10-02', 'patrickmaccaud@bluewin.ch', '0797475644', '1', '1', '3');
        /*Update*/
            /* Mise à jour des informations d'un joueur (ID_joueurs = 1) */
                UPDATE t_joueurs SET civilite = 'Madame', nom = 'Addo', prenom = 'Sylvie', date_naissance = '2009-08-04', nationnalite = 'Suisse', courriel = 'sylvieaddo@gmail.com', telephone = '781409877', FK_equipes = '2', FK_cotisations = '2', FK_passeport = '1' WHERE ID_joueurs = 1;
            /* Sélection d'un joueur spécifique après mise à jour (ID_joueurs = 1) */
                SELECT ID_joueurs, civilite, nom, prenom, date_naissance, nationnalite, courriel, telephone, FK_equipes, FK_cotisations, FK_passeport FROM t_joueurs WHERE ID_joueurs = 1;
        /*Delete*/
            /* Suppression des enregistrements d'habitation d'un joueur spécifique (FK_joueurs = 1) */
///             DELETE FROM t_habiter WHERE FK_joueurs = 1;
            /* Suppression d'un joueur spécifique (ID_joueurs = 1) */
                DELETE FROM t_joueurs WHERE ID_joueurs = 68;
            /* Sélection des informations d'adresse pour un joueur spécifique (ID_joueurs = 1) */
                SELECT ID_joueurs, civilite, nom, prenom, nom_rue FROM t_habiter
                                                                INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                                INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                                WHERE ID_joueurs = 1;
            /* Sélection d'un joueur spécifique (ID_joueurs = 1) */
                SELECT * FROM t_joueurs WHERE ID_joueurs = 1;


    /*Adresse*/
        /*Afficher*/
            /* Sélection de toutes les adresses */
                SELECT * FROM t_adresse;
            /* Sélection des informations d'une adresse spécifique (ID_adresse = 1) */
                SELECT ID_adresse, pays, canton, code_postal, ville, nom_rue, numero_rue  FROM t_adresse WHERE ID_adresse = 1;
            /* Sélection de toutes les adresses par ordre décroissant de leur ID */
                SELECT ID_adresse, pays, canton, code_postal, ville, nom_rue, numero_rue FROM t_adresse ORDER BY ID_adresse DESC;
        /*Ajouter*/
            /* Ajout d'une nouvelle adresse */
                INSERT INTO t_adresse (ID_adresse,pays, canton, code_postal, ville, nom_rue, numero_rue) VALUES (NULL, 'Suisse', 'GE', '1200', 'Genève', 'Chemin de la Balance', '87');
        /*Update*/
            /* Mise à jour des informations d'une adresse (ID_adresse = 2) */
               UPDATE t_adresse SET pays = 'Suisse', canton = 'VD', code_postal = '1807', ville = 'Blonay', nom_rue = 'Route du Village', numero_rue = 17 WHERE ID_adresse = 1;
            /* Sélection des informations d'une adresse spécifique (ID_adresse = 3) */
                SELECT ID_adresse, pays, canton, code_postal, ville, nom_rue, numero_rue FROM t_adresse WHERE ID_adresse = 3;
        /*Delete*/
            /* Suppression des enregistrements d'habitation d'une adresse spécifique (FK_adresse = 3) */
///             DELETE FROM t_habiter WHERE FK_adresse = 3;
            /* Suppression d'une adresse spécifique (ID_adresse = 3) */
                DELETE FROM t_adresse WHERE ID_adresse = 3;
            /* Sélection des informations d'un joueur habitant à une adresse spécifique (ID_adresse = 2) */
                SELECT ID_joueurs, civilite, nom, prenom, nom_rue FROM t_habiter
                                                        INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                        INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                        WHERE ID_adresse = 2;
            /* Sélection d'une adresse spécifique (ID_adresse = 6) */
                SELECT * FROM t_adresse WHERE ID_adresse = 6;

    /*Joueurs/Adresse*/
        /*films_genres_afficher*/
            /* Afficher les joueurs avec leurs adresses */ /* Avec filtre HAVING (optionnel) */
                """ SELECT ID_joueurs,civilite,nom,prenom, GROUP_CONCAT(nom_rue) AS Nom_rue_joueur FROM t_habiter
                    RIGHT JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                    LEFT JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                    GROUP BY ID_joueurs """
                """ HAVING ID_joueurs= 6"""
        /*edit_genre_film_selectedr*/
            /* Sélectionner les adresses (Nom des rues) */
                SELECT ID_adresse, nom_rue FROM t_adresse ORDER BY ID_adresse ASC;
        /*update_genre_film_selected*/
            /* Ajouter une habitation pour un joueur */
                INSERT INTO t_habiter (ID_habiter, FK_adresse, FK_joueurs) VALUES (NULL, '2', '3');
            /* Supprimer une habitation pour un joueur */
                DELETE FROM t_habiter WHERE FK_adresse = '19' AND FK_joueurs = '41';
        /*genres_films_afficher_data*/
            /* Afficher les adresses des joueurs (données spécifiques) */
                SELECT ID_joueurs, civilite, nom, prenom, GROUP_CONCAT(ID_adresse) as JoueursAdresse FROM t_habiter
                                                INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                WHERE ID_joueurs = '2'; 
            /* Sélectionner les adresses non associées à un joueur spécifique (ID_joueurs = '1') */
///             SELECT ID_adresse, nom_rue FROM t_adresse WHERE ID_adresse not in(SELECT ID_adresse as idHabiter FROM t_habiter
                                                            INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                            INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                            WHERE ID_joueurs = '1'); 
            /* Afficher les adresses d'un joueur spécifique (Nom rue)*/
                SELECT ID_joueurs, ID_adresse, nom_rue FROM t_habiter
                                                    INNER JOIN t_joueurs ON t_joueurs.ID_joueurs = t_habiter.FK_joueurs
                                                    INNER JOIN t_adresse ON t_adresse.ID_adresse = t_habiter.FK_adresse
                                                    WHERE ID_joueurs = '2';

    /*Equipes*/
        /*Afficher*/
            /* Sélection de toutes les équipes */
                SELECT * FROM t_equipes;
            /* Sélection d'une équipe spécifique par son ID et son nom */
                SELECT ID_equipes, nom_equipes FROM t_equipes WHERE ID_equipes = 1 AND nom_equipes = 'Junior B 2ème degrès';
            /* Sélection de toutes les équipes par ordre décroissant de leur ID */
                SELECT ID_equipes, nom_equipes FROM t_equipes ORDER BY ID_equipes DESC;
        /*Ajouter*/
            /* Ajout d'une nouvelle équipe */
                INSERT INTO t_equipes (ID_equipes,nom_equipes) VALUES (NULL, 'Junior Z');
        /*Update*/
            /* Mise à jour du nom d'une équipe (ID_equipes = 8) */
                UPDATE t_equipes SET nom_equipes = 'Junior H' WHERE ID_equipes = '8';
            /* Sélection d'une équipe spécifique après mise à jour (ID_equipes = 2) */
                SELECT ID_equipes, nom_equipes FROM t_equipes WHERE ID_equipes = '2';
        /*Delete*/
            /* Suppression d'une équipe (ID_equipes = 8) */
                DELETE FROM t_equipes WHERE ID_equipes = 8;
            /* Sélection d'une équipe spécifique (ID_equipes = 4) */
                SELECT * FROM t_equipes WHERE ID_equipes = 4;
            /* Sélection d'une équipe spécifique (ID_equipes = 5) */
                SELECT * FROM t_equipes WHERE ID_equipes = 5;
    
    /*Cotisations*/
        /*Afficher*/
            /* Sélection de toutes les cotisations */
                SELECT * FROM t_cotisations;
            /* Sélection d'une cotisation spécifique par ID, nom et prix */
///             SELECT ID_cotisations, nom_coti, prix_coti FROM t_cotisations WHERE ID_cotisations = 1, nom_coti = 'Junior B', prix_coti = 250;
            /* Sélection de toutes les cotisations par ordre décroissant de leur ID */
                SELECT ID_cotisations, nom_coti, prix_coti FROM t_cotisations ORDER BY ID_cotisations DESC;
        /*Ajouter*/
            /* Ajout d'une nouvelle cotisation */
                INSERT INTO t_cotisations (ID_cotisations, nom_coti, prix_coti) VALUES (NULL, 'Junior Z', 550);
        /*Update*/
            /* Mise à jour du nom et du prix d'une cotisation (ID_cotisations = 8) */
                UPDATE t_cotisations SET nom_coti = 'Junior K', prix_coti = 40 WHERE ID_cotisations = 8;
            /* Sélection d'une cotisation spécifique après mise à jour (ID_cotisations = 3) */
                SELECT ID_cotisations, nom_coti, prix_coti FROM t_cotisations WHERE ID_cotisations = 3;
        /*Delete*/
            /* Suppression d'une cotisation (ID_cotisations = 8) */
                DELETE FROM t_cotisations WHERE ID_cotisations = 8;
            /* Sélection d'une cotisation spécifique (ID_cotisations = 1) */
                SELECT * FROM t_cotisations WHERE ID_cotisations = 1;

    /*Passeport*/
        /*Afficher*/
            /* Sélection de tous les passeports */
                SELECT * FROM t_passeport;
            /* Sélection d'un passeport spécifique par ID, numéro, date de photo et date de qualification */
///             SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport WHERE ID_passeport = 2, numero_passeport = '1998907', date_photo_passeport = '2021-08-25', date_qualification = '2023-03-27';
            /* Sélection de tous les passeports par ordre décroissant de leur ID */
                SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport ORDER BY ID_passeport DESC;
        /*Ajouter*/
            /* Ajout d'un nouveau passeport */
                INSERT INTO t_passeport (ID_passeport, numero_passeport, date_photo_passeport, date_qualification) VALUES (NULL, '1122334', '2016-09-05', '2023-08-07');
        /*Update*/
            /* Mise à jour des informations d'un passeport (ID_passeport = 9) */
                UPDATE t_passeport SET numero_passeport = '2000048', date_photo_passeport = '2011-11-10', date_qualification = '2012-12-03' WHERE ID_passeport = 9;
            /* Sélection d'un passeport spécifique après mise à jour (ID_passeport = 5) */
                SELECT ID_passeport, numero_passeport, date_photo_passeport, date_qualification FROM t_passeport WHERE ID_passeport = 5;
        /*Delete*/
            /* Suppression d'un passeport (ID_passeport = 9) */
                DELETE FROM t_passeport WHERE ID_passeport = '9';
            /* Sélection d'un passeport spécifique (ID_passeport = 7) */
                SELECT * FROM t_passeport WHERE ID_passeport = '7';
