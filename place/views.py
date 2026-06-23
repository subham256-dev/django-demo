from urllib import request

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from .models import*
# Create your views here.

place_list=[
         {'country':'japan','badge':'Tokyo,Japan','city_name':'Tokyo','description':'Ancient shrines beside neon-lit skyscrapers, sublime ramen stalls, and cherry blossoms — a city of beautiful contradictions.','rating':'4.8'},
         {'country':'Greece','badge':'Santorini, Greece','city_name':'Santorini','description':'Whitewashed cliff-top villas, azure church domes, and sunsets that paint the Aegean in gold — pure Mediterranean romance.','rating':'4.9'},
         {'country':'India','badge':'Kashmir, India','city_name':'Kashmir','description':'Shikara rides on Dal Lake, saffron meadows, and Himalayan grandeur — the "Paradise on Earth" in every sense.','rating':'4.7'},
         {'country':'UAE','badge':'Dubai, UAE','city_name':'Dubai','description':'Where the future meets the desert — futuristic architecture, golden dunes, and unparalleled luxury converge.','rating':'4.6'},
         {'country':'Island','badge':'Maldives','city_name':'Maldives','description':'Overwater bungalows above impossibly turquoise lagoons — the ultimate sanctuary of barefoot luxury and serenity.','rating':'4.9'},
         {'country':'France','badge':'Paris, France','city_name':'Paris','description':'The City of Light glitters with haute couture, Impressionist art, cobbled boulevards, and the worlds most iconic skyline.','rating':'4.8'},
         {'country':'Indonesia','badge':'Bali, Indonesia','city_name':'Bali','description':'Tropical paradise with lush rice terraces, vibrant culture, and pristine beaches.','rating':'5.0'},
       ]

def dreamscape(request):
        context={'page':'Place','places':place_list}
    
        return render(request,'dreamscape.html',context)

def travel(request):
     queryset=Place.objects.all()
     context={'places':queryset,'page':'Travel Places'}

     return render(request,'travel.html',context)

def add_place(request):
      if request.method=="POST":
            data=request.POST
            name=data.get('name')
            location=data.get('location')
            description=data.get('description')
            rating=data.get('rating')
            image=request.FILES.get('image')
            Place.objects.create(
                  name=name,
                  location=location,
                  description=description,
                  rating=rating,
                  image=image
                  )
            print('place added successfully') 
            return redirect('/travel/')   
      
      context={'page':'Trave Places'}
      
        
      return render(request,'addplace.html',context)

         
        
def delete_place(request,id):
      place=Place.objects.filter(id=id)
      place.delete()
      return redirect('/travel')

def update_place(request,id):
      place=Place.objects.get(id=id)
      if request.method=='POST':
            name=request.POST.get('name')
            description=request.POST.get('description')
            location=request.POST.get('location')
            rating=request.POST.get('rating')
            image=request.FILES.get('image')

            place.name=name
            place.description=description
            place.location=location
            place.rating=rating
            if image:
                  place.image=image
                  
            place.save()
            return redirect('/travel/')
      context={'place':place}
      return render(request,'updateplace.html',context)
    
