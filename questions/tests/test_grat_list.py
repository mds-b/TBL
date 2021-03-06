from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from core.test_utils import check_messages
from model_mommy import mommy
from questions.models import (
    Question, Alternative, ExerciseSubmission,
    IRATSubmission, GRATSubmission
)

User = get_user_model()


class ListGRATTestCase(TestCase):
    """
    Test to list question into GRAT test.
    """

    def setUp(self):
        """
        This method will run before any test case.
        """

        pass

    def tearDown(self):
        """
        This method will run after any test.
        """

        pass

    def test_redirect_to_login(self):
        """
        User can not see the irat test without logged in.
        """

        pass

    def test_grat_test_pagination(self):
        """
        Test to show question by pagination.
        """

        pass

    def test_users_can_see_the_grat_list(self):
        """
        User like students, monitors and teacher can see the grat test
        with not exercise questions and when the date of grat arrive.
        """

        pass

    def test_users_can_not_see_the_grat_test(self):
        """
        User like students and monitors can not see the grat test if the
        time is behind date/time of grat teste or time is after date/time
        of grat test with its duration.
        """

        pass

    def test_only_teacher_can_change_weight_and_time(self):
        """
        Only teacher can change the grat test weight and duration.
        """

        pass

    def test_only_teacher_can_change_date_and_time(self):
        """
        Only teacher can change date and time from grat test.
        """

        pass

    def test_date_and_time_not_can_be_blank(self):
        """
        The date and time of grat test not can be blank.
        """

        pass

    def test_date_and_time_need_to_be_bigger_than_today(self):
        """
        The date and time from grat test need to be bigger than the
        date and time from today and bigger than irat test date/time with its
        duration.
        """

        pass
