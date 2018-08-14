import graphene
import graphql_jwt

import developers.schema as ds
import users.schema as us

class Query(us.Query, ds.Query, graphene.ObjectType):
	pass
	
class Mutation(us.Mutation, ds.Mutation, graphene.ObjectType):
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()	

schema = graphene.Schema(query=Query, mutation=Mutation)
