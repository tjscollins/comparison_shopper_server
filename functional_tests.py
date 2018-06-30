from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_text_in_table(self, table_id, row_text, msg=None):
        """
        Checks the text of each row to see if a given row_text appears in any
        of them.
        """
        table = self.browser.find_element_by_id(table_id)
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows], msg=msg)

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

        self.check_for_row_text_in_table(
            'list_table', 'Cheese', 
            msg="Prices for cheese did not appear in the table."
        )

        # There is still a text box inviting Joe to enter another item.  Joe
        # types in "milk"
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('milk')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now both items appear, each with their
        # own list of prices
        self.check_for_row_text_in_table(
            'list_table', 'Cheese', 
            msg="Prices for cheese did not appear in the table after adding milk."
        )
        self.check_for_row_text_in_table(
            'list_table', 'Milk', 
            msg="Prices for milk did not appear in the table."
        )

        # A third list appears on the right, listing a combined price for Joe's
        # list at each store in his area.

        self.fail('Finish the test!')


if __name__ == '__main__':
    main(warnings='ignore')
