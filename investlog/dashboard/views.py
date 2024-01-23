from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import InvestmentForm
from .models import InvestmentModel
import plotly.express as px


class OverviewView(LoginRequiredMixin, View):

    def get(self, request):
        context = {'user': request.user}
        return render(request, 'dashboard/overview.html', context=context)
    
class InvestmentsView(LoginRequiredMixin, View):
    model = InvestmentModel
    template_name = 'investments.html'
    
    def get(self, request):
        investments = InvestmentModel.objects.filter(user=self.request.user)
        context = {'user': request.user,
                   'investments': investments}
        return render(request, 'dashboard/investments.html', context=context)
    
class AddInvestmentView(LoginRequiredMixin, CreateView):
    model = InvestmentModel
    form_class = InvestmentForm
    template_name = 'dashboard/add-investment.html'
    success_url = reverse_lazy('investments')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Investment created successfully!')
        return super().form_valid(form)

    def get(self, request):
        form = InvestmentForm
        context = {'user': request.user}
        return render(request, 'dashboard/add-investment.html', {
            'context': context,
            'form': form
        })

class EditInvestmentView(LoginRequiredMixin, UpdateView):
    model = InvestmentModel
    form_class = InvestmentForm
    template_name = 'dashboard/edit-investment.html'

    def get_success_url(self):
        messages.success(self.request, 'Investment edited!')
        return reverse_lazy('investments')

class DeleteInvestmentView(LoginRequiredMixin, DeleteView):
    model = InvestmentModel
    template_name = 'dashboard/investments.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Investment deleted!')
        return reverse_lazy('investments')
    
class InvestmentGraphView(View):
    def get(self, request, *args, **kwargs):
        investments = InvestmentModel.objects.filter(user=request.user)

        labels = [investment.name for investment in investments]

        fig = px.bar(x=[investment.purchase_price for investment in investments], y=[investment.purchase_price for investment in investments])
        graph = fig.to_html()
    
        context = {'user': request.user,
                   'graph': graph}
        return render(request, 'dashboard/graphs.html', context)