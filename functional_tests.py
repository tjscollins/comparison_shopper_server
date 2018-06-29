from unittest import TestCase, main
from selenium import webdriver


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

        # Joe is invited to search for food products in his local area

        # Joe types "cheese" into a text box

        # When Joe hits enter, the page updates, and now the page shows a list
        # of cheese prices from stores local to Joe

        # There is still a text box inviting Joe to enter another item.  Joe
        # types in "milk"

        # The page updates again, and now both items appear, each with their
        # own list of prices

        # A third list appears on the right, listing a combined price for Joe's
        # list at each store in his area.

        self.fail('Finish the test!')


if __name__ == '__main__':
    main(warnings='ignore')
