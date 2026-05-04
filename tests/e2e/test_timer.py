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

# User story 2: A1
def test_add_note(page: Page):
    page.goto(URL)

    notes = page.locator(".note")
    before = notes.count()

    # Skapa note
    page.get_by_role("button", name="Add note").click()

    after = notes.count()
    assert after == before + 1

# User story 2: A2
def test_write_note_text(page: Page):
    page.goto(URL)

    page.get_by_role("button", name="Add note").click()
    page.get_by_text("Click to change text").click()
    page.keyboard.type("Min anteckning")

    assert "Min anteckning" in page.content()

# User story 3: A1
def test_delete_timer_widget(page):
    page.goto(URL)

    page.get_by_role("button", name="Add timer").click()
    widgets = page.locator(".widget")
    before = widgets.count()
    page.locator(".icon.close").first.click()

    after = widgets.count()
    assert after == before - 1
