from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *




features ={
           'family':['add_member', 'view_member', 'update_member', 'delete_member'], \
           'expense':['add_expenses', 'view_expenses', 'update_expense', 'delete_expense'], \
           'income':['add_income', 'view_income', 'update_income', 'delete_income'], \
           'payment':['add_payment_mode', 'view_payments_mode', 'update_payment_mode', 'delete_payment_mode'], \
           'cards':['add_card', 'view_cards', 'update_card', 'delete_card']
           }




class RootListView(APIView):

    def get(self, request, format=None):
        serializer_data = RootSerializer(Root.objects.all(), many=True).data
        return Response(serializer_data)

class RootDetailView(APIView):

    def get_object(self,pk):
        return Root.objects.get(id=pk)

    def get(self, request, pk, format=None):
        serializer_data = RootSerializer(Root.objects.filter(id=pk), many=True).data
        return Response(serializer_data)

    def post(self, request, format=None):
        serializer_data = None
        print(request.data)
        family = dict(request.data)
        family = Root(**family)
        family.save()
        serializer_data= RootSerializer(Root.objects.filter(id=family.id), many=True).data
        return Response(serializer_data)

    def delete(self, request, pk):
        root=self.get_object(pk)
        root.delete()
        return Response(RootSerializer(root).data)


class FamilyListView(APIView):
    def get(self, request, root_id, format=None):
        serializer_data = FamilySerializer(Family.objects.filter(family_id_id=root_id), many=True).data
        return Response(serializer_data)

class FamilyDetailView(APIView):

    def get_object(self, pk):
        pass


    def get(self, request, root_id, member_id, format=None):
        serializer_data=FamilySerializer(Family.objects.filter(id=member_id, family_id_id=root_id), many=True).data
        return Response(serializer_data)

    def post(self, request,root_id, format = None):
        serializer_data=None
        members=[]
        members_to_add = list(request.data)
        if not members_to_add:
            return Response("No members specified to be added")
        for member in members_to_add:
            member['family_id']=Root.objects.filter(id=root_id).first()
            member=Family(**member)
            members.append(member)
        try:
            serializer_data=FamilySerializer(Family.objects.bulk_create(members), many=True).data
            return Response(serializer_data)
        except Exception as e:
            return Response(e)

    def delete(self, request, root_id, member_id):
        member=Family.objects.get(id=member_id)
        member.delete()
        return Response(FamilySerializer(member).data)



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
