-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: dz
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam` (
  `idexam` int NOT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `mark` varchar(45) DEFAULT NULL,
  `amount` varchar(45) DEFAULT NULL,
  `start` varchar(45) DEFAULT NULL,
  `end` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idexam`),
  KEY `a_idx` (`surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (1,'Пупкин','5','30','2018-10-10','2019-10-10'),(2,'Васькин','4','20','2019-11-11','2020-11-11');
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privilege`
--

DROP TABLE IF EXISTS `privilege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `privilege` (
  `idprivilege` int NOT NULL,
  `path` varchar(45) DEFAULT NULL,
  `idrole` int DEFAULT NULL,
  PRIMARY KEY (`idprivilege`),
  KEY `idrole_idx` (`idrole`),
  CONSTRAINT `` FOREIGN KEY (`idrole`) REFERENCES `role` (`idrole`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privilege`
--

LOCK TABLES `privilege` WRITE;
/*!40000 ALTER TABLE `privilege` DISABLE KEYS */;
INSERT INTO `privilege` VALUES (1,'/queries/',1),(2,'/reports/stat_teacher/',1),(3,'/insert/add/',1),(4,'/schedule/',2),(5,'/insert/add/',2),(7,'/',3),(8,'/reports/',1),(9,'/insert/',1),(10,'/insert/',2),(11,'/reports/',1);
/*!40000 ALTER TABLE `privilege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `idproject` int NOT NULL,
  `date` varchar(45) DEFAULT NULL,
  `mark` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `idstudent` int DEFAULT NULL,
  `idteacher` int DEFAULT NULL,
  `idreport` int DEFAULT NULL,
  `idschedule` int DEFAULT NULL,
  PRIMARY KEY (`idproject`),
  KEY `a_idx` (`idreport`),
  KEY `b_idx` (`idschedule`),
  KEY `c_idx` (`idteacher`),
  KEY `d_idx` (`idstudent`),
  CONSTRAINT `a` FOREIGN KEY (`idreport`) REFERENCES `report` (`idreport`),
  CONSTRAINT `b` FOREIGN KEY (`idschedule`) REFERENCES `schedule` (`idschedule`),
  CONSTRAINT `c` FOREIGN KEY (`idteacher`) REFERENCES `teacher` (`idteacher`),
  CONSTRAINT `d` FOREIGN KEY (`idstudent`) REFERENCES `student` (`idstudent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'2020-10-10','4','Философия',1,1,NULL,1),(2,'2021-05-05','3','Математика',1,2,NULL,4),(3,'2021','2','Англ',1,1,NULL,NULL),(4,'2022','5','Прикмех',3,5,NULL,NULL),(5,'2021-03','4','Сапр',4,3,NULL,5),(6,'2021-09-04','3','Программирование',2,4,NULL,NULL);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `idreport` int NOT NULL,
  `mark` varchar(45) DEFAULT NULL,
  `idschedule` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idreport`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (1,'5','1');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `idrole` int NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idrole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'decan'),(2,'zamdecan'),(3,'student');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `idschedule` int NOT NULL,
  `classroom` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `idcommision` varchar(45) DEFAULT NULL,
  `isused` int DEFAULT NULL,
  PRIMARY KEY (`idschedule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1,'292','2020','1',1),(4,'54','2021-09-11','3',1),(5,'9','2021','2',1),(6,'78','2021-04-31','1',0);
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` int NOT NULL,
  `group` int DEFAULT NULL,
  `record_book` varchar(45) DEFAULT NULL,
  `fio` varchar(45) DEFAULT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idstudent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,54,NULL,'Петров Е.М','2010-08-01'),(2,54,NULL,'Кучин П.А','2000-01-01'),(3,53,NULL,'Варламов С.Ф','2001-04-10'),(4,52,NULL,'Навальный А.А','2003-09-09'),(5,51,NULL,'Навальная Ю. Б','2002-02-02');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `idteacher` int NOT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  `employment` date DEFAULT NULL,
  `dismissal` date DEFAULT NULL,
  PRIMARY KEY (`idteacher`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,NULL,'Головач','РК6','2020-10-10','2020-11-11'),(2,NULL,'Яшин','РК6','2020-11-11','2020-12-12'),(3,NULL,'Сабуров','РК9','2020-12-12','2021-01-01'),(4,NULL,'Щербаков','РК9','2021-01-01',NULL),(5,'1985-10-10','Пупкин','РК5','2018-10-10',NULL),(6,NULL,'Васькин','РК5','2019-11-11',NULL),(7,'1991-01-02','Петров','РК2','2017-02-02','2019-09-09'),(8,NULL,'Долгополов','РК2','2021-01-02',NULL);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `idrole` int DEFAULT NULL,
  PRIMARY KEY (`iduser`),
  KEY `idrole_idx` (`idrole`),
  CONSTRAINT `idrole` FOREIGN KEY (`idrole`) REFERENCES `role` (`idrole`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'a','a',1),(2,'b','b',2),(3,'c','c',3),(4,'ad','ad',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-26 17:20:18
