CREATE TABLE `instructors` (
  `instructor_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL
);

CREATE TABLE `courses` (
  `course_id` int PRIMARY KEY AUTO_INCREMENT,
  `course_name` varchar(100) NOT NULL,
  `description` text,
  `start_time` varchar(4) NOT NULL,
  `end_time` varchar(4) NOT NULL,
  `instructor_id` int NOT NULL
);

CREATE TABLE `students` (
  `student_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL
);

CREATE TABLE `enrollments` (
  `enrollment_id` int PRIMARY KEY AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `course_id` int NOT NULL,
  `enrollment_date` datetime DEFAULT (current_timestamp)
);

CREATE UNIQUE INDEX `instructors_index_0` ON `instructors` (`email`);

CREATE INDEX `courses_index_1` ON `courses` (`instructor_id`);

CREATE UNIQUE INDEX `students_index_2` ON `students` (`email`);

CREATE UNIQUE INDEX `enrollments_index_3` ON `enrollments` (`student_id`, `course_id`);

ALTER TABLE `courses` ADD FOREIGN KEY (`instructor_id`) REFERENCES `instructors` (`instructor_id`);

ALTER TABLE `enrollments` ADD FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

ALTER TABLE `enrollments` ADD FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`);
