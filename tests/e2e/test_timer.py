from playwright.sync_api import Page, expect

URL = "https://lejonmanen.github.io/timer-vue/"

# User story 1: A1
def test_create_timer_widget(page: Page):

    page.goto(URL)

    # Hur många widget finns
    before = page.locator(".widget").count()
    # Klickar på knapp
    page.get_by_role("button", name="Add timer").click()
    # Antal widget finns nu
    after = page.locator(".widget").count()
    # Finns det fler widget
    assert after == before + 1
