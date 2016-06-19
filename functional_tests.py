from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# cd env/ -> source bin/activate
# python3 manage.py runserver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check home page
        self.browser.get('http://localhost:8000')

        #find web title and todo list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #input a item to todo list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #enter 'buy peacpck feathers' at placeholder
        #(intested:綁蒼蠅魚餌)
        inputbox.send_keys('Buy peacock feathers')

        #press Enter will refresh web
        #web show 1:Buy peacock feathers
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in talbe"
        )


        #still a placeholder for enter other item
        #enter ('use peacock feathers to 製作一隻蒼蠅')
        self.fail('Finish the test!')

        #web will refresh again, and show this two items

if __name__ == '__main__':
    unittest.main(warnings='ignore')
