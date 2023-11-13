# Production Engineering - Portfolio Site

Portfolio site built in Flask. This site uses concepts learned during the entire MLH fellowship.

## Description

This portfolio has an about me, education, work experience, hobbies, and places you've visited section. The 'About Me' section allows you to enter any information you wish to provide about yourself. The education section displays a timeline of recent schools or colleges you have attended. The work experience section is where you can enter the latest projects or jobs in which you have participated in. 

This site uses the following concepts learned during this fellowship:
- VPS setup via DigitalOcean
- Scripting (bash)
- Databases
- Unit testing
- Containers
- CI/CD (GitHub Actions)
- Monitoring

## Badges
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Technologies used in this project
- Flask
- Jinja
- HTML
- CSS
- Javascript
- MySQL
- Docker

## Metrics (Prometheus & Grafana)
<img width="500" alt="metrics" src="https://github.com/rashelrr/mlh-portfolio-project/assets/66976912/f66e4253-9c23-4313-a30c-eecf63bac31f">

Site metrics after load testing by sending 1000 requests at a pace of 10 concurrent requests with Docker and ab (Apache Bench).

## Try it Out


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Author
* Rashel Rojas

## Roadmap
- Work more with the information, for example, use a database to store all portfolio information
- Adding a page to display a user's projects
- Creating more jinja templates

