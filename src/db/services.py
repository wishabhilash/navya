from db import User, Role, Perm

class Service(object):
	"""docstring for Service"""
	def __init__(self):
		super(Service, self).__init__()

	def get_entitled_perms_by_user_id(self, _id):
		_perms = []
		user = User()
		for role in user.get(_id)['roles']:
			role_obj = Role()
			_role = role_obj.get(role)
			_perms += _role['permissions']
		return _perms
		
	def user_with_permission_exists(self, _id, perm_id):
		_user_with_perm_exists = False
		user = User()
		for role in user.get(_id)['roles']:
			role_obj = Role()
			_role = role_obj.get(role)
			if perm_id in _role['permissions']:
				_user_with_perm_exists = True
				break
		return _user_with_perm_exists

	def modify_permission_of_role(self, role_id, perms):
		role = Role()
		return role.update(role_id, {"permissions": perms})

	def delete_permission(self, perm_id):
		perm = Perm()
		return perm.delete(perm_id)

