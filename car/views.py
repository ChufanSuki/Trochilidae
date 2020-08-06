from django.shortcuts import render
from car.models import Car_User, Car_Model, Car_Check
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # print("DEBUG: Session")
    # for key, value in request.session.items():
    #     print(f'{key} {value}')
    num_models = Car_Model.objects.all().count()
    num_cars = Car_User.objects.all().count()
    # Avaialable cars (state = '1')
    num_models_available = Car_Model.objects.filter(state__exact=True).count()
    num_cars_available = Car_User.objects.filter(state__exact=1).count()
    num_ridings = Riding_Info.objects.count()
    num_users = Car_User.objects.count() 
    context = {
        'num_models': num_models,
        'num_cars': num_cars,
        'num_models_available': num_models_available,
        'num_cars_available': num_cars_available,
        "num_users": num_users,
        "num_ridings": num_ridings,
        "num_visits": num_visits,
    }

    return render(request, 'car/index.html', context=context)

class ModelListView(generic.ListView):
    model = Car_Model
    # specify context_object_name, queryset, template_name, get_queryset(self), get_context_data(self, **kwargs) if needed
    # First get the existing context from our superclass.
    # Then add your new context information.
    # Then return the new (updated) context.
    template_name = 'car/model_list.html'
    context_object_name = 'model_list'
    paginate_by = 10

class ModelDetailView(generic.DetailView):
    model = Car_Model
    context_object_name = 'model'
    template_name = 'car/model_detail.html'


class UsedCarsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Car_User
    context_object_name = 'car_list'
    template_name = 'car/car_list_used_user.html'
    paginate_by = 10
    # you may use @property to decorate useful function

    def get_queryset(self):
        return Car_User.objects.filter(user=self.request.user).order_by('date')

class UsedCarsAllListView(PermissionRequiredMixin, generic.ListView):
    model = Car_User
    context_object_name = 'car_list'
    template_name = 'car/car_list_used_all.html'
    paginate_by = 10
    permission_required = 'car.can_change_state'
    
    def get_queryset(self):
        return Car_User.objects.order_by('date')
