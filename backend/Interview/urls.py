from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'), 
    path('join/', views.join_interview, name='join'),
    path('interview_test/', views.interview_test, name='interview_test'),
    path('interview/', views.index, name='interview'),
    path('no_questions_left/', views.no_questions_left, name='no_questions_left'),
    path('thankyouinterview/',views.endinterview, name="thankyouinterview"),
    path('question/<int:question_id>/', views.get_question, name='get_question'),
    path('start_transcription/', views.start_transcription, name='start_transcription'),
    path('stop_transcription/', views.stop_transcription, name='stop_transcription'),
    path('live_transcribe/', views.live_transcribe, name='live_transcribe'),
    path('get_question/', views.get_question, name='get_question'),
]