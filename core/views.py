from django.shortcuts import render, HttpResponse

# Create your views here.

def hello (request, nome, idade):
    return  HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma (request, num1, num2):
    return HttpResponse('{} + {} = {}'.format(num1, num2, num1 + num2))

def subtracao (request, num1, num2):
    return HttpResponse('{} - {} = {}'.format(num1, num2, num1 - num2))

def multiplicacao (request, num1, num2):
    return HttpResponse('{} * {} = {}'.format(num1, num2, num1 * num2))

def divisao (request, num1, num2):
    return HttpResponse('{} / {} = {}'.format(num1, num2, num1 / num2))