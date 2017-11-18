import sys, os

# Add this project to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import unittest
from src.db import Service
import json

class TestService(unittest.TestCase):
	
	def test_get_entitled_perms_by_user_id_with_user_id_user1(self):
		service = Service()
		lhs = json.dumps(service.get_entitled_perms_by_user_id('user1'))
		rhs = '''["perm1", "perm5", "perm6", "perm7"]'''
		self.assertEqual(lhs, rhs)

	def test_get_entitled_perms_by_user_id_with_user_id_none(self):
		service = Service()
		with self.assertRaises(TypeError):
			service.get_entitled_perms_by_user_id(None)

	def test_user_with_permission_exists_with_user1_perm1(self):
		service = Service()
		lhs = service.user_with_permission_exists('user1', 'perm1')
		rhs = False
		self.assertEqual(lhs, rhs)

	def test_user_with_permission_exists_with_none_perm1(self):
		service = Service()
		with self.assertRaises(TypeError):
			service.user_with_permission_exists(None, None)

	def test_modify_permission_of_role_role1(self):
		service = Service()
		lhs = json.dumps(
			service.modify_permission_of_role('role1', {"permissions": ["perm45"]})
		)
		rhs = '''{"id": "role1", "permissions": {"permissions": ["perm45"]}}'''
		self.assertEqual(lhs, rhs)

	def test_user_with_permission_exists_with_none_perm1(self):
		service = Service()
		with self.assertRaises(TypeError):
			service.modify_permission_of_role(None, None)

if __name__ == '__main__':
	unittest.main()
