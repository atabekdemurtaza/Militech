from django.test import TestCase
from post.models import Post 
from django.contrib.auth.models import User 

class PostTest(TestCase):

	@classmethod
	def setUp(cls):

		testuser = User.objects.create_user(username='testuser', password='123456')
		testuser.save()

		post_test = Post.objects.create(author=testuser, title='Test', content='A test')
		post_test.save()

	
	def test_post(self):

		post = Post.objects.get(id=1)
		author = f'{post.author}'
		title = f'{post.title}'
		content = f'{post.content}'
		self.assertEqual(author, 'testuser')
		self.assertEqual(title, 'Test')
		self.assertEqual(content, 'A test')
