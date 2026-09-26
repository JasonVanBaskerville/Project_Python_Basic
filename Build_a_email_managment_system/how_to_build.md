## Email Management System

A simple program that simulates an email system using **Object-Oriented Programming (OOP)** concepts.

### Concepts Used

* **`User`** — represents a user who can send, read, and delete emails.
* **`Email`** — stores email information such as sender, recipient, subject, message body, timestamp, and read/unread status.
* **`Inbox`** — manages a collection of emails for each user, including receiving, displaying, reading, and deleting emails.
* **Object Relationship** — each `User` has one `Inbox`, while the `Inbox` stores multiple `Email` objects.
* **Encapsulation** — each class has attributes and methods responsible for managing its own data and behavior.
* **`__str__()`** — used to display concise email information when the inbox is viewed.

### Program Workflow

1. Create two users: **Tory** and **Ramy**.
2. Tory sends an email to Ramy.
3. Ramy replies to Tory's email.
4. Ramy views the inbox.
5. Ramy reads the first email.
6. The email's status changes to **Read**.
7. Ramy deletes the email.
8. The inbox is displayed again after the email is deleted.

### Objective

This project was created as an exercise to understand **classes, objects, methods, constructors, object relationships, lists of objects, and the `__str__()` method** in Python.