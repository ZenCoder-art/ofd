<template>
    <nav class="navbar" :class="{ 'scrolled': hasScrolled }">
        <div class="navbar-bg"></div>
        <div class="container">
            <div class="navbar-content">
                <div class="navbar-left">
                    <div class="logo-container">
                        <div class="logo-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                            </svg>
                        </div>
                        <span class="logo-text">AI<span class="logo-highlight">Platform</span></span>
                    </div>
                    <div class="desktop-menu">
                        <a v-for="(item, index) in navItems" :key="index" :href="item.path" class="nav-link"
                            :class="{ 'active': activeLink === item.id }" @click="setActiveLink(item.id)">
                            <span class="nav-text">{{ item.name }}</span>
                            <span class="nav-indicator"></span>
                        </a>
                    </div>
                </div>

                <div class="navbar-right">
                    <button class="action-button">
                        <span>登录</span>
                    </button>

                    <div class="mobile-menu-button">
                        <button @click="toggleMenu" type="button" class="menu-toggle" aria-controls="mobile-menu"
                            :aria-expanded="isOpen">
                            <span class="sr-only">打开主菜单</span>
                            <div class="hamburger" :class="{ 'active': isOpen }">
                                <span class="hamburger-line"></span>
                                <span class="hamburger-line"></span>
                                <span class="hamburger-line"></span>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="mobile-menu-container" :class="{ 'open': isOpen }">
            <div class="mobile-menu-backdrop" @click="closeMenu"></div>
            <div class="mobile-menu">
                <div class="mobile-menu-header">
                    <div class="logo-container">
                        <div class="logo-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                            </svg>
                        </div>
                        <span class="logo-text">AI<span class="logo-highlight">Platform</span></span>
                    </div>
                    <button class="close-button" @click="closeMenu">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </button>
                </div>
                <div class="mobile-menu-links">
                    <a v-for="(item, index) in navItems" :key="index" :href="item.path" class="mobile-link"
                        :class="{ 'active': activeLink === item.id }" @click="setActiveLink(item.id)">
                        <span>{{ item.name }}</span>
                    </a>
                </div>
                <div class="mobile-menu-footer">
                    <button class="mobile-action-button">
                        <span>登录</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// Navigation items
const navItems = [
    { id: 'home', name: '首页', path: '/' },
    { id: 'testing', name: '统一检测中心', path: '/testing-center' },
    { id: 'model', name: '模型解释', path: '/model-explanation' },
    { id: 'api', name: 'API文档', path: '/api-docs' },
    { id: 'feedback', name: '反馈与修正', path: '/feedback' }
];

// State for mobile menu
const isOpen = ref(false);

// State for active link
const activeLink = ref('home');

// State for scroll detection
const hasScrolled = ref(false);

// Function to set active link
const setActiveLink = (link) => {
    activeLink.value = link;
    closeMenu();
};

// Function to toggle mobile menu
const toggleMenu = () => {
    isOpen.value = !isOpen.value;
    if (isOpen.value) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = '';
    }
};

// Function to close mobile menu
const closeMenu = () => {
    isOpen.value = false;
    document.body.style.overflow = '';
};

// Function to handle scroll
const handleScroll = () => {
    hasScrolled.value = window.scrollY > 20;
};

// Add scroll event listener
onMounted(() => {
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check initial scroll position
});

// Remove scroll event listener
onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* Modern navbar styling */
.navbar {
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    z-index: 1000;
    transition: all 0.3s ease;
}

.navbar-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    z-index: -1;
    transition: all 0.3s ease;
}

.navbar.scrolled .navbar-bg {
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1.5rem;
    height: 100%;
}

.navbar-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
}

.navbar-left {
    display: flex;
    align-items: center;
}

.navbar-right {
    display: flex;
    align-items: center;
}

/* Logo styling */
.logo-container {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.logo-icon {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4f46e5;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
    border-radius: 8px;
    padding: 6px;
}

.logo-text {
    font-size: 1.25rem;
    font-weight: 700;
    background: linear-gradient(to right, #1a202c, #4a5568);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.logo-highlight {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

/* Desktop menu */
.desktop-menu {
    display: none;
    margin-left: 3rem;
}

@media (min-width: 768px) {
    .desktop-menu {
        display: flex;
        align-items: center;
        gap: 2rem;
    }
}

.nav-link {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.5rem 0;
    font-size: 0.9rem;
    font-weight: 500;
    text-decoration: none;
    color: #4a5568;
    transition: color 0.3s ease;
}

.nav-text {
    position: relative;
    z-index: 1;
}

.nav-indicator {
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    transition: width 0.3s ease;
    border-radius: 2px;
}

.nav-link:hover {
    color: #1a202c;
}

.nav-link:hover .nav-indicator {
    width: 100%;
}

.nav-link.active {
    color: #4f46e5;
}

.nav-link.active .nav-indicator {
    width: 100%;
}

/* Action button */
.action-button {
    display: none;
    padding: 0.5rem 1.25rem;
    margin-right: 1rem;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.2);
}

@media (min-width: 768px) {
    .action-button {
        display: block;
    }
}

.action-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(79, 70, 229, 0.3);
}

/* Mobile menu button */
.mobile-menu-button {
    display: flex;
    align-items: center;
}

@media (min-width: 768px) {
    .mobile-menu-button {
        display: none;
    }
}

.menu-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 8px;
    background-color: rgba(79, 70, 229, 0.05);
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.menu-toggle:hover {
    background-color: rgba(79, 70, 229, 0.1);
}

.hamburger {
    position: relative;
    width: 20px;
    height: 16px;
}

.hamburger-line {
    position: absolute;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #4f46e5;
    border-radius: 2px;
    transition: all 0.3s ease;
}

.hamburger-line:nth-child(1) {
    top: 0;
}

.hamburger-line:nth-child(2) {
    top: 7px;
}

.hamburger-line:nth-child(3) {
    bottom: 0;
}

.hamburger.active .hamburger-line:nth-child(1) {
    transform: translateY(7px) rotate(45deg);
}

.hamburger.active .hamburger-line:nth-child(2) {
    opacity: 0;
}

.hamburger.active .hamburger-line:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}

/* Mobile menu */
.mobile-menu-container {
    position: fixed;
    top: 0;
    right: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    pointer-events: none;
    z-index: 2000;
}

.mobile-menu-container.open {
    pointer-events: auto;
}

.mobile-menu-backdrop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(3px);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.mobile-menu-container.open .mobile-menu-backdrop {
    opacity: 1;
}

.mobile-menu {
    position: absolute;
    top: 0;
    right: 0;
    width: 80%;
    max-width: 350px;
    height: 100%;
    background: white;
    box-shadow: -5px 0 30px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    transform: translateX(100%);
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.mobile-menu-container.open .mobile-menu {
    transform: translateX(0);
}

.mobile-menu-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    border-bottom: 1px solid rgba(229, 231, 235, 0.5);
}

.close-button {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    background: rgba(79, 70, 229, 0.05);
    color: #4f46e5;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.close-button svg {
    width: 20px;
    height: 20px;
}

.close-button:hover {
    background: rgba(79, 70, 229, 0.1);
}

.mobile-menu-links {
    flex: 1;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    overflow-y: auto;
}

.mobile-link {
    display: block;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    color: #4a5568;
    transition: all 0.3s ease;
}

.mobile-link:hover {
    background-color: rgba(79, 70, 229, 0.05);
    color: #4f46e5;
}

.mobile-link.active {
    background-color: rgba(79, 70, 229, 0.1);
    color: #4f46e5;
}

.mobile-menu-footer {
    padding: 1.5rem;
    border-top: 1px solid rgba(229, 231, 235, 0.5);
}

.mobile-action-button {
    width: 100%;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.2);
}

.mobile-action-button:hover {
    box-shadow: 0 6px 15px rgba(79, 70, 229, 0.3);
}
</style>