from rest_framework import routers
from monthly_expenses import views


router= routers.SimpleRouter()
router.register(r'family', views.FamilyViewSet)