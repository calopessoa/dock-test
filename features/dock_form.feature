Feature: Dock Home Page

    A page that allows the user to interact in english and to fill its form to get in contact with their Business team

Scenario: Changing the page's language to english
  Given that I`ve accessed the home page
  And  clicked to accept the cookies
  When I click to change the page`s language
  Then I see that Dock have more than 69 million active accounts
  And 45% CAGR since 2014

Scenario: Filling the form and sending it to the team
  Given that I`ve accessed the home page
  And  clicked to accept the cookies
  When I fill out all the required forms
  And I click to send it
  Then I see a message that validates my request
