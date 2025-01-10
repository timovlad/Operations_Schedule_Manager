from django.test import TestCase
from .forms import PatientForm, SurgeryForm
from .models import Doctor, Department, Patient, Surgery, OperatingRoom
from django.utils import timezone
from datetime import timedelta
from django.test import TestCase
from .forms import PatientForm, SurgeryForm
from .models import Doctor, Department, Patient, Surgery, OperatingRoom
from django.utils import timezone
from datetime import timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class ManagerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.department = Department.objects.create(name="Хирургия")

        self.doctor = User.objects.create_user(
            username="testdoctor",
            password="password123",
            department=self.department,
            first_name="Иван",
            last_name="Иванов"
        )
        self.client.login(username="testdoctor", password="password123")

        self.operating_room = OperatingRoom.objects.create(name="Операционная №1")

        self.surgery = Surgery.objects.create(
            surgery_name="Аппендэктомия",
            start_time=timezone.now() + timedelta(days=1),
            operating_room=self.operating_room
        )

        self.patient = Patient.objects.create(
            first_name="Петр",
            last_name="Петров",
            doctor=self.doctor,
            department=self.department,
            room_number=101,
            operation=self.surgery
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/index.html")

    def test_doctor_list_view(self):
        response = self.client.get(reverse("doctor_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/doctor_list.html")
        self.assertContains(response, "Иван Иванов")

    def test_patient_list_view(self):
        response = self.client.get(reverse("patient_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/patient_list.html")
        self.assertContains(response, "Петр Петров")

    def test_patient_create_view_get(self):
        response = self.client.get(reverse("patient_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/patient_form.html")

    def test_patient_create_view_post(self):
        data = {
            "first_name": "Анна",
            "last_name": "Сидорова",
            "doctor": self.doctor.id,
            "department": self.department.id,
            "room_number": 102,
            "operation": self.surgery.id
        }
        response = self.client.post(reverse("patient_create"), data)
        self.assertEqual(response.status_code, 302)  # Должно перенаправить
        self.assertRedirects(response, reverse("patient_list"))
        self.assertTrue(Patient.objects.filter(first_name="Анна", last_name="Сидорова").exists())

    def test_patient_update_view_get(self):
        response = self.client.get(reverse("patient_update", kwargs={"pk": self.patient.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/patient_form.html")

    def test_patient_update_view_post(self):
        data = {
            "first_name": "Петр",
            "last_name": "Иванов",
            "doctor": self.doctor.id,
            "department": self.department.id,
            "room_number": 103,
            "operation": self.surgery.id
        }
        response = self.client.post(reverse("patient_update", kwargs={"pk": self.patient.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("patient_list"))
        # Обновляем объект из базы данных
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.last_name, "Иванов")
        self.assertEqual(self.patient.room_number, 103)

    def test_patient_delete_view_get(self):
        response = self.client.get(reverse("patient_delete", kwargs={"pk": self.patient.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/patient_confirm_delete.html")

    def test_patient_delete_view_post(self):
        response = self.client.post(reverse("patient_delete", kwargs={"pk": self.patient.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("patient_list"))
        self.assertFalse(Patient.objects.filter(pk=self.patient.pk).exists())

    def test_surgery_list_view(self):
        response = self.client.get(reverse("surgery_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/surgery_list.html")
        self.assertContains(response, "Аппендэктомия")

    def test_surgery_create_view_get(self):
        response = self.client.get(reverse("surgery_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/surgery_form.html")

    def test_surgery_create_view_post(self):
        data = {
            "surgery_name": "Холецистэктомия",
            "start_time": timezone.now() + timedelta(days=2),
            "operating_room": self.operating_room.id
        }
        response = self.client.post(reverse("surgery_create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("surgery_list"))
        self.assertTrue(Surgery.objects.filter(surgery_name="Холецистэктомия").exists())

    def test_surgery_update_view_get(self):
        response = self.client.get(reverse("surgery_update", kwargs={"pk": self.surgery.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/surgery_form.html")

    def test_surgery_update_view_post(self):
        data = {
            "surgery_name": "Аппендэктомия (обновлено)",
            "start_time": timezone.now() + timedelta(days=3),
            "operating_room": self.operating_room.id
        }
        response = self.client.post(reverse("surgery_update", kwargs={"pk": self.surgery.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("surgery_list"))
        self.surgery.refresh_from_db()
        self.assertEqual(self.surgery.surgery_name, "Аппендэктомия (обновлено)")

    def test_surgery_delete_view_get(self):
        response = self.client.get(reverse("surgery_delete", kwargs={"pk": self.surgery.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Manager/surgery_confirm_delete.html")

    def test_surgery_delete_view_post(self):
        response = self.client.post(reverse("surgery_delete", kwargs={"pk": self.surgery.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("surgery_list"))
        self.assertFalse(Surgery.objects.filter(pk=self.surgery.pk).exists())

    def test_login_required_redirect(self):
        self.client.logout()
        protected_views = [
            reverse("doctor_list"),
            reverse("patient_list"),
            reverse("patient_create"),
            reverse("surgery_list"),
            reverse("surgery_create"),
        ]
        for url in protected_views:
            response = self.client.get(url)
            self.assertRedirects(response, f"{reverse("login")}?next={url}")




class PatientFormTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Кардиология")
        self.doctor = Doctor.objects.create_user(
            username="doc1",
            password="password123",
            first_name="Иван",
            last_name="Петров",
            department=self.department
        )
        self.operating_room = OperatingRoom.objects.create(name="Операционная №1")
        self.surgery = Surgery.objects.create(
            surgery_name="Операция на сердце",
            start_time=timezone.now() + timedelta(days=1),
            operating_room=self.operating_room
        )

    def test_valid_patient_form(self):
        data = {
            "first_name": "Андрей",
            "last_name": "Сидоров",
            "doctor": self.doctor.id,
            "department": self.department.id,
            "room_number": 101,
            "operation": self.surgery.id
        }
        form = PatientForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_patient_form_missing_fields(self):
        data = {}
        form = PatientForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_invalid_patient_form_invalid_room_number(self):
        data = {
            "first_name": "Андрей",
            "last_name": "Сидоров",
            "doctor": self.doctor.id,
            "department": self.department.id,
            "room_number": "abc",
            "operation": self.surgery.id
        }
        form = PatientForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("room_number", form.errors)


class SurgeryFormTest(TestCase):
    def setUp(self):
        # Создаем необходимые объекты для тестирования формы
        self.operating_room = OperatingRoom.objects.create(name="Операционная №1")

    def test_valid_surgery_form(self):
        data = {
            "surgery_name": "Удаление аппендикса",
            "start_time": timezone.now() + timedelta(days=1),
            "operating_room": self.operating_room.id
        }
        form = SurgeryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_surgery_form_past_start_time(self):
        data = {
            "surgery_name": "Удаление аппендикса",
            "start_time": timezone.now() - timedelta(days=1),  # Прошедшая дата
            "operating_room": self.operating_room.id
        }
        form = SurgeryForm(data=data)

    def test_invalid_surgery_form_missing_fields(self):
        data = {}
        form = SurgeryForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


