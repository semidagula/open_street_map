import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
"""This module provides functionality to check multiple data from a web page."""


class OpenStreetMap(unittest.TestCase):
    """ acest modul are ca scop testarea functionaliatii dupa cautare a adreselor """
    SEARCH_BOX = By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[1]/input"
    SEARCH_BUTTON = By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[1]/div/div[2]/input"
    FROM_BUTTON = By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[2]/div[2]/input"
    TO_BUTTON = By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a/img"
    ROUTE_BUTTON = By.XPATH, "/html/body/div/div[1]/div[1]/form[2]/div[4]/div[2]/input"
    ROUTE_CALC = By.XPATH, "/html/body/div/div[1]/div[1]/form[1]/div/div[2]/a"
    DISTANCE = By.XPATH, "/html/body/div/div[1]/div[5]/p[1]"
    FROM = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[2]/div[2]/div[2]/input")
    TO = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[2]/div[3]/div[2]/input")
    START = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[2]/div[4]/div[2]/input")
    DISTANCE1 = (By.XPATH, "//*[@id='sidebar_content']/p[1]")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.openstreetmap.org')
        self.driver.maximize_window()

    def test1_search_city(self):
        """testez cautarea unui oras"""
        self.driver.find_element(*self. SEARCH_BOX).send_keys("search_city")
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(3)
        result = self.driver.find_element(By.XPATH, '//div/ul/li/a[@data-id="2077868"]')
        assert result.text, 'Suceava, România'

    def test2_city_street(self):
        """testez cautarea unei strazi, oras"""
        self.driver.find_element(*self. SEARCH_BOX).send_keys("city_street")
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(3)
        res = self.driver.find_element(By.XPATH, '//div/ul/li/a[@data-id="25853887"]')
        assert res, 'Strada Narciselor, Zamca, Suceava, 720176, România'

    def test3_city_street_nr(self):
        """testez cautarea unei adrese dupa strada, nr, oras"""
        self.driver.find_element(*self. SEARCH_BOX).send_keys("city_street_nr")
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        time.sleep(3)
        rezultat = self.driver.find_element(By.XPATH, '//div/ul/li/a[@data-id="209362627"]')
        assert rezultat.text, 'Bulevardul 1 Mai, George Enescu, Suceava, 720238, România'

    def test4_distance_between_cities(self):
        """testez distanta dintre doua orase"""
        self.driver.find_element(*self.ROUTE_CALC).click()
        time.sleep(3)
        self.driver.find_element(*self.FROM).send_keys("from")
        self.driver.find_element(*self.TO).send_keys("to")
        self.driver.find_element(*self.START).click()
        time.sleep(3)
        distance = self.driver.find_element(*self.DISTANCE1).text
        assert distance, 'Distanță: 418km. Durată: 8:12.'

    def tearDown(self) -> None:
        """inchid browserul"""
        self.driver.quit()
