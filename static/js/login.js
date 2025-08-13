// LogIn page
// Form elements
const loginForm = document.getElementById('loginForm');
const studentIdInput = document.getElementById('studentId');
const passwordInput = document.getElementById('password');
const clearBtn = document.getElementById('clearId');
const togglePassword = document.getElementById('togglePassword');

// Clear button functionality
studentIdInput.addEventListener('input', function() {
    clearBtn.style.display = this.value ? 'block' : 'none';
});

clearBtn.addEventListener('click', function() {
    studentIdInput.value = '';
    clearBtn.style.display = 'none';
    studentIdInput.focus();
});

// Password toggle functionality
document.addEventListener('DOMContentLoaded', function () {
        const togglePassword = document.getElementById('togglePassword');
        const passwordInput = document.getElementById('password');
        const eyeOpen = document.getElementById('eye-open');
        const eyeClosed = document.getElementById('eye-closed');

        togglePassword.addEventListener('click', function () {
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';
            
            // Ko'z ikonkasini almashtirish
            eyeOpen.style.display = isPassword ? 'none' : 'inline';
            eyeClosed.style.display = isPassword ? 'inline' : 'none';
        });

        // Dastlabki holatda eye-open ko‘rinadi, eye-closed yashirin
        eyeOpen.style.display = 'inline';
        eyeClosed.style.display = 'none';
    });


// Form validation
function validateForm() {
    let isValid = true;
    
    if (studentIdInput.value.trim() === '') {
        studentIdInput.classList.add('error');
        isValid = false;
    } else {
        studentIdInput.classList.remove('error');
    }

    if (passwordInput.value.trim() === '') {
        passwordInput.classList.add('error');
        isValid = false;
    } else {
        passwordInput.classList.remove('error');
    }

    return isValid;
}



// Remove error styling on input
studentIdInput.addEventListener('input', function() {
    this.classList.remove('error');
});

passwordInput.addEventListener('input', function() {
    this.classList.remove('error');
});

// Enter key navigation
studentIdInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        passwordInput.focus();
    }
});

passwordInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        loginForm.dispatchEvent(new Event('submit'));
    }
});


// messageni ma'lum vaqtdan keyin olib tashlash
setTimeout(function () {
    document.querySelectorAll('.messages .alert').forEach(function (el) {
        el.style.opacity = '0';
        setTimeout(function () {
            el.remove();
        }, 500); // animatsiya tugashi uchun yarim soniya kutamiz
    });
}, 3000);