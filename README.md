# drugstore
Minimal Flask App
=================

Basic API with Flask, Flask-RESTful and
Docker

Usage
-----

Clone the repo:

    git clone https://github.com/imationdcl/drugstore.git
    cd drugstore/api

Run docker-compose:

    docker-compose up --build -d

Or run the sample server:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py

Run test:

    pytest -v

Try the endpoints:

    curl --request GET \
        --url http://localhost:5000/drugstores
    
    curl --request GET \
        --url 'http://localhost:5000/drugstores?local_nombre=AHUMADA
        
    curl --request GET \
        --url 'http://localhost:5000/drugstores?comuna_id=83'
  
    curl --request GET \
        --url 'http://localhost:5000/drugstores?local_nombre=AHUMADA&comuna_id=83'
