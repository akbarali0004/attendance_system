document.getElementById('userProfile').addEventListener('click', function() {
    const dropdown = document.getElementById('userDropdown');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', function(e) {
    const profile = document.getElementById('userProfile');
    const dropdown = document.getElementById('userDropdown');
    if (!profile.contains(e.target)) {
        dropdown.style.display = 'none';
    }
});