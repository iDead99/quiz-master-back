from rest_framework import routers
from . import views

router=routers.DefaultRouter()

router.register('masters', views.MasterViewSet, basename='master')
router.register('quizzes', views.QuizViewSet, basename='quiz')
router.register('questions', views.QuestionViewSet, basename='question')

urlpatterns = router.urls