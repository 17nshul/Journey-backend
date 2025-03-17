-- Create the database
CREATE DATABASE IF NOT EXISTS journal_backend;
USE journal_backend;

-- Create the user table
CREATE TABLE IF NOT EXISTS user (
    email VARCHAR(128) PRIMARY KEY,
    password VARCHAR(64) NOT NULL,
    name VARCHAR(32) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the journal_entry table
CREATE TABLE IF NOT EXISTS journal_entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(128),
    entry_text TEXT NOT NULL,
    mood VARCHAR(32),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_email) REFERENCES user(email) ON DELETE CASCADE
);

-- Create the mood_analytics table (optional, for storing mood trends)
CREATE TABLE IF NOT EXISTS mood_analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(128),
    mood VARCHAR(32),
    entry_date DATE,
    FOREIGN KEY (user_email) REFERENCES user(email) ON DELETE CASCADE
);