document.addEventListener("DOMContentLoaded", function () {
  // Get the language selector element
  var languageSelector = document.getElementById("language-selector");

  // Add event listener for the language selector change event
  languageSelector.addEventListener("change", function () {
    // Get the selected language from the language selector
    var language = languageSelector.value;

    // Send a POST request to the server to set the language
    fetch("/set-language", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ language: language }),
    })
      .then(function (response) {
        if (response.ok) {
          console.log(`Setting language to ${language}`);
          location.reload(); // Reload the page after changing the language
        } else {
          console.error("Failed to set language");
        }
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  });
});
