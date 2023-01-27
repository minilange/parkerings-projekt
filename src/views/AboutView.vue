<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-8">
        <div class="action-prompt">
          <h2 class="display-6">ABOUT US</h2>
          <hr>
          <div class="description mt-4">
            <h4>Description:</h4>
            <p>
              Our parking app makes it easy to find and reserve a spot in garages and lots
              near your destination. Simply search for your desired location and select from
              a list of available options. You can also save your favorite parking spots for
              quick access later. Plus, with our in-app payment system, you can quickly and
              securely pay for your spot without having to fumble for change or credit
              cards. No more circling the block or worrying about getting a ticket - our app
              makes parking a breeze.
            </p>
            <hr />
          </div>
          <div class="our-team mt-2">
            <h4>Our team:</h4>
            <p>
              Our coding team is proud to present our latest creation: a parking application
              that makes it easy for drivers to find and reserve a spot in garages and lots
              near their destination. With a user-friendly interface and an in-app payment
              system, our app streamlines the parking process and saves users time and
              hassle. The team worked diligently to ensure that the app is reliable and
              efficient, and we are confident that it will greatly improve the parking
              experience for drivers everywhere. We hope you enjoy using our app as much as
              we enjoyed creating it!
            </p>
            <hr />
          </div>
          <div class="feedback mt-2 mb-4">
            <h4>Feedback:</h4>
            <p>
              Thank you for using our parking app! We value your feedback and would love to
              hear about your experience. Please take a moment to rate your parking spot and
              leave a review. Your feedback will help us improve the app and provide a
              better service for all our users. Thank you for your support!
            </p>
            <a class="btn btn-primary btn-dark" href="mailto:carlleeladefoged@gmail.com">
              Send us some feedback!
            </a>
          </div>
        </div>
      </div>
      <div class="col-lg-4 mt-lg-0 mt-4">
        <div class="action-prompt">
          <h2 class="display-6">CONTACT US</h2>
          <hr />
          <div class="row contact-us">
            <h4 class="">Phone:</h4>
            <div class="col-lg-12 contact-row">
              <img width="50" height="50" src="../assets/Phone.png" alt="Phone" />
              <p>+45 12 34 56 78</p>
            </div>
            <hr class="mt-4" />
            <h4 class="">Mail:</h4>
            <div class="col-lg-12 contact-row">
              <img width="50" height="50" src="../assets/Mail.png" alt="Mail" />
              <p>support@easierpark.dk</p>
            </div>
            <hr class="mt-4" />
            <h4 class="">Location:</h4>
            <div class="col-lg-12 contact-row">
              <img width="50" height="50" src="../assets/Location.png" alt="Location" />
              <p>Vikærsvej 46, 2. th 8240 Risskov</p>
            </div>
            <hr class="mt-4" />
            <h4 class="">Livechat:</h4>
            <div class="col-lg-12 contact-row">
              <img width="50" height="50" src="../assets/Livechat.png" alt="Livechat" />
              <p>Livechat funktion på vej!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.action-prompt {
  /* Override */
  height: 100%;
}

.contact-us {
  flex-direction: column;
}

.contact-us .contact-row {
  margin-top: 15px;
  display: flex;
  align-items: flex-end
}

.contact-us .contact-row img {
  margin-right: 20px;
}
</style>
