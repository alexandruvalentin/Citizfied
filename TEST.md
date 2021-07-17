## Encountered Issues
  - Testing has been done frequently while building this application. While there were many encountered issues and bugs along the way, most of them were fixed quickly.

## Testing User Stories
  - ## As a user I need:
    - to navigate through your website quickly and efficiently
    >:heavy_check_mark: The navigation bar is visible almost at all times and various CTAs are available across the page.
    - to easily understand the purpose of your website
    >:heavy_check_mark: The hero container displays a very big heading describing the website's purpose and two CTAs.
    - to be able to register to your website in order to make use of all its features
    >:heavy_check_mark: The registration page allows the user to sign up. and then log in to the website where they can add and then manage their reviews.
    - to be able to submit, edit and/or delete content in your app
    >:heavy_check_mark: Users can add reviews and later manage them in their profile's page.
    - to look up other user’s reviews using a search engine
    >:heavy_check_mark: The main page REVIEWS form displays reviews by categories: Most Recent and Top Rated. In addition, a search bar was implemented to allow the user to look up whatever they would like.
    - to be able to access your website across a range of devices
    >:heavy_check_mark: The website was built with a mobile-first approach and is fully responsive.

## Testing Code
> :heavy_check_mark: Every javascript method was tested for the expected outcome by using the app, in console by using `console.log()` or by manually calling the function.

> :heavy_check_mark: Every python function and route was tested for the expected outcome by using the app, by accessing the route, in python console, while debug mode was ON, and by the `print()` function.

## Testing Functionality
  - ### Testing Links and Buttons
    - top navigation bar is fully functional, including the brand logo. :heavy_check_mark:
    - mobile navigation toggle "burger" is functional, opening and closing as expected. :heavy_check_mark:
    - 'Find A Review' button takes you to the main page search engine. :heavy_check_mark:
    - 'Add A Review' button takes you to the Add Review form. :heavy_check_mark:
    - 'Edit' button re-opens the review form. :heavy_check_mark:
    - 'Delete' button triggers a prompt message that's double-checking with you if the action should continue, as expected. :heavy_check_mark:
    - 'Update' button of the profile page updates the display name. :heavy_check_mark:
    - 'Add Review' logs the completed form to web app and database. :heavy_check_mark:
    - the rating slider is adding a half star to the rating stars with each 0.5 step and the counter also displays correctly. :heavy_check_mark:

  - ### Testing Form Validation
    - Every form(Register, Log In and Add Review) was tested for validation by trying to submit without data and then with one field at a time. Every field asks for input. Also, I have removed the required attribute from every field, using Chrome's DevTools, and resubmitted the form: the backend validation works, returning error messages for every required field. :heavy_check_mark:

  - ### Testing CRUD Functionality
    - **CREATE**: The 'create' functionality was tested by adding data to the designated fields. Works as expected. Forms are being uploaded to the database correctly :heavy_check_mark:
    - **READ**: The 'read' functionality was tested by verifying that the generated data is being correctly displayed in the right section. :heavy_check_mark:
    - **UPDATE**: The 'update' functionality was tested by editing the current user's reviews and by updating their Display Name from their profile page. No issues found :heavy_check_mark:
    - **DELETE**: The 'delete' functionality was tested by deleting items uploaded by the current user. Clicking on the trash icon will trigger a prompt message which will complete the action upon approval.

## Testing Compatibility
  - ### Responsiveness
    - Responsiveness was explored and tested using DevTools and on a wide variety of devices of different sizes, in both portrait and landscape, in order to detect any issue. No issues were found; elements align correctly in space, none being obstructed. In conclusion, the website is fully responsive. :heavy_check_mark:

  - ### OS Test
    - Desktop
    > Testing was done on Windows 7 and Windows 10. Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. In conclusion, the website is desktop system-cross compatible.
    - Mobile
    > Testing was done on Android 10, iOS 13 and iOS 14. Features appear to be functional from top to bottom. Buttons, links, slideshow gallery and contact form, all work correctly. No overflow, overlay or error messages encountered. In conclusion, the website is mobile system-cross compatible.

  - ### Devices test
    > Testing was done on ASUS TUF FX705G, Galaxy S20, iPhone 7/8/11/12/12 Pro and iPad Pro 12.9 2020. Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. Everything falls into place in space. In conclusion, the website is platform-cross compatible.

  - ### Browser test
    > The website was tested on Google Chrome, Firefox, Safari and Microsoft Edge. Browser versions were all up to date. Further testing was done using [BrowserLing](https://www.browserling.com/). Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. Everything falls into place in space. In conclusion, the website is browser-cross compatible.

## Testing Performance

## Testing Accessibility

## Code Validation
  - ### HTML :heavy_check_mark:
    > Tested and validated using W3C Validator. Issues were adjusted and the only warning is received is for the lack of heading in the section elements which is not conclusive since the validator doesn't get the dynamically loaded content (which has headings for each page). The content for each page was separately tested with the same validator by direct input. No other errors or warnings.

  - ### CSS :heavy_check_mark:
    > Tested and validated with W3C CSS Validator. Only errors displayed are warnings concerning the vendor prefixes, which can be ignored.

  - ### JavaScript :heavy_check_mark:
    > Javascript methods and functions were tested for the expected outcome in the console using the console.log() command.

  - ### Python :heavy_check_mark:
    > Python has been validated during building process by **VSCode** integrated extensions **[Pylint](https://www.pylint.org/)** and **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)**, which are in compliance with PEP8 style guide. **No errors or issues**.
