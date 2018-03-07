from django.conf.urls import url

from .views import AttachmentView, ObjectView

urlpatterns = [
    url(r'^add_attachment/$', AttachmentView.as_view()),
    url(r'^$', AttachmentView.as_view()),
    url(r'^create_object/$', ObjectView.as_view()),
]
