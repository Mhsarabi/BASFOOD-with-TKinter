# Bas Food --- Application Guide

This guide explains the main sections of Bas Food and describes the
typical ordering flow.

## 1. Home page

The home page is the main entry point to Bas Food. It introduces the
restaurant application and provides navigation to the available
sections.

![Bas Food home page](docs/images/home-page.png)

From the navigation area, users can open the menu categories:

-   Iranian Foods
-   Fast Food
-   Drinks

The invoice section is used to review an order.

## 2. Iranian Foods

The Iranian Foods section displays the available Iranian dishes with
their pictures, names, prices, and order buttons.

![Iranian foods page](docs/images/iranian-foods.png)

To order an item, find the desired dish and use its **Order** button.
The selected item is then handled by the application's ordering flow.

## 3. Fast Food

The Fast Food section provides a separate menu for fast-food items.

Users can browse the available items, check their displayed prices, and
use the corresponding order controls to add items to the order.

> The supplied screenshots do not include the Fast Food page. This
> section is therefore described without an illustrative screenshot.

## 4. Drinks

The Drinks section provides access to the drinks menu. Users can browse
the available drinks and use the order controls provided by the
interface.

> The supplied screenshots do not include the Drinks page. This section
> is therefore described without an illustrative screenshot.

## 5. Invoice

The Invoice section presents a summary of the order, including the
selected items and their prices. It helps users review the order amount.

![Invoice and luck feature](docs/images/invoice-and-luck.png)

The invoice is also where the random luck feature is available.

### Random luck discount

The luck feature is random: when the user tries their luck, the
application determines whether a discount is granted. If the user wins,
a discount is applied to the total price.

The discount is not guaranteed on every attempt. The final amount should
be checked in the invoice after the luck result is shown.

## 6. Typical ordering flow

1.  Open Bas Food.
2.  Choose a menu category: Iranian Foods, Fast Food, or Drinks.
3.  Browse the available items and their prices.
4.  Use the order buttons for the desired items.
5.  Open the Invoice section to review the order.
6.  Optionally use the luck feature.
7.  Check the final total shown by the application.

## 7. Notes

-   Keep the `pic/` directory in its expected location because the
    application uses local image assets.
-   Run `app_resturant.py` from the project root to ensure relative
    asset paths resolve correctly.
-   The random discount feature may or may not grant a discount.
