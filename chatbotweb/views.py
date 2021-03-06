from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.db.models import Count

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

from chatbot.chat import ChatBot
from chatbotweb.serializers import UserSerializer, GroupSerializer, RegisterSerializer

from chatbotweb.models import ScraperCookieCatcher

def index(request):
    return render(request, '__chat.html')

def api_send_chat(request):

    currentUserId = ChatBot.getUserByFirstName(firstName='Божидар')

    chatbotResponse = ChatBot.Input(sentence=request.POST.get("input", ""), fromUserId=currentUserId);
    return HttpResponse(chatbotResponse)

def api_get_random_question(request):

    currentUserId = ChatBot.getUserByFirstName(firstName='Божидар')

    chatbotResponse = ChatBot.getRandomQuestion(forUserId=currentUserId);
    return HttpResponse(chatbotResponse)

def api_scraper_cookie_catcher(request):

    website_domain = request.GET.get("website_domain")

    cookiesList = []
    getCookies = ScraperCookieCatcher.objects.raw('SELECT * FROM chatbotweb_scrapercookiecatcher WHERE website_domain = %s ORDER BY catching_date DESC', [website_domain])
    for cookie in getCookies:
        cookiesList.append({
            "id":cookie.id,
            "website_domain":cookie.website_domain,
            "cookies_data":cookie.cookies_data,
            "catching_date":cookie.catching_date,
        })

    return JsonResponse(cookiesList, safe=False)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer