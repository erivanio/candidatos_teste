# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.views.generic import CreateView
from apps.core.forms import CandidateForm
from apps.core.models import Candidate


class CandidateCreateView(CreateView):
    form_class = CandidateForm
    model = Candidate
    template_name = 'register.html'

    def form_valid(self, form):
        candidate = form.save()
        subject = 'Obrigado por se candidatar'
        content_front = 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato.'
        content_back = 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato.'
        content_mobile = 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato.'
        content_generic= 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato.'
        flag = False
        if candidate.html >= 7 and candidate.css >= 7 and candidate.javascript >= 7:
            email = EmailMessage(subject, content_front, to=[candidate.email])
            email.send()
            flag = True
        if candidate.python >= 7 and candidate.django >= 7:
            email = EmailMessage(subject, content_back, to=[candidate.email])
            email.send()
            flag = True
        if candidate.ios >= 7 and candidate.android >= 7:
            email = EmailMessage(subject, content_mobile, to=[candidate.email])
            email.send()
            flag = True
        if not flag:
            email = EmailMessage(subject, content_generic, to=[candidate.email])
            email.send()
        messages.success(self.request, 'Candidato cadastrado com sucesso!')
        return redirect('candidate_register')


