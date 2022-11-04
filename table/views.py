from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
from .forms import *
from django.conf import settings
from .models import *
import pandas as pd
from sqlalchemy import create_engine
from django.views.generic import ListView
from django.core.paginator import Paginator

def home(request):
    demo = Demo.objects.all().order_by('-id')
    paginator = Paginator(demo, 20) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        uploaded_file = request.FILES['file']


        if uploaded_file.name.endswith('.csv'):
            try:
                savefile = FileSystemStorage()
                name = savefile.save(uploaded_file.name, uploaded_file)
                
                d = os.getcwd()
                file_directory = d + '/media/' + name

                df = pd.read_csv(str(file_directory))
                
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']
                database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format( user=user,password=password,database_name=database_name,)
                engine = create_engine(database_url)

                df.to_sql(Demo._meta.db_table, con=engine, if_exists='append', index=False)
            except:
                messages.warning(request, 'Something Went Wrong, Try Again')

        else:
            messages.warning(request, 'cant upload file. please use csv format')



            
    return render(request, 'table/home.html', {'form':form, 'demo':demo, 'page_obj':page_obj})

