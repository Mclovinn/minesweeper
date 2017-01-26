Feature: Example


Scenario: Initial Scenario
    Given Initial page
    Then Initial page showed

Scenario: Initial Scenario
    Given Initial page
    Then The game board is showed


Scenario: 3x3 table Scenario
    Given Initial page
    Then The 3x3 game board is showed

Scenario: Not bomb scenario
    Given Initial page
    When press button with position (1, 2)
    Then NOT_BOMB is showed

Scenario: Not bomb scenario
    Given Initial page
    When press button with position (1, 1)
    Then BOMB is showed
