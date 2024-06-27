from django.views.generic import ListView, DetailView
from .models import Member

class MemberListView(ListView):
    model = Member
    template_name = 'member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'member_list.html'
    context_object_name = 'member'
