import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

main_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Main Page</title>
    </head>
    <body>
        <h1>Welcome to our online store!</h1>
        <ul>
            <li><a href="/">Main</a></li>
            <li><a href="/about">About</a></li>
        </ul>
        <img src="https://images.pexels.com/photos/3944405/pexels-photo-3944405.jpeg?auto=compress&cs=tinysrgb&w=1260&h=
        750&dpr=2" alt="Various products" style="width: 600px">
        <p>This is the main page of our internet shop. Browse our collection of products and find amazing deals!</p>
  
    </body>
    </html>
"""

about_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us</title>
    </head>
    <body>
        <h1>About Us</h1>
        <ul>
            <li><a href="/">Main</a></li>
            <li><a href="/about">About</a></li>
        </ul>
        <img src="https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=1260&h=
        750&dpr=2" alt="Our team" style="width: 600px">
        <p>We are a dedicated team working to provide you with the best products and services. Learn more about our mission and vision!</p>
       
    </body>
    </html>
"""


def main(request):
    logger.info('Main page accessed')
    return HttpResponse(main_html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(about_html)

# Create your views here.
