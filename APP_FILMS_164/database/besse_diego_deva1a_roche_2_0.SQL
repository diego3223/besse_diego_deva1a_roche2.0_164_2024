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
  `canton` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `code_postal` int DEFAULT NULL,
  `ville` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nom_rue` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `numero_rue` int DEFAULT NULL,
  PRIMARY KEY (`ID_adresse`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_adresse : ~10 rows (environ)
INSERT INTO `t_adresse` (`ID_adresse`, `pays`, `canton`, `code_postal`, `ville`, `nom_rue`, `numero_rue`) VALUES
	(1, 'Suisse', 'VD', 1844, 'Villeneuve', 'Route de Praz-Bérard', 3),
	(2, 'Suisse', 'VD', 1852, 'Roche', 'Rue du Grand-Cerclet ', 210),
	(3, 'Suisse', 'VD', 1860, 'Aigle', 'Rue du Carroz-Devant ', 10),
	(4, 'Suisse', 'VD', 1696, 'Vouvry', 'Rue du Hameau', 7),
	(5, 'Suisse', 'VD', 1847, 'Rennaz', 'Route de Noville ', 5),
	(6, 'Suisse', 'VD', 1800, 'Vevey', 'Route de Carroz Derrière ', 9),
	(7, 'Suisse', 'VD', 1845, 'Noville', 'Route d\'Evian', 7),
	(8, 'Suisse', 'VD', 1815, 'Montreux', 'Chemin du Levant ', 9),
	(19, 'Suisse', 'VS', 1950, 'Saillon', 'Chemin de la Cascade', 87),
	(45, 'Suisse', 'VS', 1846, 'Chessel', 'Avenue de Jordil ', 12);

-- Listage de la structure de table module_164_diego_besse. t_cotisations
DROP TABLE IF EXISTS `t_cotisations`;
CREATE TABLE IF NOT EXISTS `t_cotisations` (
  `ID_cotisations` int NOT NULL AUTO_INCREMENT,
  `nom_coti` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `prix_coti` int DEFAULT NULL,
  PRIMARY KEY (`ID_cotisations`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_equipes : ~7 rows (environ)
INSERT INTO `t_equipes` (`ID_equipes`, `nom_equipes`) VALUES
	(1, 'Junior B 2ème degrès'),
	(2, 'Junior féminines FF-15'),
	(4, 'Junior C 1er degré'),
	(5, 'Junior D/9 - 1'),
	(7, 'Junior E'),
	(8, 'Junior F'),
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
  CONSTRAINT `FK_t_habiter_t_joueurs` FOREIGN KEY (`FK_joueurs`) REFERENCES `t_joueurs` (`ID_joueurs`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_habiter : ~10 rows (environ)
INSERT INTO `t_habiter` (`ID_habiter`, `FK_joueurs`, `FK_adresse`) VALUES
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5),
	(6, 6, 6),
	(7, 7, 7),
	(8, 8, 8),
	(9, 41, 19),
	(29, 1, 1),
	(43, 1, 45);

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
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_joueurs : ~9 rows (environ)
INSERT INTO `t_joueurs` (`ID_joueurs`, `civilite`, `nom`, `prenom`, `date_naissance`, `nationnalite`, `courriel`, `telephone`, `FK_equipes`, `FK_cotisations`, `FK_passeport`) VALUES
	(1, 'Monsieur', 'Abbassaggi', 'Bastien', '2007-10-09', 'Suisse', 'sabbassaggi@gmail.com', 787201490, 1, 1, 1),
	(2, 'Monsieur', 'Ahmetovic', 'Ervin', '2011-12-06', 'Suisse', 'sanelaahmetovic31@gmail.com', 799470403, 5, 5, 2),
	(3, 'Monsieur', 'Ameijenda Vidal', 'Daniel', '2009-09-28', 'Espagne', 'noeliavb8@hotmail.com', 792687849, 4, 4, 3),
	(4, 'Monsieur ', 'Amory Vallotton', 'Terry', '2008-10-30', 'Suisse', 'terry.vallo@bluewin.ch', 792829325, 1, 1, 4),
	(5, 'Madame', 'Andaloro', 'Lisa', '2010-04-01', 'Suisse', 'andal@bluewin.ch', 763799915, 2, 2, 5),
	(6, 'Monsieur', 'Soares Amorim', 'Tiago', '2008-09-02', 'Portugal', 'sofia-tiago2010@hotmail.com', 787493381, 1, 1, 6),
	(7, 'Madame', 'Spidalieri', 'Ohra', '2010-07-14', 'Italie', 'stephane.spidalieri@bluewin.ch', 792120457, 2, 2, 7),
	(8, 'Monsieur', 'Smajlaj', 'Albin', '2010-03-03', 'Kosovo', 'demesmajlaj1@outlook.com', 763916032, 4, 4, 8),
	(41, 'Monsieur', 'Dante', 'Cédric', '2007-02-06', 'Suisse', 'cedric.dante@gmail.com', 768783276, 1, 1, 9);

-- Listage de la structure de table module_164_diego_besse. t_passeport
DROP TABLE IF EXISTS `t_passeport`;
CREATE TABLE IF NOT EXISTS `t_passeport` (
  `ID_passeport` int NOT NULL AUTO_INCREMENT,
  `numero_passeport` int DEFAULT NULL,
  `date_photo_passeport` date DEFAULT NULL,
  `date_qualification` date DEFAULT NULL,
  PRIMARY KEY (`ID_passeport`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164_diego_besse.t_passeport : ~9 rows (environ)
INSERT INTO `t_passeport` (`ID_passeport`, `numero_passeport`, `date_photo_passeport`, `date_qualification`) VALUES
	(1, 1951612, '2020-01-08', '2020-01-20'),
	(2, 1998907, '2021-08-25', '2023-03-27'),
	(3, 1999789, '2021-08-27', '2021-09-03'),
	(4, 1079751, '2016-09-05', '2016-09-14'),
	(5, 2000048, '2023-10-05', '2021-09-16'),
	(6, 1152557, '2019-09-04', '2018-03-18'),
	(7, 2003871, '2021-09-19', '2021-09-12'),
	(8, 1999152, '2021-08-25', '2021-09-02'),
	(9, 2003872, '2023-05-05', '2021-05-13');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
