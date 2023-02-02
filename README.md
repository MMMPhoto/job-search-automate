# Job Search Automate

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

## Description

Job Search Automate is a Python application that uses regex methods to sort and categorize LinkedIn API data based on keywords, automating a process that otherwise would take significant time and effort. The App uses the unofficial [LinkedIn API](https://github.com/tomquirk/linkedin-api) created by [Tom Quirk](https://github.com/tomquirk) and adds some extra keyword search functionality to filter and categorize results.

Currently the app uses hardcoded variables as search inputs and 
The Social Network API program is a Node.js server-side application that runs a Mongo NoSQL database containing data for a social media platform. The program uses the Mongoose package for object modeling and communicating with the database, and the Express package for routing. Since the program is entirely back-end, it's helpful to use an API tool such as Postman to make GET, POST, PUT, and DELETE calls to view and manipulate the database.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Questions](#questions)

## Installation

To install, simply download the application root folder and helper files. Then type "npm install" on the command line to download all npm dependancies, which include Mongoose, Express, and Validator, a package used to validate email addresses. To get the database connection up and running, the user will need to have Mongo running on their machine.

## Usage

To run the app, simply type "npm start" in the command line of the root folder. The app will load the database connection. Since the application is back end only, at this point the user will need to access an API tool such as Postman or Insomnia to make applicable GET, POST, PUT, and DELETE routes. The database contains 2 models  which are located at /api/ on the user's localhost port: Users and Thoughts. They can access these models in the database via /api/users and /api/thoughts. There are consequently several routes the user can access:

- GET routes for all Users, one User (by ID), all Thoughts, and one Thought (by ID)
- POST routes for adding one User, one Thought, one Friend to a User's Friend list, and adding one Reaction to a Thought
- PUT routes for updating one User or one Thought
- DELETE routes for removing one User, one Thought, one Friend from a User's Friend list, and removing one Reaction to a Thought

[Video walkthrough of Using the App](https://drive.google.com/file/d/10hrM5UrXzrYdhK5o7Iq1sL0WKy5Y7UzT/view)

![Usage Screenshot 1](./assets/social-network-api-screenshot-1.png?raw=true)

![Usage Screenshot 2](./assets/social-network-api-screenshot-2.png?raw=true)
  
![Usage Screenshot 3](./assets/social-network-api-screenshot-3.png?raw=true)

## Features

- Access the database for a social network platform
- Use NoSQL database to dynamically view or alter data
- Easy to install and run

## Questions

If you have additional questions, please contact me at: max.mcdonough@gmail.com

Github: [MMMPhoto](https://github.com/MMMPhoto)
  
[Github Repo for this Application](https://github.com/MMMPhoto/Social-Network-API)

--------------------------------------

### &copy; 2023 Max McDonough
