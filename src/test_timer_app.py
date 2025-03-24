import re

from playwright.sync_api import Page, expect

def test_show_add_timer_button(page: Page):
    """Testscenario [T1] – Kontrollera att knappen 'Add timer' är synlig och kan klickas"""
    # 1: Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # 2. Kontrollera att knappen "Add timer" finns och är synlig.
    add_timmer_button = page.locator('button:has-text("Add timer")')
    expect(add_timmer_button).to_be_visible()

    # 3. Klicka på knappen "Add timer".
    add_timmer_button.click()

def test_add_note_button(page: Page):
    """Kontrollera att knappen 'Add note' är synlig och kan klickas"""
    # 1. Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # 2. Kontrollera att knappen "Add note" finns och är synlig.
    add_note_button = page.locator('button:has-text("Add note")')
    expect(add_note_button).to_be_visible()

    # 3. Klicka på knappen "Add note".
    add_note_button.click()

    # 4. Kontrollera att en text "Click to change text" visas på skärmen.
    note_text = page.locator('h3:has-text("Click to change text")').first
    expect(note_text).to_be_visible()

    # 5. Klicka på texten "Click to change text".
    note_text.click()

    # 6. Klicka på texten "Click to change text".
    note_input = page.locator('input[placeholder="Description"]').first
    expect(note_input).to_be_visible()

    # 7. Fyll i ny text
    note_input.fill("Note 1")

    # 8. Tryck på "Enter" för att spara
    page.keyboard.press("Enter")

    # 9. Kontrollera att texten har ändrats till "Note 1"
    updated_note_text = page.locator('h3:has-text("Note 1")').first
    expect(updated_note_text).to_be_visible()

    # 10. Klicka på "Add note" igen och addera en ny text, ändra texten till "Note 2".
    add_note_button.click()

    # Kontrollera att en text "Click to change text" visas på skärmen.
    second_note_text = page.locator('h3:has-text("Click to change text")').last
    expect(second_note_text).to_be_visible()

    # Klicka på texten "Click to change text".
    second_note_text.click()

    # Klicka på texten "Click to change text".
    second_note_input = page.locator('input[placeholder="Description"]').last
    expect(second_note_input).to_be_visible()

    # Fyll i ny text
    second_note_input.fill("Note 2")

    # Tryck på "Enter" för att spara
    page.keyboard.press("Enter")

    # Kontrollera att texten har ändrats till "Note 2"
    updated_second_note_text = page.locator('h3:has-text("Note 2")').last
    expect(updated_second_note_text).to_be_visible()

    # 11. Ändra ordningen på "Note 1" och "Note 2" när man klickar på pilen
    up_arrow_button = page.locator('.icon.up').first
    up_arrow_button.click()

    # 12. Kontrollera om ordningen har ändrats
    expect(page.locator('h3:has-text("Note 2")')).to_be_visible()
    expect(page.locator('h3:has-text("Note 1")')).to_be_visible()

    # 13. Testar delete button (korgen)
    delete_button = page.locator('.icon.close').first
    delete_button.click()

    # Kontrollera om texten tas bort
    expect(page.locator('h3:has-text("Note 1")')).not_to_be_visible()
    expect(page.locator('h3:has-text("Note 2")')).to_be_visible()

def test_timer_start_and_reset(page: Page):
    # 1. Kontrollera att timern visas korrekt på sidan efter att du har klickat på knappen "Add timer".
    # Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Kontrollera att knappen "Add timer" finns och är synlig.
    add_timmer_button = page.locator('button:has-text("Add timer")')
    expect(add_timmer_button).to_be_visible()

    # Klicka på knappen "Add timer".
    add_timmer_button.click()

    # 2. Kontrollera att timern startar från 15:00.
    timer_text = page.locator('div.row.time')
    expect(timer_text).to_have_text("15:00")

    # 3. Klicka på "Start" och kontrollera att timern börjar räkna ner.
    start_button = page.locator('button:has-text("Start")')
    start_button.click()

    # 4. Klicka på "Reset" och kontrollera att timern återställs till 15:00.
    reset_button = page.locator('button:has-text("Reset")')
    reset_button.click()
    expect(timer_text).to_have_text("15:00")

def test_change_timer_title(page: Page):
    # 1. Navigera till webbsidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # 2. Kontrollera att knappen "Add timer" finns och är synlig, klicka på den
    add_timmer_button = page.locator('button:has-text("Add timer")')
    expect(add_timmer_button).to_be_visible()
    add_timmer_button.click()

    # 3. Kontrollera att titeln "Break" visas.
    timer_title = page.locator('h3')
    expect(timer_title).to_have_text("Break 🖊️")

    # 4. Klicka på titeln för att redigera den
    timer_title.click()

    # Fyll i en ny titel, t.ex. "Fika"
    title_input = page.locator('input[placeholder="Title"]')
    title_input.wait_for(state="visible", timeout=200)

    # 5. Fyll i en ny titel, t.ex. "Fika"
    title_input.fill("Fika")

    # 6. Tryck på "Enter" för att spara den nya titeln
    page.keyboard.press("Enter")

    updated_timer_title = page.locator('h3')
    expect(updated_timer_title).to_have_text("Fika 🖊️")















