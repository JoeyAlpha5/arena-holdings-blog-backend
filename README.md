# Arena Blog - Backend

The Arena Blog curates travel stories from travellers from all parts of the world. If you're planning a trip to any part of the world, be sure to checkout what others have to say about the location.

This documentation provides a breakdown of the Backend code for this application.

Use the sections listed below to get started with running the application on your machine. 

## Documentation sections
- [Setting up the app](#setting-up-the-app)
- [Third party libraries and packages use](#third-party-libraries)
- [Application Preview](#application-preview)
- [Future improvements](#future-improvement)


### Setting up the app

1. To get started, clone this repository using the following git command
```
git clone https://github.com/JoeyAlpha5/arena-holdings-blog-backend.git
```


2. Once the repo has been cloned, in your terminal cd into the project folder and run the command below to install all the required packages and libraries

```
pip install -r requirements.txt
```


### Third party libraries

This section lists all the third party libraries, dependencies and images that have been used and the reasons for including them.

1. [Django Rest Framework](https://www.django-rest-framework.org/). The django rest framework simplifies the process of building RestFul APIs and given the time constraint using it helped speed up the process of building the blog APIs.

2. [Django CORS Headers](https://pypi.org/project/django-cors-headers/). The backend app has been deployed on Heroku. You can preview the app [here](https://arena-django-backend.herokuapp.com/). This package allowed me to specify which domains can load resources from the backen. Currently only the following domains can load resouces/data, localhost and arena-django-backend.herokuapp.com

3. [Whitenoise](https://pypi.org/project/whitenoise/). Whitenoise has been added to serve static files when loading the app.


### Application preview

You can preview the backend app [here](https://arena-django-backend.herokuapp.com/). To add more articles visit the following [link](https://arena-django-backend.herokuapp.com/admin).

Please see the admin credentials below:
```
username: joey
password: 123456
```

To submit a message, visit the following [here](https://arena-django-backend.herokuapp.com/sendMessage)

To send a message, paste in the following json data to test the sendMessage API

```
{
    "message_sender_name":"name",
    "message_sender_email":"email",
    "message_sender_mobile_number":"mobile",
    "message_content":"message",
}
```


### Future improvements

Currently the sqlite3 database that's storing the app's data is hosted together with the application on Heroku. Seperating the database from the backend using a 3 tier architecture will provide better security and flexibility, for example by setting up an RDS database on AWS you can make use of all the database configurations offered by AWS, such as automating backups.

The backend application is also missing test cases, which can be helpful when testing out new features before deployment