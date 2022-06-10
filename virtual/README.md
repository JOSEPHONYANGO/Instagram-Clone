# Instagram Clone
<hr>



>  **A personal instagram clone application that displays images for others to see.**

## Specifications




## Getting Started
<hr>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
  1.Git
  2.Python: 3.8.10 versions
  3.Django: 3.10 or greater version
  4.Have Internet connection
  5.Virtual Environment
  6.Gunicorn
  7.Chrome Browser

```

### Installing

> Follow this procedure to get my project up and running in your Desktop or Laptop.

```
> Install Django Framework '''$pip install django==1.11'''
> Install Python Version --3.6.4
> Install gunicorn in (virtual) -python3.6 -m pip install gunicorn
> Install the Heroku Cli
> $ git clone https://github.com/MrazTevin/Gallery-Application.git
> $ Python3.6 -m venv Virtual
> $ Source virtual/bin/activate
```


## Running the tests
* To test the functionalities of this app run the command below on your terminal:
  1.First cd Gallery-Application/exhibit then;
  ```
  $Python3.6 manage.py test
  ```  

###  End to end tests
1. Save : Will test if one is able to save i.e save the image location.
2. Delete : Will test if one is able to delete i.e delete the image location.
3. Instance : Will test the instance of the class i.e TestInstance of Image Class

```
def test_save_method(self):
    self.outdoor.save_location()
    location = Location.objects.all()
    self.assertTrue(location)
```

### Coding style Tests

- This tests will enable us write methods that we need for our app to function, which we will       include in our models file

```
def save_location(self):
      self.save()

  def delete_location(self):
      self.save()
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Python](https://www.python.org/) - Development language used
* [Bootstrap5](https://getbootstrap.com/) - Used to design app layout.
* [UI KIT](https://getuikit.com) - Used for UI/Ux 
* [MDB Bootstrap](https://mdbootstrap.com/) - Used to design the User Interface
* [Heroku](https://www.heroku.com/) - Used to deploy application


## Authors

* **Joseph Otieno** - *Initial work* - [PingPong](https://mraztevin.github.io/Ping-Pong/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moringa School
