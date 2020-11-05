# SQUIZZ Web Ordering Application Backend

## Table Of Contents
1. **[Project Description](#Project-Description)**
2. **[Features](#Features)**
3. **[Documentation](#Documentation)**
4. **[System Requirements](#System-Requirements)**
5. **[Technologies Used](#Technologies-Used)**
6. **[AWS Deployment Guide](#AWS-Deployment-Guide)**
7. **[Setup Guide](#Setup-Guide)**
8. **[Unit Testing](#Unit-Testing)**
9. **[User Acceptance Tests](#User-Acceptance-Tests)**
10. **[Traceability Matrix](#Traceability-Matrix)**
11. **[Attribution](#Attribution)**

## Project Description
This repository contains the backend source code for the SQUIZZ Web Ordering Application. It also contains the entire documentation for the project, an AWS deployment guide, and unit tests.

The web ordering application is a B2B/B2C system that supports the product catalogues of Holyoake, and PJ SAS Trading. It allows users to procure orders for different products, and to view in-browser rendered 3D models for Holyoake swirl diffusers. It also supports dynamic customer-level pricing based on the current selected customer.

Please check out the [frontend repository](https://github.com/ansabkhaliq/frontend) for more details on the frontend client.

This project also integrates with our custom desktop utility that converts IFC files into 3D models. The repository for the utility can be found [here](https://github.com/ansabkhaliq/IFCConverto).

## Features
* Import products from the SQUIZZ API
* Import prices from the SQUIZZ API
* Import categories from the SQUIZZ API
* Import customer data form the SQUIZZ API
* Send order details to SQUIZZ API to create orders
* Sync customer pricing data when customer is switching
* Provides a method to import 3D model meta data from the desktop utility
* Provides a method to import 3D model URL from the desktop utility
* Authenticates the front end user
* Authenticates an organization and establish a session with SQUIZZ API
* Provide data for products search via barcode or product code
* Provide complete list of products along with their categories for the frontend

## Documentation
All of the process and product related documentation for the project can be found [here](./Docs) in the `Docs` directory.

## System Requirements
The backend can be run on any operating system.

Listed below are the requirements to run the application:
* [Python 3.8](https://www.python.org/) or above
* [Docker](https://www.docker.com/) (only if you want to run the backend using Docker) 

We recommend using [Visual Studio Code](https://code.visualstudio.com/download) or [PyCharm](https://www.jetbrains.com/pycharm/) for development.

## Technologies Used
* [Python 3.8](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/) for our backend framework
* [PyMySQL](https://pymysql.readthedocs.io/en/latest/) for a Python MySQL client library

## AWS Deployment Guide
This repository includes a deployment guide and a Docker Compose file for deploying the entire application (including the frontend client and database) on AWS. These files can be found [here](./deployment).

## Setup Guide
There are two ways to deploy the backend and database, either locally or in production. You can run the backend by either setting up a virtual environment or using Docker.

### Using a Virtual Environment
 1. Set up a virtual environment
    ```
    $ python -m venv venv
    $ venv\Scripts\activate.bat
    $ pip install -r requirements.txt
    ```
    **Note:** These commands are for Windows. They are similar for Mac or Linux

2. Install MySQL Workbench and MySQL Server
  If you don't know how to do this, watch this [tutorial](https://www.youtube.com/watch?v=u96rVINbAUI)

3. Run the script `FinalSqlDump.sql` in `backend/db/data` in MySQL Workbench to create the database and populate the tables

4. Modify SQL Server credentials in lines 22-25 in `app/config.py`
    ```
    HOST = ...               # MySQL Hostname (e.g. 'localhost')
    USER = ...               # MySQL Username
    PASSWORD = ...           # MySQL Password
    DB_NAME = "squizz_app"
    ```
5. Start the Flask server
    ```
    $ python -m flask run
    ```

### Using Docker
1. Create an image for the backend
    ```bash
    $ docker build -t squizz/flask-backend:latest .
    ```

2. Run the backend container
    ```bash
    $ docker run -p 5000:5000 --name flask-backend squizz/flask-backend:latest
    ```

## Unit Testing
The unit tests are written in Python using [pytest](https://docs.pytest.org/en/stable/).

To install `pytest`:
```bash
$ pip install pytest
```
**Note**: Before you can run the tests, you need to start the backend server first.

To run the tests, first ensure that you are in the root directory of the backend. Then, run:
```bash
$ pytest
```

## User Acceptance Tests
The user acceptance tests can be found [here](https://github.com/ansabkhaliq/backend/blob/master/Test%20Cases%20Docs/Test%20Cases%20Report.pdf).


## Traceability Matrix
The traceability matrix can be found on the last page of the user acceptance tests document. Please refer to [User Acceptance Tests](#User-Acceptance-Tests).

## Attribution
Created by SQ-Wombat and SQ-Koala.