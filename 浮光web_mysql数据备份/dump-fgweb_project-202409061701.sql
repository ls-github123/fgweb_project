-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 182.92.217.5    Database: fgweb_project
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 轮播广告',6,'add_bannermodel'),(22,'Can change 轮播广告',6,'change_bannermodel'),(23,'Can delete 轮播广告',6,'delete_bannermodel'),(24,'Can view 轮播广告',6,'view_bannermodel'),(25,'Can add 导航菜单',7,'add_navmodel'),(26,'Can change 导航菜单',7,'change_navmodel'),(27,'Can delete 导航菜单',7,'delete_navmodel'),(28,'Can view 导航菜单',7,'view_navmodel'),(29,'Can add 用户表',8,'add_usersmodel'),(30,'Can change 用户表',8,'change_usersmodel'),(31,'Can delete 用户表',8,'delete_usersmodel'),(32,'Can view 用户表',8,'view_usersmodel'),(33,'Can add course direction model',9,'add_coursedirectionmodel'),(34,'Can change course direction model',9,'change_coursedirectionmodel'),(35,'Can delete course direction model',9,'delete_coursedirectionmodel'),(36,'Can view course direction model',9,'view_coursedirectionmodel'),(37,'Can add teacher model',10,'add_teachermodel'),(38,'Can change teacher model',10,'change_teachermodel'),(39,'Can delete teacher model',10,'delete_teachermodel'),(40,'Can view teacher model',10,'view_teachermodel'),(41,'Can add course category model',11,'add_coursecategorymodel'),(42,'Can change course category model',11,'change_coursecategorymodel'),(43,'Can delete course category model',11,'delete_coursecategorymodel'),(44,'Can view course category model',11,'view_coursecategorymodel'),(45,'Can add course model',12,'add_coursemodel'),(46,'Can change course model',12,'change_coursemodel'),(47,'Can delete course model',12,'delete_coursemodel'),(48,'Can view course model',12,'view_coursemodel'),(49,'Can add activate model',13,'add_activatemodel'),(50,'Can change activate model',13,'change_activatemodel'),(51,'Can delete activate model',13,'delete_activatemodel'),(52,'Can view activate model',13,'view_activatemodel'),(53,'Can add discount model',14,'add_discountmodel'),(54,'Can change discount model',14,'change_discountmodel'),(55,'Can delete discount model',14,'delete_discountmodel'),(56,'Can view discount model',14,'view_discountmodel'),(57,'Can add discount type model',15,'add_discounttypemodel'),(58,'Can change discount type model',15,'change_discounttypemodel'),(59,'Can delete discount type model',15,'delete_discounttypemodel'),(60,'Can view discount type model',15,'view_discounttypemodel'),(61,'Can add course activate model',16,'add_courseactivatemodel'),(62,'Can change course activate model',16,'change_courseactivatemodel'),(63,'Can delete course activate model',16,'delete_courseactivatemodel'),(64,'Can view course activate model',16,'view_courseactivatemodel'),(65,'Can add course chapter model',17,'add_coursechaptermodel'),(66,'Can change course chapter model',17,'change_coursechaptermodel'),(67,'Can delete course chapter model',17,'delete_coursechaptermodel'),(68,'Can view course chapter model',17,'view_coursechaptermodel'),(69,'Can add course lessons model',18,'add_courselessonsmodel'),(70,'Can change course lessons model',18,'change_courselessonsmodel'),(71,'Can delete course lessons model',18,'delete_courselessonsmodel'),(72,'Can view course lessons model',18,'view_courselessonsmodel'),(73,'Can add coupon models',19,'add_couponmodels'),(74,'Can change coupon models',19,'change_couponmodels'),(75,'Can delete coupon models',19,'delete_couponmodels'),(76,'Can view coupon models',19,'view_couponmodels'),(77,'Can add coupon log model',20,'add_couponlogmodel'),(78,'Can change coupon log model',20,'change_couponlogmodel'),(79,'Can delete coupon log model',20,'delete_couponlogmodel'),(80,'Can view coupon log model',20,'view_couponlogmodel'),(81,'Can add coupon course model',21,'add_couponcoursemodel'),(82,'Can change coupon course model',21,'change_couponcoursemodel'),(83,'Can delete coupon course model',21,'delete_couponcoursemodel'),(84,'Can view coupon course model',21,'view_couponcoursemodel'),(85,'Can add coupon course direction model',22,'add_couponcoursedirectionmodel'),(86,'Can change coupon course direction model',22,'change_couponcoursedirectionmodel'),(87,'Can delete coupon course direction model',22,'delete_couponcoursedirectionmodel'),(88,'Can view coupon course direction model',22,'view_couponcoursedirectionmodel'),(89,'Can add coupon course category model',23,'add_couponcoursecategorymodel'),(90,'Can change coupon course category model',23,'change_couponcoursecategorymodel'),(91,'Can delete coupon course category model',23,'delete_couponcoursecategorymodel'),(92,'Can view coupon course category model',23,'view_couponcoursecategorymodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_fg_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_fg_users_id` FOREIGN KEY (`user_id`) REFERENCES `fg_users` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-09-06 08:51:39.530790','1','张老师',2,'[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]',10,2),(2,'2024-09-06 08:51:55.427743','2','李老师',2,'[{\"changed\": {\"fields\": [\"\\u8bb2\\u5e08\\u5934\\u50cf\"]}}]',10,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(23,'coupon','couponcoursecategorymodel'),(22,'coupon','couponcoursedirectionmodel'),(21,'coupon','couponcoursemodel'),(20,'coupon','couponlogmodel'),(19,'coupon','couponmodels'),(13,'course','activatemodel'),(16,'course','courseactivatemodel'),(11,'course','coursecategorymodel'),(17,'course','coursechaptermodel'),(9,'course','coursedirectionmodel'),(18,'course','courselessonsmodel'),(12,'course','coursemodel'),(14,'course','discountmodel'),(15,'course','discounttypemodel'),(10,'course','teachermodel'),(6,'home','bannermodel'),(7,'home','navmodel'),(5,'sessions','session'),(8,'users','usersmodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-06 08:20:53.716420'),(2,'contenttypes','0002_remove_content_type_name','2024-09-06 08:20:53.841533'),(3,'auth','0001_initial','2024-09-06 08:20:54.365322'),(4,'auth','0002_alter_permission_name_max_length','2024-09-06 08:20:54.464298'),(5,'auth','0003_alter_user_email_max_length','2024-09-06 08:20:54.480436'),(6,'auth','0004_alter_user_username_opts','2024-09-06 08:20:54.497172'),(7,'auth','0005_alter_user_last_login_null','2024-09-06 08:20:54.513410'),(8,'auth','0006_require_contenttypes_0002','2024-09-06 08:20:54.519785'),(9,'auth','0007_alter_validators_add_error_messages','2024-09-06 08:20:54.543522'),(10,'auth','0008_alter_user_username_max_length','2024-09-06 08:20:54.555510'),(11,'auth','0009_alter_user_last_name_max_length','2024-09-06 08:20:54.569688'),(12,'auth','0010_alter_group_name_max_length','2024-09-06 08:20:54.605269'),(13,'auth','0011_update_proxy_permissions','2024-09-06 08:20:54.644536'),(14,'auth','0012_alter_user_first_name_max_length','2024-09-06 08:20:54.656108'),(15,'users','0001_initial','2024-09-06 08:20:55.251376'),(16,'admin','0001_initial','2024-09-06 08:20:55.499713'),(17,'admin','0002_logentry_remove_auto_add','2024-09-06 08:20:55.515356'),(18,'admin','0003_logentry_add_action_flag_choices','2024-09-06 08:20:55.540525'),(19,'course','0001_initial','2024-09-06 08:20:56.085106'),(20,'course','0002_alter_coursecategorymodel_remark_and_more','2024-09-06 08:20:56.116271'),(21,'course','0003_alter_coursemodel_status_alter_teachermodel_avatar_and_more','2024-09-06 08:20:56.147557'),(22,'course','0004_activatemodel_discountmodel_discounttypemodel_and_more','2024-09-06 08:20:56.674391'),(23,'course','0005_alter_activatemodel_end_time_and_more','2024-09-06 08:20:56.689972'),(24,'course','0006_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.013545'),(25,'course','0007_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.053151'),(26,'course','0008_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.083634'),(27,'course','0009_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.118418'),(28,'coupon','0001_initial','2024-09-06 08:20:57.742189'),(29,'coupon','0002_alter_couponlogmodel_use_status_and_more','2024-09-06 08:20:57.757861'),(30,'coupon','0003_alter_couponlogmodel_use_status','2024-09-06 08:20:57.790925'),(31,'course','0010_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.815509'),(32,'course','0011_alter_activatemodel_end_time_and_more','2024-09-06 08:20:57.916852'),(33,'home','0001_initial','2024-09-06 08:20:58.080566'),(34,'home','0002_alter_navmodel_postion','2024-09-06 08:20:58.093647'),(35,'home','0003_alter_navmodel_postion','2024-09-06 08:20:58.113021'),(36,'home','0004_alter_navmodel_postion','2024-09-06 08:20:58.125662'),(37,'home','0005_alter_navmodel_postion','2024-09-06 08:20:58.137368'),(38,'home','0006_alter_navmodel_postion','2024-09-06 08:20:58.161000'),(39,'home','0007_alter_navmodel_postion','2024-09-06 08:20:58.176247'),(40,'sessions','0001_initial','2024-09-06 08:20:58.264466');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_activate`
--

DROP TABLE IF EXISTS `fg_activate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_activate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `description` longtext,
  `remark` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_activate_name_fe2eceec` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_activate`
--

LOCK TABLES `fg_activate` WRITE;
/*!40000 ALTER TABLE `fg_activate` DISABLE KEYS */;
INSERT INTO `fg_activate` VALUES (1,'浮光学城-5周年庆',1,1,0,'2022-02-17 10:42:54.340893','2022-02-17 10:42:54.340933','2022-02-17 00:00:00.000000','2021-08-01 00:00:00.000000','<p>5周年庆，各种活动促销内容展示图片</p>','负责人：组织：外勤：');
/*!40000 ALTER TABLE `fg_activate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_banner`
--

DROP TABLE IF EXISTS `fg_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_banner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `link` varchar(300) NOT NULL,
  `note` varchar(100) NOT NULL,
  `is_http` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_banner_name_20b4855c` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_banner`
--

LOCK TABLES `fg_banner` WRITE;
/*!40000 ALTER TABLE `fg_banner` DISABLE KEYS */;
INSERT INTO `fg_banner` VALUES (1,'1',1,1,0,'2021-07-15 03:39:49.859000','2021-07-15 03:39:51.437000','banner/2022/1.jpg','/project','暂无',0),(2,'2',1,1,0,'2021-07-15 03:39:49.859000','2021-07-15 03:39:51.437000','banner/2022/2.jpg','/project','暂无',0),(3,'3',1,1,0,'2021-07-15 03:39:49.859000','2021-07-15 03:39:51.437000','banner/2022/3.jpg','/project','暂无',0),(4,'4',1,1,0,'2021-07-15 03:39:49.859000','2021-07-15 03:39:51.437000','banner/2022/4.jpg','/project','暂无',0),(5,'5',1,1,0,'2021-07-15 03:39:49.859000','2021-07-15 03:39:51.437000','banner/2022/5.jpg','/project','暂无',0);
/*!40000 ALTER TABLE `fg_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_coupon`
--

DROP TABLE IF EXISTS `fg_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_coupon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `discount` smallint NOT NULL,
  `coupon_type` smallint NOT NULL,
  `get_type` smallint NOT NULL,
  `total` int DEFAULT NULL,
  `has_total` int DEFAULT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `condition` int NOT NULL,
  `per_limit` smallint NOT NULL,
  `sale` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_coupon_name_a114d32e` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_coupon`
--

LOCK TABLES `fg_coupon` WRITE;
/*!40000 ALTER TABLE `fg_coupon` DISABLE KEYS */;
INSERT INTO `fg_coupon` VALUES (1,'30元通用优惠券',1,1,0,'2022-05-04 10:35:40.569417','2022-06-30 10:25:00.353212',1,0,0,10000,10000,'2022-05-04 10:35:00.000000','2023-01-02 10:35:00.000000',100,1,'-30'),(2,'前端学习通用优惠券',1,1,0,'2022-05-04 10:36:58.401527','2022-05-04 10:36:58.401556',1,1,0,100,100,'2022-05-04 10:36:00.000000','2022-08-04 10:36:00.000000',0,1,'-50'),(3,'Typescript课程专用券',1,1,0,'2022-05-04 10:38:36.134581','2022-05-04 10:38:36.134624',2,3,0,1000,1000,'2022-05-04 10:38:00.000000','2022-08-04 10:38:00.000000',0,1,'*0.88'),(4,'python七夕专用券',1,1,0,'2022-05-04 10:40:08.022904','2022-06-30 10:25:46.949197',1,2,1,200,200,'2022-05-04 10:39:00.000000','2022-11-15 10:39:00.000000',0,1,'-99'),(5,'算法学习优惠券',1,1,0,'2021-08-05 10:05:07.837008','2022-06-30 10:26:12.133812',2,2,0,1000,1000,'2022-08-05 10:04:00.000000','2022-12-25 10:04:00.000000',200,1,'*0.85');
/*!40000 ALTER TABLE `fg_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_coupon_course`
--

DROP TABLE IF EXISTS `fg_coupon_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_coupon_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `course_id` bigint NOT NULL,
  `coupon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_coupon_course_course_id_c4e1e5e2` (`course_id`),
  KEY `fg_coupon_course_coupon_id_7dc23ac9` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_coupon_course`
--

LOCK TABLES `fg_coupon_course` WRITE;
/*!40000 ALTER TABLE `fg_coupon_course` DISABLE KEYS */;
INSERT INTO `fg_coupon_course` VALUES (1,'2022-05-04 10:38:36.140929',1,3),(2,'2022-05-04 10:38:36.143166',2,3);
/*!40000 ALTER TABLE `fg_coupon_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_coupon_course_category`
--

DROP TABLE IF EXISTS `fg_coupon_course_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_coupon_course_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `coupon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_coupon_course_category_category_id_af02f840` (`category_id`),
  KEY `fg_coupon_course_category_coupon_id_6570d53b` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_coupon_course_category`
--

LOCK TABLES `fg_coupon_course_category` WRITE;
/*!40000 ALTER TABLE `fg_coupon_course_category` DISABLE KEYS */;
INSERT INTO `fg_coupon_course_category` VALUES (1,'2022-05-04 10:40:08.029505',20,4),(2,'2022-05-04 10:40:08.042891',21,4),(3,'2021-08-05 10:05:07.966221',33,5);
/*!40000 ALTER TABLE `fg_coupon_course_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_coupon_course_direction`
--

DROP TABLE IF EXISTS `fg_coupon_course_direction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_coupon_course_direction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `direction_id` bigint NOT NULL,
  `coupon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_coupon_course_direction_direction_id_a10acfa9` (`direction_id`),
  KEY `fg_coupon_course_direction_coupon_id_21165d25` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_coupon_course_direction`
--

LOCK TABLES `fg_coupon_course_direction` WRITE;
/*!40000 ALTER TABLE `fg_coupon_course_direction` DISABLE KEYS */;
INSERT INTO `fg_coupon_course_direction` VALUES (1,'2022-05-04 10:36:58.414461',1,2);
/*!40000 ALTER TABLE `fg_coupon_course_direction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_coupon_log`
--

DROP TABLE IF EXISTS `fg_coupon_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_coupon_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `use_time` datetime(6) DEFAULT NULL,
  `use_status` smallint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `coupon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_coupon_log_name_b73a795f` (`name`),
  KEY `fg_coupon_log_user_id_353ae856` (`user_id`),
  KEY `fg_coupon_log_coupon_id_5327188f` (`coupon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_coupon_log`
--

LOCK TABLES `fg_coupon_log` WRITE;
/*!40000 ALTER TABLE `fg_coupon_log` DISABLE KEYS */;
INSERT INTO `fg_coupon_log` VALUES (5,'30元通用优惠券222',1,1,0,'2022-05-04 12:00:25.051976','2022-06-30 10:25:17.681298',NULL,0,1,1),(8,'前端学习通用优惠券',1,1,0,'2022-05-04 12:03:24.331024','2022-06-30 10:22:45.834401',NULL,0,1,2),(9,'Typescript课程专用券',1,1,0,'2022-05-04 12:03:31.692397','2022-06-30 10:23:41.492205',NULL,0,1,3),(10,'python七夕专用券',1,1,0,'2022-05-04 12:03:38.225438','2022-06-30 10:25:49.797318',NULL,0,1,4),(11,'前端学习通用优惠券',1,1,0,'2022-05-04 12:09:25.406437','2022-06-30 10:23:55.832262',NULL,0,1,2),(12,'算法学习优惠券',1,1,0,'2021-08-05 10:06:06.036230','2022-06-30 10:26:20.723668',NULL,0,1,5);
/*!40000 ALTER TABLE `fg_coupon_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_activate_price`
--

DROP TABLE IF EXISTS `fg_course_activate_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_activate_price` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `activate_id` bigint NOT NULL,
  `course_id` bigint NOT NULL,
  `discount_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_course_activate_price_name_6abdebf7` (`name`),
  KEY `fg_course_activate_price_activate_id_f61330d1` (`activate_id`),
  KEY `fg_course_activate_price_course_id_48b6802c` (`course_id`),
  KEY `fg_course_activate_price_discount_id_8c21127c` (`discount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_activate_price`
--

LOCK TABLES `fg_course_activate_price` WRITE;
/*!40000 ALTER TABLE `fg_course_activate_price` DISABLE KEYS */;
/*!40000 ALTER TABLE `fg_course_activate_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_category`
--

DROP TABLE IF EXISTS `fg_course_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(200) NOT NULL,
  `remark` longtext,
  `direction_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fg_course_category_direction_id_612d2d0e_fk_fg_course` (`direction_id`),
  CONSTRAINT `fg_course_category_direction_id_612d2d0e_fk_fg_course` FOREIGN KEY (`direction_id`) REFERENCES `fg_course_direction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=415 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_category`
--

LOCK TABLES `fg_course_category` WRITE;
/*!40000 ALTER TABLE `fg_course_category` DISABLE KEYS */;
INSERT INTO `fg_course_category` VALUES (346,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Vue.js','',1),(347,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Typescript','',1),(348,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','React.js','',1),(349,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','HTML','',1),(350,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','JavaScript','',1),(351,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Angular','',1),(352,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Node.js','',1),(353,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','WebApp','',1),(354,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','小程序','',1),(355,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','前端工具','',1),(356,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','HTML/CSS','',1),(357,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Html5','',1),(358,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','CSS3','',1),(359,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Java','',2),(360,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','SpringBoot','',2),(361,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Spring Cloud','',2),(362,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','SSM','',2),(363,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','PHP','',2),(364,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','.net','',2),(365,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Python','',2),(366,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','爬虫','',2),(367,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Django','',2),(368,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Flask','',2),(369,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Go','',2),(370,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','C','',2),(371,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','C++','',2),(372,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','C#','',2),(373,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Flutter','',3),(374,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Android','',3),(375,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','iOS','',3),(376,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','React native','',3),(377,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','计算机网络','',4),(378,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','算法与数据结构','',4),(379,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','数学','',4),(380,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','微服务','',5),(381,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','机器学习','',5),(382,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','深度学习','',5),(383,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','计算机视觉','',5),(384,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','自然语言处理','',5),(385,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','数据分析&挖掘','',5),(386,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','大数据','',6),(387,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Hadoop','',6),(388,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Spark','',6),(389,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Hbase','',6),(390,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Flink','',6),(391,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Storm','',6),(392,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','阿里云','',7),(393,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','容器','',7),(394,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Docker','',7),(395,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Kubernetes','',7),(396,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','运维','',8),(397,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','自动化运维','',8),(398,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','中间件','',8),(399,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Linux','',8),(400,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','测试','',9),(401,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','功能测试','',9),(402,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','性能测试','',9),(403,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','自动化测试','',9),(404,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','接口测试','',9),(405,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','MySQL','',10),(406,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Redis','',10),(407,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','MongoDB','',10),(408,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','设计基础','',11),(409,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','设计工具','',11),(410,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','APPUI设计','',11),(411,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','Unity 3D','',13),(412,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','cocos creator','',13),(413,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','求职面试','',14),(414,1,1,0,'2021-07-22 08:00:19.366304','2021-07-22 08:00:19.367343','leetcode','',14);
/*!40000 ALTER TABLE `fg_course_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_chapter`
--

DROP TABLE IF EXISTS `fg_course_chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_chapter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint NOT NULL,
  `summary` longtext,
  `pub_date` date NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_course_chapter_name_4bf01f43` (`name`),
  KEY `fg_course_chapter_course_id_62bddd8f` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_chapter`
--

LOCK TABLES `fg_course_chapter` WRITE;
/*!40000 ALTER TABLE `fg_course_chapter` DISABLE KEYS */;
INSERT INTO `fg_course_chapter` VALUES (1,'Typescript快速入门',1,0,'2022-03-21 05:39:39.925451','2022-03-21 05:39:39.925775',1,'<p>Typescript快速入门的相关概念以及基本安装和基本使用</p>','2022-03-21',1);
/*!40000 ALTER TABLE `fg_course_chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_direction`
--

DROP TABLE IF EXISTS `fg_course_direction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_direction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `remark` longtext,
  `recomment_home_hot` tinyint(1) NOT NULL,
  `recomment_home_top` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_direction`
--

LOCK TABLES `fg_course_direction` WRITE;
/*!40000 ALTER TABLE `fg_course_direction` DISABLE KEYS */;
INSERT INTO `fg_course_direction` VALUES (1,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','前端开发','',1,1),(2,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','后端开发','',1,1),(3,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','移动开发','',1,1),(4,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','计算机基础','',1,1),(5,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','前沿技术','',1,1),(6,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','云计算','',1,1),(7,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','大数据','',1,1),(8,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','运维','',1,1),(9,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','测试','',1,1),(10,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','数据库','',1,1),(11,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','UI设计','',1,1),(12,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','多媒体','',1,1),(13,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','游戏','',1,1),(14,1,1,0,'2021-07-22 05:42:01.290060','2021-07-22 05:42:01.290088','求职面试','',1,1);
/*!40000 ALTER TABLE `fg_course_direction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_info`
--

DROP TABLE IF EXISTS `fg_course_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_info` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `course_cover` varchar(100) DEFAULT NULL,
  `course_video` varchar(100) DEFAULT NULL,
  `course_type` smallint NOT NULL,
  `level` smallint NOT NULL,
  `description` longtext,
  `status` smallint NOT NULL,
  `pub_date` date NOT NULL,
  `period` int NOT NULL,
  `attachment_path` varchar(300) DEFAULT NULL,
  `attachment_link` varchar(300) DEFAULT NULL,
  `students` int NOT NULL,
  `lessons` int NOT NULL,
  `pub_lessons` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `credit` int DEFAULT NULL,
  `recomment_home_hot` tinyint(1) NOT NULL,
  `recomment_home_top` tinyint(1) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `direction_id` bigint DEFAULT NULL,
  `teacher_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_course_info_teacher_id_cd3286b1_fk_fg_teacher_id` (`teacher_id`),
  KEY `fg_course_info_name_29329021` (`name`),
  KEY `fg_course_info_category_id_7b063318` (`category_id`),
  KEY `fg_course_info_direction_id_f6a1eac2` (`direction_id`),
  CONSTRAINT `fg_course_info_teacher_id_cd3286b1_fk_fg_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `fg_teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_info`
--

LOCK TABLES `fg_course_info` WRITE;
/*!40000 ALTER TABLE `fg_course_info` DISABLE KEYS */;
INSERT INTO `fg_course_info` VALUES (1,'7天Typescript从入门到放弃',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-10.png','',0,0,'<p>7天Typescript从入门到放弃</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,1100,70,15,800.00,NULL,0,0,2,1,1),(2,'3天Typescript精修',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-9.png','',0,0,'<p>3天Typescript精修</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,9704,100,100,998.00,NULL,1,0,2,1,2),(3,'3天学会Vue基础',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-8.png','',0,0,'<p>3天学会Vue基础</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,988,130,54,500.00,NULL,1,0,1,1,2),(4,'算法与数据结构体系课',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-7.png','',0,0,'<p>算法与数据结构体系课</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,1303,150,50,998.00,NULL,0,1,33,4,4),(5,'python基础入门',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-6.png','',0,0,'<p>python基础入门</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,4302,140,30,100.00,NULL,0,1,20,2,4),(6,'javascript进阶',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-5.png','',0,0,'<p>javascript进阶</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,1125,180,100,1750.00,NULL,1,0,5,1,3),(7,'爬虫进阶之逆向工程',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-4.png','',0,0,'<p>爬虫进阶之逆向工程</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,223,145,55,400.00,NULL,0,0,21,2,3),(8,'Kubernetes 入门到进阶实战',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-3.png','',0,0,'<p>Kubernetes 入门到进阶实战</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,6074,70,20,500.00,NULL,1,0,50,7,3),(9,'Android 应用程序构建实战',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-2.png','',0,0,'<p>Android 应用程序构建实战</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,1059,110,50,550.00,NULL,0,0,29,3,1),(10,'Kotlin从入门到精通',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-1.png','',0,0,'<p>Kotlin从入门到精通</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,870,120,0,500.00,NULL,1,0,29,3,1),(11,'深度学习之神经网络',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-11.png','',0,0,'<p>深度学习之神经网络</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,6002,115,70,80.00,NULL,1,0,37,5,1),(12,'OpenCV入门到进阶',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-12.png','',0,0,'<p>OpenCV入门到进阶</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,1029,100,70,390.00,NULL,0,1,38,5,2),(13,'Go容器化微服务系统实战',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-13.png','',0,0,'<p>Go容器化微服务系统实战</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,24202,65,65,399.00,NULL,0,0,35,5,1),(14,'RabbitMQ精讲',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-14.png','',0,0,'<p>RabbitMQ精讲</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,980,100,100,710.00,NULL,0,0,53,8,4),(15,'TensorFlow基础',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-15.png','',0,0,'<p>RabbitMQ精讲</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,670,220,100,1590.00,NULL,0,1,36,5,2),(16,'ZooKeeper分布式架构搭建',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-16.png','',0,0,'<p>ZooKeeper分布式架构搭建</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,90,88,35,40.00,NULL,1,0,35,5,3),(17,'高性能MySQL调优',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-17.png','',0,0,'<p>高性能MySQL调优</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,40,300,60,998.00,NULL,1,1,60,10,3),(18,'MySQL事务处理精选',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-18.png','',0,0,'<p>MySQL事务处理精选</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,640,65,30,1000.00,NULL,1,0,60,10,1),(19,'MongoDB入门到进阶',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-19.png','',0,0,'<p>MongoDB入门到进阶</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,11205,86,40,1100.00,NULL,0,1,62,10,3),(20,'Redis入门课程',1,1,0,'2021-07-22 04:35:05.696823','2021-07-22 04:35:05.696871','course/cover/course-20.png','',0,0,'<p>Redis入门课程</p>',0,'2021-07-22',7,'fuguang-celery用法1.zip',NULL,120,100,40,1199.00,NULL,1,1,61,10,2);
/*!40000 ALTER TABLE `fg_course_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_course_lesson`
--

DROP TABLE IF EXISTS `fg_course_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_course_lesson` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `orders` smallint NOT NULL,
  `lesson_type` smallint NOT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `lesson_link` varchar(255) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  `free_trail` tinyint(1) NOT NULL,
  `chapter_id` bigint NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_course_lesson_name_302aaaa9` (`name`),
  KEY `fg_course_lesson_chapter_id_870c3071` (`chapter_id`),
  KEY `fg_course_lesson_course_id_77d7fa17` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_course_lesson`
--

LOCK TABLES `fg_course_lesson` WRITE;
/*!40000 ALTER TABLE `fg_course_lesson` DISABLE KEYS */;
INSERT INTO `fg_course_lesson` VALUES (9,'Typescript的函数声明',1,0,'2022-03-21 05:44:44.347650','2022-03-21 05:44:44.347716',4,2,'4:00','https://fuguangoline.oss-cn-beijing.aliyuncs.com/uploads/course/video/1.mp4','2022-03-21 05:44:44.347764',1,2,1);
/*!40000 ALTER TABLE `fg_course_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_discount`
--

DROP TABLE IF EXISTS `fg_discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_discount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `condition` int NOT NULL,
  `sale` varchar(50) NOT NULL,
  `discount_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_discount_name_ad3974ec` (`name`),
  KEY `fg_discount_discount_type_id_7da0560e` (`discount_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_discount`
--

LOCK TABLES `fg_discount` WRITE;
/*!40000 ALTER TABLE `fg_discount` DISABLE KEYS */;
/*!40000 ALTER TABLE `fg_discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_discount_type`
--

DROP TABLE IF EXISTS `fg_discount_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_discount_type` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `remark` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_discount_type_name_3c89afbe` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_discount_type`
--

LOCK TABLES `fg_discount_type` WRITE;
/*!40000 ALTER TABLE `fg_discount_type` DISABLE KEYS */;
INSERT INTO `fg_discount_type` VALUES (1,'免费',1,1,0,'2022-02-17 10:43:38.546870','2022-02-17 10:43:38.546901',NULL),(2,'折扣',1,1,0,'2022-02-17 10:43:49.161997','2022-02-17 11:19:58.799363',NULL),(3,'减免',1,1,0,'2022-02-17 10:44:05.712935','2022-02-17 11:41:16.504340',NULL),(4,'限时免费',1,1,0,'2022-02-17 10:44:23.053845','2022-02-17 10:44:23.053925',NULL),(5,'限时折扣',1,1,0,'2022-02-17 10:44:31.999352','2022-02-17 10:44:31.999382',NULL),(6,'限时减免',1,1,0,'2022-02-17 10:44:39.100270','2022-02-17 10:44:39.100305',NULL);
/*!40000 ALTER TABLE `fg_discount_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_nav`
--

DROP TABLE IF EXISTS `fg_nav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_nav` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `link` varchar(100) NOT NULL,
  `is_http` tinyint(1) NOT NULL,
  `postion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_nav_name_ba02cba6` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_nav`
--

LOCK TABLES `fg_nav` WRITE;
/*!40000 ALTER TABLE `fg_nav` DISABLE KEYS */;
INSERT INTO `fg_nav` VALUES (1,'免费课',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'0'),(2,'项目课',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/project',0,'0'),(3,'学位课',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/postion',0,'0'),(4,'习题库',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/exam',0,'0'),(5,'浮光在线',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','https://www.com',1,'0'),(6,'企业服务',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(7,'关于我们',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(8,'联系我们',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(9,'商务合作',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(10,'帮助中心',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(11,'意见反馈',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1'),(12,'新手指南',1,1,0,'2022-08-15 01:27:27.350000','2022-08-15 01:27:28.690000','/free',0,'1');
/*!40000 ALTER TABLE `fg_nav` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_teacher`
--

DROP TABLE IF EXISTS `fg_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_teacher` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `orders` int NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `role` smallint NOT NULL,
  `title` varchar(100) NOT NULL,
  `signature` varchar(255) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `brief` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fg_teacher_name_d05e15c9` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_teacher`
--

LOCK TABLES `fg_teacher` WRITE;
/*!40000 ALTER TABLE `fg_teacher` DISABLE KEYS */;
INSERT INTO `fg_teacher` VALUES (1,'张老师',1,1,0,'2021-07-22 04:31:27.741562','2024-09-06 08:51:39.470518',0,'BAT中某某技术总监','xxxxxxxx','avatar/2024/QQ图片20140322191217_8FZ68xW.jpg','<p>2009入行，在IT行业深耕13年，删库无数，行内同行送称号：删库小王子。</p>'),(2,'李老师',1,1,0,'2021-07-22 04:31:27.741562','2024-09-06 08:51:55.394280',0,'BAT中某某技术顾问','xxxxxxxx','avatar/2024/2_zbKy5tA.jpg','<p>百变小王子，各种框架信手拈来。</p>'),(3,'王老师',1,1,0,'2021-07-22 04:31:27.741562','2021-07-22 04:31:27.741708',0,'BAT中某某技术主管','xxxxxxxx','teacher/avatar.jpg','<p>草根站长，专注运维20年。</p>'),(4,'红老师',1,1,0,'2021-07-22 04:31:27.741562','2021-07-22 04:31:27.741708',0,'BAT中某某项目经理','xxxxxxxx','teacher/avatar.jpg','<p>美女讲师，说话好听。</p>');
/*!40000 ALTER TABLE `fg_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_users`
--

DROP TABLE IF EXISTS `fg_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `money` decimal(9,2) NOT NULL,
  `credit` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_users`
--

LOCK TABLES `fg_users` WRITE;
/*!40000 ALTER TABLE `fg_users` DISABLE KEYS */;
INSERT INTO `fg_users` VALUES (1,'pbkdf2_sha256$870000$3acDPJqfNiOoNoAWwEvjXe$RiDm9oM6eow2JfDDoSsHqrGdp60RDY9hCmt7WBcpkfU=',NULL,0,'18795190581','','','',0,1,'2024-09-06 08:45:22.983272','18795190581','avatar/2024/default.jpg','',0.00,0),(2,'pbkdf2_sha256$870000$67SksY3dRaONIfyp3nP8VN$MQhde1dO/5pQwTMmzRbCp+5+c8DJJN3VjrIaawc3Q5E=','2024-09-06 08:50:38.095305',1,'admin','','','lpsserver443@outlook.com',1,1,'2024-09-06 08:50:20.764457','','','',0.00,0);
/*!40000 ALTER TABLE `fg_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_users_groups`
--

DROP TABLE IF EXISTS `fg_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usersmodel_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fg_users_groups_usersmodel_id_group_id_d4366f37_uniq` (`usersmodel_id`,`group_id`),
  KEY `fg_users_groups_group_id_c8251a7c_fk_auth_group_id` (`group_id`),
  CONSTRAINT `fg_users_groups_group_id_c8251a7c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `fg_users_groups_usersmodel_id_dfe206c7_fk_fg_users_id` FOREIGN KEY (`usersmodel_id`) REFERENCES `fg_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_users_groups`
--

LOCK TABLES `fg_users_groups` WRITE;
/*!40000 ALTER TABLE `fg_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `fg_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fg_users_user_permissions`
--

DROP TABLE IF EXISTS `fg_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fg_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usersmodel_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fg_users_user_permission_usersmodel_id_permission_2b74bae6_uniq` (`usersmodel_id`,`permission_id`),
  KEY `fg_users_user_permis_permission_id_cf3040dd_fk_auth_perm` (`permission_id`),
  CONSTRAINT `fg_users_user_permis_permission_id_cf3040dd_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `fg_users_user_permissions_usersmodel_id_e139ba15_fk_fg_users_id` FOREIGN KEY (`usersmodel_id`) REFERENCES `fg_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fg_users_user_permissions`
--

LOCK TABLES `fg_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `fg_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `fg_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'fgweb_project'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-06 17:01:44
