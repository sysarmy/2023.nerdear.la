const success_message = document.getElementById("success-message");
function submit_entry() {
	let name = document.getElementById("name");
	let surname = document.getElementById("surname");

	let entry = {
		name: name.value,
		surname: surname.value,
	};

	//window.location is the host IP address, in local development its localhost:8000
	fetch(`${window.location}/submit_contact`, {
		method: "POST",
		credentials: "include",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(entry),
	}).then((response) => {
		// Check if the response was successful, return if not
		if (!response.ok) {
			console.error("Error: Response was not ok " + response.status);
			return;
		}
		// Handle the data
		response.json().then((data) => {
			console.log(data);
		});
	});
	console.log("This should not appear in an error");
}
document
	.getElementById("contact-form")
	.addEventListener("submit", function (event) {
		event.preventDefault();
		console.log("holasd");
		submit_entry();
	});
