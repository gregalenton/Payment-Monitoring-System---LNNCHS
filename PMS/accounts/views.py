from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.views import generic
from . import forms
from django.core.urlresolvers import (reverse_lazy, reverse)
from django.contrib.auth.decorators import login_required
from funds.models import Due, Receipt



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))


def user_login(request):
    if request.user.is_authenticated():
        return render_to_response('accounts/homepage-admin.html')
    else:
        context = RequestContext(request)

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render_to_response('accounts/homepage-admin.html', {}, context)
                else:
                    return HttpResponse("Account disabled.")
            else:
            
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        else:

            return render_to_response('accounts/login.html', {}, context)


class HomeView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('accounts/home.html', {}, {})


class AdminHomeView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('accounts/homepage-admin.html')


class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class AddStudentView(LoginRequiredMixin, generic.CreateView):

    template_name = 'accounts/add_student.html'
    form_class = forms.AddStudentForm
    model = models.StudentInfo

    def form_valid(self, form):
        student = form.save(commit=False)      
        due = Due.objects.all()
        total = 0

        if len(due) > 0:
            for d in due:
                total = d.due_cost+total

        student.student_toPay = total

        return super(AddStudentView, self).form_valid(form)

    def get_success_url(self):
 
        return reverse('funds:changessaved')


class EditStudentView(LoginRequiredMixin, generic.UpdateView):
    model = models.StudentInfo
    template_name = 'accounts/edit_student.html'
    fields = ['student_lastname', 'student_firstname', 'student_middlename',
              'student_birthday', 'student_year', 'student_section',
              'student_gender', 'student_address', 'student_guardian',
              'student_guardian_contact', 'student_guardian_address', 'student_scholarship',
              'student_sibling', 'student_bandMem']


    def get_success_url(self):
        return reverse('funds:changessaved')

    def get_context_data(self, **kwargs):

        context = super(EditStudentView, self).get_context_data(**kwargs)
        context['action'] = reverse('accounts:editstudent',
                                    kwargs={'pk': self.get_object().student_id})

        return context


class SearchStudentView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('accounts/search_student.html') 

    # def StudentInfoView(request):
    #     if 'input' in request.GET and request.GET['input']:
    #         inp = request.GET['input']
    #         student = models.StudentInfo.objects.get(student_lastname=inp)
    #         return render(request, 'accounts/search_studentinfo_result.html',
    #             {'student': student, 'query': inp})
    #     else:
    #         return HttpResponseRedirect('/accounts/displaysearchresults/')   


class ViewStudentInfoView(LoginRequiredMixin, generic.DetailView):
    model = models.StudentInfo
    template_name = 'accounts/studentinfo_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super(ViewStudentInfoView, self).get_context_data(**kwargs)
        context['action'] = reverse('accounts:viewstudentinfo',
                                    kwargs={'pk': self.get_object().student_id})

        return context


class ViewAllStudentsView(LoginRequiredMixin, generic.ListView):
    model = models.StudentInfo
    template_name = 'accounts/viewallstudents.html'


class StudentsWithLiabilitiesView(LoginRequiredMixin, generic.ListView):
    model = models.StudentInfo
    template_name = 'accounts/students_with_liabilities.html'

    def get_context_data(self, **kwargs):

        context = super(StudentsWithLiabilitiesView, self).get_context_data(**kwargs)        
        students = models.StudentInfo.objects.all()

        total = 0
        stud = []

        for s in students:
            if s.student_toPay != 0:
                stud.append(s)

        context['stud'] = stud

        return context


class CreatePaymentView(LoginRequiredMixin, generic.CreateView):
    template_name = 'accounts/create_payment.html'
    form_class = forms.CreatePaymentForm


    def form_valid(self, form):
        student_id = form.cleaned_data['student_id']
        paying = form.cleaned_data['amount']
        student = models.StudentInfo.objects.get(student_id=student_id.student_id)
        toPay = student.student_toPay
        if toPay != 0:
            dif = toPay-paying
            student.student_toPay = dif
            paid = student.student_paid
            total = paid+paying
            student.student_paid = total
            student.save()
            #return render_to_response('accounts/receiptinfo.html', )
        else:
            #please change this one to some template :)
            return HttpResponse("Student already paid full.")

        return super(CreatePaymentView, self).form_valid(form)

    def get_context_data(self, **kwargs):

        context = super(CreatePaymentView, self).get_context_data(**kwargs)
        context['action'] = reverse('accounts:receiptinfo')

        return context

    def get_success_url(self):
        return reverse('accounts:receiptinfo')

    #     return reverse('accounts:receiptinfo', kwargs={'receipt_id': self.kwargs['receipt_id']})

class EnterDiscountView(LoginRequiredMixin, generic.CreateView):
    template_name = 'accounts/create_payment.html'
    form_class = forms.CreatePaymentForm

    def form_valid(self, form):
        student_id = form.cleaned_data['student_id']
        paying = form.cleaned_data['amount']
        student = models.StudentInfo.objects.get(student_id=student_id.student_id)
        toPay = student.student_toPay
        if toPay != 0:
            dif = toPay-paying
            student.student_toPay = dif
            student.save()
        else:
            #please change this one to some template :)
            return HttpResponse("Student already paid full.")
        return super(EnterDiscountView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:receiptinfo')


class ReceiptInfoView(LoginRequiredMixin, generic.TemplateView):

    def get(self, request):
        return render(request, 'accounts/receiptinfo.html')
    # template_name = 'accounts/receiptinfo.html'
    # context_object_name = 'receipt'

    # def get_context_data(self, **kwargs):
    #     context = super(ReceiptInfoView, self).get_context_data(**kwargs)
    #     context['action'] = reverse('accounts:receiptinfo',
    #                                 kwargs={'pk': self.get_object().receipt_id})

    #     return context


class ChangeSchoolYearView(LoginRequiredMixin, generic.DeleteView):
    def get(self, request):
        year = "12"
        #models.StudentInfo.objects.filter(student_year=year).delete()
        students = models.StudentInfo.objects.all()

        if len(students) > 0:
            for s in students:
                if s.student_year == "7":
                    if s.student_toPay == 0:
                        s.student_year = "8"
                elif s.student_year == "8":
                    if s.student_toPay == 0:
                        s.student_year = "9"
                elif s.student_year == "9":
                    if s.student_toPay == 0:
                        s.student_year = "10"
                elif s.student_year == "10":
                    if s.student_toPay == 0:
                        s.student_year = "11"
                elif s.student_year == "11":
                    if s.student_toPay == 0:
                        s.student_year = "12"
                s.save()
                if s.student_year =="12":
                    if s.student_toPay == 0:
                        models.StudentInfo.objects.filter(student_id=s.student_id).delete()

        return render(request, 'funds/changessaved.html',)


def DisplaySearchResults(request):
    if request.user.is_authenticated():
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            students = models.StudentInfo.objects.filter(student_lastname=inp)
            return render(request, 'accounts/search_student_result.html',
                {'students': students, 'query': inp})
        else:
            return HttpResponseRedirect('/accounts/searchstudent/')
    else:
        return HttpResponseRedirect('/accounts/login')


def DisplayResults(request):
    if request.user.is_authenticated():
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            students = models.StudentInfo.objects.filter(student_id=inp)
            return render(request, 'accounts/create_payment_result.html',
                {'students': students, 'query': inp})
        else:
            return HttpResponseRedirect('/accounts/createpayment/')
    else:
        return HttpResponseRedirect('/accounts/login')

