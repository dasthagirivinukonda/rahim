# rahim
project

description


class HomePageView(ListView):
    model= Employee
    template_name= 'vdas/home.html'


class DetailPageView(DetailView):
    model=Employee
    template_name= 'vdas/detail.html'
    context_object_name= "anything"
class CreatePageView(CreateView):
    model=Employee
    template_name= 'vdas/Create.html'

    fields= '__all__'


class UpdatePageView(UpdateView):
    model=Employee
    template_name= 'vdas/edit.html'

    fields= ['name','age']
class DeletePageView(DeleteView):
    model=Employee
    template_name= 'vdas/delete.html'
    success_url= reverse_lazy('home')


