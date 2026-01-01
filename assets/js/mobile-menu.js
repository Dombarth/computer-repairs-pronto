// Shared mobile menu behavior for all pages
// - Opens/closes the full-screen mobile drawer
// - Closes on link click (so you don't end up with a stuck overlay)
// - Locks body scroll while open

(function () {
  function initMobileMenu() {
    var toggle = document.getElementById('menuToggle');
    var closeBtn = document.getElementById('menuClose');
    var menu = document.getElementById('mobileMenu');

    if (!toggle || !closeBtn || !menu) return;

    function openMenu() {
      menu.classList.add('active');
      document.body.classList.add('mobile-menu-open');
    }

    function closeMenu() {
      menu.classList.remove('active');
      document.body.classList.remove('mobile-menu-open');

      // Reset submenus when closing
      menu.querySelectorAll('.mobile-submenu.active').forEach(function (sub) {
        sub.classList.remove('active');
      });
      menu.querySelectorAll('.submenu-toggle span').forEach(function (span) {
        if (span) span.textContent = '+';
      });
    }

    toggle.addEventListener('click', function () {
      if (menu.classList.contains('active')) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    closeBtn.addEventListener('click', function () {
      closeMenu();
    });

    // Close on any real navigation click inside the menu
    menu.querySelectorAll('a[href]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var href = (a.getAttribute('href') || '').trim();
        if (!href || href === '#') return;
        closeMenu();
      });
    });

    // Expand/collapse submenus
    menu.querySelectorAll('.submenu-toggle').forEach(function (toggleEl) {
      toggleEl.addEventListener('click', function (e) {
        e.preventDefault();
        var submenu = toggleEl.nextElementSibling;
        var span = toggleEl.querySelector('span');

        if (!submenu) return;
        submenu.classList.toggle('active');
        if (span) span.textContent = submenu.classList.contains('active') ? '-' : '+';
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileMenu);
  } else {
    initMobileMenu();
  }
})();

