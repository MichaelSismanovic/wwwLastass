class Kontaktformular {
    constructor() {

      this.vornameField = document.getElementById("vorname");
      this.nachnameField = document.getElementById("nachname");
      this.telefonnummerField = document.getElementById("telefonnummer");
      this.emailField = document.getElementById("email");
      this.nachrichtField = document.getElementById("nachricht");
      this.rechenaufgabeField = document.getElementById("rechenaufgabe");
      this.submitButton = document.getElementById("submitButton");  
    }
  
    handleSubmit(event) {
      event.preventDefault();
  
      this.submitButton.disabled = true;
  
      const vorname = this.vornameField.value;
      const nachname = this.nachnameField.value;
      const telefonnummer = this.telefonnummerField.value;
      const email = this.emailField.value;
      const nachricht = this.nachrichtField.value;
      const rechenaufgabe = this.rechenaufgabeField.value;

       fetch('/kontakt', {
         method: 'POST',
         body: JSON.stringify({ vorname, nachname, telefonnummer, email, nachricht, rechenaufgabe }),
         headers: { 'Content-Type': 'application/json' }
       })
       .then(response => {
         this.submitButton.disabled = false;
       })
       .catch(error => {
         this.submitButton.disabled = false;
       });
  
    }
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const kontaktformular = new Kontaktformular();
  });
  
  