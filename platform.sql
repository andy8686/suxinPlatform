/*
初始化数据库文件..
SQLyog Professional v12.09 (64 bit)
MySQL - 8.0.19 : Database - platform
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`platform` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `platform`;

/*Table structure for table `job_execute_log` */

DROP TABLE IF EXISTS `job_execute_log`;

CREATE TABLE `job_execute_log` (
  `id` char(32) DEFAULT NULL,
  `service_id` char(8) DEFAULT NULL,
  `login_id` char(32) DEFAULT NULL,
  `in_param` varchar(4000) DEFAULT NULL,
  `out_param` varchar(4000) DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `end_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `job_execute_log` */

/*Table structure for table `login_log` */

DROP TABLE IF EXISTS `login_log`;

CREATE TABLE `login_log` (
  `id` varchar(32) DEFAULT NULL,
  `user_id` varchar(32) DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `last_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `login_log` */

insert  into `login_log`(`id`,`user_id`,`create_date`,`last_date`) values ('200121bad-4e47-9f09-4b11f7bc2ffd','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:34:20','2020-01-21 21:34:20'),('2001211f9-4ca2-9df3-8b9d4c598198','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:36:42','2020-01-21 21:36:42'),('2001213ac-47f9-b400-a6ce6b730dc7','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:36:48','2020-01-21 21:36:48'),('200121dcb-4904-baa1-bb3d557417ae','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:37:07','2020-01-21 21:37:07'),('200121a60-47f3-b44f-5480e40b661c','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:37:07','2020-01-21 21:37:07'),('200121118-4bd6-b137-ee4686545920','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:37:24','2020-01-21 21:37:24'),('200121255-414c-a7d0-56d9de00b672','2001142ba-424b-9c73-6f91c92c7020','2020-01-21 21:37:34','2020-01-21 21:37:34');

/*Table structure for table `module_tab` */

DROP TABLE IF EXISTS `module_tab`;

CREATE TABLE `module_tab` (
  `sys_id` char(2) NOT NULL,
  `module_id` char(2) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `note` varchar(1024) DEFAULT NULL,
  `id` char(4) GENERATED ALWAYS AS (concat(`sys_id`,`module_id`)) VIRTUAL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `module_tab` */

insert  into `module_tab`(`sys_id`,`module_id`,`name`,`create_date`,`note`,`id`) values ('pf','us','系统用户','2020-01-21 19:00:49',NULL,'pfus'),('pf','m1','模块管理','2020-01-21 19:00:49','模块管理包括系统管理','pfm1'),('pf','m2','系统菜单','2020-01-21 19:00:49',NULL,'pfm2'),('pf','sm','服务管理','2020-01-21 19:00:49','服务管理','pfsm');

/*Table structure for table `service_tab` */

DROP TABLE IF EXISTS `service_tab`;

CREATE TABLE `service_tab` (
  `sys_id` char(2) NOT NULL,
  `module_id` char(2) NOT NULL,
  `service_id` char(4) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `create_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `in_param` varchar(1024) DEFAULT NULL,
  `out_param` varchar(1024) DEFAULT NULL,
  `note` varchar(1024) DEFAULT NULL,
  `id` char(8) GENERATED ALWAYS AS (concat(`sys_id`,`module_id`,`service_id`)) VIRTUAL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `service_tab` */

insert  into `service_tab`(`sys_id`,`module_id`,`service_id`,`name`,`create_date`,`in_param`,`out_param`,`note`,`id`) values ('pf','sm','0001','查询服务','2020-01-21 19:20:42','{\"login_id\":[\">0\",\"str\"] ,\"id\":[\">0\",\"str\"]}','{\"error\":\"值为0:表示成功,其他都是错误\",\"list\":\"返回服务列表[服务ID,服务名,输入参数,返回参数,备注]\"}',NULL,'pfsm0001'),('pf','sm','0002','新增服务','2020-01-21 19:20:42','{\"login_id\":[\">0\",\"str\"],\"sys_id\":[\"==2\",\"str\"],\"module_id\": [\"==2\", \"str\"], \"name\": [\">0\", \"str\"],\"in_param\": [\">6\", \"str\"],\"out_param\": [\">0\", \"str\"],\"note\": [\"==0\", \"str\"]}','{\"error\":\"值为0:表示注册成功,其他都是错误\"}',NULL,'pfsm0002'),('pf','sm','0003','测试模块','2020-01-21 19:20:42','{\"login_id\":[\">0\",\"str\"],\"sys_id\":[\">0\",\"str\"],\"module_id\": [\"==2\", \"str\"], \"name\": [\">6\", \"str\"],\"in_param\": [\">6\", \"str\"],\"out_param\": [\">0\", \"str\"],\"note\": [\"==0\", \"str\"]}','{\"error\":\"值为0:表示注册成功,其他都是错误\"}',NULL,'pfsm0003'),('pf','us','0001','用户登录验证','2020-01-21 19:20:42','{\"phone\":[\"==11\",\"int\",\"用户登陆账号\"] ,\"password\":[\">6\",\"str\",\"用户密码\"]}','{\"error\":\"值为0时表示服务正确,其他都是错误\",\"login_id\":\"用户登录期间的ID\"}',NULL,'pfus0001'),('pf','us','0002','新增用户','2020-01-21 19:20:42','{\"login_id\":[\">0\",\"str\"],\"phone\": [\"==11\", \"int\"], \"password\": [\">6\", \"str\"],\"oldpassword\": [\">6\", \"str\"],\"name\": [\">0\", \"str\"],\"birthday\": [\"==8\", \"dateyyyymmdd\"], \"sex\": [\"==1\", \"str\"],\"email\": [\"==0\", \"dateyyyymmdd\"],\"account\": [\"==0\", \"str\"]}','{\"error\":\"值为0:表示注册成功,其他都是错误\"}',NULL,'pfus0002'),('pf','us','0003','111','2020-01-21 21:15:24','11','112','212','pfus0003');

/*Table structure for table `sys_tab` */

DROP TABLE IF EXISTS `sys_tab`;

CREATE TABLE `sys_tab` (
  `id` char(2) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sys_tab` */

insert  into `sys_tab`(`id`,`name`,`create_date`) values ('pf','平台系统','2019-12-28 18:09:42');

/*Table structure for table `sys_users` */

DROP TABLE IF EXISTS `sys_users`;

CREATE TABLE `sys_users` (
  `id` varchar(32) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `birthday` datetime DEFAULT NULL,
  `sex` char(1) DEFAULT '0',
  `phone` bigint DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `account` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `sys_users` */

insert  into `sys_users`(`id`,`name`,`birthday`,`sex`,`phone`,`email`,`account`,`password`,`create_date`) values ('2001142ba-424b-9c73-6f91c92c7020','zhangsan',NULL,'1',13085000000,'13085000000@qq.com','13085000000','13085000000','2020-01-21 19:30:16');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
