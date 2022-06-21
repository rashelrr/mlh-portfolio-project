# Production Engineering - Portfolio Site

Portfolio site built in Flask. This site will be the foundation for activities we do in the whole program.

## Description

This portfolio has an about me, education, work experience and contact section. The about me section allows you to enter any information you wish to provide about yourself. The education section displays a timeline of recent schools or colleges you have attended. The work experience section allows you to enter the latest projects or jobs in which you have participated. The contact section is for people to take action after viewing your portfolio.

On the other hand, we have two separate pages which are connected to the portfolio in which you can show your hobbies (including images) and the places in the world that you have visited.

## Badges
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Technologies used in this project
- Flask
- HTML
- CSS
- Javascript
- Bootstrap
- Jinja

## Try it Out
http://rashelrojasportfolio.duckdns.org:5000/

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

## Authors
* Rashel Rojas
* Carlos Seda 

## Roadmap
- Work more with the information, for example, use a database to store all portfolio information
- Adding a page to display a user's projects
- Creating more jinja templates

