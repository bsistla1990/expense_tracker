from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect

from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import *
from .models import *




features ={
           'family':['add_member', 'view_member', 'update_member', 'delete_member'], \
           'expense':['add_expenses', 'view_expenses', 'update_expense', 'delete_expense'], \
           'income':['add_income', 'view_income', 'update_income', 'delete_income'], \
           'payment':['add_payment_mode', 'view_payments_mode', 'update_payment_mode', 'delete_payment_mode'], \
           'cards':['add_card', 'view_cards', 'update_card', 'delete_card']
           }




class LoginView(APIView):
    def post(self,request):
        user=dict(request.data)
        user=Family.objects.filter(login_name=user['login_name'])
        if not user:
            return Response("Login Failed")
        print(dir(request))
        print(request.user)
        return Response(FamilySerializer(user, many=True).data)






class RootListView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/root_list.html'

    def get(self, request, format=None):
        roots=Root.objects.all()
        serializer_data = RootSerializer(roots, many=True).data
        return Response({'roots':serializer_data})

class RootDetailView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/root_detail.html'

    def get_object(self,pk):
        return Root.objects.get(id=pk)

    def get(self, request, pk, format=None):
        serializer_data = RootSerializer(Root.objects.filter(id=pk), many=True).data
        print(serializer_data)
        return Response({'root':serializer_data})

    def post(self, request, format=None):
        family = dict(request.data)
        for root in family['name']:

            family = Root(name=root)
            family.save()
        serializer_data= RootSerializer(Root.objects.filter(id=family.id), many=True).data
        #return Response(serializer_data)
        return redirect('list_root')

    def put(self, request, format=None):
        pk=request.data
        print(pk)
        pk=pk['id']
        root = self.get_object(pk)
        serializer = RootSerializer(root, data=request.data)
        serializer.save()


    def delete(self, request, pk):
        root=self.get_object(pk)
        root.delete()
        return Response(RootSerializer(root).data)


class FamilyListView(APIView):
    def get(self, request, root_id, format=None):
        serializer_data = FamilySerializer(Family.objects.filter(root=root_id), many=True).data
        return Response(serializer_data)

class FamilyDetailView(APIView):

    def get(self, request, member_id, format=None):
        serializer_data=FamilySerializer(Family.objects.filter(id=member_id), many=True).data
        return Response(serializer_data)

    def post(self, request,format = None):
        members=[]
        members_to_add = list(request.data)
        if not members_to_add:
            return Response("No members specified to be added")
        for member in members_to_add:
            #Need to change this logic
            root_id=1

            member['root']=Root.objects.filter(id=root_id).first()
            member=Family(**member)
            members.append(member)
        serializer_data=FamilySerializer(Family.objects.bulk_create(members), many=True).data
        return Response(serializer_data)

    def delete(self, request, member_id):
        member=Family.objects.get(id=member_id)
        member.delete()
        return Response(FamilySerializer(member).data)



class IncomeListView(APIView):
    def get(self, request, root_id, format=None):
        serializer_data = []
        family_members=Family.objects.filter(root=root_id)
        for member in family_members:
            income=IncomeSerializer(Income.objects.filter(earned_by=member.id), many=True).data
            serializer_data.append(income)
        return Response(serializer_data)

class IncomeFilterView(APIView):
    def post(self, request):
        pass

class IncomeDetailView(APIView):
    def get(self, request, income_id):
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




class ExpenseListView(APIView):
    def get(self, request, root_id, format=None):
        serializer_data = []
        family_members=Family.objects.filter(root=root_id)
        for member in family_members:
            income=IncomeSerializer(Income.objects.filter(earned_by=member.id), many=True).data
            serializer_data.append(income)
        return Response(serializer_data)

class ExpenseFilterView(APIView):
    def post(self, request):
        pass

class ExpenseDetailView(APIView):
    def get(self, request, income_id):
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