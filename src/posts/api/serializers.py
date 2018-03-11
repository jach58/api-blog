from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    SerializerMethodField
    )


from posts.models import Post

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model= Post
        fields= [
            #'id',
            'title',
            #'slug',
            'content',
            'publish'
        ]

post_detail_url = HyperlinkedIdentityField(
        view_name = 'posts-api:detail',
        lookup_field = 'slug'
        )

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model= Post
        fields= [
            'url',
            'user',
            'image',
            'html',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'comments',
        ]

    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_html(self,obj):
        return obj.get_markdown()

    def get_comments(self,obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs,many=True).data
        return comments

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model= Post
        fields= [
            'url',
            'user',
            'slug',
            'title',
            'content',
            'publish',
        ]



"""

data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-02-2012",
    "slug": "yeahh-buddy",
}


new_item = PostSerializer(data=data):
    if new_item.is_valid():
        new_item.save()
    else:
        print(new_item.errors)


----UPDATE, DELETE shell---

obj = Post.objects.get(id=1)

data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-02-2012",
    "slug": "yeahh-buddy",
}


new_item = PostSerializer(obj,data=data):
    if new_item.is_valid():
        new_item.save()
    else:
        print(new_item.errors)

new_item.data

obj.delet()

"""