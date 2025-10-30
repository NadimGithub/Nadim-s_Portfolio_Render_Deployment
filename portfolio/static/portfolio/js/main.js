/**
* Template Name: Personal
* Updated: Jan 29 2024 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/personal-free-resume-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
    const header = document.querySelector('#header');

    // Typed.js initialization
    const typed = document.querySelector('.typed');
    if (typed) {
      let typed_strings = typed.getAttribute('data-typed-items');
      typed_strings = typed_strings.split(',');
      new Typed('.typed', {
        strings: typed_strings,
        loop: true,
        typeSpeed: 100,
        backSpeed: 50,
        backDelay: 2000
      });
    }

    function showSection(targetId) {
      // Hide all sections first
      sections.forEach(section => {
        section.style.display = 'none';
        section.classList.remove('active');
      });

      // Show target section
      if (targetId === '#header') {
        header.style.display = 'block';
        header.classList.add('active');
      } else {
        const targetSection = document.querySelector(targetId);
        if (targetSection) {
          header.style.display = 'none';
          header.classList.remove('active');
          targetSection.style.display = 'block';
          targetSection.classList.add('active');
          // Reset scroll position
          targetSection.scrollTop = 0;
        }
      }

      // Update active state of links
      navLinks.forEach(link => {
        if (link.getAttribute('href') === targetId) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }

    // Add click event to each nav link
    navLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        showSection(targetId);
      });
    });

    // Show header by default
    showSection('#header');
  });

  // Progress bar animation
  function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const progressBar = entry.target;
          const value = progressBar.getAttribute('aria-valuenow');
          progressBar.style.setProperty('--progress-width', `${value}%`);
          progressBar.classList.add('animate');
          observer.unobserve(progressBar);
        }
      });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => {
      observer.observe(bar);
    });
  }

  // Initialize progress bars when document is loaded
  document.addEventListener('DOMContentLoaded', initializeProgressBars);

  // Email functionality
  // function emailsend() {
  //   const form = document.querySelector('.php-email-form');
  //   if (form) {
  //     form.addEventListener('submit', function(e) {
  //       e.preventDefault();
  //       alert('Email functionality will be implemented soon!');
  //     });
  //   }
  // }
  
  // emailsend();

  // Section transitions
  document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
  
    // Show home section by default
    document.querySelector('#header').classList.add('active');

    navLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        // Remove active class from all sections and add fade-out
        sections.forEach(section => {
          if (section.classList.contains('active')) {
            section.classList.remove('active');
            section.classList.add('fade-out');
          }
        });

        // After fade out animation, hide previous section and show new one
        setTimeout(() => {
          sections.forEach(section => {
            section.classList.remove('fade-out');
            section.style.display = section === targetSection ? 'block' : 'none';
          });

          // Add active class and fade-in to target section
          targetSection.classList.add('active', 'fade-in');

          // Remove fade-in class after animation completes
          setTimeout(() => {
            targetSection.classList.remove('fade-in');
          }, 500);
        }, 500);

        // Update active nav link
        navLinks.forEach(navLink => navLink.classList.remove('active'));
        link.classList.add('active');
      });
    });
  });

  // Mobile Navigation
  document.querySelectorAll('.mobile-nav-toggle').forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      const navMenu = this.closest('.nav-content').querySelector('.nav-menu');
      navMenu.classList.toggle('active');
      this.querySelector('i').classList.toggle('bi-list');
      this.querySelector('i').classList.toggle('bi-x');
    });
  });

  // Close mobile menu when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-content')) {
      document.querySelectorAll('.nav-menu').forEach(menu => {
        menu.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-toggle i').forEach(icon => {
        icon.classList.remove('bi-x');
        icon.classList.add('bi-list');
      });
    }
  });

  // Close mobile menu when clicking a nav link
  document.querySelectorAll('.nav-menu .nav-link').forEach(link => {
    link.addEventListener('click', function() {
      document.querySelectorAll('.nav-menu').forEach(menu => {
        menu.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-toggle i').forEach(icon => {
        icon.classList.remove('bi-x');
        icon.classList.add('bi-list');
      });
    });
  });
})();