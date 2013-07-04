from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, get_list_or_404

from .models import Story
from .forms import StoryForm


class AllStories(TemplateView):

    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()[:5]
        return render(request, 'AllStories.html', {
            'stories': stories,
            'user': request.user,
        })

    def post(self, request, *args, **kwargs):
        # print request.POST
        searchWord = request.POST.get('search')
        if searchWord != '':
            listOfPosts = get_list_or_404(Story, title__contains=searchWord)
            return render(request, 'ajaxReturn.html', {
                'listOfPosts': listOfPosts,
            })
        else:
            pass


class MakeStory(TemplateView):

    def get(self, request, *args, **kwargs):
        form = StoryForm()
        return render(request, 'MakeForm.html', {
            'form': form,
        })

    def post(self, request):
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stories')
        else:
            return render(request, 'MakeForm.html', {
                'form': form,
            })