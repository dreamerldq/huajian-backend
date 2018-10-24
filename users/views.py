from django.shortcuts import render

# Create your views here.



def create_user(request):
    user_data = json.loads(request.body)
    user = User(
        username=user_data['userName'],
        password=user_data['password'],
        phone_number=user_data['phone_number'],
        email=user_data['email'],
        create_date=timezone.now()
    )
    user.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)


def edit_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.get(pk=id)
    user.username = user_data['username']
    user.password = user_data['password']
    user.email = user_data['email']
    user.phone_number = user_data['phone_number']
    user.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)




def get_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.filter(id=id)

    user_obj = query_set_to_dir(user)
    response = {
        'data': user_obj,
        'status': 'success'
    }
    return JsonResponse(response)


def delete_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.filter(id=id)
    user.delete()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)
