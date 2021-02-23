// The following code was taken from
// https://testdriven.io/blog/django-stripe-subscriptions/
// and
// https://stripe.com/docs/billing/subscriptions/checkout
// It is used to set up Stripe external checkout form
// to handle subscriptions


// Get Stripe public key
fetch("/subscription/config/")
// convert to JS object
.then((result) => { return result.json(); })
// Get data
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

 // When Submit button is clicked, generate and get Checkout Session ID
 let submitBtn = document.querySelector("#submitBtn");
 if (submitBtn !== null) {
   submitBtn.addEventListener("click", () => {
   // Get Checkout Session ID
   fetch("/subscriptions/create-checkout-session/")
     .then((result) => { return result.json(); })
     .then((data) => {
       console.log(data);
       // Redirect to seccure Checkout form hosted by Stripe
       return stripe.redirectToCheckout({sessionId: data.sessionId})
     })
     .then((res) => {
       console.log(res);
     });
   });
 }
});