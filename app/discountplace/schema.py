import graphene
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Place


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class PlaceNode(DjangoObjectType):
    class Meta:
        model = Place
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'information': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )

class PlaceType(DjangoObjectType):
    class Meta:
        model = Place


class Query(AbstractType):
    """Note these are automatically camelCased by graphene"""
    place = relay.Node.Field(PlaceNode)
    places = graphene.List(PlaceType)

    all_places = DjangoFilterConnectionField(PlaceNode)

    def resolve_places(self, info, **kwargs):
        return Place.objects.all()
