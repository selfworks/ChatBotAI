from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    registration_date = models.DateTimeField('date published')

class UserPersonality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    personality_key = models.CharField(max_length=200)
    personality_value = models.CharField(max_length=200)

class ChatbotQuestionSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    question_key = models.CharField(max_length=200, default='')
    asked_question_date = models.DateTimeField('date published')

class ChatbotConversations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_date = models.DateTimeField('date published')
    finishing_date = models.DateTimeField('date published', null=True)

class ChatbotPersonality(models.Model):
    personality_key = models.CharField(max_length=200)
    personality_value = models.CharField(max_length=200)

class ScraperCookieCatcher(models.Model):
    cookies_data = models.JSONField()
    website_domain = models.CharField(max_length=200, null=True)
    catching_date = models.DateTimeField('date published')