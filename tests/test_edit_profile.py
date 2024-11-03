from __future__ import annotations
import time
from typing import TYPE_CHECKING

from pages.profile_edit_media_page import EditMediaPage
from pages.edit_profile_page import EditProfilePage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from tests.base_test import BaseTest

if TYPE_CHECKING:
    from dto.user import User


class TestEditProfile(BaseTest):

    def test_edit_avatar(self, existing_user: User, avatar_img) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        edit_media_page = EditMediaPage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")

        # WHEN
        home_page.wait_title_contains()
        # Check that user auth_token cookie exist.
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        # THEN set and save new avatar image.
        edit_profile_page.avatar_form.send_keys(avatar_img)
        edit_media_page.apply_button.click()
        edit_profile_page.profile_save_button.click()

        # In case u need to see Twitter displays changes - uncomment "sleep".
        time.sleep(3)

    def test_edit_background(self, existing_user: User, background_img) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        edit_media_page = EditMediaPage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")

        # WHEN
        home_page.open()
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        # THEN set and save new background image.
        edit_profile_page.background_form.send_keys(background_img)
        edit_media_page.apply_button.click()
        edit_profile_page.profile_save_button.click()

        time.sleep(3)

    def test_edit_name(self, existing_user: User, faker) -> None:
        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")
        faker.random.seed()
        name_data = faker.name()

        # WHEN
        home_page.open()
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        edit_profile_page.name_form.click()
        edit_profile_page.name_form = name_data
        edit_profile_page.profile_save_button.click()
        time.sleep(2)

        # THEN check if name data was successfully changed.
        profile_page.open()
        profile_page.wait_title_contains()
        assert profile_page.user_first_last_name.text == name_data

    def test_edit_bio(self, existing_user: User, faker) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")
        faker.random.seed()
        bio_data = faker.job()

        # WHEN
        home_page.open()
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        edit_profile_page.bio_form.click()
        edit_profile_page.bio_form = bio_data
        edit_profile_page.profile_save_button.click()
        time.sleep(2)

        # THEN check if bio data was successfully changed.
        profile_page.open()
        profile_page.wait_title_contains()
        assert profile_page.user_bio.text == bio_data

    def test_edit_location(self, existing_user: User, faker) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")
        faker.random.seed()
        location_data = faker.country()

        # WHEN
        home_page.open()
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        edit_profile_page.location_form.click()
        edit_profile_page.location_form = location_data
        edit_profile_page.profile_save_button.click()
        time.sleep(2)

        # THEN check if location data was successfully changed.
        profile_page.open()
        profile_page.wait_title_contains()
        assert profile_page.user_location.text == location_data

    def test_edit_website(self, existing_user: User, faker) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        edit_profile_page = EditProfilePage(self.driver)
        profile_page = ProfilePage(self.driver,
                                   page_uri=f"/{existing_user.username}",
                                   title_contains=f" (@{existing_user.username}) / Twitter")
        faker.random.seed()
        website_data = faker.hostname()

        # WHEN
        home_page.open()
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.profile_button.click()
        profile_page.wait_title_contains()
        profile_page.edit_profile_button.click()

        edit_profile_page.website_form.click()
        edit_profile_page.website_form = website_data
        edit_profile_page.profile_save_button.click()
        time.sleep(2)

        # THEN check if website data was successfully changed.
        profile_page.open()
        profile_page.wait_title_contains()
        assert profile_page.user_website.text == website_data
