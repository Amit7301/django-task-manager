# Django Task Manager 📝

A simple and intuitive task management application built with the Django web framework. This project allows users to create, read, update, delete their tasks.

## Features ✨

* **User Authentication**: Users can register, log in, and log out to manage their personal tasks.
* **CRUD Operations**: Full functionality to Create, Read, Update, and Delete tasks.
* **Task Completion**: Easily mark tasks as complete.
* **Responsive Design**: The application is designed to be accessible on both desktop and mobile devices.

## Technologies Used 💻

* **Backend**: Django
* **Frontend**: HTML, CSS (with a focus on a clean, minimal design)
* **Database**: SQLite (default for development)

## Getting Started 🚀

### Prerequisites

* Python 3.8+
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    
    git clone [https://github.com/Amit7301/django-task-manager](https://github.com/Amit7301/django-task-manager)
    cd django-task-manager
    

2.  **Create and activate a virtual environment:**
    
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
   

3.  **Install the required packages:**
    
    pip install -r requirements.txt
    

4.  **Run database migrations:**
    
    python manage.py makemigrations
    python manage.py migrate
    

5.  **Create a superuser (optional, for accessing the Django admin panel):**
    
    python manage.py createsuperuser
    

6.  **Run the development server:**
    
    python manage.py runserver
    

The application will be available at `http://127.0.0.1:8000`.

## Project Structure 📁

* `todo_list/`: Main Django project directory.
* `base/`: The main application for the task manager.
    * `models.py`: Defines the `Task` model.
    * `views.py`: Contains the logic for handling requests.
    * `urls.py`: URL configurations for the app.
    * `templates/`: HTML templates for the user interface.
* `requirements.txt`: Lists all project dependencies.
* `.gitignore`: Specifies files to be ignored by Git.

## Contributing 🤝

Contributions are welcome! If you find a bug or have a feature request, please open an issue.
