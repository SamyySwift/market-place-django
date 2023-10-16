# Online market Place - README

This document provides information about the views, their functionalities, and URLs for the core and related applications in the project.

## Environment Setup

- Clone the repo
- Run `pipenv install` to install all required packages
- Don't forget to set the database to connect to your own database
- Run `python manage.py migrate` to migrate the tables to a new database
- `Run python manage.py runserver` to start the server

## Core Views

### Index View

- URL: `core/home`
- Functionality: Displays a list of available items for sale and navigation by categories.
- Allowed Permissions: Public access.

### Contact View

- URL: `xore/contact`
- Functionality: Displays a contact page.
- Allowed Permissions: Public access.

### Profile View

- URL: `core/profile/<int:pk>`
- Functionality: Displays a user's profile information.
- Allowed Permissions: Requires user to be authenticated.

### Signup View

- URL: `core/signup`
- Functionality: Allows users to create an account.
- Allowed Permissions: Public access for registration, requires authentication for editing.

### Login View

- URL: `core/login`
- Functionality: Allows users to log in to their accounts.
- Allowed Permissions: Public access for login, requires authentication for account access.

### Logout View

- URL: `core/logout`
- Functionality: Allows users to log out of their accounts.
- Allowed Permissions: Requires user to be authenticated.

### Update User View

- URL: `core/update-profile`
- Functionality: Allows users to update their account details and profile.
- Allowed Permissions: Requires user to be authenticated.

### Delete Account View

- URL: `core/delete`
- Functionality: Allows users to delete their accounts.
- Allowed Permissions: Requires user to be authenticated.

## Item Views

### Detail View

- URL: `/item/<int:pk>`
- Functionality: Displays details of a specific item.
- Allowed Permissions: Public access.

### Browse View

- URL: `core/browse`
- Functionality: Allows users to browse items by category or search by name.
- Allowed Permissions: Public access.

### New Item View

- URL: `items/new-item`
- Functionality: Allows users to create and add a new item.
- Allowed Permissions: Requires user to be authenticated.

### Edit Item View

- URL: `/item/edit/<int:pk>`
- Functionality: Allows users to edit details of a specific item they created.
- Allowed Permissions: Requires user to be authenticated.

### Delete Item View

- URL: `/item/delete/<int:pk>`
- Functionality: Allows users to delete items they created.
- Allowed Permissions: Requires user to be authenticated.

## Dashboard Views

### User Dashboard View

- URL: `dashboard/user-dashboard`
- Functionality: Displays a dashboard for users, showing items they have created.
- Allowed Permissions: Requires user to be authenticated.

## URLs

- The URLs are organized into different namespaces, such as "core," "dashboard," and "item," to keep the project structured and maintainable.

## Deployment and Database

Deployment Platform: The application has been deployed on [Render](https://online-market-place-ksqy.onrender.com/), a cloud platform that simplifies the deployment process.
Database: The project uses a PostgreSQL database for data storage, ensuring data reliability and performance.
