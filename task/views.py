from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MasterTaskSerializer
from .models import MasterTasks
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import replyToTaskForm,rejectTaskForm
from .models import MasterTasks
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .operations import *

# Create your views here.


class MasterTaskDataView(APIView):
    def post(self,request):
        ser=MasterTaskSerializer(data=request.data)
        if ser.is_valid():
            MasterTasks.objects.create(cust_id=ser.data['cust_id'],quest_id=ser.data['quest_id'],title=ser.data['title'],category=ser.data['category'],
                                       question=ser.data['question'])
            return Response({"status":"Success"},status=200)
        return Response(ser.errors,status=400)

class PostDetailsView(DetailView):
    model = MasterTasks

@login_required()
def replyToTaskView(request,pk):
    if request.method=='POST':
        obj = get_object_or_404(MasterTasks, id=pk)
        form=replyToTaskForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            obj.status='SOLVED'
            obj.solvedBy=request.user.username
            obj.save()
            return redirect('profile')
    else:
        form=replyToTaskForm()

    return render(request,'task/reply.html',{'form':form})

@login_required()
def approveTaskView(request,pk):
    obj = get_object_or_404(MasterTasks, id=pk)
    obj.status = 'APPROVED'
    obj.approvedBy = request.user.username
    obj.save()
    StatusCallBack(obj)
    messages.success(request, f'Approved the Solution')
    return redirect('profile')

@login_required()
def rejectTaskView(request,pk):
    if request.method == 'POST':
        obj = get_object_or_404(MasterTasks, id=pk)
        form = rejectTaskForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            obj.status = 'REOPENED'
            obj.solvedBy = request.user.username
            obj.save()
            messages.warning(request, f'Rejected the Solution')
            return redirect('profile')
    else:
        form = rejectTaskForm()

    return render(request, 'task/reject.html', {'form': form})













