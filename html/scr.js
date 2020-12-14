let result = document.getElementById('result');
let button = document.getElementById('button');
let patient = ["насморк","гипертония"];
let jsons = JSON.stringify(patient);
console.log('nn:',jsons);

button.addEventListener('click', function() {

fetch('http://mira.shadow.chancellery/plsrv/answer', {
  method: 'post',
  headers: { "Content-Type": "application/json" },
  body: jsons
}).then(
              response => {
                      return response.json();
              }
      ).then(
             json => {console.log('ii:', JSON.stringify(json));}
      );
});
