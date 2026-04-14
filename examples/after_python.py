"""
This module provides functions for user management and email sending.
"""

import smtplib
import sqlite3
from typing import List, Dict

# Constants
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'myapp@gmail.com'
EMAIL_PASSWORD = 'password123'  # Consider using environment variables or a secure storage

def create_connection() -> sqlite3.Connection:
    """
    Creates a connection to the SQLite database.
    
    Returns:
        A connection to the SQLite database.
    """
    return sqlite3.connect('db.sqlite3')

def create_user(username: str, password: str, email: str, send_email: bool) -> bool:
    """
    Creates a new user and sends an email if specified.
    
    Args:
        username: The username of the new user.
        password: The password of the new user.
        email: The email address of the new user.
        send_email: Whether to send an email to the new user.
    
    Returns:
        True if the user was created successfully, False otherwise.
    """
    if user_exists(username):
        print("User exists")
        return False
    
    insert_user(username, password, email)
    
    if send_email:
        send_welcome_email(username, email)
    
    return True

def user_exists(username: str) -> bool:
    """
    Checks if a user with the given username exists.
    
    Args:
        username: The username to check.
    
    Returns:
        True if the user exists, False otherwise.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

def insert_user(username: str, password: str, email: str) -> None:
    """
    Inserts a new user into the database.
    
    Args:
        username: The username of the new user.
        password: The password of the new user.
        email: The email address of the new user.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, email))
    conn.commit()
    conn.close()

def send_welcome_email(username: str, email: str) -> None:
    """
    Sends a welcome email to the given user.
    
    Args:
        username: The username of the user.
        email: The email address of the user.
    """
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = f'Hi {username} welcome!'
        server.sendmail(EMAIL_ADDRESS, email, msg)
        server.quit()
        print("Email sent")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def get_all_users() -> List[Dict[str, str]]:
    """
    Retrieves all users from the database.
    
    Returns:
        A list of dictionaries containing user information.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return [{'user': row[0], 'pass': row[1], 'mail': row[2]} for row in rows]

def delete_user(username: str) -> None:
    """
    Deletes a user from the database.
    
    Args:
        username: The username of the user to delete.
    """
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    conn.close()