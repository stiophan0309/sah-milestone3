function sendMail(contactForm) {
    emailjs.send("gmail", "rosie", {
        "name": contactForm.name.value,
        "email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}