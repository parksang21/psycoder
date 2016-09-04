from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course, Category


class IndexView(generic.ListView):
    template_name = 'lecture/department.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class CourseListView(generic.DeleteView):
    model = Category
    template_name = 'lecture/development_category.html'
    context_object_name = 'category'



