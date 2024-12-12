from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page request")
    friends=['Ankit','Rahul','Sanjiv']
    return JsonResponse(friends,safe=False)
    return HttpResponse("This is home page")

