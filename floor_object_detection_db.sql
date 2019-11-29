-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2019 at 04:31 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `floor_object_detection_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_details`
--

CREATE TABLE `admin_details` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `pass_view` varchar(255) DEFAULT NULL,
  `admin_email` varchar(255) DEFAULT NULL,
  `admin_image` varchar(255) DEFAULT NULL,
  `status` enum('1','0') NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_details`
--

INSERT INTO `admin_details` (`id`, `username`, `password`, `pass_view`, `admin_email`, `admin_image`, `status`) VALUES
(1, 'admin', 'e10adc3949ba59abbe56e057f20f883e', '123456', 'jwm@gmail.com', NULL, '1'),
(2, 'tapan', 'e10adc3949ba59abbe56e057f20f883e', '123456', 'tapanb@mridayaitservices.com', 'logo9.png', '1');

-- --------------------------------------------------------

--
-- Table structure for table `matterport_tags`
--

CREATE TABLE `matterport_tags` (
  `id` int(11) NOT NULL,
  `tag_label` varchar(255) DEFAULT NULL,
  `tag_description` text,
  `manufacturer` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `purchased` date DEFAULT NULL,
  `last_refill` date DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `repair_cost` double(10,2) DEFAULT NULL,
  `replace_cost` double(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `matterport_tags`
--

INSERT INTO `matterport_tags` (`id`, `tag_label`, `tag_description`, `manufacturer`, `model`, `purchased`, `last_refill`, `image`, `repair_cost`, `replace_cost`) VALUES
(1, '11176 - Microware', 'Manufacturer: Sunbeam\r\nModel: 67DCVVH \r\nPurchased: 12/08/2017\r\nLast Repair: 07/07/2018', 'Sunbeam', '67DCVVH ', '2017-12-08', '2018-07-07', NULL, 180.00, 286.00),
(2, '12976 - Refrigerator', 'Manufacturer: LG\r\nModel: RRG667 \r\nPurchased: 12/08/2017\r\nLast Repair: 07/07/2018', 'LG', 'RRG667 ', '2017-12-08', '2018-07-07', NULL, 860.00, 2186.00),
(3, '12120 – Light Fixture', 'Manufacturer: McAllen\r\nModel: 112667 \r\nPurchased: 12/08/2017\r\nLast Repair: 07/07/2018', NULL, NULL, '2017-12-08', '2018-07-07', NULL, 172.00, 138.00),
(4, '12122– Dishwasher', 'Manufacturer: Samsung\r\nModel: BB5TY\r\nPurchased: 12/08/2017\r\nLast Repair: NA', NULL, NULL, '2017-12-08', NULL, NULL, 220.00, 468.00),
(5, '87765 – Kitchen Faucet', 'Manufacturer: Blanco\r\nModel: 66YT7 \r\nPurchased: 11/07/2017\r\nLast Repair: 04/21/2018', NULL, NULL, '2017-11-07', '2018-08-21', NULL, 128.00, 208.00),
(6, '12120 – M&Ms', 'Manufacturer: M&Ms\r\nModel: NA \r\nPurchased: 08/08/2019\r\nLast Refill: 10/07/2019', NULL, NULL, '2019-08-08', '2019-10-07', NULL, 0.00, 6.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_details`
--
ALTER TABLE `admin_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matterport_tags`
--
ALTER TABLE `matterport_tags`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_details`
--
ALTER TABLE `admin_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `matterport_tags`
--
ALTER TABLE `matterport_tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
