# Course Management System


This is a Course Management System developed using Django, which handles both the frontend and backend. Although the initial requirement was to create separate frontend and backend components, Django was chosen to streamline development, allowing for easier integration and a more cohesive development process.

please note that this repo is for both frontend and backend

## Project Overview

The Course Management System allows users to manage courses, including creating, updating, and deleting courses. The system is built using Django, a powerful web framework that simplifies the development of both the frontend and backend.

## Technologies Used

- **Backend & Frontend**: Django 5.1
- **Database**: SQLite3
- **Python Version**: 3.12
- **Docker**: Used for containerization and deployment

## Project Structure

- `app/`: Contains the main Django application.
- `requirements.txt`: Contains the list of dependencies for the project.
- `Dockerfile`: Used to build a Docker image of the application.
- `db.sqlite3`: SQLite3 database file.
- `manage.py`: Django's command-line utility.

## Setup and Execution

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12
- Docker
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/your_github_username/course-management-system.git
cd course-management-system
