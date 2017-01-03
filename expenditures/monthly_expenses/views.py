from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout

from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import *
from .models import *




features ={
           'root' :['add_root', 'view_root', 'update_root', 'delete_root'], \
           'family':['add_member', 'view_member', 'update_member', 'delete_member'], \
           'expense':['add_expenses', 'view_expenses', 'update_expense', 'delete_expense'], \
           'income':['add_income', 'view_income', 'update_income', 'delete_income'], \
           'payment':['add_payment_mode', 'view_payments_mode', 'update_payment_mode', 'delete_payment_mode'], \
           'cards':['add_card', 'view_cards', 'update_card', 'delete_card']
           }
"""

features ={
           'root' : 'list_root' \
           'family':
           'expense':['add_expenses', 'view_expenses', 'update_expense', 'delete_expense'], \
           'income':['add_income', 'view_income', 'update_income', 'delete_income'], \
           'payment':['add_payment_mode', 'view_payments_mode', 'update_payment_mode', 'delete_payment_mode'], \
           'cards':['add_card', 'view_cards', 'update_card', 'delete_card']
           }

"""





class HomeView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/index.html'

    def get(self, request, format=None):
        print("home view",request.user)
        if request.user.is_anonymous():
            return redirect('login_view')
        links=features.keys()
        return Response({'features':list(links)})


class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/login.html'

    def get(self, request, format=None):
        if not request.user.is_anonymous():
            return redirect('index_view')
        return Response()


class LoginValidationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/index.html'


    def post(self,request):
        creds=dict(request.data)
        if not request.user.is_anonymous():
            return redirect('home_view')
        user = authenticate(username=creds['user_name'][0], password=creds['password'][0])
        print("user is",user)
        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            return Response("Invalid Login")


class LogOutView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/login.html'

    def get(self ,request):
        logout(request)
        return Response({'status':'Logout Successful'})






class RootListView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/root_list.html'

    def get(self, request, format=None):
        print(dir(request.session))
        print(request.session.session_key)
        print(request.session.items())
        print(request.session.values())
        print(request.session.keys())
        serializer_data=[]
        roots = Root.objects.all()
        roots = RootSerializer(roots, many=True).data
        for root in roots:
            root=dict(root)
            serializer_data.append(root)
        serializer_data=sorted(serializer_data , key=lambda k: k['id'])
        return Response({'roots':serializer_data})

class RootUpdateView(APIView):

    def post(self, request):
        pk = request.data
        root = Root.objects.get(id=pk['id'])
        root.name=pk['name']
        serializer = RootSerializer(root, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('list_root')
        return Response("Exception")

class RootDeleteView(APIView):

    def post(self,request):
        pk = request.data
        root = Root.objects.get(id=pk['id'])
        root.delete()
        return redirect('list_root')

class RootDetailView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'monthly_expenses/root_detail.html'


    def get(self, request, pk, format=None):
        serializer_data = RootSerializer(Root.objects.filter(id=pk), many=True).data
        serializer_data= serializer_data[0]
        serializer_data = dict(serializer_data)
        return Response({'root':serializer_data})



########################################################################################################################


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
