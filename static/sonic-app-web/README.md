# Mastercard Sonic Reference App.
---
A static web application project which demonstrates the integration of Web SDK for Mastercard Sonic Brand at Checkout.

The purpose of this reference application is to show the appropriate placement of code snippets to initialize the SDK and play the Checkout Sound and Animation.

For detail Web SDK documentation, visit [here](https://developer.mastercard.com/mastercard-sonic-branding/documentation/).

# Technologies & Tools used
---
#### Language
* HTML
* JavaScript
#### Supported browsers
* All latest PC and Mobile browsers except IE.
#### IDE
* Any HTML & JavaScript editor
#### Running the application.
* Setup any http server to host the reference application on the local machine
* Place all content of the directory on your local server's root directory.
* To run the application, open localhost with your specific port and path.

# Features  
---
This application implements the following primary use cases:

1. A transaction using Mastercard payment card
2. A transaction using payment card other than Mastercard

  
## 1. A transaction using Mastercard payment card

When checkout is performed using Mastercard payment card, Mastercard Checkout Sound and Animation needs to be played on approval of the transaction.

Note: Mastercard Checkout Sound and Animation must not be played if the transaction is declined or failed. The fail scenario is not covered in the reference application.

### Actors
* Consumer/Shopper
* Merchant Application

### Preconditions

The user has selected products to be purchased and is ready to perform checkout.
  
### User journey
* User is on the checkout screen
* User ***selects the Mastercard payment card*** from saved cards
* User confirms the order and initiates the payment.
* The transaction is processed and successfully approved.
* ***Mastercard Checkout Sound and Animation is played*** which enhances sensory experience and enforces trust in the Mastercard brand.
* The order is placed and the user can see the order ID.

#### Code Example
  * Include .js in you HTML page.
  
    You can include mc-sonic component as a javascript in your page as:
    ```
    <script src="<path to>./assets/js/mc-sonic.min.js"></script>
    ```
  
  * Web SDK provides 3 types of configuration to be played on successful transactions.

      1. `default`  (both Sound and Animation will be played)
      2. `sound-only`
      3. `animation-only`
        
      This reference app is configured with `default`.

  * Web SDK provides 2 background color values to display for background on successful transactions. 

      1. `black`  (default)
      2. `white`
        
      This reference app is configured with `black`.
  
  * Web SDK provides 2 types of cues with different sounds and animations for different user actions on successful transactions.

      1. `checkout` (default)
      2. `securedby`
        
      This reference app is configured with `checkout`.
      
      To change other modes like `sound-only` or `animation-only` go to `index.html` line number `111`
    
      ```html
              <mc-sonic id="mc-sonic"></mc-sonic>
      ```

  * The animation will be played with a black background by default. To change the background to white, go to `index.html` and update the <mc-sonic> tag with following code.
    
      ```html
          <mc-sonic id="mc-sonic" sonicBackground="white"></mc-sonic>
      ```
  
  * It can also be done via javascript. Go to `assest/index.js` and add `el.sonicBackground = white;` in a function `onPaySuccess` to disable or clear the background.

      ```javascript
             if (cardType === "mastercard") {
                 let el = document.getElementById("mc-sonic");
                 el.sonicBackground = white;
                 el.play()
             } else {
                 onCompletion()
             }
      ```
  * The animation will be played with checkout cue by default. To change the cue, go to `index.html` and update the <mc-sonic> tag with following code.
    
      ```html
          <mc-sonic id="mc-sonic" sonicCue="securedby"></mc-sonic>
      ```
   * It can also be done via javascript. Go to `assest/index.js` and add `el.sonicCue = securedby;` in a function `onPaySuccess` to disable.

        ```javascript
             if (cardType === "mastercard") {
                 let el = document.getElementById("mc-sonic");
                 el.sonicCue = securedby
                 el.play()
             } else {
                 onCompletion()
             }
        ```
## 2. A transaction using payment card other than Mastercard
  
### User journey

* User is on the checkout screen
* ***User selects the payment card other than Mastercard*** from saved cards
* User confirms the order and initiates the payment.
* The transaction is processed and successfully approved.
* ***Mastercard Checkout Sound and Animation is NOT played***.
* The order is placed and the user can see the order ID.

#### Code Example

* Mastercard payment card is selected by default. User selected card is set in `assets/index.js` at line number `39`

  ```javascript
    let cardType = document.getElementById("cardSelector").value;
  ```
  

* `onPaySuccess()` is responsible for playing Mastercard Checkout Sound and Animation based on card type.


  ```javascript
  function onPaySuccess() {
      let confirmOrderStep = document.getElementById("confirmOrderStep");
      let animationStep = document.getElementById("animationStep");

      animationStep.classList.remove("hide")
      confirmOrderStep.classList.add("hide")
      window.scrollTo({ top: 0, behavior: 'auto' });

      let cardType = document.getElementById("cardSelector").value;

    if (cardType === "mastercard") {
        let el = document.getElementById("mc-sonic");
        el.play()
    } else {
        onCompletion()
    }
  }
  ``` 

## Author
---
- Name: **Mastercard Sonic Brand**
- Contact: **Ask.Brand.Manager@mastercard.com**

## Support
---
Please email to **Ask.Brand.Manager@mastercard.com** for additional support if required.
 
## License
---
Apache 2.0 License
### Copyright © 1994-2021, All Right Reserved by Mastercard.
