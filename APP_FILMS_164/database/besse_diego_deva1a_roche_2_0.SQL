-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: MACCAUD_OLIVIER_INFO1X_FILMS_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS module_164_diego_besse;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS module_164_diego_besse;

-- Utilisation de cette base de donnée

USE module_164_diego_besse;


-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour module_164_diego_besse
DROP DATABASE IF EXISTS `module_164_diego_besse`;
CREATE DATABASE IF NOT EXISTS `module_164_diego_besse` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `module_164_diego_besse`;

-- Listage de la structure de table module_164_diego_besse. t_adresse
DROP TABLE IF EXISTS `t_adresse`;
CREATE TABLE IF NOT EXISTS `t_adresse` (
  `ID_adresse` int NOT NULL AUTO_INCREMENT,
  `pays` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `canton` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `code_postal` int DEFAULT NULL,
  `ville` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `numero_rue` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_adresse`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_adresse : ~5 rows (environ)
INSERT INTO `t_adresse` (`ID_adresse`, `pays`, `canton`, `code_postal`, `ville`, `numero_rue`) VALUES
	(1, 'Suisse', 'VD', 1844, 'Villeneuve', 'Route de Praz-Bérard 3A'),
	(2, 'Suisse', 'VD', 1852, 'Roche', 'Rue du Grand-Cerclet 210'),
	(3, 'Suisse', 'VD', 1844, 'Villeneuve', 'Rue du Carroz-Devant 10'),
	(4, 'Suisse', 'VD', 1844, 'Villeneuve', 'Rue du Hameau 7'),
	(5, 'Suisse', 'VD', 1847, 'Rennaz', 'Route de Noville 5');

-- Listage de la structure de table module_164_diego_besse. t_cotisations
DROP TABLE IF EXISTS `t_cotisations`;
CREATE TABLE IF NOT EXISTS `t_cotisations` (
  `ID_cotisations` int NOT NULL AUTO_INCREMENT,
  `nom_coti` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `prix_coti` int DEFAULT NULL,
  PRIMARY KEY (`ID_cotisations`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_cotisations : ~6 rows (environ)
INSERT INTO `t_cotisations` (`ID_cotisations`, `nom_coti`, `prix_coti`) VALUES
	(1, 'Junior B', 250),
	(2, 'Junior féminines FF-15', 200),
	(4, 'Junior C', 250),
	(5, 'Junior D', 220),
	(7, 'Junior E', 200),
	(8, 'Junior F', 150);

-- Listage de la structure de table module_164_diego_besse. t_equipes
DROP TABLE IF EXISTS `t_equipes`;
CREATE TABLE IF NOT EXISTS `t_equipes` (
  `ID_equipes` int NOT NULL AUTO_INCREMENT,
  `nom_equipes` varchar(22) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_equipes`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_equipes : ~7 rows (environ)
INSERT INTO `t_equipes` (`ID_equipes`, `nom_equipes`) VALUES
	(1, 'Junior B 2ème degré'),
	(2, 'Junior féminines FF-15'),
	(4, 'Junior C 1er degré'),
	(5, 'Junior D/9 - 1'),
	(7, 'Junior E'),
	(8, 'Junior F '),
	(13, 'Junior D/9 - 2');

-- Listage de la structure de table module_164_diego_besse. t_habiter
DROP TABLE IF EXISTS `t_habiter`;
CREATE TABLE IF NOT EXISTS `t_habiter` (
  `ID_habiter` int NOT NULL AUTO_INCREMENT,
  `FK_joueurs` int DEFAULT NULL,
  `FK_adresse` int DEFAULT NULL,
  PRIMARY KEY (`ID_habiter`),
  KEY `FK_joueurs` (`FK_joueurs`),
  KEY `FK_adresse` (`FK_adresse`),
  CONSTRAINT `FK_t_habiter_t_adresse` FOREIGN KEY (`FK_adresse`) REFERENCES `t_adresse` (`ID_adresse`),
  CONSTRAINT `FK_t_habiter_t_joueurs` FOREIGN KEY (`FK_joueurs`) REFERENCES `t_joueurs` (`ID_joueurs`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_habiter : ~5 rows (environ)
INSERT INTO `t_habiter` (`ID_habiter`, `FK_joueurs`, `FK_adresse`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5);

-- Listage de la structure de table module_164_diego_besse. t_joueurs
DROP TABLE IF EXISTS `t_joueurs`;
CREATE TABLE IF NOT EXISTS `t_joueurs` (
  `ID_joueurs` int NOT NULL AUTO_INCREMENT,
  `civilite` varchar(22) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nom` varchar(22) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `prenom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `nationnalite` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `courriel` varchar(50) DEFAULT NULL,
  `telephone` int DEFAULT NULL,
  `FK_equipes` int DEFAULT NULL,
  `FK_cotisations` int DEFAULT NULL,
  `FK_passeport` int DEFAULT NULL,
  PRIMARY KEY (`ID_joueurs`),
  KEY `FK_equipes` (`FK_equipes`),
  KEY `FK_cotisations` (`FK_cotisations`),
  KEY `FK_passeport` (`FK_passeport`),
  CONSTRAINT `FK_t_joueurs_t_cotisations` FOREIGN KEY (`FK_cotisations`) REFERENCES `t_cotisations` (`ID_cotisations`),
  CONSTRAINT `FK_t_joueurs_t_equipes` FOREIGN KEY (`FK_equipes`) REFERENCES `t_equipes` (`ID_equipes`),
  CONSTRAINT `FK_t_joueurs_t_passeport` FOREIGN KEY (`FK_passeport`) REFERENCES `t_passeport` (`ID_passeport`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_joueurs : ~5 rows (environ)
INSERT INTO `t_joueurs` (`ID_joueurs`, `civilite`, `nom`, `prenom`, `date_naissance`, `nationnalite`, `courriel`, `telephone`, `FK_equipes`, `FK_cotisations`, `FK_passeport`) VALUES
	(1, 'Monsieur', 'Abbassaggi', 'Bastien', '2007-10-09', 'Suisse', 'sabbassaggi@gmail.com', 787201490, 1, 1, 1),
	(2, 'Monsieur', 'Ahmetovic', 'Ervin', '2011-12-06', 'Suisse', 'sanelaahmetovic31@gmail.com', 799470403, 5, 5, 2),
	(3, 'Monsieur', 'Ameijenda Vidal', 'Daniel', '2009-09-28', 'Espagne', 'noeliavb8@hotmail.com', 792687849, 4, 4, 3),
	(4, 'Monsieur ', 'Amory Vallotton', 'Terry', '2008-10-30', 'Suisse', 'terry.vallo@bluewin.ch', 792829325, 1, 1, 4),
	(5, 'Madame', 'Andaloro', 'Lisa', '2010-04-01', 'Suisse', 'andal@bluewin.ch', 763799915, 2, 2, 5);

-- Listage de la structure de table module_164_diego_besse. t_passeport
DROP TABLE IF EXISTS `t_passeport`;
CREATE TABLE IF NOT EXISTS `t_passeport` (
  `ID_passeport` int NOT NULL AUTO_INCREMENT,
  `numero_passeport` int DEFAULT NULL,
  `date_photo_passeport` date DEFAULT NULL,
  `date_qualification` date DEFAULT NULL,
  PRIMARY KEY (`ID_passeport`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_passeport : ~5 rows (environ)
INSERT INTO `t_passeport` (`ID_passeport`, `numero_passeport`, `date_photo_passeport`, `date_qualification`) VALUES
	(1, 1951612, '2020-01-08', '2020-01-20'),
	(2, 1998907, '2021-08-25', '2023-03-27'),
	(3, 1999789, '2021-08-27', '2021-09-03'),
	(4, 1079751, '2016-09-05', '2016-09-14'),
	(5, 2000048, '2023-10-05', '2021-09-16');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
