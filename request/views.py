# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Request
from .forms import RequestForm
from meals.models import Meals, MealsFoodStock
from django.contrib.auth.decorators import login_required
from receiver.models import Receiver


@login_required(login_url='receiver_login')
def request_food(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Get the quantity requested by the receiver
            requested_quantity = form.cleaned_data['quantity']
            print(requested_quantity)

            # Get the meal associated with the request
            #meal_id = request.POST.get('meal_id')  # Assuming you have a hidden input in your form for meal_id
            meal_f = MealsFoodStock.objects.filter(quantity__gt=0).first()
            print(meal_f)
            #m_id = meal_f.meals_id
            #print('Meal:', m_id)
            #meal = MealsFoodStock.objects.get(meals__id=m_id)

            if meal_f:
                m_id = meal_f.meals_id
                print('Meal:', m_id)
                combo_meals = MealsFoodStock.objects.filter(meals_id=m_id)
                if combo_meals:
                    # Check if there is enough quantity available in any of the combo meals
                    total_quantity_available = sum(meal.quantity for meal in combo_meals)
                    # Check if there is enough quantity available
                    print(total_quantity_available)
                    if requested_quantity <= total_quantity_available:
                        # Retrieve the Receiver instance associated with the logged-in user
                        receiver = Receiver.objects.get(user=request.user)
                        # Allocate the requested quantity to the receiver
                        for meal in combo_meals:
                            meal.quantity -= requested_quantity
                            meal.save()

                        # Create a Request entry for the receiver
                        new_request = Request(
                            status='Pending',
                            meals_food_stock=meal,
                            receiver=receiver,  # Adjust based on your user model
                            quantity=requested_quantity
                        )
                        new_request.save()

                        # Redirect to a success page or do other necessary actions
                        return redirect('request_list')
                    else:
                        # Not enough quantity available, handle this case
                        messages.error(request, 'Not enough quantity available for the requested items.')
            else:
                # Handle the case where the meal is not found
                messages.error(request, 'Combo Meal not found.')

    else:
        form = RequestForm()

    return render(request, 'request/request_food.html', {'form': form})

'''@login_required(login_url='receiver_login')
def request_food(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Get the quantity requested by the receiver
            requested_quantity = form.cleaned_data['quantity']

            # Find the nearest expiry MealsFoodStock
            nearest_expiry_stock = MealsFoodStock.objects.filter(
                quantity__gte=requested_quantity,
                food_stock__total_quantity__gte=requested_quantity,
            ).order_by('food_stock__food_name').first()

            if nearest_expiry_stock:
                receiver = Receiver.objects.get(user=request.user)
                # Create a new request with the selected MealsFoodStock
                new_request = Request(
                    status='Pending',
                    meals_food_stock=nearest_expiry_stock,
                    receiver=receiver,
                    quantity=requested_quantity,
                )
                new_request.save()

                # Update the quantity of the MealsFoodStock
                nearest_expiry_stock.quantity -= requested_quantity
                nearest_expiry_stock.save()

                return redirect('request_list')
    else:
        form = RequestForm()

    return render(request, 'request/request_food.html', {'form': form})'''


@login_required(login_url='receiver_login')
def request_list(request):
    receiver = Receiver.objects.get(user=request.user)
    requests = Request.objects.filter(receiver=receiver)
    return render(request, 'request/request_list.html', {'requests': requests})


