from tastypie.resources import ModelResource
from .models import Posts


class PostsResource(ModelResource):
    class Meta:
        queryset = Posts.objects.all()
        resource_name = 'posts'
