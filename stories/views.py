from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Story
from .forms import StoryForm


class AllStories(TemplateView):

    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()
        return render(request, 'AllStories.html', {
            'stories': stories,
        })


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


class Ajax(TemplateView):

    def post(self, request, *args, **kwargs):
        # TODO First, get the post data that we want

        # TODO If we get post data that is correct

            # Todo Use post data to do whatever it is that you want to do

        # Todo Render template with results
        pass