from django.urls import path
from .views import homeView,CursoListView,CursoCreateView,CursoUpdateView,CursoDeleteView, CursoDetailView
from .views import AlcanceCreateView, AlcanceUpdateView, AlcanceDeleteView
from .views import RecomendacionCreateView, RecomendacionUpdateView, RecomendacionDeleteView
from .views import CapituloCreateView, CapituloUpdateView, CapituloDeleteView
from .views import TemaCreateView, TemaUpdateView, TemaDeleteView
from .views import DetalleCreateView, DetalleUpdateView, DetalleDeleteView

visitante_patterns = ([
	path('', homeView),
	path('lista_cursos/', CursoListView.as_view(),name='lista_cursos'),
	path('nuevo_curso/', CursoCreateView.as_view(),name='nuevo_curso'),
	path('editar_curso/<int:pk>/', CursoUpdateView.as_view(),name='editar_curso'),
	path('borrar_curso/<int:pk>/', CursoDeleteView.as_view(),name='borrar_curso'),
	path('detalle_curso/<int:pk>/', CursoDetailView.as_view(),name='detalle_curso'),
	path('nuevo_alcance/', AlcanceCreateView.as_view(),name='nuevo_alcance'),
	path('editar_alcance/<int:pk>/',(AlcanceUpdateView.as_view()), name='editar_alcance'),
	path('borrar_alcance/<int:pk>/',(AlcanceDeleteView.as_view()), name='borrar_alcance'),
	path('nueva_recomendacion/', RecomendacionCreateView.as_view(),name='nueva_recomendacion'),
	path('editar_recomendacion/<int:pk>/',(RecomendacionUpdateView.as_view()), name='editar_recomendacion'),
	path('borrar_recomendacion/<int:pk>/',(RecomendacionDeleteView.as_view()), name='borrar_recomendacion'),
	path('nuevo_capitulo/', CapituloCreateView.as_view(),name='nuevo_capitulo'),
	path('editar_capitulo/<int:pk>/',(CapituloUpdateView.as_view()), name='editar_capitulo'),
	path('borrar_capitulo/<int:pk>/',(CapituloDeleteView.as_view()), name='borrar_capitulo'),
	path('nuevo_tema/',(TemaCreateView.as_view()), name='nuevo_tema'),
	path('editar_tema/<int:pk>/',(TemaUpdateView.as_view()), name='editar_tema'),
	path('borrar_tema/<int:pk>/',(TemaDeleteView.as_view()), name='borrar_tema'),
	path('nuevo_detalle/',(DetalleCreateView.as_view()), name='nuevo_detalle'),
	path('editar_detalle/<int:pk>/',(DetalleUpdateView.as_view()), name='editar_detalle'),
	path('borrar_detalle/<int:pk>/',(DetalleDeleteView.as_view()), name='borrar_detalle'),

],'visitante')
