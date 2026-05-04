from playwright.sync_api import Page, expect

URL = "https://lejonmanen.github.io/timer-vue/"

# User story 1: A1
def test_create_timer_widget(page: Page):

    page.goto(URL)
    widgets = page.locator(".widget")
    before = widgets.count()

    page.get_by_role("button", name="Add timer").click()
    expect(widgets).to_have_count(before + 1)
