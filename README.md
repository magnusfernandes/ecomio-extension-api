<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Ecomio extension</h3>
  <p align="center">
    Extension to track sustainability for flights on skyscanner & kayak
    <br />
    ·
    <a href="https://github.com/magnusfernandes/ecomio-extension-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/magnusfernandes/ecomio-extension-api/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Tracks the trip destination and calculates the sustainability score for that trip.

- Reads origin, destination, start date & end date of users itinerary from [Kayak](kayak.com) & [Skyscanner](https://www.skyscanner.com/)
- Sustainability score is color coded.
  - [0-40] RED
  - [40-100] GREEN

### Built With

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

Require docker to run this project

  ```sh
  docker build --tag ecomio-django .
  docker run -d -p 3400:8000  -v src:/ecomio_src --name ecomio_app ecomio-django
  ```

### Admin dashboard

1. Create superuser
   ```sh
   python manage.py createsuperuser
   ```
2. Admin URL
   ```sh
   http://localhost:3400/admin/
   ```

### Postman docs
[API docs](https://github.com/magnusfernandes/ecomio-extension-api/docs/postman_collection.json)

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/magnusfernandes/ecomio-extension-api/issues) for a list of proposed features (and known issues).

<!-- CONTACT -->

## Contact

Magnus Fernandes - (magnusfernandes1295@gmail.com)

Project Link: [https://github.com/magnusfernandes/ecomio-extension-api.git](https://github.com/magnusfernandes/ecomio-extension-api.git)