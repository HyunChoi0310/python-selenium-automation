from pages.base_page import Page

class MainPage(Page):

    def open_main(self):
        self.open_url('http://www.amazon.com/')

    def open_product(self):
        self.open_url('https://www.amazon.com/Dell-OptiPlex-Computer-Desktop-Keyboard/dp/B09TN242Q5/ref=zg_bs_565098_sccl_3/132-7782273-6146205?psc=1')