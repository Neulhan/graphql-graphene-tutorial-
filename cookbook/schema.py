import graphene

import ingredients.schema as ingredientsSchema


class Query(ingredientsSchema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

