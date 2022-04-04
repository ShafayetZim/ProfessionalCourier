from django.urls import include, path

from . import views

urlpatterns = [
    path('parcel-type',views.TypeView.as_view(), name='parcel-type'),  # type list
    path('parcel-type/new', views.add_type, name='new-parcel-type'),  # new-type
    path('edit-type/<int:pk>', views.TypeUpdateView.as_view(), name='edit-type'),  # edit-type
    path('delete-type/<int:id>', views.delete_type, name='delete-type'),  # delete-type
    # path('parcel-list',views.ParcelView.as_view(), name='parcel-list'),  # parcel list
    path('parcel-list', views.ParcelListView.as_view(), name="parcel-list"),  # parcel list
    path('print-invoice/<str:order_no>', views.print_invoice, name='print-invoice'),  # print invoice
    path('new', views.add_parcel, name='new-parcel'),  # new parcel
    path('edit-parcel/<str:pk>', views.ParcelUpdateView.as_view(), name='edit-parcel'),  # edit-parcel
    path('track-parcel/<str:pk>', views.TrackingView.as_view(), name='track-parcel'),  # track-parcel
    path('delete-invoice/<str:order_no>', views.invoice_delete, name='delete-invoice'),  # delete-type
    path('ajax/load-district/', views.load_district, name='ajax_load_district'),
    path('ajax/load-sub/', views.load_sub, name='ajax_load_sub'),
]