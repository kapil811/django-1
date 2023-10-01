# django-1 
## Welcome To My First Django project : a sample site using html, css, bootstrap and django forms.
In this site i had worked with urls, views and templates. i had send data from views to templates using dict[ param= {'data1':output1}] and gained data from form template in views using request.POST.get('element_name')

*caiptalizing and removing punctuations of users text*


##### index.html(home page)
 - navbar  
 - alert element  
 - form  
    - text area  
    - capitalize the text switch  
    - remove the punctuations switch  
    - submit button  
sending form data to views.edit using post method
  
##### views.py  
- index  
- aboutus  
- contactus  
- edit  
    - geting form data using post request  
    - writing logic to capitalize the text and remove punctuations  
    - sending data to edit.hmtl using dictionary
##### about us page  
  - image with  introductry text  
##### contactus page  
  - contact information  
##### edit page  
  - display output : capitalize text and removed punctuations text
