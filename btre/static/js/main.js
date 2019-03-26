const date = new Date();
const year = document.querySelector('.year'); 
if(year){
    year.innerHTML = date.getFullYear();
};

setTimeout(function(){
    $('.alert').fadeOut();
}, 3000)
