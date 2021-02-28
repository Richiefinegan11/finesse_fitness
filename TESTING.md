# Table of Contents

1. [Functionality](#functionality)

1. [Validators](#validators)
    - [HTML5](#html5)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)

1. [Compatibility](#compatibility)

1. [Performance](#performance)

1. [User Stories](#user-stories)

1. [Bugs](#bugs)
    - [Identified Bugs](#identified-bugs)
    - [Existing Bugs](#existing-bugs)

1. [Future Testing](#future-testing)
# Functionality
- #### Navigation bar
    - The navigation bar is positioned at the top of the screen and stays visible on the top of the screen when the site is being scrolled.
    - Home page, Subscription and Blog links bring the user to the relevant pages.
    - Shop link when clicked, drops down a menu with item categories that bring the user to the shop page with the selected category displayed and items filtered.
    - Search bar is active for the store and returns items containing the searched word in the title or description.
    - Bag icon brings the user to the bag page.
    - When the user icon is clicked on, it opens up a dropdown menu displaying different options depending on whether the user is logged in or not. For logged-in users, 'My Profile' and 'Log Out' are displayed. Non authorized users to see 'Register'and 'Log In'.
    - When each link in the user dropdown is clicked, the user is navigated to the appropriate page.
    - On mobile and tablet views, the navbar collapses and a hamburger menu button is displayed instead.
    - When clicked, the hamburger menu reveals main menu items, the menu links are collapsed back in the navbar.
    - The logo is a clickable link, when clicked on it brings the user to the home page.

- #### Footer
    - Footer is visible on all pages
    - When social links are clicked in the footer, a new tab opens and the relevant social page is displayed.

- #### Search bar
    - On smaller devices, the search bar is an icon and when clicked it drops down
    - When an empty form is submitted, an error message is displayed on the right and the user is directed to the shop page were all products are displayed.
    - When a value is entered and 'Search' is clicked, the user is navigated to the 'Products' page (aka Shop) with matched results displayed.

- #### Registration
    - When a user clicks on the 'Register' button from the main navbar or 'Sign Up' button in various alluth pages (such as 'Sign In'), the user is directed to the 'Home' page.
    - User can also navigate to the 'Subscriptions' page from the main navbar.
    - In the form, all fields are required, if any are left out, the allauth displays a validation message.
    - Allauth will also display a validation error if e-mails do not match, the username is shorter than 4 characters, passwords don't match, or if the password is not up to standards (too short, too similar to the username or e-mail, too easy/common).
    - When 'Sign Up' is clicked with a valid form, a message is displayed to let the user know that they have to validate their e-mail address.
    - User receives an e-mail from Finesse Fitness with a link that brings the user to the 'Confirm E-mail Address'. When 'confirm" is clicked on this page, the user is re-directed to the 'Sign In' page.
    - When the user registers, their profile is created and they will be automatically appointed the 'Bronze' (free subscription) 
    - From the 'Register' page, the user can access the 'Login' page using the link which is functional.

- #### Sign Out / Log in
    - Sign in form allows users to sign in using their existing account
    - For sign-in, the validation form will display a validation message if either password or username/e-mail are left blank.
    - Form will display a validation error if  username/e-mail and/or password were incorrect so malicious users don't know specifically which field was incorrect.
    - When the 'Forgot Password' link is clicked, the user is navigated to a page where they are prompted to enter their e-mail address. They will then receive an e-mail with a link to reset the password. When the link is clicked, the user is navigated to the page and prompted to enter the new password twice. If this is successful, the user is navigated to a success page.
    - When the 'Sign Up' link is clicked on the 'Login' page, the user is brought to the Register page.
    - When valid credentials are entered on the Log In page, the user is logged in and redirected to either the 'Home Page' page if they just signed up.
    - Log Out page has one button, which when clicked, removes the user's session and logs the user out. The user is then re-directed to the Home page.

- #### Home Page
    - Home page scrolls nicely and is responsive on all screen sizes.
    - All buttons are working and bring the user to the relevant page. 'Join Now' button brings the user to the sign up page.
    - 'Subscribe' button brings the user to the subscriptions page
    - 'Shop Now' button brings the user to the shop so they can buy products.

- #### Shop Page
    - When the Shop link in the navbar is clicked, a dropdown offers the user to select a category or view all items in the shop. Either option brings the user to the same Products page with items filtered to the selected category.
    - There are 4 category buttons on the top of the page that have a hover effect and also are styled differently when the category has been chosen.
    - When a category button is clicked, items are filtered to the selected category.
    - There is a filter/sort button just above the products, the sorting buttons that sort selected items by ratings, price, or alphabetically/reverse.
    - All of the sorting buttons have a hover effect to let the user easily identify which button will be clicked.
    - All products are laid out in a grid and a responsive design, resizing to have 4 items per row on extra-large screens, 3 on medium, 2 on small, and 1 on mobile view.
    - Each product have their Image, title, rating, price and 'View Item' button visible.
    - When the 'View Item' button is clicked, the user is brought to the product detail page.
    - When Item's image is clicked, the user is brought to the product detail page.
    - Admin will have the option to edit or delete the product on this page

- #### Product Detail Page
    - Keep Shopping button brings the user back to the previous page they were on.
    - Product Detail Page displays product image, title, description, quantity selector, price, 'Add To Bag' button.
    - If the product has sizes, an option bar will be displayed with the choices of sizes.
    - When the user clicks +/- buttons for quantity, the quantity increases or decreases, and the price updates to reflect that.
    - the - button and + button are disabled (function and style) if the user has entered 1, they cannot enter less than that.
    - Typing has been disabled to prevent as much as possible for the user to 'accidentally' select more or less than the allowed quantity.
    - Arrow buttons are still available for entering quantity.
    - If the user overrides the front-end validation (deleting HTML max and min attributes in 
    - When the user has selected a valid quantity and the 'Add to cart' button is clicked, an item is added to the bag, with the correct size if selected and a bag notification is displayed with all items in the bag and the page is refreshed.
    - Admin will have the option to edit or delete the product on this page

- #### Subscriptions Page
    - This page should be displayed slightly differently depending on if the user is logged in or not.
    - For a non-authorized user it displays all three memberships with benefits, images, titles, price, and 'Subcribe' buttons.
    - If a non-authorized user tries to subscribe, they will recieve and error message and be directed to the sign up page
    - Authorized user will have already been given the free subscription by default, they will see chnage on the other options that they are not subscribed to.
    - When the authorised user chooses the new subscription, they are brought to a checkout page, where they are shown the subscription benefits. They can cancel, which brings them back to the shop page or confirm which brings them to their profile with their new subscription applied.
    - When the user goes back to the subscription page, their subscription will have a border around it, indicating their current subscription.

- #### Shopping Bag Page and toast
    - When the user clicks 'Add to the bag' from the products detail view, the item is added to the bag and bag toast is displayed.
    - In bag toast, the user sees item image, price, quantity, and total.
    - If the user changes the quantity in the bag toast, the page refreshes, and the cart, as well as bag toast, are updated.
    - User can navigate to the bag page from the navbar, bag toast, or checkout page.
    - On the page, the user sees a summary of their order, with items, their price, image, quantity, and total displayed. They also see the subtotal and a note that this amount excludes the delivery charges.
    - When 'Keep Shopping' is clicked, the user is navigated to the shop page.
    - When 'Secure Checkout' is clicked, the user is navigated to the checkout page to proceed with the payment.
    - when +/- buttons are clicked, quantity is updated and the page refreshed, this logic is the same as on the product detail page however loops through all the items and each is functioning as expected.
    - When 'Remove' is clicked, the item is removed from the bag.
    - If the last item is removed, the user will see an 'your bag is empty' text and a button redirecting them to the shop page.

- #### Checkout Page
    - On the checkout page, the user sees Delivery, Shipping, and Payment Info forms and order summary.
    - All fields are required apart from the 'Region/State', if they are not filled out, validation will prompt the user to fill it in.
    - If a user submits the form with an invalid phone number, and an error message will let them know that the form and phone number are invalid.
    - If the user enters invalid card details, Stripe will return an error with an error message displayed.
    - When a valid form has been filled out, and the user clicks on 'Complete Order' they are then are re-directed to the Checkout Success page where they can see their order details, with a customer, and shipment details added.
    - When the user clicks on the 'Click here to chekout out our clothing' button, they are re-directed to the shop page with only clothing showing.

- #### Profile Page
    - When user signs in, they are re-directed to the Profile page, user can also access it via the 'My details' link in the user dropdown in the navbar.
    - User sees the subscription summary at the bottom with the name and the monthly price. 
    - When a user clicks on 'Shop Now' under subscription summary, they are navigated to the shop page where they can see more details.
    - In the profile user also sees their profile details that user can edit/add and click save to amend them in the database.
    - The user can also see their order history on the right hand side of their profile

- #### Blog
  - When the user navigates to the blog, they can see the blog title, author and date/time added. They will also see the start of the blog content, that cuts off after 200 characters
  - They read more button bring the user to the blog chosen and reveals the blog content.
  - When the user is on the blog detail page, there is a "Back to blog" button at the bottom to bring them back to the blog


# Validators

## [HTML5](https://validator.w3.org/)
- Home - Pass
- Shop - Pass
- Product Details - Pass
- Subscription - Pass
- Subscripton Change - Pass
- Checkout - Pass
- Checkout Success - Pass
- Profile - Pass
- Add Product - Pass
- Edit Product - Pass
- Log In - Pass
- Register - Pass
- Blog - Pass
- Base - Pass

## [CSS3](https://jigsaw.w3.org/css-validator/)
- Chekout CSS - 1 error (-webkit-transition is an unknown vendor extension)
- Shop CSS - Pass
- Profile CSS - Pass
- Subscription CSS - Pass
- Base CSS - Pass


## [JSHint](https://jshint.com/)
- Stripe Element JS - Pass
- Shop JS - Pass
- Countryfireld JS - Pass


## [PEP8](http://pep8online.com/)


# Usability
- To test the ease of navigation, this website was shared with friends and family of different ages and different levels of computer/smart device knowledge. There were no issues identified regarding the simplicity of navigating the website.
- The testers also verified that all functionality aspects are working as explained above and as expected.
- Testers expressed that the design is easy to understand and navigate.

# Compatibility
* The website was exhaustively tested for responsiveness on Chrome DevTools and Responsive Web Design Checker all screen sizes provided. Different viewport sizes were simulated ranging from as small as Galaxy Fold (280px) to large desktop sizes (1200px and above).

# Performance Testing

# User Stories

- #### Common user stories
    1. I want to easily navigate the site so that I can find what I'm looking for quickly.
        - Navbar is always located at the top of the page so that the user can easily navigate to the pages they are looking for.
        - Most popular call-to-action buttons are displayed on the home page so that users can find the membership and shop pages quickly.
    1. I want to be able to contact the company if I'm experiencing an issue.
        - Social links are located in the footer allowing the user to contact the company in three different ways
    1. I want the website to be readable on all screen sizes.
        - The website is responsive and tested on all screen sizes allowing the user to have an equally good experience on mobile as well as desktop devices.
        - Navbar collapses on screen sizes medium and down, this prevents overcrowding of links on smaller screen sizes.
        - rem instead of px was used as much as possible to aid with responsiveness.


* As a first time visitor I want to:
  * Easily understand the purpose of the site so that I can decide whether I want to invest my time into it.
    * The user can see from the hompage what the site offers from the why choose use section
  * Understand the benefits of becoming a member/registering for the site so that I can decide if I want to.
    * If the user goes to the subscription page, they will see the benefits
  * View and compare all subscription so that I can decide what subscription if any, I want to subscribe to.
  * Easily find where I can register for the site so that I don't waste my time looking for it and I'm not discouraged not to sign up.
    * There is a call to action on the top of the homepage
  * Be able to quickly register and start using the site so that I can have my account and receive the benefits
    * There is a register button under the my account tab on the navigation bar
  * Check out the blog and see if the information is good and competent
    * The blog is easily found from the main nav

* As a casual shopper I want to
  * Navigate to the shop page easily so that I can find what I need quickly.
    * The shop page can be easily found from the main nav and also bottom of the homepage if the user has been scrolling
  * Filter all products by category so that I can quickly have oversight of the products that I'm interested in.
    * The shop link on the navbar has dropdown with categories for the user to choose from
  * Sort all items by date added, name or price so that I can identify new products, products that fit my budget, and find easier what I'm looking for.
    * When on the shop page the user can sort via icons indicating the preferred sorting option
  * Search for an item from anywhere on the site so that I can easily find what I'm looking for.
    * The search bar is always at the top, so the user can search the shop from anywhere on the site
  * Be able to see the price of the item without clicking into it so that I can easily decide if I can afford the item.
    * The price is shown on the main shop page for each item
  * Be able to see more details about the product so that I can make an educated decision of whether to purchase the item.
    * If the user clicks the item image or view item button, they are taking to the product detail page
  * Select the quantity of the product so that I can choose how many products I'm purchasing and not have to add the same item multiple times.
    * There is a quantity selector on the product detail page
  * See my shopping cart as items are added to know how the total without having to go to another page.
    * A message is shown every time a user adds a product, totaling the value of the bag items
  * Edit the quantity of added items so that I don't have to remove and add items again.
    * In the bag, the quanitity can be easily higher or lowered and updated
  * Remove added items easily so that I can purchase only the items that I want.
    * There is a remove link which will completely remove the item from the bag
  * See my shopping cart before checkout so that I can make changes before purchase.
    * The bag page has the facilities for this
  * See all charges included before making a payment so that I can decide if I want to proceed with the purchase.
    * The bag page totals up the item before the user clicks to checkout
  * View my order as I'm checking out to be able to confirm what I'm purchasing.
    easily add my details without too many steps so that I don't get discouraged by the lengthy checkout process.
      * An order summary will show on the right hand side of the checkout page
  * Securely add my payment information so that I feel safe giving my card details.
    * Stripe handles the payments securely at the bottom of the checkout page
  * See Order confirmation
    * The user will be taken to a confirmation page when they complete their purchase that shows all this info
  * Change from paid membership so that I don't have to pay for it.
    * The user can easily change on the subscription page
  
* As a member I want to:
  * Log in and sign out quickly and easily so that I can access or close my account.
    * Sign In button is located in the navbar and is accessible to the user from all pages.
    * Sign In link is displayed on the Register page so that User can easily navigate to it
    * Checkout page further displays the Sign In link if the user isn't signed in.
  * See my personal account information so that I can manage my details.
    * The user can do this on their profile once registered
  * Change the subscription easily so that I can control what benefits and expenses I'm having.
    * User can easily change their subscription on the subscription page
  * See my order history so that I can have the confirmation and details for all of them in one place and manage them easily.
    * The order history will show on the user profiles
  * Receive benefits as a member so that I get my money's worth.
    * Subscribed members recieve offers based on their subscription choice
  
* As an admin I want to:
  * Be able to add an item so that I can update the products on the site.
    *  Admin can access admin site from which they can add items, membership plans, delivery types.
  * Be able to edit and remove items so that I can customize items on the site and offer new deals to customers depending on the demand and new trends.
    *  Amin can edit the item from the admin page.
  * Add and edit new subscriptions so that I can customize the price and benefits depending on the popularity of the subscription.
    * This can be achieved from the admin pag
  * Add and edit new delivery types to accommodate shipping to more countries.
    * This can be achieved from the admin page
  * Have oversight of the user data so that if anyone is experiencing an issue I can investigate and resolve the issue.
    * This can be achieved from the admin page
  * Add new blog entries as needed
    * This can be achieved from the admin page reaches the footer

# Bugs and comments
* Bugs:
  * While doing this project, I ran in to alot of issues which made time scarce.
    * Git pod was down for the first 3 days of the project, I had chose to us VS code which delayed me further
    * Deployment -  On deployment, I ran in to many issues as I had to install alot of technologies to get my IDE working, that were outside of the scope of the course.
* Existing Bugs:
  * The subscription discount still needs to be applied to the user on checkout. I ran out of time to implement this.
  * The footer does not stick to the bottom of the page where there is not full content, eg. sign-up page.
  * The back to the top button stops functioning when enters the footer

# Future Testing
- Future testing will include automated tests such as Jasmine for JS and built-in Django automated testing for Python and implement Travis CI.