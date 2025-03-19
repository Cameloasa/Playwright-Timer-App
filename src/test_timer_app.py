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
    note_text = page.locator('h3:has-text("Click to change text")')
    expect(note_text).to_be_visible()
