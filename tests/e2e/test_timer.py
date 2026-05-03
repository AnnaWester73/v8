from playwright.sync_api import Page, expect

URL = "https://lejonmanen.github.io/timer-vue/"

# User story 1: A1
def test_create_timer_widget(page: Page):

    page.goto(URL)

    page.get_by_role("button", name="Add timer").click()
    expect(page.get_by_text("Break")).to_be_visible()
