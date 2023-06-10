function toggleForm() {
  var registrationType = document.getElementById("registrationType").value;


  // Hide all registration forms
  document.getElementById("individualForm").style.display = "none";
  document.getElementById("smeForm").style.display = "none";
  document.getElementById("corporateForm").style.display = "none";
  document.getElementById("mentorForm").style.display = "none";
  document.getElementById("elearningForm").style.display = "none";
  document.getElementById("touristForm").style.display = "none";

  // Show the selected registration form
  document.getElementById(registrationType + "Form").style.display = "block";

}
let rt  = document.getElementById("registrationType");
let form =  document.getElementById("form");
let initialfm = form.id;
rt.addEventListener("change", function(){
  form.id = rt.value !== ''? rt.value: initialfm;
}) 
