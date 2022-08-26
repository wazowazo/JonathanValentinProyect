from pydoc import Doc
from django.shortcuts import render
from MVT_N1.models import Familiar
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiares(request):
    """Como la carga de datos NO la hacemos desde formularios, creo tres variables de tipo Familiar: family1, family2, y family3.
    """
    #Carga de datos de familiar #1
    family1=Familiar(nombre="Joel", apellido="Valentin",parentesco="Hermano", fechaDeNacimiento="1994-05-20", edad=26)
    family1.save()
     
    #Carga de datos de familiar #2
    family2=Familiar(nombre="Yoanna", apellido="Valentin",parentesco="Hermana", fechaDeNacimiento="1989-06-30", edad=33)
    family2.save()
    
    #Carga de datos de familiar #3
    family3=Familiar(nombre="Trinidad", apellido="Bernatowiez",parentesco="Novia", fechaDeNacimiento="1998-04-23", edad=24)
    family3.save()

   
   #Diccionario para el Template
    family_list=[family1, family2, family3]
    diccionario={"lista":family_list}

    plantilla=loader.get_template("template1.html")
    doc=plantilla.render(diccionario)


    return HttpResponse(doc)