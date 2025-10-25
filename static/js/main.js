

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Auto-refresh data every 30 seconds (optional)
function autoRefresh() {
    // Check if we're on a dashboard page
    if (window.location.pathname.includes('dashboard') || 
        window.location.pathname.includes('capacity') ||
        window.location.pathname.includes('alerts')) {
        
        // Uncomment to enable auto-refresh
        // setTimeout(() => {
        //     window.location.reload();
        // }, 30000); // 30 seconds
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Dotsh Monitoring Dashboard loaded');
    autoRefresh();
});


