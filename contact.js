class contactForm {
	constructor(name, email, phone, message, captcha, solution, csrf) {
		this.name = name;
		this.email = email;
		this.phone = phone;
		this.message = message;
		this.captcha = captcha;
		this.solution = solution;
		this.csrf = csrf;

		localStorage.setItem('name', name);
		localStorage.setItem('email', email);
		localStorage.setItem('phone', phone);
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
				else
					document.getElementById("form").style.display = "none";
			});
	}

	send(csrf) {
		document.getElementById("submitBtn").disabled = true;
		fetch('send-contact', {
			method: 'POST',
			headers: { 
				'Content-Type': 'application/json',
				'X-CSRF-TOKEN': csrf
			},
			body: JSON.stringify(this),
		}).then(this.handleResponse);
	}
}

document.getElementById("form").addEventListener("submit", e => {
	e.preventDefault();

	const name = this.form.elements.name.value;
	const email = this.form.elements.email.value;
	const phone = this.form.elements.phone.value;
	const message = this.form.elements.message.value;
	const captcha = this.form.elements.captcha.value;
	const solution = this.form.elements.solution.value;
	const csrf = this.form.elements.csrf.value;

	const form = new contactForm(name, email, phone, message, captcha, solution);

	form.send(csrf);
});

if (localStorage.getItem('name') && localStorage.getItem('phone') && localStorage.getItem('email')) {
  document.getElementById('name').value = localStorage.getItem('name');
  document.getElementById('phone').value = localStorage.getItem('phone');
  document.getElementById('email').value = localStorage.getItem('email');
}
