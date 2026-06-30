document.addEventListener('DOMContentLoaded', () => {
    // ============================================
    // Theme Toggling
    // ============================================
    const themeToggleBtn = document.getElementById('theme-toggle');
    const root = document.documentElement;
    
    const savedTheme = localStorage.getItem('ai-portal-theme');
    if (savedTheme) {
        root.setAttribute('data-theme', savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        root.setAttribute('data-theme', 'light');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = root.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            root.setAttribute('data-theme', newTheme);
            localStorage.setItem('ai-portal-theme', newTheme);
            // Update icon
            const icon = themeToggleBtn.querySelector('ion-icon');
            if (icon) icon.setAttribute('name', newTheme === 'light' ? 'sunny-outline' : 'moon-outline');
        });
        // Set initial icon
        const currentTheme = root.getAttribute('data-theme');
        const icon = themeToggleBtn.querySelector('ion-icon');
        if (icon && currentTheme === 'light') icon.setAttribute('name', 'sunny-outline');
    }

    // ============================================
    // Mobile Sidebar Toggle
    // ============================================
    const mobileToggleBtn = document.getElementById('mobile-toggle');
    const sidebar = document.getElementById('sidebar');
    const mobileOverlay = document.getElementById('mobile-overlay');

    function openSidebar() {
        sidebar.classList.add('open');
        if (mobileOverlay) mobileOverlay.classList.add('visible');
    }

    function closeSidebar() {
        sidebar.classList.remove('open');
        if (mobileOverlay) mobileOverlay.classList.remove('visible');
    }

    if (mobileToggleBtn) {
        mobileToggleBtn.addEventListener('click', () => {
            sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
        });
    }

    if (mobileOverlay) {
        mobileOverlay.addEventListener('click', closeSidebar);
    }

    // ============================================
    // Scroll Animations (Intersection Observer)
    // ============================================
    function initAnimations() {
        const observerOptions = { root: null, rootMargin: '0px 0px -50px 0px', threshold: 0.05 };
        const animateObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.animate-on-scroll').forEach(el => {
            // Reset state for freshly loaded content
            if (!el.classList.contains('animate-in')) {
                animateObserver.observe(el);
            }
        });

        // Initialize Mermaid if available
        if (typeof mermaid !== 'undefined') {
            const isDark = root.getAttribute('data-theme') !== 'light';
            mermaid.initialize({
                startOnLoad: false,
                theme: isDark ? 'dark' : 'default',
                securityLevel: 'loose',
                fontFamily: 'Inter',
                flowchart: { curve: 'basis' }
            });
            // Render any unprocessed mermaid blocks
            try {
                mermaid.init(undefined, document.querySelectorAll('.mermaid:not([data-processed])'));
            } catch(e) { /* Mermaid may throw on re-init */ }
        }
    }

    initAnimations();

    // ============================================
    // Sidebar Navigation (Standard link navigation)
    // ============================================
    // All sidebar links use standard <a href> navigation.
    // The "active" state is set based on the current page filename.
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.sidebar .nav-item').forEach(link => {
        const href = link.getAttribute('href');
        link.classList.remove('active');
        if (href === currentPage) {
            link.classList.add('active');
        }
    });
});
