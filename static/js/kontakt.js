 class Kontaktformular {
    constructor() {
      this.container = document.getElementById("myForm");
      this.handleSubmit = this.handleSubmit.bind(this);
      this.container.addEventListener("submit", this.handleSubmit);
      
      this.submitButton = document.getElementById("submitButton"); 
    }
  
    handleSubmit(event) {
      event.preventDefault();

      const formData = new FormData(this.container);
      fetch('/kontakt', {
         method: 'POST',
         body: formData,
        headers: { 'Accept': 'application/json' }
       })
       .then(response => {
         this.submitButton.disabled = true;
       })
       .catch(error => {
         this.submitButton.disabled = true;
       });
  
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('myForm');
    const kontaktformular = new Kontaktformular();
  });





  