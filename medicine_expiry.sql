/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - medicine_expiry
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`medicine_expiry` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `medicine_expiry`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`shop_id`,`complaint`,`replay`,`date`) values 
(1,1,1,'good','hai','01-11-2022'),
(2,1,1,'good','ok','2022-11-01 14:23:48');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'amal','amaljith123','user'),
(9,'preethi','preethi@123','shop'),
(10,'hari','medicals','shop');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(65) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`medicine_name`,`description`,`stock`,`price`,`exp_date`,`status`) values 
(1,'meftal fort ','painkiller','100','75','2022-10-31',''),
(2,'astalin25g','skdlashd','150','23','2024-05-06','');

/*Table structure for table `medicine_shop` */

DROP TABLE IF EXISTS `medicine_shop`;

CREATE TABLE `medicine_shop` (
  `medicineshop_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`medicineshop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medicine_shop` */

insert  into `medicine_shop`(`medicineshop_id`,`medicine_id`,`shop_id`) values 
(1,1,1),
(2,2,2);

/*Table structure for table `order_child` */

DROP TABLE IF EXISTS `order_child`;

CREATE TABLE `order_child` (
  `oc_id` int(11) NOT NULL AUTO_INCREMENT,
  `om_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `date` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`oc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `order_child` */

insert  into `order_child`(`oc_id`,`om_id`,`medicine_id`,`quantity`,`price`,`date`) values 
(1,1,1,'2','75','2022-10-27 11:40:45'),
(8,4,1,'7','75','2022-11-01 13:45:57'),
(9,5,1,'1','75','2022-11-01 14:19:43');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `om_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `total` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`om_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `order_master` */

insert  into `order_master`(`om_id`,`user_id`,`shop_id`,`total`,`date`,`status`) values 
(1,1,1,'380','2022-10-27 11:40:45','Dispatched'),
(4,1,1,'525','2022-11-01 13:45:57','paid'),
(5,1,1,'75','2022-11-01 14:19:43','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`user_id`,`shop_id`,`amount`,`date`) values 
(1,1,1,'5000','5-2-2001'),
(2,1,1,'525','2022-11-01 13:49:56'),
(3,1,1,'525','2022-11-01 13:50:14');

/*Table structure for table `purchase_child` */

DROP TABLE IF EXISTS `purchase_child`;

CREATE TABLE `purchase_child` (
  `pc_id` int(11) NOT NULL AUTO_INCREMENT,
  `pm_id` int(11) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `cost_price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `purchase_child` */

insert  into `purchase_child`(`pc_id`,`pm_id`,`medicine_id`,`quantity`,`cost_price`) values 
(1,1,1,'100','70');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `pm_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` int(11) DEFAULT NULL,
  `vendor_name` varchar(50) DEFAULT NULL,
  `total_amt` varchar(50) DEFAULT NULL,
  `purc_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`pm_id`,`shop_id`,`vendor_name`,`total_amt`,`purc_date`) values 
(1,1,'who','7000','2022-10-27 09:31:17');

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `shop_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `shop` */

insert  into `shop`(`shop_id`,`login_id`,`shop_name`,`place`,`phone`,`email`) values 
(1,9,'preethi medicals','thuravoor cherthala','8147886995','preethi@gmail.com'),
(2,10,'medicals','mamalakkandam','7895641235','hari@gmail.com');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,2,'amal','jith','eranakulam','9458662535','amaljith@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
