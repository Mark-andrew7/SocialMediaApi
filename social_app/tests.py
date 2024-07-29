from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm

# Create your tests here.
class ProfileManagementTests(TestCase):
  def setUp(self):
    self.client = Client()
    self.user = User.objects.create_user(username='testuser', email='test@example.com', password='1234')
    self.profile = Profile.objects.create(user=self.user, bio='Test bio', location='Test location')
    self.client.login(username='testuser', password='1234')

  def test_view_profile(self):
    response = self.client.get(reverse('view_profile', args=[self.user.username]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.profile.bio)
    self.assertContains(response, self.profile.location)

  def test_update_profile(self):
    response = self.client.post(reverse('create_or_update_profile'), {
      'bio': 'Updated bio',
      'location': 'Updated location'
    })
    self.assertEqual(response.status_code, 302)
    self.profile.refresh_from_db()
    self.assertEqual(self.profile.bio, 'Updated bio')
    self.assertEqual(self.profile.location, 'Updated location')

  def test_create_profile(self):
    new_user = User.objects.create_user(username='newuser', email='new@example.com', password='1234')
    self.client.login(username='newuser', password='1234')
    response = self.client.post(reverse('create_or_update_profile'), {
      'bio': 'New bio set',
      'location': 'User location set'
    })
    self.assertEqual(response.status_code, 302)
    new_profile = Profile.objects.get(user=new_user)
    self.assertEqual(new_profile.bio, 'New bio set')
    self.assertEqual(new_profile.location, 'User location set')

  def test_view_other_user_profile(self):
    other_user = User.objects.create_user(username='otheruser', email='other@example.com', password='abcd')
    other_profile = Profile.objects.create(user=other_user, bio='Other user bio', location='Other user location')
    response = self.client.get(reverse('view_profile', args=[other_user.username]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, other_profile.bio)
    self.assertContains(response, other_profile.location)