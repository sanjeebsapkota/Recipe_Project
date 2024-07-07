from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def receipes(request):
    if request.method == 'POST':#bring all data
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_category = request.POST.get('receipe_category')
        receipe_process = request.POST.get('receipe_process')
        receipe_ingredient = request.POST.get('receipe_ingredient')
        receipe_image = request.FILES.get('receipe_image')
        ##save all the data inside this model below code is used
        Receipe.objects.create(receipe_name=receipe_name,receipe_description=receipe_description,receipe_category=receipe_category,receipe_process=receipe_process,receipe_ingredient=receipe_ingredient,receipe_image=receipe_image)
        return redirect('/receipes/') 

    return render(request,'receipes.html')

        

def receipelist(request):
    receipes = Receipe.objects.all()
    context ={'receipes':receipes}
    return render(request,'receipelist.html',context)



def edit(request, pk):
    receipe_obj = Receipe.objects.get(pk=pk)
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_category = request.POST.get('receipe_category')
        receipe_process = request.POST.get('receipe_process')
        receipe_ingredient = request.POST.get('receipe_ingredient')
        receipe_image = request.FILES.get('receipe_image')  # Use request.FILES for images

        # Update the existing object
        receipe_obj.receipe_name = receipe_name
        receipe_obj.receipe_description = receipe_description
        receipe_obj.receipe_category = receipe_category
        receipe_obj.receipe_process = receipe_process
        receipe_obj.receipe_ingredient = receipe_ingredient
        if receipe_image:  # Update image only if provided
            receipe_obj.receipe_image = receipe_image
        receipe_obj.save()  # Save the updated object

        return redirect('receipelist')  # Redirect to recipe list after update

    # Render the edit form with existing data if request is GET
    context = {'receipe': receipe_obj}
    return render(request, 'edit.html', context)


# def edit(request,pk):
#     receipe_obj = Receipe.objects.get(id=pk)
#     if request.method =="POST":
#         receipe_name = request.POST.get('receipe_name')
#         receipe_description = request.POST.get('receipe_description')
#         receipe_category = request.POST.get('receipe_category')
#         receipe_process = request.POST.get('receipe_process')
#         receipe_ingredient = request.POST.get('receipe_ingredient')
#         receipe_image = request.POST.get('receipe_image')
#         Receipe.objects.create(receipe_name=receipe_name,receipe_description=receipe_description,receipe_category=receipe_category,receipe_process=receipe_process,receipe_ingredient=receipe_ingredient,receipe_image=receipe_image)
#         return redirect('receipelist')
    
    
#     data ={'receipe':receipe_obj}
#     return render (request,'edit.html',context=data)
    
def delete(request,pk):
    receipe_obj = Receipe.objects.get(id=pk) 
    receipe_obj.delete()
    return redirect('/receipelist/')

            
def home(request):
    return render(request,'home.html')
    

    