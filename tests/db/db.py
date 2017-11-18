import sys, os

# Add this project to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import unittest
from src.db import User, Role, Perm
import json

class TestUser(unittest.TestCase):
	
	def test_get_user_if_id_is_user1(self):
		user = User()
		lhs = json.dumps(user.get('user1'))
		rhs = '''{"id": "user1", "roles": ["role1", "role3"]}'''
		self.assertEqual(lhs, rhs)

	def test_get_user_if_id_is_none(self):
		user = User()
		lhs = json.dumps(user.get(None))
		rhs = 'null'
		self.assertEqual(lhs, rhs)

class TestRole(unittest.TestCase):
	
	def test_get_role_if_id_is_role1(self):
		role = Role()
		lhs = json.dumps(role.get('role1'))
		rhs = '''{"id": "role1", "permissions": ["perm1", "perm5"]}'''
		self.assertEqual(lhs, rhs)

	def test_get_role_if_id_is_none(self):
		role = Role()
		lhs = json.dumps(role.get(None))
		rhs = 'null'
		self.assertEqual(lhs, rhs)

	def test_set_role_perm_to_perm7_for_role1(self):
		role = Role()
		lhs = json.dumps(role.update('role1', {"permissions": ["perm7"]}))
		rhs = '''{"id": "role1", "permissions": ["perm7"]}'''
		self.assertEqual(lhs, rhs)

if __name__ == '__main__':
	unittest.main()
		