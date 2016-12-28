from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FamilySerializer
from .models import *
import json




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



class FamilyView(APIView):
    def get(self, request):
        serializer_data=None
        filters=dict(request.GET)
        if not filters:
            serializer_data=FamilySerializer(Family.objects.all(), many=True).data
        else:
            pass
        return Response(serializer_data)

    def post(self, request):
        serializer_data=None
        members=[]
        members_to_add = list(request.data)
        if not members_to_add:
            return Response("No members specified to be added")
        for member in members_to_add:
            member=Family(**member)
            members.append(member)
        try:
            serializer_data=FamilySerializer(Family.objects.bulk_create(members), many=True).data
            return Response("Created family members successfully")
        except Exception as e:
            return Response(e)

    def delete(self, request):
        filters=dict(request.GET)
        if not filters:
            return Response("Nothing to delete")


class IncomeView(APIView):
    def get(self, request):
        res=dict()
        filters= dict(request.GET)
        if not filters:
            res=Income.objects.all()
        else:
            pass

        return Response(json.dumps(res))

    def post(self, request):
        print(request.data)
        return Response("POST")