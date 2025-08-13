function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed');
    
    // Mobile responsive
    if (window.innerWidth <= 768) {
        sidebar.classList.toggle('active');
    }
}

// Semester tab functionality
document.querySelectorAll('.semester-tab').forEach(tab => {
    tab.addEventListener('click', function() {
        document.querySelectorAll('.semester-tab').forEach(t => t.classList.remove('active'));
        this.classList.add('active');
    });
});

// Grid item hover effects
document.querySelectorAll('.grid-item').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Add click animation
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
        
        console.log('Clicked:', this.querySelector('h4').textContent);
    });
});

// Auto-hide success notification
setTimeout(() => {
    const notification = document.querySelector('.success-notification');
    if (notification) {
        notification.style.opacity = '0';
        notification.style.transform = 'translateY(100px)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }
}, 5000);

// Handle responsive sidebar on window resize
window.addEventListener('resize', function() {
    const sidebar = document.getElementById('sidebar');
    if (window.innerWidth > 768) {
        sidebar.classList.remove('active');
    }
});

// Close sidebar when clicking outside on mobile
document.addEventListener('click', function(e) {
    if (window.innerWidth <= 768) {
        const sidebar = document.getElementById('sidebar');
        const toggleBtn = document.querySelector('.toggle-btn');
        
        if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target) && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
        }
    }
});

// Add smooth scrolling to navigation links
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        
        // Add active class to clicked link
        this.classList.add('active');
        
        console.log('Navigation:', this.querySelector('.nav-text').textContent);
    });
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