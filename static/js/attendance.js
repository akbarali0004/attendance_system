// Davomat sahifasidagi checkboxlarni hisoblash
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