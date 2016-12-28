from rest_framework.viewsets import ModelViewSet

from .serializers import FamilySerializer
from .models import Family




features ={
           'family':['add_member', 'view_member', 'update_member', 'delete_member'], \
           'expense':['add_expenses', 'view_expenses', 'update_expense', 'delete_expense'], \
           'income':['add_income', 'view_income', 'update_income', 'delete_income'], \
           'payment':['add_payment_mode', 'view_payments_mode', 'update_payment_mode', 'delete_payment_mode'], \
           'cards':['add_card', 'view_cards', 'update_card', 'delete_card']
           }


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class=FamilySerializer
    #serializer= FamilySerializer(family_members, many=True)
    #return Responseserializer.data)
