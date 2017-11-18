import os
import json

class Singleton(type):
	_instances = {}
	'''
	Metaclass to make another class behave as a singleton
	'''

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			print "collection loaded"
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class DB(object):
	__metaclass__ = Singleton

	storage = {}

	def __init__(self):
		super(DB, self).__init__()
		
	def _load(self, _file):
		# Load requested file and create a in-memory hash for
		# O(1) data fetch
		if not _file:
			raise Exception("No data file provided")
		
		_f = open(_file)
		data = json.loads(_f.read())
		_f.close()
		for user in data:
			self.storage[user['id']] = user

	def get(self, key):
		# Fetch the requested key and return
		return self.storage.get(key, None)

	def update(self, key, _update):
		if not isinstance(key, str):
			raise TypeError('Key must be a string')

		if not isinstance(_update, dict):
			raise TypeError('Update data must be a dict')

		data = self.storage.get(key, None)
		data.update(_update)
		try:
			self.storage[key] = data
		except KeyError, e:
			raise e
		
		return self.storage.get(key, None)

	def delete(self, _id):
		if not isinstance(_id, str):
			raise TypeError('param must be a string.')
		
		try:
			del self.storage[_id]
		except KeyError, e:
			raise e
		return True


class User(DB):
	"""docstring for User"""

	_file_path = os.path.dirname(os.path.abspath(__file__)) + "/data/users.json"

	def __init__(self):
		super(User, self).__init__()
		self._load(self._file_path)

class Role(DB):
	"""docstring for Role"""

	_file_path = os.path.dirname(os.path.abspath(__file__)) + "/data/roles.json"

	def __init__(self):
		super(Role, self).__init__()
		self._load(self._file_path)

class Perm(DB):
	"""docstring for Perm"""

	_file_path = os.path.dirname(os.path.abspath(__file__)) + "/data/permissions.json"

	def __init__(self):
		super(Perm, self).__init__()
		self._load(self._file_path)
