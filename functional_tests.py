from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_shopping_list(self):

        # Joe has heard about this new site for comparison grocery shopping so
        # he checks out its homepage
        self.browser.get('http://localhost:8000')

        # Joe notices the title of the site in the browser window
        self.assertIn('Comparison Shopper', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Comparison Shopper', header_text)

        # Joe is invited to search for food products in his local area
        input_box = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter an item from your grocery list'
        )

        # Joe types "cheese" into a text box
        input_box.send_keys('cheese')

        # When Joe hits enter, the page updates, and now the page shows a list
        # of cheese prices from stores local to Joe
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Cheese' for row in rows),
            msg=f"Prices for cheese did not appear in the table.  Contents were: {table.text}"
        )

        # There is still a text box inviting Joe to enter another item.  Joe
        # types in "milk"
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('milk')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now both items appear, each with their
        # own list of prices
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Cheese', [row.text for row in rows],
            msg=f"Prices for cheese did not appear in the table after adding milk.  Contents were: {table.text}"
        )
        self.assertIn('Milk', [row.text for row in rows],
            msg=f"Prices for milk did not appear in the table.  Contents were: {table.text}"
        )

        # A third list appears on the right, listing a combined price for Joe's
        # list at each store in his area.

        self.fail('Finish the test!')


if __name__ == '__main__':
    main(warnings='ignore')
