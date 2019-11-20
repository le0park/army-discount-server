import graphene
from discountplace import schema as discountplace_schema


class Query(
        discountplace_schema.Query,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)