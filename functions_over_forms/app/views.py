from django.shortcuts import render
from app.forms import FontTimes, NoTeenSum, XyzThere, CenteredAverage

def font_times(request):
    form = FontTimes(request.GET)
    
    if form.is_valid():
        user_string = form.cleaned_data["string_input"]
        user_integer = form.cleaned_data["integer_input"]

        final_string = user_string[0:3] * user_integer

       


        return render(request, "fonttimes.html", { "form": form, "final_string": final_string})
    else:
        user_string = None
        user_integer = None
        final_string = None

        return render(request, "fonttimes.html", {"form": form})

def no_teen_sum(request):
    form = NoTeenSum(request.GET)

    if form.is_valid():
        user_int_1 = form.cleaned_data["integer_1"]
        user_int_2 = form.cleaned_data["integer_2"]
        user_int_3 = form.cleaned_data["integer_3"]

        final_sum = 0

        if user_int_1 in range(13, 20):
            user_int_1 = 0
            
        if user_int_2 in range(13, 20):
            user_int_2 = 0
            
        if user_int_3 in range(13, 20):
            user_int_3 = 0
        
        final_sum = user_int_1 + user_int_2 + user_int_3

        return render(request, "noteensum.html", {'form': form, 'final_sum': final_sum})
    else:
        user_int_1 = None
        user_int_2 = None
        user_int_3 = None
        final_sum = None

        return render(request, "noteensum.html", {"form": form})

        

    

def xyz_there(request):
    form = XyzThere(request.GET)

    if form.is_valid():
        user_given = form.cleaned_data["given_string"]

        if 'xyz' and '.xyz' not in user_given:
            user_given = True
        else:
            user_given = False
        

        return render(request, "xyzthere.html", {"form": form, "user_given": user_given})
    else:
        user_given = None

        return render(request, "xyzthere.html", {"form": form})

def centered_average(request):
    form = CenteredAverage(request.GET)

    if form.is_valid():
        # Initialize the user list with the given values, ensuring no None values are included
        user_list = [
            form.cleaned_data["given_amount_1"],
            form.cleaned_data["given_amount_2"],
            form.cleaned_data["given_amount_3"],
            form.cleaned_data["given_amount_4"],
            form.cleaned_data["given_amount_5"],
        ]

        # Append the 6th and 7th values only if they are not None or empty
        given_amount_6 = form.cleaned_data["given_amount_6"]
        given_amount_7 = form.cleaned_data["given_amount_7"]

        if given_amount_6 is not None and given_amount_6 != '':
            user_list.append(given_amount_6)
        if given_amount_7 is not None and given_amount_7 != '':
            user_list.append(given_amount_7)

        if len(user_list) > 2:
            
            user_list.sort()
            user_list = user_list[1:-1]  
            centered_avg = sum(user_list) / len(user_list) 
            centered_avg = int(centered_avg)
        else:
            centered_avg = None

        return render(request, "centeredaverage.html", {
            "form": form,
            "centered_avg": centered_avg
        })

    else:
        return render(request, "centeredaverage.html", {"form": form})



        
            

    


