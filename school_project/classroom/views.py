


from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DetailView, DeleteView
from classroom.forms import ContactForm
from django.urls import reverse_lazy 
from classroom.models import Teacher



class HomeView(TemplateView):
    
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm 
    
    template_name = 'classroom/contact.html'

    
    success_url = reverse_lazy('classroom:thank_you')

    
    def form_valid(self, form):  
       
        print(form.cleaned_data)
        return super().form_valid(form)  
         


    
class TeacherCreateView(CreateView):  
    
    model = Teacher  s.py` is (here `teacher_form.html`);

    fields = '__all__' 

    success_url = reverse_lazy('classroom:thank_you')



class TeacherListView(ListView): 
    model = Teacher  
    queryset = Teacher.objects.order_by('first_name')


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
   
   
    model = Teacher
    
    fields = '__all__'  
    
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    
    model = Teacher
    
    success_url = reverse_lazy('classroom:list_teacher')

