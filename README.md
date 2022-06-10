# Photoshare
A personal gallery application that you display your photos for others to see, with categories, image name, descriptions and foreign key.


asgiref==3.5.2
backports.zoneinfo==0.2.1
certifi==2022.5.18.1
charset-normalizer==2.0.12
dj-database-url==0.5.0
Django==4.0.5
django-crispy-forms==1.14.0
django-db==0.0.7
django-heroku==0.3.1
django-resized==1.0.0
django-tinymce==3.4.0
gunicorn==20.1.0
html2text==2020.1.16
idna==3.3
numpy==1.22.4
Pillow==9.1.1
postgres==4.0
psycopg2==2.9.3
psycopg2-binary==2.9.3
psycopg2-pool==1.1
PyMySQL==1.0.2
python-decouple==3.6
requests==2.27.1
sqlparse==0.4.2
urllib3==1.26.9
whitenoise==6.2.0




## Author  
  
[Kipkemoi Elvis](https://github.com/DynastyElvis)  
  
 
##  Live Link  
 Click [View Site](https://elvis-gallery.herokuapp.com/)  to visit the site


[Go Back to the top](#Photoshare)

## Screenshots 
###### Home Landing-Page
 
<img src="https://raw.githubusercontent.com/DynastyElvis/Photoshare-App/master/static/images/Screenshot%20from%202022-06-10%2011-24-59.png">
 
 ###### Open image to view
 <img src="https://raw.githubusercontent.com/DynastyElvis/Photoshare/main/photoshare/static/images/Screenshot%20from%202022-05-29%2019-52-34.png"> 

 ###### Add Image to the Collage Gallery
 <img src="https://raw.githubusercontent.com/DynastyElvis/Photoshare/main/photoshare/static/images/Screenshot%20from%202022-05-29%2019-52-43.png">

 ###### ADMIN Dashboard to manage the pictures
 <img src="https://raw.githubusercontent.com/DynastyElvis/Photoshare/main/photoshare/static/images/Screenshot%20from%202022-05-30%2017-45-23.png">



## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

[Go Back to the top](#Photoshare)


## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/DynastyElvis/Photoshare```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  


[Go Back to the top](#Photoshare)


## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django ](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [HTML](https://www.w3schools.com/css/)  
* [Boostrap](https://getbootstrap.com/)  
* [CSS](https://www.w3schools.com/css/)  

[Go Back to the top](#Photoshare)


## License

[MIT LICENCE](https://github.com/DynastyElvis/Photoshare/blob/main/LICENSE)


Copyright (c) 2022 K. E. Rono



[Go Back to the top](#Photoshare)

## Known Bugs

No Known Bugs.

## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :kipkemoilvs@gmail.com

## Authors Info
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)


[Go Back to the top](#Photoshare)
