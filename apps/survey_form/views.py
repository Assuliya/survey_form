from django.shortcuts import render, redirect, HttpResponse


def index(request):
	return render(request, 'survey_form/index.html')


def survey(request):
	if request.method == "POST":

		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']

		try:
			request.session['times'] += 1
		except:
			request.session['times'] = 1

		return redirect('/send')
		
	else:
		return redirect('/')


def output(request):
	return render(request, 'survey_form/output.html')
