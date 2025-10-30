# Portfolio Website

A Django-based personal portfolio website showcasing my skills, projects, and experience.

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
cd portfolio_project
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
portfolio_project/
├── portfolio/              # Main app
│   ├── static/            # Static files (CSS, JS, images)
│   └── templates/         # HTML templates
├── portfolio_project/     # Project settings
├── manage.py
└── requirements.txt
```

## Features

- Responsive design
- Animated background
- Project showcase
- Skills section
- Contact form
- Mobile-friendly navigation

## Technologies Used

- Django 5.0.2
- Bootstrap 5
- HTML5/CSS3
- JavaScript
- Typed.js
