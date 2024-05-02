# UI Automation

## Framework

The UI automation framework utilizes Microsoft's Playwright.

- The framework automatically handles element checks and waiting, eliminating the need for users to manually download browser drivers for popular browsers like Google Chrome. Simply specify the desired channel in the parameters.
- Compared to Selenium, the framework offers faster startup times, and its codegen generator supports recording user actions and generating corresponding code, similar to the functionality of Selenium IDE.
- The framework provides additional built-in element locator methods compared to Selenium, eliminating the need for further customization.

## Design Pattern

The framework follows the Page Object Model (POM) design pattern.

- base
  - Encapsulates assertion methods to determine element visibility.
  - Simulates human-like input methods.
  - Asserts whether an element is selected.
  - Provides screenshot functionality.
  - Encapsulates click handlers.
  - Enables opening web pages.
- data
  - Contains data required for the Data-Driven Testing (DDT) approach in each module. The format and fields can be freely defined based on module requirements.
- page
  - Stores elements for each module. Elements can be automatically generated using the Playwright codegen command. Currently, only two locator methods are added, and additional methods need to be implemented in the future.
- testcase
  - Serves as the debugging module. Methods should be modified based on the fields defined in the data folder, using decorators.
- tools
  - Implements neural network-based automatic captcha recognition and a CSV data import decorator using manual closure.

## Optimization

The framework still has significant room for optimization and exploration.

- Integrate pytest for assertions, replacing the manually implemented CSV reader decorator using closures.
- Transition from Data-Driven Testing (DDT) to Keyword-Driven Testing (KDT) approach.
- Implement multi-tab concurrent and asynchronous operations for different test modules using multithreading.
