from django.http import HttpResponse 
import pathlib
this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):

    html_ = """
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>lewis is my name what is your name</h1>
    </body>
    </html>
     """

    return HttpResponse(html_)
