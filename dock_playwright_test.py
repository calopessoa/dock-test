import re
from playwright.sync_api import Page, expect

def test_dock_homepage_has_a_unica_plataforma(page: Page):
  page.goto("https://dock.tech/")

  expect(page).to_have_title(re.compile("Dock - Tech your business free"))

  know_our_solutions = page.get_by_role("link", name="Conheça nossas soluções")
  expect(know_our_solutions).to_have_attribute("href", "#nossas-solucoes")
  # know_our_solutions.click()

  # expect(page).to_have_url(re.compile(".*nossas-solucoes"))