from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def translate_app(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        print(txt)

        translator = Translator()
        tr = translator.translate(txt, dest='ig', src="auto")
        print(tr.text)
        #huasa_tr = translator.translate(txt, dest= 'ha')
        #igbo_tr = translator.translate(txt, dest='ig')
        #yoruba_tr = translator.translate(txt, dest='yo')
        
        return render(request, 'translate.html', {"result": tr})

    return render(request, 'translate.html')

