import time

import random

import pytest


from element.check_box import CheckBox


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_check_box(self):
        check_box_page = CheckBox(self.driver)
        check_box_page.find_item().click()
        check_box_page.find_expand_all().click()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        actual_result_text = check_box_page.find_text()
        expected_result_text = check_box_page.expected_text
        assert actual_result_text == expected_result_text
        assert input_checkbox == output_result
