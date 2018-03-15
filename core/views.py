#from django.http import HttpResponse
from django.shortcuts import render

def hi(request, w, x):
    s = w + x
    return render(request, 'hi.html',{
        's' : s,
    })
    #w = request.GET.get('w')
    #return HttpResponse(w+x)

def r(request, start, stop):
    if start>stop:
        start, stop = stop, start

        # x = start
        # start = stop
        # stop =x

    rr = range(start, stop + 1)
    if start > stop:
        rr = reversed(rr)
    return render(request, 'r.html', {
        'rr':rr,
    })