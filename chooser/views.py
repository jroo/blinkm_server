from chooser.models import CurrentScript
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def method_submit(request):
    cs = CurrentScript(script=int(request.POST['script_num']))
    cs.save()
    return HttpResponse(":p")
    
def current_script(request):
    cs = CurrentScript.objects.all().order_by('-id')[:1]
    return render_to_response("chooser/current_script.json", { 'command':cs[0] })
    
def reset(request):
    cs = CurrentScript(script=9)
    cs.save()
    return HttpResponseRedirect('/')
    