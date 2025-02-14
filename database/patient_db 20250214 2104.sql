-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.7.43-log


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema patient_db
--

CREATE DATABASE IF NOT EXISTS patient_db;
USE patient_db;

--
-- Definition of table `register_pat`
--

DROP TABLE IF EXISTS `register_pat`;
CREATE TABLE `register_pat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hpatcode` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pfname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pmname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `plname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psuffix` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pbirthdate` date DEFAULT NULL,
  `psex` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pcstatus` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psaddress` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pscity` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psbrgy` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psregion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psdistrict` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `psprovince` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pszipcode` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pscountry` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `praddress` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prcity` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prbrgy` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prregion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prdistrict` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prprovince` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `przipcode` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prcountry` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cpname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cpaddress` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cptel` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cprelationship` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `pstats` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `register_pat`
--

/*!40000 ALTER TABLE `register_pat` DISABLE KEYS */;
/*!40000 ALTER TABLE `register_pat` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
