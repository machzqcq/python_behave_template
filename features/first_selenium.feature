Feature: Open website and print title
    Scenario: Open website
      Given I open seleniumframework website
      Then I print the title

    Scenario: print current url
      Given I open seleniumframework website
      Then I print current url

    Scenario: Browser back, forward and refresh
      Given I open seleniumframework website
      And I click ABOUT link
      Then I click back on the browser
      And I click forward on the browser
      And I click refresh on the browser
