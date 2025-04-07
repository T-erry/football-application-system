# Football API  
The goal of this project was to build a secure, scalable, and well-structured REST API using Django and DRF. The API allows users to register, authenticate, and interact with data about active footballers. Admins also get an enhanced admin panel to manage records easily.

##  Project Setup
- Initialized a new Django project and structured it following best practices.
- Integrated Django Rest Framework for API development.
- Configured a PostgreSQL database for performance and scalability.

## API Endpoints

- POST	api/auth/register/	- Register a new user
- POST	/api/auth/login/	- Login & get JWT token
- POST	/api/token/refresh/	- Refresh JWT access token
- GET	    /api/players/	- List all players
- GET	    /api/players/?search=	- Search/filter players
- GET     /api//users/  - List all users
- DELETE	api/users/<id>/	- Delete a user 
- POST	/api/users/<uuid>/toggle_favorite/	- Toggle a favorite player for the user
- GET	   /api/users/<uuid>/list_favorites/	- List all favorited players for the authenticated user

### Data Management
- Loaded a custom JSON dataset of footballers into the PostgreSQL database.

- Created Django models to represent player data and user accounts.

### API Features
- Created fully functional CRUD operations for managing footballer and user data.

- Added search and filter capabilities:

- Filter by age, club, market value, and name.

### Admin Customization
Customized Django Admin for the Player model:

Added list filters, custom display fields, and search functionality for a smoother admin experience.

### Technologies Used
- Backend: Django, Django Rest Framework

- Database: PostgreSQL

- Authentication: JWT (via SimpleJWT)

- Admin: Django Admin with custom filters/search

