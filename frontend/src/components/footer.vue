<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3 class="footer-title">关于我们</h3>
                    <p class="footer-text">
                        我们的AI模型检测与解释平台致力于提供全面的AI模型评估、解释和优化服务，
                        帮助开发者和企业更好地理解和应用人工智能技术。
                    </p>
                </div>

                <div class="footer-section">
                    <h3 class="footer-title">快速链接</h3>
                    <ul class="footer-links">
                        <li><a href="/" class="footer-link">首页</a></li>
                        <li><a href="/testing-center" class="footer-link">统一检测中心</a></li>
                        <li><a href="/model-explanation" class="footer-link">模型解释</a></li>
                        <li><a href="/api-docs" class="footer-link">API文档</a></li>
                        <li><a href="/feedback" class="footer-link">反馈与修正</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3 class="footer-title">资源中心</h3>
                    <ul class="footer-links">
                        <li><a href="/blog" class="footer-link">技术博客</a></li>
                        <li><a href="/tutorials" class="footer-link">教程指南</a></li>
                        <li><a href="/case-studies" class="footer-link">案例研究</a></li>
                        <li><a href="/faq" class="footer-link">常见问题</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3 class="footer-title">订阅更新</h3>
                    <p class="footer-text">订阅我们的通讯，获取最新的AI技术资讯和平台更新。</p>
                    <form class="subscribe-form" @submit.prevent="subscribeNewsletter">
                        <input type="email" v-model="email" placeholder="您的邮箱地址" class="subscribe-input" required />
                        <button type="submit" class="subscribe-button">订阅</button>
                    </form>
                </div>
            </div>

            <div class="footer-social">
                <h3 class="social-title">关注我们</h3>
                <div class="social-links">
                    <a href="#" class="social-link" aria-label="微信">
                        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M9.5 8.5C9.5 7.67157 8.82843 7 8 7C7.17157 7 6.5 7.67157 6.5 8.5C6.5 9.32843 7.17157 10 8 10C8.82843 10 9.5 9.32843 9.5 8.5Z"
                                fill="currentColor" />
                            <path
                                d="M16.5 13.5C16.5 12.6716 15.8284 12 15 12C14.1716 12 13.5 12.6716 13.5 13.5C13.5 14.3284 14.1716 15 15 15C15.8284 15 16.5 14.3284 16.5 13.5Z"
                                fill="currentColor" />
                            <path
                                d="M16 8.5C16 9.32843 16.6716 10 17.5 10C18.3284 10 19 9.32843 19 8.5C19 7.67157 18.3284 7 17.5 7C16.6716 7 16 7.67157 16 8.5Z"
                                fill="currentColor" />
                            <path
                                d="M9 13.5C9 14.3284 9.67157 15 10.5 15C11.3284 15 12 14.3284 12 13.5C12 12.6716 11.3284 12 10.5 12C9.67157 12 9 12.6716 9 13.5Z"
                                fill="currentColor" />
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M12.5 1C6.14873 1 1 6.14873 1 12.5C1 18.8513 6.14873 24 12.5 24C18.8513 24 24 18.8513 24 12.5C24 6.14873 18.8513 1 12.5 1ZM5.5 9.5C5.5 6.46243 8.46243 4 12 4C15.5376 4 18.5 6.46243 18.5 9.5C18.5 10.3246 18.3216 11.1092 18 11.8293C18.3216 11.9399 18.6235 12.0816 18.9018 12.2505C19.2978 12.4859 19.6547 12.7717 19.9619 13.0981C20.5826 13.7581 21 14.6085 21 15.5C21 18.5376 18.0376 21 14.5 21C13.6754 21 12.8908 20.8216 12.1707 20.5C12.0601 20.8216 11.9184 21.1235 11.7495 21.4018C11.5141 21.7978 11.2283 22.1547 10.9019 22.4619C10.2419 23.0826 9.39149 23.5 8.5 23.5C5.46243 23.5 3 20.5376 3 17C3 14.9624 4.13964 13.1911 5.82432 12.2459C5.63803 11.7369 5.5 11.1385 5.5 10.5V9.5Z"
                                fill="currentColor" />
                        </svg>
                    </a>
                    <a href="#" class="social-link" aria-label="微博">
                        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M10.9 14.1C10.9 12.3 13 10.5 15.5 10.5C18 10.5 19.5 12 19.5 13.5C19.5 15 18 17.5 15 17.5C12 17.5 10.9 15.9 10.9 14.1Z"
                                fill="currentColor" />
                            <path
                                d="M11.5 14.5C11.5 13.1193 12.6193 12 14 12C15.3807 12 16.5 13.1193 16.5 14.5C16.5 15.8807 15.3807 17 14 17C12.6193 17 11.5 15.8807 11.5 14.5Z"
                                fill="currentColor" />
                            <path
                                d="M14.5 14C14.5 13.7239 14.7239 13.5 15 13.5C15.2761 13.5 15.5 13.7239 15.5 14C15.5 14.2761 15.2761 14.5 15 14.5C14.7239 14.5 14.5 14.2761 14.5 14Z"
                                fill="currentColor" />
                            <path
                                d="M13 14C13 13.7239 13.2239 13.5 13.5 13.5C13.7761 13.5 14 13.7239 14 14C14 14.2761 13.7761 14.5 13.5 14.5C13.2239 14.5 13 14.2761 13 14Z"
                                fill="currentColor" />
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12ZM18.7773 9.20642C18.6137 9.1694 18.4473 9.14 18.28 9.12C18.1254 9.10228 17.9689 9.09734 17.814 9.105C17.6622 9.11252 17.5119 9.13396 17.3654 9.16889C17.2256 9.20208 17.0894 9.24841 16.9587 9.30722C16.8343 9.36331 16.7151 9.43125 16.6028 9.50999C16.4967 9.58414 16.3972 9.66839 16.3055 9.76158C16.2196 9.84997 16.1411 9.94661 16.0709 10.0501C16.0059 10.1463 15.9488 10.2485 15.9004 10.3553C15.8565 10.4541 15.8207 10.5566 15.7935 10.6616C15.7695 10.7566 15.7529 10.8533 15.7438 10.9511C15.7361 11.0379 15.7345 11.1252 15.7391 11.2123C15.7446 11.2883 15.7552 11.3638 15.7708 11.4382C15.7877 11.5041 15.8086 11.5689 15.8333 11.6323C15.8595 11.6887 15.8887 11.7437 15.9208 11.7971C15.9546 11.8438 15.9906 11.8889 16.0287 11.9323C16.0686 11.9693 16.1101 12.0047 16.1531 12.0383C16.1981 12.0669 16.2442 12.0938 16.2913 12.1189C16.3405 12.1401 16.3905 12.1595 16.4412 12.1771C16.4941 12.1918 16.5475 12.2047 16.6013 12.2157C16.6574 12.2245 16.7138 12.2315 16.7704 12.2366C16.8294 12.2401 16.8885 12.2417 16.9476 12.2415C17.0092 12.2398 17.0707 12.2362 17.132 12.2307C17.1959 12.2239 17.2595 12.2151 17.3227 12.2044C17.3886 12.1926 17.4539 12.1787 17.5186 12.1628C17.5861 12.1459 17.6528 12.1268 17.7187 12.1055C17.7874 12.0833 17.8552 12.0588 17.9219 12.0321C17.9915 12.0045 18.0599 11.9745 18.1269 11.9423C18.1969 11.9091 18.2654 11.8735 18.3323 11.8356C18.4023 11.7966 18.4705 11.7551 18.5368 11.7112C18.6063 11.6661 18.6737 11.6184 18.7389 11.5683C18.8074 11.5168 18.8735 11.4627 18.9371 11.4061C19.0042 11.3479 19.0685 11.2869 19.1298 11.2233C19.1947 11.1579 19.2563 11.0896 19.3144 11.0187C19.3763 10.9457 19.4343 10.8697 19.4882 10.7909C19.5461 10.7097 19.5994 10.6254 19.6478 10.5384C19.7003 10.4487 19.7473 10.3559 19.7886 10.2605C19.8341 10.1621 19.8731 10.0608 19.9053 9.95704C19.9418 9.84957 19.9707 9.73927 19.9918 9.62704C20.0173 9.50957 20.0341 9.39027 20.0418 9.27004C20.0518 9.14457 20.0518 9.01857 20.0418 8.89304C20.0341 8.76757 20.0173 8.64304 19.9918 8.52004C19.9707 8.40304 19.9418 8.28757 19.9053 8.17504C19.8731 8.06604 19.8341 7.96004 19.7886 7.85704C19.7473 7.75704 19.7003 7.66004 19.6478 7.56604C19.5994 7.47404 19.5461 7.38604 19.4882 7.30204C19.4343 7.22204 19.3763 7.14604 19.3144 7.07304C19.2563 7.00204 19.1947 6.93404 19.1298 6.86904C19.0685 6.80504 19.0042 6.74404 18.9371 6.68604C18.8735 6.62904 18.8074 6.57504 18.7389 6.52304C18.6737 6.47304 18.6063 6.42504 18.5368 6.38004C18.4705 6.33604 18.4023 6.29504 18.3323 6.25604C18.2654 6.21804 18.1969 6.18304 18.1269 6.14904C18.0599 6.11704 17.9915 6.08704 17.9219 6.05904C17.8552 6.03304 17.7874 6.00904 17.7187 5.98704C17.6528 5.96604 17.5861 5.94704 17.5186 5.93004C17.4539 5.91404 17.3886 5.90004 17.3227 5.88804C17.2595 5.87704 17.1959 5.86804 17.132 5.86104C17.0707 5.85504 17.0092 5.85104 16.9476 5.84904C16.8885 5.84704 16.8294 5.84904 16.7704 5.85204C16.7138 5.85704 16.6574 5.86404 16.6013 5.87304C16.5475 5.88304 16.4941 5.89604 16.4412 5.91104C16.3905 5.92804 16.3405 5.94704 16.2913 5.96804C16.2442 5.99304 16.1981 6.01904 16.1531 6.04804C16.1101 6.08104 16.0686 6.11704 16.0287 6.15404C15.9906 6.19704 15.9546 6.24204 15.9208 6.28904C15.8887 6.34204 15.8595 6.39704 15.8333 6.45304C15.8086 6.51704 15.7877 6.58204 15.7708 6.64804C15.7552 6.72204 15.7446 6.79704 15.7391 6.87304C15.7345 6.96004 15.7361 7.04704 15.7438 7.13404C15.7529 7.23204 15.7695 7.32904 15.7935 7.42404C15.8207 7.52904 15.8565 7.63104 15.9004 7.73004C15.9488 7.83704 16.0059 7.93904 16.0709 8.03504C16.1411 8.13904 16.2196 8.23504 16.3055 8.32404C16.3972 8.41704 16.4967 8.50104 16.6028 8.57504C16.7151 8.65404 16.8343 8.72204 16.9587 8.77804C17.0894 8.83704 17.2256 8.88304 17.3654 8.91604C17.5119 8.95104 17.6622 8.97204 17.814 8.98004C17.9689 8.98704 18.1254 8.98204 18.28 8.96504C18.4473 8.94504 18.6137 8.91504 18.7773 8.87804C18.7773 8.87804 18.7773 9.20642 18.7773 9.20642ZM9.5 8.5C9.5 7.67157 8.82843 7 8 7C7.17157 7 6.5 7.67157 6.5 8.5C6.5 9.32843 7.17157 10 8 10C8.82843 10 9.5 9.32843 9.5 8.5ZM16.5 13.5C16.5 12.6716 15.8284 12 15 12C14.1716 12 13.5 12.6716 13.5 13.5C13.5 14.3284 14.1716 15 15 15C15.8284 15 16.5 14.3284 16.5 13.5ZM16 8.5C16 9.32843 16.6716 10 17.5 10C18.3284 10 19 9.32843 19 8.5C19 7.67157 18.3284 7 17.5 7C16.6716 7 16 7.67157 16 8.5ZM9 13.5C9 14.3284 9.67157 15 10.5 15C11.3284 15 12 14.3284 12 13.5C12 12.6716 11.3284 12 10.5 12C9.67157 12 9 12.6716 9 13.5Z"
                                fill="currentColor" />
                        </svg>
                    </a>
                    <a href="#" class="social-link" aria-label="知乎">
                        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12.2 4H9.8V15H12.2V4Z" fill="currentColor" />
                            <path
                                d="M11 16.5C10.1716 16.5 9.5 17.1716 9.5 18C9.5 18.8284 10.1716 19.5 11 19.5H17L14 16.5H11Z"
                                fill="currentColor" />
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12ZM7.5 7.5H14.5V11.5H7.5V7.5Z"
                                fill="currentColor" />
                        </svg>
                    </a>
                    <a href="#" class="social-link" aria-label="GitHub">
                        <svg class="social-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M12 2C6.477 2 2 6.477 2 12C2 16.418 4.865 20.166 8.839 21.489C9.339 21.581 9.521 21.278 9.521 21.017C9.521 20.783 9.512 20.036 9.508 19.205C6.726 19.859 6.139 17.977 6.139 17.977C5.685 16.915 5.028 16.613 5.028 16.613C4.132 15.967 5.097 15.98 5.097 15.98C6.094 16.052 6.626 17.034 6.626 17.034C7.521 18.559 8.97 18.025 9.54 17.775C9.631 17.133 9.889 16.699 10.175 16.419C7.955 16.137 5.62 15.318 5.62 11.47C5.62 10.411 6.01 9.544 6.646 8.864C6.545 8.614 6.201 7.649 6.747 6.24C6.747 6.24 7.587 5.977 9.497 7.303C10.295 7.086 11.15 6.977 12 6.974C12.85 6.977 13.705 7.086 14.504 7.303C16.413 5.977 17.251 6.24 17.251 6.24C17.798 7.649 17.454 8.614 17.353 8.864C17.99 9.544 18.378 10.411 18.378 11.47C18.378 15.328 16.039 16.134 13.813 16.411C14.172 16.75 14.492 17.429 14.492 18.463C14.492 19.937 14.479 20.692 14.479 21.017C14.479 21.28 14.659 21.586 15.167 21.487C19.138 20.161 22 16.416 22 12C22 6.477 17.523 2 12 2Z"
                                fill="currentColor" />
                        </svg>
                    </a>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <div class="container">
                <p class="copyright">© {{ currentYear }} AI模型检测与解释平台 | 保留所有权利</p>
                <div class="footer-bottom-links">
                    <a href="/privacy" class="bottom-link">隐私政策</a>
                    <a href="/terms" class="bottom-link">使用条款</a>
                    <a href="/sitemap" class="bottom-link">网站地图</a>
                </div>
            </div>
        </div>
    </footer>
</template>

<script setup>
import { ref, computed } from 'vue';

// Email for newsletter subscription
const email = ref('');

// Get current year for copyright
const currentYear = computed(() => new Date().getFullYear());

// Function to handle newsletter subscription
const subscribeNewsletter = () => {
    // Here you would typically send the email to your backend
    alert(`感谢订阅！我们将发送更新到: ${email.value}`);
    email.value = ''; // Clear the input after submission
};
</script>

<style scoped>
.footer {
    background-color: #f8f9fa;
    color: #333;
    padding-top: 3rem;
    margin-top: 2rem;
    border-top: 1px solid #e9ecef;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.footer-content {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

@media (min-width: 640px) {
    .footer-content {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 960px) {
    .footer-content {
        grid-template-columns: repeat(4, 1fr);
    }
}

.footer-section {
    margin-bottom: 1.5rem;
}

.footer-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #333;
}

.footer-text {
    font-size: 0.875rem;
    line-height: 1.5;
    color: #555;
    margin-bottom: 1rem;
}

.footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-links li {
    margin-bottom: 0.5rem;
}

.footer-link {
    color: #555;
    text-decoration: none;
    font-size: 0.875rem;
    transition: color 0.2s;
}

.footer-link:hover {
    color: #4f46e5;
}

.subscribe-form {
    display: flex;
    margin-top: 1rem;
}

.subscribe-input {
    flex: 1;
    padding: 0.5rem 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 0.25rem 0 0 0.25rem;
    font-size: 0.875rem;
}

.subscribe-input:focus {
    outline: none;
    border-color: #4f46e5;
}

.subscribe-button {
    background-color: #4f46e5;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0 0.25rem 0.25rem 0;
    font-size: 0.875rem;
    cursor: pointer;
    transition: background-color 0.2s;
}

.subscribe-button:hover {
    background-color: #4338ca;
}

.footer-social {
    margin: 2rem 0;
    text-align: center;
}

.social-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
}

.social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
    background-color: #f3f4f6;
    color: #4f46e5;
    transition: background-color 0.2s, color 0.2s;
}

.social-link:hover {
    background-color: #4f46e5;
    color: white;
}

.social-icon {
    width: 1.25rem;
    height: 1.25rem;
}

.footer-bottom {
    border-top: 1px solid #e9ecef;
    padding: 1.5rem 0;
}

.footer-bottom .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

@media (min-width: 768px) {
    .footer-bottom .container {
        flex-direction: row;
        justify-content: space-between;
    }
}

.copyright {
    font-size: 0.875rem;
    color: #6b7280;
}

.footer-bottom-links {
    display: flex;
    gap: 1.5rem;
}

.bottom-link {
    font-size: 0.875rem;
    color: #6b7280;
    text-decoration: none;
    transition: color 0.2s;
}

.bottom-link:hover {
    color: #4f46e5;
}
</style>