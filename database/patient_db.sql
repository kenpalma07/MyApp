CREATE DATABASE patient_db;
USE patient_db;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `register_pat` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `hpatcode` varchar(255) DEFAULT NULL,
  `pfname` varchar(255) DEFAULT NULL,
  `pmname` varchar(255) DEFAULT NULL,
  `plname` varchar(255) DEFAULT NULL,
  `psuffix` varchar(255) DEFAULT NULL,
  `pbirthdate` date DEFAULT NULL,
  `psex` varchar(255) DEFAULT NULL,
  `pcstatus` varchar(255) DEFAULT NULL,
  `psaddress` varchar(255) DEFAULT NULL,
  `pscity` varchar(255) DEFAULT NULL,
  `psbrgy` varchar(255) DEFAULT NULL,
  `psregion` varchar(255) DEFAULT NULL,
  `psdistrict` varchar(255) DEFAULT NULL,
  `psprovince` varchar(255) DEFAULT NULL,
  `pszipcode` varchar(255) DEFAULT NULL,
  `pscountry` varchar(255) DEFAULT NULL,
  `praddress` varchar(255) DEFAULT NULL,
  `prcity` varchar(255) DEFAULT NULL,
  `prbrgy` varchar(255) DEFAULT NULL,
  `prregion` varchar(255) DEFAULT NULL,
  `prdistrict` varchar(255) DEFAULT NULL,
  `prprovince` varchar(255) DEFAULT NULL,
  `przipcode` varchar(255) DEFAULT NULL,
  `prcountry` varchar(255) DEFAULT NULL,
  `cpname` varchar(255) DEFAULT NULL,
  `cpaddress` varchar(255) DEFAULT NULL,
  `cptel` varchar(255) DEFAULT NULL,
  `cprelationship` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `pstats` varchar(255) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
