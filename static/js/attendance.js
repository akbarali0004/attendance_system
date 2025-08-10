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


// baho qoyish inputni sozlash
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', function () {
        if (this.value.length > 3) {
            this.value = this.value.slice(0, 3); // 3 xonadan oshmasin
        }
        if (this.value > 100) {
            this.value = 100; // 100 dan katta bo‘lsa, avtomatik 100 qilib qo‘yish
        }
        if (this.value < 0) {
            this.value = 0; // 0 dan kichik bo‘lsa, 0
        }
    });
});


// progressbar ni ramgini ozgartirish
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("progress").forEach(bar => {
        let value = bar.value;
        let color;

        if (value < 50) {
            color = "red";
        } else if (value < 80) {
            color = "orange";
        } else {
            color = "green";
        }

        bar.style.setProperty("--progress-color", color);
        bar.parentElement.querySelector(".progress-text").textContent = value + "%";
    });
});
