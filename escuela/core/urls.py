from django.urls import path
from .views import homeView, NuevoCursoView,DetalleCursoView,ListaCursosView, EnPreparacionView
from .views import EditarCursoView, BorrarCursoView
from .views import DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView
from .views import InscripcionView, EstudioView, ConstruidoView

core_patterns=([
	path('',homeView,name="home"),
	path('nuevoCurso/',NuevoCursoView,name="nuevoCurso"),
	path('detalle_curso/<int:pk>/', DetalleCursoView,name='detalle_curso'),
	path('lista_cursos/', ListaCursosView,name='lista_cursos'),
	path('en_preparacion/', EnPreparacionView,name='en_preparacion'),
	path('editar_curso/<int:pk>/', EditarCursoView,name='editar_curso'),
	path('borrar_curso/<int:pk>/', BorrarCursoView,name='borrar_curso'),
	path('lista_disciplinas/', DisciplinaListView.as_view(),name='lista_disciplinas'),
	path('nueva_disciplina/', DisciplinaCreateView.as_view(),name='nueva_disciplina'),
	path('editar_disciplina/<int:pk>/', DisciplinaUpdateView.as_view(),name='editar_disciplina'),
	path('borrar_disciplina/<int:pk>/', DisciplinaDeleteView.as_view(),name='borrar_disciplina'),
	path('inscripcion/<int:curso>/', InscripcionView,name='inscripcion'),
	path('estudio/<int:curso>/', EstudioView,name='estudio'),
	path('construido/', ConstruidoView,name='construido'),
],'core')