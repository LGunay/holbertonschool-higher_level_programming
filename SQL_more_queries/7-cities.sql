-- Cities table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id int AUTO_INCREMENT  PRIMARY KEY, state_id int NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
