const menuToggle1 = document.getElementById('menuToggle');
const menuToggle2 = document.getElementById('menuToggle2');
const closeBtn = document.getElementById('closeSidebar');
const sidebar = document.getElementById('sidebar');
const main = document.querySelector('.main');

menuToggle1.addEventListener('click', () => {
    sidebar.classList.toggle('hidden');
    main.classList.toggle('shift');
    menuToggle1.classList.toggle('active');
});

menuToggle2.addEventListener('click', () => {
    sidebar.classList.toggle('hidden');
    main.classList.toggle('shift');
    menuToggle2.classList.toggle('active');
});

closeBtn.addEventListener('click', () => {
    sidebar.classList.toggle('hidden');
    main.classList.toggle('shift');
    menuToggle1.classList.toggle('active');
    menuToggle2.classList.toggle('active');
})