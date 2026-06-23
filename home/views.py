from django.shortcuts import render

from django.http import HttpResponse


peoples=[
    {"name":"Subham","age":19},
    {"name":"Subhajeet","age":19},
    {"name":"Priyanshu","age":20},
    {"name":"Jyoti","age":19},
    {"name":"Deepak","age":16},
    {"name":"Rahul","age":13},
     {"name":"puchu","age":67},
    ]

city_list=[
    {"name":"New York","rating":4.8},
    {"name":"Los Angeles","rating":4.8},
    {"name":"Chicago","rating":4.5},
    {"name":"Houston","rating":4.2},
    {"name":"Phoenix","rating":4.1},
    {"name":"Philadelphia","rating":4.0},
    {"name":"San Antonio","rating":3.9},
    {"name":"Dallas","rating":3.9},
    {"name":"Birmingham","rating":3.7},
    {"name":"Liverpool ","rating":3.8},
    {"name":"Manchester ","rating":3.6},
]

def home(request):
    return render(request,"index.html",context={"people":peoples,'page':'Django'})

def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)


def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html",context)

def success_page(request):
    return HttpResponse("<h1>Hey I am a Success page.</h1>")


def city(request):
    context={'page':'Top-city',"cities":city_list}
    return render(request,'city.html',context)
