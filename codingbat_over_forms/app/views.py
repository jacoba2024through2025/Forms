from django.shortcuts import render
from app.forms import HowOld, HeyYou, Order

def heyyou(request):
    form = HeyYou(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name_data"]
        return render(request, "heyyou.html", {"form": form, "name": name})
    else:
        name = None
        return render(request, "heyyou.html", {"form": form})



    


def howold(request):
    form = HowOld(request.GET)
    if form.is_valid():
        end_year = form.cleaned_data["end_year"]
        birth_year = form.cleaned_data["birth_year"]
        age = end_year - birth_year
        return render(request, "howold.html", {"form": form, "end_year": end_year, "birth_year": birth_year, "age": age})
    else:
        end_year = None
        birth_year = None
        age = None
        return render(request, "howold.html", {"form": form})

    

def order(request):
    form = Order(request.GET)

    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = f"{burgers * 4.5 + fries * 1.5 + drinks * 1:.2f}"
        return render(request, "order.html", {"form": form, "burgers": burgers, "fries": fries, "drinks": drinks, "total": total})
    else:
        burgers = None
        fries = None
        drinks = None
        total = None
        return render(request, "order.html", {"form": form})
    
    


    











#from app.forms import AddForm, SignUpForm
#def root(request):

    #context = {}
    #if request.method == "POST":
        #form = SignUpForm(request.POST)
        #if form.is_valid():
            #context["signup_success"] = True
    #else:
        #form = SignUpForm()
    #context["form"] = form

    #return render(request, "root.html", context)
    
    
#def add(request):
    #form = AddForm(request.GET)
    #if form.is_valid():
        #x = form.cleaned_data["x"]
        #y = form.cleaned_data["y"]
        #z = form.cleaned_data["z"]
        #answer = x + y + z
        #return render(request, "add.html", { "form": form, "x": x, "y": x, "z": z, "answer": answer})
    #else:
        #return render(request, "add.html", {"form": form})
    
