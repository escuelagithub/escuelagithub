from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from core.models import curso

# Create your views here.
def homeView(request):
    mensaje_adicional = {'mensaje':'Este es un mensaje adicional'}
    return render(request, "home.html", mensaje_adicional)

class CursoListView(ListView):

    model = curso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        criterio = self.request.GET['criterio']
        lista = None
        if criterio =='*':
            lista = curso.objects.filter(completo=True)
        elif criterio != '':
            lista = curso.objects.filter(titulo__icontains = criterio,completo=True) | curso.objects.filter(descripcion__icontains=criterio,completo=True)

        context['lista'] = lista    

        return context    

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from core.forms import CursoForm
from django.shortcuts import HttpResponseRedirect

class CursoCreateView(CreateView):
    model = curso
    form_class = CursoForm
    template_name = 'visitante/curso_form.html'
    # success_url = reverse_lazy('core:home')

    def get_success_url(self):
        return reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_template'] = 'Registro de un nuevo Curso'
        return context          

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        User = request.user
        if form.is_valid():
            Curso = form.save(commit=False)
            Curso.profesor = User
            Curso.save()
            # Vuelve al visitante, profesor
            User = request.user
            if User.first_name == 'a':
                User.first_name = 'b'
            else:
                User.first_name = 'p'
            User.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'core/curso_form.html', {'form': form})

from django.views.generic.edit import UpdateView

class CursoUpdateView(UpdateView):
    model = curso
    form_class = CursoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('core:en_preparacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Curso = self.object
        context['titulo_template'] = 'Edicion de: '
        context['titulo'] = Curso.titulo
        # Lista de alcances
        context['lista_alcances'] = alcance.objects.filter(curso = Curso)
        # Lista de recomendaciones
        context['lista_recomendaciones'] = recomendacion.objects.filter(curso = Curso)
        # Lista de capitulo
        context['lista_capitulos'] = capitulo.objects.filter(curso = Curso)

        return context

from django.views.generic.edit import DeleteView

class CursoDeleteView(DeleteView):
    model = curso
    success_url = reverse_lazy('core:en_preparacion')

from django.views.generic.detail import DetailView
from django.contrib.auth.models import AnonymousUser

class CursoDetailView(DetailView):

    model = curso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estado = 'n'
        if not self.request.user ==  AnonymousUser():
            estado = 's'
        context['estado'] = estado
        context['reviews'] = 60
        # alcances
        context['lista_alcances'] = alcance.objects.filter(curso = self.object)
        # recomendaciones
        context['lista_recomendaciones'] = recomendacion.objects.filter(curso = self.object)

        return context

from .models import alcance
from .forms import AlcanceForm
from core.models import curso

class AlcanceCreateView(CreateView):
    model = alcance
    form_class = AlcanceForm

    def get_success_url(self,*args):
        print('args',args)
        return reverse_lazy('visitante:editar_curso', args=[args[0].id]) + '?correcto=ok'

    def get_context_data(self,**kwargs):
        context = super(AlcanceCreateView,self).get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id=self.request.GET['curso_id'])
        context['titulo_template'] = "Registro de un alcance"
        return context      

    def post(self,request,*args,**kwargs):
        Curso = curso.objects.get(id=request.POST['curso_id'])
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Alcance = form.save(commit=False)
            Alcance.curso = Curso
            Alcance.save()
            return HttpResponseRedirect(self.get_success_url(Curso))
        else:
            return render(request,'visitante/alcance_form.html',{'form':form,'curso':Curso,'titulo_template':'Registro de un alcance'})

class AlcanceUpdateView(UpdateView):
    model = alcance
    form_class = AlcanceForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.POST['curso_id']]) + '?correcto=ok'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id= self.request.GET['curso_id'])
        context['titulo_template'] = 'Edicion del alcance'
        context['titulo'] = self.object.descripcion

        return context

class AlcanceDeleteView(DeleteView):
    model = alcance
    # success_url = reverse_lazy('visitante:en_preparacion')

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.GET['curso_id']]) + '?correcto'

from .models import recomendacion
from .forms import RecomendacionForm

class RecomendacionCreateView(CreateView):
    model = recomendacion
    form_class = RecomendacionForm
    template_name = 'visitante/recomendacion_form.html'

    def get_success_url(self,*args):
        return reverse_lazy('visitante:editar_curso', args=[args[0].id]) + '?correcto'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        curso_post = curso.objects.get(id=request.POST['curso_id'])
        if form.is_valid():
            Recomendacion= form.save(commit=False)
            Recomendacion.curso = curso_post
            Recomendacion.save()
            return HttpResponseRedirect(self.get_success_url(curso_post))
        else:
            return render(request, 'visitante/alcance_form.html', {'form': form,'curso':curso_post})  

    def get_context_data(self,**kwargs):
        context = super(RecomendacionCreateView, self).get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id= self.request.GET['curso_id'])
        context['titulo_template'] = 'Registro de una recomendacion'

        return context

class RecomendacionUpdateView(UpdateView):
    model = recomendacion
    form_class = RecomendacionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.POST['curso_id']]) + '?correcto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id= self.request.GET['curso_id'])
        context['titulo_template'] = 'Edicion de la recomendacion'
        context['titulo'] = self.object.materia
        return context

class RecomendacionDeleteView(DeleteView):
    model = recomendacion
    # success_url = reverse_lazy('visitante:en_preparacion')

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.GET['curso_id']]) + '?correcto'


from .models import capitulo
from .forms import CapituloForm

class CapituloCreateView(CreateView):
    model = capitulo
    form_class = CapituloForm
    template_name = 'visitante/capitulo_form.html'

    def get_success_url(self,*args):
        return reverse_lazy('visitante:editar_curso', args=[args[0].id]) + '?correcto'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        curso_post = curso.objects.get(id=request.POST['curso_id'])
        if form.is_valid():
            Capitulo= form.save(commit=False)
            Capitulo.curso = curso_post
            Capitulo.save()
            return HttpResponseRedirect(self.get_success_url(curso_post))
        else:
            return render(request, 'visitante/alcance_form.html', {'form': form,'curso':curso_post})  

    def get_context_data(self,**kwargs):
        context = super(CapituloCreateView, self).get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id= self.request.GET['curso_id'])
        return context


class CapituloUpdateView(UpdateView):
    model = capitulo
    form_class = CapituloForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.POST['curso_id']]) + '?correcto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curso'] = curso.objects.get(id= self.request.GET['curso_id'])
        # Temas
        context['lista_temas'] = tema.objects.filter(capitulo = self.object)

        return context

class CapituloDeleteView(DeleteView):
    model = capitulo
    # success_url = reverse_lazy('visitante:en_preparacion')

    def get_success_url(self):
        return reverse_lazy('visitante:editar_curso', args=[self.request.GET['curso_id']]) + '?correcto'

from .models import tema
from .forms import TemaForm

class TemaCreateView(CreateView):
    model = tema
    form_class = TemaForm
    template_name = 'visitante/tema_form.html'

    def get_success_url(self,*args):
        return reverse_lazy('visitante:editar_capitulo', args=[args[0].id]) + '?curso_id=' + str(args[0].curso.id)  + '&correcto'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        capitulo_post = capitulo.objects.get(id=request.POST['capitulo_id'])
        if form.is_valid():
            Tema= form.save(commit=False)
            Tema.capitulo = capitulo_post
            Tema.save()
            return HttpResponseRedirect(self.get_success_url(capitulo_post))
        else:
            return render(request,'visitante/tema_form.html',{'form':form,'capitulo':capitulo_post})

    def get_context_data(self,**kwargs):
        context = super(TemaCreateView, self).get_context_data(**kwargs)
        context['capitulo'] = capitulo.objects.get(id= self.request.GET['capitulo_id'])
        return context

class TemaUpdateView(UpdateView):
    model = tema
    form_class = TemaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        curso_id =capitulo.objects.get(id=self.request.POST['capitulo_id']).curso.id
        return reverse_lazy('visitante:editar_capitulo', args=[self.request.POST['capitulo_id']]) + '?curso_id=' + str(curso_id) + '&correcto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['capitulo'] = capitulo.objects.get(id= self.request.GET['capitulo_id'])
        # Detalles
        # context['lista_detalles'] = detalle.objects.filter(tema = self.object)   
        lista = []
        for obj in detalle.objects.filter(tema = self.object):
            if obj.imagen != '':
                lista.append([obj,'imagen'])
            elif obj.media != '':
                lista.append([obj,'media'])
            elif obj.texto != '':
                lista.append([obj,'texto'])
            else:
                lista.append([obj,''])
        context['lista_detalles'] = lista

        return context

class TemaDeleteView(DeleteView):
    model = tema
    # success_url = reverse_lazy('visitante:en_preparacion')

    def get_success_url(self):
        curso_id =capitulo.objects.get(id=self.request.GET['capitulo_id']).curso.id
        return reverse_lazy('visitante:editar_capitulo', args=[self.request.GET['capitulo_id']]) + '?curso_id=' + str(curso_id) + '&correcto'

from .models import detalle
from .forms import DetalleForm
import os.path

class DetalleCreateView(CreateView):

    model = detalle
    form_class = DetalleForm
    template_name = 'visitante/detalle_form.html'

    def get_success_url(self,*args):
        return reverse_lazy('visitante:editar_tema', args=[args[0].id]) + '?capitulo_id=' + str(args[0].capitulo.id) + '&correcto'

    def post(self,request,*args,**kwargs):
        videos = ['.mp4','.ogv','.webM']
        audios = ['.mp3','.wav']
        textos = ['.txt','.odt','.docs','.pdf']
        form = self.form_class(request.POST)
        tema_post = tema.objects.get(id=request.POST['tema_id'])
        if form.is_valid():
            nombre = request.FILES.get('media')
            Detalle= form.save(commit=False)
            Detalle.tema = tema_post
            Detalle.nombrearchivo = nombre
            # nombre, extension = os.path.splitext(os.getcwd() + '/media/visitante/' + str(nombre))
            extension = os.path.splitext(os.getcwd() + '/media/visitante/' + str(nombre))[1]
            # videos
            for tipo in videos:
                if tipo == extension:
                    Detalle.tipoarchivo = 'v'
                    break
            # audios
            for tipo in audios:
                if tipo == extension:
                    Detalle.tipoarchivo = 'a'
                    break
            # textos
            for tipo in textos:
                if tipo == extension:
                    Detalle.tipoarchivo = 't'
                    break
            if Detalle.tipoarchivo == 'n':
                Detalle.media = None
                Detalle.nombrearchivo = ''
            Detalle.save()
            return HttpResponseRedirect(self.get_success_url(tema_post))
        return render(request, 'visitante/detalle_form.html', {'form': form})       

    def get_context_data(self,**kwargs):
        context = super(DetalleCreateView, self).get_context_data(**kwargs)
        context['tema'] = tema.objects.get(id= self.request.GET['tema_id'])
        return context    

class DetalleUpdateView(UpdateView):
    model = detalle
    form_class = DetalleForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        capitulo_id =tema.objects.get(id=self.request.POST['tema_id']).capitulo.id
        return reverse_lazy('visitante:editar_tema', args=[self.request.POST['tema_id']]) + '?capitulo_id=' + str(capitulo_id) + '&correcto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tema'] = tema.objects.get(id= self.request.GET['tema_id'])
        return context

    def post(self,request,*args,**kwargs):
        videos = ['.mp4','.ogv','.webM']
        audios = ['.mp3','.wav']
        textos = ['.txt','.odt','.docs','.pdf']
        self.object = self.get_object()
        form = self.get_form()
        Detalle = form.save(commit=False)
        nombre = request.FILES.get('media')
        Detalle.nombrearchivo = nombre
        # nombre, extension = os.path.splitext(os.getcwd() + '/media/visitante/' + str(nombre))
        extension = os.path.splitext(os.getcwd() + '/media/visitante/' + str(nombre))[1]
        # videos
        for tipo in videos:
            if tipo == extension:
                Detalle.tipoarchivo = 'v'
                break
        # audios
        for tipo in audios:
            if tipo == extension:
                Detalle.tipoarchivo = 'a'
                break
        # textos
        for tipo in textos:
            if tipo == extension:
                Detalle.tipoarchivo = 't'
                break
        if Detalle.tipoarchivo == 'n':
            Detalle.media = None
            Detalle.nombrearchivo = ''

        Detalle.save()

        return HttpResponseRedirect(self.get_success_url())

class DetalleDeleteView(DeleteView):
    model = detalle
    # success_url = reverse_lazy('visitante:en_preparacion')

    def get_success_url(self):
        capitulo_id =tema.objects.get(id=self.request.GET['tema_id']).capitulo.id
        return reverse_lazy('visitante:editar_tema', args=[self.request.GET['tema_id']]) + '?capitulo_id=' + str(capitulo_id) + '&correcto'

