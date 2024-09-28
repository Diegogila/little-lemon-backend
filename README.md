# Restaurant Booking API - Little Lemon

This project is a RESTful API to manage the booking system and menu of the **Little Lemon** restaurant. It uses Django, Django Rest Framework (DRF), and Djoser for token-based authentication.

## Installation

Follow these steps to set up the project in your local environment using a virtual environment:

1. Clone the repository:
   git clone https://github.com/your-username/littlelemon.git

2. Navigate to the project directory:
   cd littlelemon

3. Create a virtual environment:
   python -m venv env

4. Activate the virtual environment:
   - On macOS and Linux:
     source env/bin/activate
   - On Windows:
     .\env\Scripts\activate

5. Install the dependencies:
   pip install -r requirements.txt

6. Apply the migrations:
   python manage.py migrate

7. Start the development server:
   python manage.py runserver

8. To deactivate the virtual environment when you're done working, use:
   deactivate

## Authentication

This API uses token-based authentication. To obtain an authentication token, follow the login instructions below.

### Login

To log in and obtain a token, send a POST request to the /api-token-auth/ URL with your username and password:

POST /api-token-auth/
{
  "username": "your_username",
  "password": "your_password"
}

The server will return an authentication token that must be included in the headers of all subsequent authenticated requests:

Authorization: Token your_token

### Logout

To log out, you can simply remove the token from the client-side storage (e.g., session or local storage) or invalidate it if you have implemented a token revocation mechanism.

## Endpoints

### App URLs (restaurant/urls.py)

- `/` (GET): Main view that returns a basic page handled by the index function.
- `/api/menu/` (GET): Returns a list of menu items. Handled by the MenuItemsView.
- `/api/menu/<int:pk>` (GET, PUT, DELETE): Performs read, update, and delete operations on a specific menu item identified by its pk (primary key). Handled by the SingleMenuItemView.
- `/api/bookings/` (GET, POST, PUT, DELETE): Manages restaurant bookings via a router that includes several booking-related views.
- `/api-token-auth/` (POST): Endpoint to obtain a user authentication token.

### Project URLs (littlelemon/urls.py)

- `/admin/`: Django admin interface for managing the project’s models and data.
- `/`: Includes all the URLs defined in the restaurant/urls.py file for the restaurant booking application functionality.
- `/registration/`: Endpoint for handling user registration, authentication, and account-related operations using Djoser.

  - `/registration/`: Handles user registration and authentication (login/logout).
  - `/registration/token/`: Manages token-based authentication using Djoser.

## Example Requests

### Get the Menu

GET /api/menu/

### Get a Menu Item

GET /api/menu/1

### Create a Booking (Requires Authentication)

POST /api/bookings/
Authorization: Token your_token

{
  "table": 4,
  "date": "2024-10-05",
  "time": "20:00",
  "guests": 2
}

## Technologies Used

- Django: Backend framework.
- Django Rest Framework (DRF): Framework to create RESTful APIs.
- Djoser: Library that handles user registration and authentication operations.
- Token Authentication: Uses tokens to securely handle user authentication.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

