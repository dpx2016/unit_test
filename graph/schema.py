import unittest1.schema
# import games.schema
import graphene


class Query(unittest1.schema.Query, graphene.ObjectType):
    pass


class Mutation(unittest1.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
