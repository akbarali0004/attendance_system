// // ✅ Davomat checkboxlarini hisoblaydigan funksiya
// function updateAttendanceCount() {
//     const checkboxes = document.querySelectorAll('.attendance-checkbox');
//     let count = 0;
//     checkboxes.forEach(cb => {
//         if (cb.checked) count++;
//     });
//     document.getElementById('count-display').textContent = `${count} ta`;
// }

// // ✅ Sahifa yuklanganda hisobla
// updateAttendanceCount();

// // ✅ Har bir checkboxda o‘zgarish bo‘lsa — hisobni yangilab bor
// document.querySelectorAll('.attendance-checkbox').forEach(cb => {
//     cb.addEventListener('change', updateAttendanceCount);
// });

document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.attendance-checkbox');
    const display = document.getElementById('count-display');

    function updateAttendanceCount() {
        let count = 0;
        checkboxes.forEach(cb => {
            if (cb.checked) count++;
        });
        if (display) {
            display.textContent = `${count} ta`;
        }
    }

    updateAttendanceCount();

    checkboxes.forEach(cb => {
        cb.addEventListener('change', updateAttendanceCount);
    });
});
