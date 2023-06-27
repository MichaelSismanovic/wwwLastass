class contactForm {
	constructor(firstname, lastname, email, phone, message, captcha, solution) {
		this.firstname = firstname;
		this.lastname = lastname;
		this.email = email;
		this.phone = phone;
		this.message = message;
		this.captcha = captcha;
		this.solution = solution;
	}

	handleResponse(res) {
		if (res.status != 200) {
			document.getElementById("notification").textContent = `${res.status} ${res.statusText}. please try again later`;
			document.getElementById("submitBtn").disabled = false;

		} else	
			res.text().then(text => {
				document.getElementById("notification").textContent = text;
				if (text != "success")
					document.getElementById("submitBtn").disabled = false;
			});
	}

	send() {
		document.getElementById("submitBtn").disabled = true;
		fetch('send-contact', {
			method: 'POST',
			headers: { 
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(this),
		}).then(this.handleResponse);
	}
}

document.getElementById("form").addEventListener("submit", e => {
	e.preventDefault();

	const firstname = this.form.elements.firstname.value;
	const lastname = this.form.elements.lastname.value;
	const email = this.form.elements.email.value;
	const phone = this.form.elements.phone.value;
	const message = this.form.elements.message.value;
	const captcha = this.form.elements.captcha.value;
	const solution = this.form.elements.solution.value;

	const form = new contactForm(firstname, lastname, email, phone, message, captcha, solution);

	form.send();
});
