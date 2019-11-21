from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, main_page_view, logout, users_list


class TestUrls(SimpleTestCase):

    def test_home_page_urls_is_resolved(self):
        url = reverse('home')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, main_page_view)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_urls_is_resolved(self):
        url = reverse('register')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_register_status_code(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)

    def test_register_view_url_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_register_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_logout_urls_is_resolved(self):
        url = reverse('logout')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, logout)

    def test_logout_status_code(self):
        response = self.client.get('/logout/')
        self.assertEquals(response.status_code, 302)

    def test_logout_view_url_by_name(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)




