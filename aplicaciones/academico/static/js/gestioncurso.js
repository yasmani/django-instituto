(function (){

    const btneliminacion = document.querySelectorAll(".btneliminacion");

    btneliminacion.forEach(btn => {
    btn.addEventListener('click', (e) => {
        const confirmacion = confirm(' ¿Seguro de eliminar el curso ? ');
        if(!confirmacion){
            e.preventDefault();
        }
    });
});


})();