from pages.base_page import Page

class MainPage(Page):

    def open_main(self):
        self.open_url('http://www.amazon.com/')

    def open_product(self):
        self.open_url('https://www.amazon.com/Dell-OptiPlex-Computer-Desktop-Keyboard/dp/B09TN242Q5/ref=zg_bs_565098_sccl_3/132-7782273-6146205?psc=1')

    def open_product_closing_category(self):
        self.open_url('https://www.amazon.com/Ecokauer-Buttons-Children-Birthday-Clothing/dp/B08HRRBT9G/ref=sr_1_1_sspa?psc=1&qid=1679170816&refinements=p_n_size_six_browse-vebin%3A4940398011&s=apparel&sr=1-1-spons&smid=A1Q8JNJWHJWBVR&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTFo5WU1WRVdYRkpZJmVuY3J5cHRlZElkPUEwMjk2Njk3M0NURUU5VFBXUjVFVCZlbmNyeXB0ZWRBZElkPUEwODAxMzg5MUlJRVY5NFFITFpNUiZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')