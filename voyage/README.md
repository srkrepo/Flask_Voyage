## Happy Sailing ##

Dockerized navigation package `Voyage (ResT API)`, using ``Docker, Flask, Flask-RESTful, Ngnix and Postgress``.


```
.
├── course                   # -- COURSE - Applicatio proxy for Voyage -- #
│   ├── config.py
│   ├── create_model.py
│   ├── db.py
│   ├── Dockerfile
│   ├── _init_.py
│   ├── manage.py
│   ├── models              # -- Course(Model) - Voyage's App -- #
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── sailing.py
│   │   └── ship.py
│   ├── __pycache__
│   ├── requirements.txt
│   ├── resources           # -- Course(Resource) - Voyage's App -- #
│   │   ├── index.py
│   │   ├── __init__.py
│   │   ├── ping.py
│   │   ├── __pycache__
│   │   ├── sailing.py
│   │   └── ship.py
│   ├── sailing_data.csv    (Data used for Preload)
│   ├── ship_data.csv       (Data used for Preload)
│   ├── static              # -- Course(static) - Voyage's App -- #
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   └── main.css
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       └── main.js
│   ├── templates           # -- Course(telpates) - Voyage's App -- #
│   │   ├── base.html
│   │   └── index.html
│   └── testcases.py        # -- Tesetcases - Voyage's App -- #
├── docker-compose.yml      # -- Docker compose - Voyage's App -- #
├── __init__.py
├── nginx                   # -- NGNIX - Reverse proxy for Voyage -- #
│   ├── Dockerfile
│   └── nginx.conf
├── postgres                # -- POSTGRES - Relational DB for Voyage -- #
│   ├── Dockerfile
│   └── __init__.py
├── __pycache__
└── README.md                # Read Me #
```


#### Steps to run ####
1. Open a terminal and run `docker-compose up --build`. Wait until the following output shows up on the terminal.

```
postgres    | 2019-02-08 10:56:48.983 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres    | 2019-02-08 10:56:49.252 UTC [61] LOG:  database system was shut down at 2019-02-08 10:56:48 UTC
postgres    | 2019-02-08 10:56:49.385 UTC [1] LOG:  database system is ready to accept connections
course_1    | [2019-02-08 10:56:49 +0000] [1] [INFO] Starting gunicorn 19.9.0
course_1    | [2019-02-08 10:56:49 +0000] [1] [INFO] Listening at: http://0.0.0.0:5060 (1)
course_1    | [2019-02-08 10:56:49 +0000] [1] [INFO] Using worker: sync
course_1    | [2019-02-08 10:56:49 +0000] [9] [INFO] Booting worker with pid: 9
``` 

2. Then initialize table and preload the data by running `docker-compose run course /usr/local/bin/python create_model.py`. 

3. Open the url [http://127.0.0.1:5060](http://127.0.0.1:5060) on your browser.. ````Happy Sailing!````


#### Sample Output: ####
##### Usage: http://127.0.0.1:5000/ping  (Basic api call) #####
```
{
	message: "Happy Sailing"
}

```

##### Usage: http://127.0.0.1:5000/api/ships #####

```
{
    Ships: [
        {
            imo: 9247455,
            name: "Australian Spirit"
        },
        {
            imo: 9632179,
            name: "Mathilde Maersk"
        },
        {
            imo: 9595321,
            name: "MSC Preziosa"
        }
    ]
}
```


#### Usage: http://127.0.0.1:5000/api/positions/9632179 ####
```
{
    Positions: [
        {
            date_at: "2019-01-14 18:59:06+00",
            imo: 9632179,
            latitude_at: -2.40604996681213,
            longitude_at: 49.9175834655762
        },
        {
            date_at: "2019-01-14 18:40:18+00",
            imo: 9632179,
            latitude_at: -2.51836657524109,
            longitude_at: 49.8978996276855
        }
    ]
}

```

#####  python -m unittest testcases.CourseTestCase #####
````

Sample Testcase results:
------------------------


Test case for the ShipModel

[<ShipModel 9247455>, <ShipModel 9632179>, <ShipModel 9595321>]
b'{\n    "Ships": [\n        {\n            "imo": 9247455,\n            "name": "Australian Spirit"\n        },\n        {\n            "imo": 9632179,\n            "name": "Mathilde Maersk"\n        },\n        {\n            "imo": 9595321,\n            "name": "MSC Preziosa"\n        }\n    ]\n}\n'
.
----------------------------------------------------------------------
Ran 1 test in 0.153s

OK

---------------- ---------------------------------------------------------------------- ----------------------------------------------------------------------


Test case for the SailingModel

b'{\n    "Positions": [\n        {\n            "date_at": "2019-01-14 18:31:22+00",\n            "imo": 9247455,\n            "latitude_at": 69.7120666503906,\n            "longitude_at": 17.5403633117676\n        }\n    ]\n}\n'
.
----------------------------------------------------------------------
Ran 1 test in 0.169s


````

#### ToDo ####
* Plot map
* Logger


```
Cheers..!
(Happy Sailing)
```