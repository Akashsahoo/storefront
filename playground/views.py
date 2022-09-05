from email import message
from django.core.mail import EmailMessage,send_mail,mail_admins,BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
#from .tasks import notify_customers
import requests
from rest_framework.views import APIView
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import logging

logger = logging.getLogger(__name__)




class HelloView(APIView):
    
    def get(self,request):
        try:
            logging.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logging.info("Recieved the response")
            data = response.json()  
            return render(request, 'hello.html', {'name': data})
        except requests.ConnectionError:
            logging.critical('httpbin is offline')
        #return render(request, 'hello.html', {'name': data})




# class HelloView(APIView):
#     @method_decorator(cache_page(5 * 60))
#     def get(self,request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()  
#         return render(request, 'hello.html', {'name': data})


# 





# def say_hello(request):
#     #notify_customers.delay('Hello')
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#        response = requests.get('https://httpbin.org/delay/2')
#        data = response.json()
#        cache.set(key,data,10*60)
#     return render(request, 'hello.html', {'name': cache.get(key)})






# def say_hello(request):
#     try:
#        message = BaseEmailMessage(
#            template_name='emails/hello.html',
#            context={'name':'Mosh'}
#        )
#        message.send(['john@moshbuy.com'])
#     except BadHeaderError:
#         pass   
#     return render(request, 'hello.html', {'name': 'Mosh'})
# def say_hello(request):
#     try:
#        message = EmailMessage('subject','message','from@moshbuy.com',['john@moshbuy.com'])
#        message.attach_file('playground/static/images/blackmagic.png')
#        message.send()
#        #send_mail('subject','message','info@moshbuy.com',['bob@moshbuy.com'])
#        #mail_admins('subject','message',html_message='message')
#     except BadHeaderError:
#         pass   
#     return render(request, 'hello.html', {'name': 'Mosh'})
