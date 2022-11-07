-- Create new tables for help
-- jr00t

-- select the database to use
USE graphlinq;

-- drop help table if exists
DROP TABLE IF EXISTS `help`;

-- create help table
CREATE TABLE `help` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`html` TEXT NOT NULL,
	`title` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`id`)
);

-- insert help data
INSERT INTO `graphlinq`.`help` (`html`, `title`) VALUES ('This is the html <b>TEXT</b> to return.', 'Title Here');


-- drop helper table if exists
DROP TABLE IF EXISTS `helper`;

-- create helper table
CREATE TABLE `helper` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`nodetype` VARCHAR(50) NOT NULL UNIQUE,
	`nodehelp` TEXT NOT NULL,
	`nodelink` VARCHAR(150) NOT NULL,
	PRIMARY KEY (`id`)
);
