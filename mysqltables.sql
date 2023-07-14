-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: grocery
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `index` bigint DEFAULT NULL,
  `SrNo` bigint DEFAULT NULL,
  `Itemname` text,
  `Unit Price(Rs.)` bigint DEFAULT NULL,
  `Quantity` bigint DEFAULT NULL,
  `Amount` bigint DEFAULT NULL,
  KEY `ix_bill_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (0,1,'Tetley(contains 10 tea bags)',130,3,390),(1,2,'Tata Tea Premium(500g)',210,1,210),(2,3,'Rice per kg',60,1,60);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `itemno` int NOT NULL,
  `itemname` char(30) NOT NULL,
  PRIMARY KEY (`itemno`,`itemname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Grains and Bread'),(2,'Dairy Products'),(3,'Condiments'),(4,'Cleaning and Washing products'),(5,'Tea/Coffee or Chocolates'),(6,'Stationery Items');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item1`
--

DROP TABLE IF EXISTS `item1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item1` (
  `SrNo` int DEFAULT NULL,
  `products` char(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item1`
--

LOCK TABLES `item1` WRITE;
/*!40000 ALTER TABLE `item1` DISABLE KEYS */;
INSERT INTO `item1` VALUES (1,'Rice per kg',60),(2,'Bread',39),(3,'All-purpose flour per kg',40),(4,'pasta',25),(5,'Oats per kg',75);
/*!40000 ALTER TABLE `item1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item2`
--

DROP TABLE IF EXISTS `item2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item2` (
  `SrNo` int DEFAULT NULL,
  `products` char(32) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item2`
--

LOCK TABLES `item2` WRITE;
/*!40000 ALTER TABLE `item2` DISABLE KEYS */;
INSERT INTO `item2` VALUES (1,'milk(500ml)',23),(2,'Paneer(200g)',82),(3,'Amul Cheese Slices(100g)',71),(4,'Curd(85g)',10),(5,'Butter(100g)',45);
/*!40000 ALTER TABLE `item2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item3`
--

DROP TABLE IF EXISTS `item3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item3` (
  `SrNo` int DEFAULT NULL,
  `products` char(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item3`
--

LOCK TABLES `item3` WRITE;
/*!40000 ALTER TABLE `item3` DISABLE KEYS */;
INSERT INTO `item3` VALUES (1,'Salt(1kg)',20),(2,'Black Pepper(100g)',70),(3,'Herbs & Spices(100g)',85),(4,'Honey(100g)',62),(5,'Vinegar(200g)',45),(6,'Sugar(1kg)',35);
/*!40000 ALTER TABLE `item3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item4`
--

DROP TABLE IF EXISTS `item4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item4` (
  `SrNo` int DEFAULT NULL,
  `products` char(30) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item4`
--

LOCK TABLES `item4` WRITE;
/*!40000 ALTER TABLE `item4` DISABLE KEYS */;
INSERT INTO `item4` VALUES (1,'Dettol Hand Wash(900ml)',141),(2,'Scotch brite Scrub Pad(2pcs)',15),(3,'Ariel Detergent Powder(500g)',100),(4,'Vim Dishwash Bar(125g)',10);
/*!40000 ALTER TABLE `item4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item5`
--

DROP TABLE IF EXISTS `item5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item5` (
  `SrNo` int DEFAULT NULL,
  `products` char(40) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item5`
--

LOCK TABLES `item5` WRITE;
/*!40000 ALTER TABLE `item5` DISABLE KEYS */;
INSERT INTO `item5` VALUES (1,'Tata Tea Premium(500g)',210),(2,'Tetley(contains 10 tea bags)',130),(3,'Red Label Brooke Bond Tea(250g)',113),(4,'BRU Green Label Coffee(200g)',84),(5,'Nescafe Classic Instant Coffee(50 g)',150),(6,'Cadbury Dairy Milk Chocolate Bars(50 g)',40),(7,'Nestle Kitkat Bars(37.3 g)',25),(8,'Cadbury Bournville Dark Chocolate(80 g)',95);
/*!40000 ALTER TABLE `item5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item6`
--

DROP TABLE IF EXISTS `item6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item6` (
  `SrNo` int DEFAULT NULL,
  `products` char(40) DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item6`
--

LOCK TABLES `item6` WRITE;
/*!40000 ALTER TABLE `item6` DISABLE KEYS */;
INSERT INTO `item6` VALUES (1,'Classmate Notebook Single Line 172 pgs',21),(2,'Camlin Exam Geometry Box',120),(3,'Fevicol MR Squeeze Bottle(200 Grams)',75),(4,'Apsara extra dark pencils(10 pencils)',50),(5,'Reynolds Trimax Pen (Blue) - Pack of 2',80),(6,'ETI Cello Tape 1 Inch 65M (2pcs)',80);
/*!40000 ALTER TABLE `item6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `userid` char(30) DEFAULT NULL,
  `pass` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('RADHA','radha'),('RAJ','raj'),('GEETA','geeta'),('SANIA','sania'),('KARAN','karan'),('SAM','sam'),('ANKANA','ankana'),('GEETANJALI','geetanjali'),('MONA','mona');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-30 11:39:57
