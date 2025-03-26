<template>
    <div class="home-container">
        <!-- Background elements -->
        <div class="bg-shape bg-shape-1"></div>
        <div class="bg-shape bg-shape-2"></div>
        <div class="bg-shape bg-shape-3"></div>
        <div class="bg-shape bg-shape-4"></div>
        <div class="bg-shape bg-shape-5"></div>

        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-content">
                <h1 class="title">
                    <span class="gradient-text">招聘欺诈</span>
                    <span>智能检测平台</span>
                </h1>
                <p class="subtitle">保护求职者权益，识别虚假招聘信息，让求职更安心</p>
                <div class="cta-buttons">
                    <button class="primary-button">
                        <span>立即检测</span>
                        <svg class="button-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13.75 6.75L19.25 12L13.75 17.25" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M19 12H4.75" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </button>
                    <button class="secondary-button">
                        <span>了解更多</span>
                        <svg class="button-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 5.75V18.25" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M18.25 12L12 18.25L5.75 12" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </button>
                </div>
            </div>
            <div class="hero-image">
                <div class="hero-image-container">
                    <div class="hero-image-glow"></div>
                    <svg class="hero-svg" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                        <path fill="#4F46E5"
                            d="M39.9,-65.7C51.5,-58.4,60.8,-47.8,67.2,-35.5C73.6,-23.2,77.1,-9.1,76.3,4.7C75.5,18.5,70.3,32,61.7,42.8C53.1,53.6,41.1,61.7,28.1,67.2C15.1,72.7,1.1,75.6,-13.9,74.8C-28.9,74,-44.9,69.5,-57.1,59.9C-69.3,50.3,-77.7,35.7,-80.9,20C-84.1,4.3,-82.1,-12.5,-75.3,-26.3C-68.5,-40.1,-56.9,-51,-44,-59.5C-31.1,-68,-15.5,-74.1,-0.3,-73.6C14.9,-73.1,29.9,-66,39.9,-65.7Z"
                            transform="translate(100 100)" />
                    </svg>
                </div>
            </div>
        </section>

        <!-- Stats Section -->
        <section class="stats-section">
            <div class="stats-container">
                <div class="stat-item">
                    <div class="stat-value">
                        <span class="counter" data-target="10000">0</span>+
                    </div>
                    <div class="stat-label">已检测招聘信息</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">
                        <span class="counter" data-target="98">0</span>%
                    </div>
                    <div class="stat-label">检测准确率</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">
                        <span class="counter" data-target="500">0</span>+
                    </div>
                    <div class="stat-label">成功识别欺诈案例</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">
                        <span class="counter" data-target="24">0</span>/7
                    </div>
                    <div class="stat-label">全天候保护</div>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="features">
            <h2 class="section-title">
                <span class="gradient-text">主要功能</span>
            </h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon-container">
                        <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 12L11 14L15 10" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path
                                d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                stroke="currentColor" stroke-width="2" />
                        </svg>
                    </div>
                    <h3>多维度欺诈检测</h3>
                    <p>通过文本分析、公司信息验证、联系方式核查等多维度分析，全面识别招聘欺诈</p>
                    <div class="card-hover-effect"></div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-container">
                        <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M12 16V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M12 8H12.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>风险评估报告</h3>
                    <p>提供详细的风险评估报告，包括风险等级、具体风险点分析和安全建议</p>
                    <div class="card-hover-effect"></div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-container">
                        <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M21 10H3" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M21 6H3" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M21 14H3" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M21 18H3" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>多种检测方式</h3>
                    <p>支持手动输入、文件上传、网页链接等多种检测方式，满足不同场景需求</p>
                    <div class="card-hover-effect"></div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon-container">
                        <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M4 19V5C4 3.89543 4.89543 3 6 3H19.4C19.7314 3 20 3.26863 20 3.6V16.7143"
                                stroke="currentColor" stroke-width="2" />
                            <path d="M8 3V7H12V3" stroke="currentColor" stroke-width="2" />
                            <path d="M6 21H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M6 17H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M15 13.5V10.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M8 13.5V10.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                            <path d="M11.5 13.5V10.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
                        </svg>
                    </div>
                    <h3>开放API接口</h3>
                    <p>提供完整的API文档和接口，支持第三方平台和应用集成我们的检测服务</p>
                    <div class="card-hover-effect"></div>
                </div>
            </div>
        </section>

        <!-- How It Works Section -->
        <section class="how-it-works">
            <h2 class="section-title">
                <span class="gradient-text">如何使用</span>
            </h2>
            <div class="steps-container">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>提交招聘信息</h3>
                        <p>通过手动输入、上传文件或提供网页链接的方式提交需要检测的招聘信息</p>
                    </div>
                </div>
                <div class="step-connector">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                        <path d="M12 5L19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>AI智能分析</h3>
                        <p>我们的AI系统会从多个维度分析招聘信息，识别潜在的欺诈风险和可疑点</p>
                    </div>
                </div>
                <div class="step-connector">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                        <path d="M12 5L19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>获取检测结果</h3>
                        <p>获得详细的风险评估报告，了解招聘信息的可信度和潜在风险</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <section class="testimonials">
            <h2 class="section-title">
                <span class="gradient-text">用户评价</span>
            </h2>
            <div class="testimonial-slider" ref="testimonialSlider">
                <div class="testimonial-slide">
                    <div class="testimonial-card">
                        <div class="testimonial-content">
                            <svg class="quote-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M10 11H6C4.89543 11 4 10.1046 4 9V7C4 5.89543 4.89543 5 6 5H8C9.10457 5 10 5.89543 10 7V11ZM10 11V13C10 15.2091 8.20914 17 6 17H5"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path
                                    d="M20 11H16C14.8954 11 14 10.1046 14 9V7C14 5.89543 14.8954 5 16 5H18C19.1046 5 20 5.89543 20 7V11ZM20 11V13C20 15.2091 18.2091 17 16 17H15"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                            <p>这个平台帮我识别出了一个看似正规的招聘骗局，避免了我交纳所谓的"培训费"。检测报告详细指出了多个可疑点，非常专业。</p>
                        </div>
                        <div class="testimonial-author">
                            <div class="author-avatar">
                                <div class="avatar-placeholder">LY</div>
                            </div>
                            <div class="author-info">
                                <h4>李阳</h4>
                                <p>应届毕业生</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-slide">
                    <div class="testimonial-card">
                        <div class="testimonial-content">
                            <svg class="quote-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M10 11H6C4.89543 11 4 10.1046 4 9V7C4 5.89543 4.89543 5 6 5H8C9.10457 5 10 5.89543 10 7V11ZM10 11V13C10 15.2091 8.20914 17 6 17H5"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path
                                    d="M20 11H16C14.8954 11 14 10.1046 14 9V7C14 5.89543 14.8954 5 16 5H18C19.1046 5 20 5.89543 20 7V11ZM20 11V13C20 15.2091 18.2091 17 16 17H15"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                            <p>作为一家招聘平台，我们集成了这个API来保护用户安全。系统能够准确识别出虚假招聘信息，大大提升了平台的安全性和用户信任度。</p>
                        </div>
                        <div class="testimonial-author">
                            <div class="author-avatar">
                                <div class="avatar-placeholder">ZM</div>
                            </div>
                            <div class="author-info">
                                <h4>张敏</h4>
                                <p>招聘网站产品经理</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="testimonial-slide">
                    <div class="testimonial-card">
                        <div class="testimonial-content">
                            <svg class="quote-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M10 11H6C4.89543 11 4 10.1046 4 9V7C4 5.89543 4.89543 5 6 5H8C9.10457 5 10 5.89543 10 7V11ZM10 11V13C10 15.2091 8.20914 17 6 17H5"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path
                                    d="M20 11H16C14.8954 11 14 10.1046 14 9V7C14 5.89543 14.8954 5 16 5H18C19.1046 5 20 5.89543 20 7V11ZM20 11V13C20 15.2091 18.2091 17 16 17H15"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                            <p>我们学校将这个平台推荐给所有即将毕业的学生，帮助他们避免求职陷阱。系统的多维度检测和详细分析报告让学生能够更安心地找工作。</p>
                        </div>
                        <div class="testimonial-author">
                            <div class="author-avatar">
                                <div class="avatar-placeholder">WJ</div>
                            </div>
                            <div class="author-info">
                                <h4>王俊</h4>
                                <p>大学就业指导中心主任</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="testimonial-controls">
                <button class="control-button prev" @click="prevTestimonial">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 12H5" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                        <path d="M12 19L5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                </button>
                <div class="testimonial-dots">
                    <span class="dot active" @click="goToTestimonial(0)"></span>
                    <span class="dot" @click="goToTestimonial(1)"></span>
                    <span class="dot" @click="goToTestimonial(2)"></span>
                </div>
                <button class="control-button next" @click="nextTestimonial">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                        <path d="M12 5L19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                </button>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="cta-section">
            <div class="cta-content">
                <h2>保护您的求职安全</h2>
                <p>立即使用我们的招聘欺诈检测平台，避免陷入求职陷阱</p>
                <button class="cta-button">
                    <span>免费检测</span>
                    <svg class="button-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13.75 6.75L19.25 12L13.75 17.25" stroke="currentColor" stroke-width="2"
                            stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M19 12H4.75" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                </button>
            </div>
        </section>

        <!-- FAQ Section -->
        <section class="faq-section">
            <h2 class="section-title">
                <span class="gradient-text">常见问题</span>
            </h2>
            <div class="faq-container">
                <div class="faq-item" :class="{ 'active': activeQuestion === 1 }" @click="toggleQuestion(1)">
                    <div class="faq-question">
                        <h3>如何判断招聘信息是否存在欺诈风险？</h3>
                        <div class="faq-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" :class="{ 'hidden': activeQuestion === 1 }" />
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <div class="faq-answer" :class="{ 'show': activeQuestion === 1 }">
                        <p>我们的系统会从多个维度分析招聘信息，包括公司信息真实性、联系方式可靠性、薪资合理性、工作描述专业性等。系统会给出综合风险评分和具体风险点分析，帮助您判断招聘信息的可信度。</p>
                    </div>
                </div>
                <div class="faq-item" :class="{ 'active': activeQuestion === 2 }" @click="toggleQuestion(2)">
                    <div class="faq-question">
                        <h3>平台支持检测哪些类型的招聘信息？</h3>
                        <div class="faq-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" :class="{ 'hidden': activeQuestion === 2 }" />
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <div class="faq-answer" :class="{ 'show': activeQuestion === 2 }">
                        <p>我们的平台支持各类招聘信息的检测，包括但不限于招聘网站上的职位信息、招聘邮件、社交媒体招聘帖子、招聘传单等。您可以通过手动输入、上传文件（PDF、Word、图片等）或提供网页链接的方式提交需要检测的信息。
                        </p>
                    </div>
                </div>
                <div class="faq-item" :class="{ 'active': activeQuestion === 3 }" @click="toggleQuestion(3)">
                    <div class="faq-question">
                        <h3>检测结果有多准确？</h3>
                        <div class="faq-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" :class="{ 'hidden': activeQuestion === 3 }" />
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <div class="faq-answer" :class="{ 'show': activeQuestion === 3 }">
                        <p>我们的系统基于大量真实招聘欺诈案例训练，结合最新的AI技术和专家规则，检测准确率达到98%以上。系统会持续学习和更新，以应对不断变化的欺诈手段。不过，我们仍建议您结合检测结果和自身判断做出决策。
                        </p>
                    </div>
                </div>
                <div class="faq-item" :class="{ 'active': activeQuestion === 4 }" @click="toggleQuestion(4)">
                    <div class="faq-question">
                        <h3>如何集成贵平台的API？</h3>
                        <div class="faq-icon">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" :class="{ 'hidden': activeQuestion === 4 }" />
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <div class="faq-answer" :class="{ 'show': activeQuestion === 4 }">
                        <p>我们提供完整的RESTful
                            API接口，支持您将我们的检测服务集成到自己的应用或平台中。您可以在我们的API文档中找到详细的接口说明、请求参数、响应格式和示例代码。我们支持多种编程语言的SDK，包括JavaScript、Python、Java等。
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// For FAQ section
const activeQuestion = ref(null);

const toggleQuestion = (index) => {
    if (activeQuestion.value === index) {
        activeQuestion.value = null;
    } else {
        activeQuestion.value = index;
    }
};

// For testimonial slider
const currentTestimonial = ref(0);
const testimonialSlider = ref(null);
const autoplayInterval = ref(null);

const goToTestimonial = (index) => {
    currentTestimonial.value = index;
    updateTestimonialSlider();
    resetAutoplay();
};

const nextTestimonial = () => {
    currentTestimonial.value = (currentTestimonial.value + 1) % 3;
    updateTestimonialSlider();
    resetAutoplay();
};

const prevTestimonial = () => {
    currentTestimonial.value = (currentTestimonial.value - 1 + 3) % 3;
    updateTestimonialSlider();
    resetAutoplay();
};

const updateTestimonialSlider = () => {
    if (testimonialSlider.value) {
        testimonialSlider.value.style.transform = `translateX(-${currentTestimonial.value * 100}%)`;

        // Update dots
        const dots = document.querySelectorAll('.testimonial-dots .dot');
        dots.forEach((dot, index) => {
            if (index === currentTestimonial.value) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }
};

const startAutoplay = () => {
    autoplayInterval.value = setInterval(() => {
        nextTestimonial();
    }, 5000);
};

const resetAutoplay = () => {
    if (autoplayInterval.value) {
        clearInterval(autoplayInterval.value);
        startAutoplay();
    }
};

// For counter animation
const animateCounters = () => {
    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // ms
        const step = target / (duration / 16); // 60fps

        let current = 0;
        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };

        updateCounter();
    });
};

// Intersection Observer for animations
const setupIntersectionObserver = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('stats-container')) {
                    animateCounters();
                }
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    // Observe elements
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        observer.observe(section);
    });

    // Observe specific elements
    const statsContainer = document.querySelector('.stats-container');
    if (statsContainer) {
        observer.observe(statsContainer);
    }
};

onMounted(() => {
    // Initialize testimonial slider
    updateTestimonialSlider();
    startAutoplay();

    // Setup animations
    setupIntersectionObserver();
});

onUnmounted(() => {
    // Clear autoplay interval
    if (autoplayInterval.value) {
        clearInterval(autoplayInterval.value);
    }
});
</script>

<style scoped>
/* Base styles from your existing code */
.home-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
    position: relative;
    overflow: hidden;
}

.bg-shape {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    z-index: -1;
    opacity: 0.5;
}

.bg-shape-1 {
    width: 500px;
    height: 500px;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.2) 0%, rgba(147, 51, 234, 0.2) 100%);
    top: -200px;
    right: -100px;
    animation: float 15s ease-in-out infinite alternate;
}

.bg-shape-2 {
    width: 400px;
    height: 400px;
    background: linear-gradient(135deg, rgba(236, 72, 153, 0.2) 0%, rgba(79, 70, 229, 0.2) 100%);
    bottom: -150px;
    left: -150px;
    animation: float 20s ease-in-out infinite alternate-reverse;
}

.bg-shape-3 {
    width: 300px;
    height: 300px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(59, 130, 246, 0.2) 100%);
    top: 40%;
    left: 30%;
    animation: float 25s ease-in-out infinite alternate;
}

.bg-shape-4 {
    width: 350px;
    height: 350px;
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(239, 68, 68, 0.15) 100%);
    top: 60%;
    right: -100px;
    animation: float 18s ease-in-out infinite alternate-reverse;
}

.bg-shape-5 {
    width: 250px;
    height: 250px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(6, 182, 212, 0.15) 100%);
    bottom: 10%;
    left: 20%;
    animation: float 22s ease-in-out infinite alternate;
}

@keyframes float {
    0% {
        transform: translate(0, 0) rotate(0deg);
    }

    100% {
        transform: translate(50px, 50px) rotate(10deg);
    }
}

/* Hero section styles from your existing code */
.hero {
    padding: 6rem 0 4rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
}

.hero-content {
    flex: 1;
    max-width: 600px;
    z-index: 1;
}

.title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    color: #1a202c;
    display: flex;
    flex-direction: column;
}

.gradient-text {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #ec4899 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    display: inline-block;
}

.subtitle {
    font-size: 1.5rem;
    color: #4a5568;
    margin-bottom: 2.5rem;
    line-height: 1.5;
    font-weight: 400;
}

.cta-buttons {
    display: flex;
    gap: 1.5rem;
    margin-top: 2.5rem;
}

.primary-button,
.secondary-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.875rem 1.75rem;
    border-radius: 0.5rem;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    z-index: 1;
}

.primary-button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border: none;
    box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3);
}

.primary-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
    z-index: -1;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.primary-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 20px -3px rgba(79, 70, 229, 0.4);
}

.primary-button:hover::before {
    opacity: 1;
}

.secondary-button {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    color: #4f46e5;
    border: 1px solid rgba(79, 70, 229, 0.3);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.secondary-button:hover {
    background: rgba(255, 255, 255, 0.95);
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    border-color: rgba(79, 70, 229, 0.5);
}

.button-icon {
    width: 1.25rem;
    height: 1.25rem;
    transition: transform 0.3s ease;
}

.primary-button:hover .button-icon,
.secondary-button:hover .button-icon {
    transform: translateX(3px);
}

/* Hero image styles from your existing code */
.hero-image {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.hero-image-container {
    position: relative;
    width: 350px;
    height: 350px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-image-glow {
    position: absolute;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(79, 70, 229, 0.3) 0%, rgba(79, 70, 229, 0) 70%);
    border-radius: 50%;
    animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        transform: scale(0.9);
        opacity: 0.5;
    }

    50% {
        transform: scale(1.1);
        opacity: 0.8;
    }
}

.hero-svg {
    width: 100%;
    height: 100%;
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

/* Stats section */
.stats-section {
    padding: 3rem 0;
    margin: 2rem 0;
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2.5rem;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(229, 231, 235, 0.5);
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.stats-container.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.stat-item {
    text-align: center;
}

.stat-value {
    font-size: 3rem;
    font-weight: 800;
    color: #4f46e5;
    margin-bottom: 0.5rem;
    line-height: 1;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.stat-label {
    font-size: 1rem;
    color: #4a5568;
    font-weight: 500;
}

/* Features section styles from your existing code */
.features {
    padding: 6rem 0;
    position: relative;
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.features.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.section-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 4rem;
    color: #1a202c;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2.5rem;
}

.feature-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2.5rem 2rem;
    text-align: center;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    z-index: 1;
}

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 30px -10px rgba(79, 70, 229, 0.2);
    border-color: rgba(79, 70, 229, 0.2);
}

.feature-icon-container {
    width: 70px;
    height: 70px;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    transition: all 0.3s ease;
}

.feature-card:hover .feature-icon-container {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.2) 0%, rgba(124, 58, 237, 0.2) 100%);
    transform: scale(1.1) rotate(5deg);
}

.feature-icon {
    width: 35px;
    height: 35px;
    color: #4f46e5;
    transition: all 0.3s ease;
}

.feature-card:hover .feature-icon {
    transform: scale(1.1);
}

.feature-card h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #1a202c;
}

.feature-card p {
    color: #4a5568;
    line-height: 1.6;
    font-size: 1rem;
}

.card-hover-effect {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.05) 0%, rgba(124, 58, 237, 0.05) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: -1;
}

.feature-card:hover .card-hover-effect {
    opacity: 1;
}

/* How It Works section */
.how-it-works {
    padding: 6rem 0;
    position: relative;
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.how-it-works.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.steps-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    margin-top: 3rem;
}

.step-item {
    flex: 1;
    min-width: 250px;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
}

.step-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px -10px rgba(79, 70, 229, 0.2);
    border-color: rgba(79, 70, 229, 0.2);
}

.step-number {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 auto 1.5rem;
}

.step-content h3 {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #1a202c;
}

.step-content p {
    color: #4a5568;
    line-height: 1.6;
}

.step-connector {
    width: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4f46e5;
}

.step-connector svg {
    width: 40px;
    height: 40px;
}

/* Testimonials section */
.testimonials {
    padding: 6rem 0;
    position: relative;
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.testimonials.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.testimonial-slider {
    display: flex;
    overflow: hidden;
    margin: 3rem 0;
    transition: transform 0.5s ease;
}

.testimonial-slide {
    min-width: 100%;
    padding: 0 1rem;
}

.testimonial-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2.5rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
}

.testimonial-content {
    position: relative;
    padding-top: 2rem;
    margin-bottom: 2rem;
}

.quote-icon {
    position: absolute;
    top: 0;
    left: 0;
    width: 30px;
    height: 30px;
    color: #4f46e5;
    opacity: 0.5;
}

.testimonial-content p {
    font-size: 1.125rem;
    line-height: 1.7;
    color: #4a5568;
}

.testimonial-author {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.author-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatar-placeholder {
    color: white;
    font-weight: 600;
    font-size: 1.125rem;
}

.author-info h4 {
    font-size: 1.125rem;
    font-weight: 700;
    color: #1a202c;
    margin-bottom: 0.25rem;
}

.author-info p {
    font-size: 0.875rem;
    color: #4a5568;
}

.testimonial-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
}

.control-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(5px);
    border: 1px solid rgba(229, 231, 235, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4f46e5;
    cursor: pointer;
    transition: all 0.3s ease;
}

.control-button:hover {
    background: rgba(79, 70, 229, 0.1);
    transform: translateY(-2px);
}

.control-button svg {
    width: 20px;
    height: 20px;
}

.testimonial-dots {
    display: flex;
    gap: 0.5rem;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(79, 70, 229, 0.2);
    cursor: pointer;
    transition: all 0.3s ease;
}

.dot.active {
    background: #4f46e5;
    transform: scale(1.2);
}

/* CTA Section */
.cta-section {
    margin: 4rem 0;
    padding: 4rem;
    border-radius: 1.5rem;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.9) 0%, rgba(124, 58, 237, 0.9) 100%);
    color: white;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px -10px rgba(79, 70, 229, 0.4);
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.cta-section.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.cta-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fill-opacity='0.1' fill-rule='evenodd'/%3E%3C/svg%3E");
    opacity: 0.2;
    z-index: 0;
}

.cta-content {
    position: relative;
    z-index: 1;
}

.cta-section h2 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

.cta-section p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.9;
}

.cta-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 1rem 2rem;
    background: white;
    color: #4f46e5;
    border: none;
    border-radius: 0.5rem;
    font-size: 1.125rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 20px -3px rgba(0, 0, 0, 0.2);
}

/* FAQ Section */
.faq-section {
    padding: 6rem 0;
    position: relative;
    transform: translateY(30px);
    opacity: 0;
    transition: all 0.6s ease;
}

.faq-section.animate-in {
    transform: translateY(0);
    opacity: 1;
}

.faq-container {
    margin-top: 3rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.faq-item {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
    overflow: hidden;
    transition: all 0.3s ease;
}

.faq-item.active {
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    border-color: rgba(79, 70, 229, 0.2);
}

.faq-question {
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
}

.faq-question h3 {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1a202c;
}

.faq-icon {
    width: 24px;
    height: 24px;
    color: #4f46e5;
    transition: transform 0.3s ease;
}

.faq-item.active .faq-icon {
    transform: rotate(90deg);
}

.hidden {
    display: none;
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease, padding 0.3s ease;
}

.faq-answer.show {
    max-height: 300px;
    padding: 0 1.5rem 1.5rem;
}

.faq-answer p {
    color: #4a5568;
    line-height: 1.6;
}

/* Animation classes */
.animate-in {
    transform: translateY(0) !important;
    opacity: 1 !important;
}

/* Responsive styles */
@media (max-width: 1024px) {
    .hero {
        flex-direction: column;
        text-align: center;
        padding: 4rem 0 2rem;
    }

    .hero-content {
        max-width: 100%;
        margin-bottom: 3rem;
    }

    .title {
        font-size: 3rem;
        align-items: center;
    }

    .cta-buttons {
        justify-content: center;
    }

    .hero-image-container {
        width: 300px;
        height: 300px;
    }

    .stats-container {
        grid-template-columns: repeat(2, 1fr);
    }

    .steps-container {
        flex-direction: column;
        gap: 2rem;
    }

    .step-connector {
        transform: rotate(90deg);
        margin: 1rem 0;
    }

    .cta-section {
        padding: 3rem 2rem;
    }
}

@media (max-width: 768px) {
    .title {
        font-size: 2.5rem;
    }

    .subtitle {
        font-size: 1.25rem;
    }

    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }

    .primary-button,
    .secondary-button {
        width: 100%;
        max-width: 300px;
    }

    .feature-grid {
        grid-template-columns: 1fr;
    }

    .section-title {
        font-size: 2rem;
    }

    .stats-container {
        grid-template-columns: 1fr;
    }

    .cta-section h2 {
        font-size: 2rem;
    }
}

@media (max-width: 480px) {
    .title {
        font-size: 2rem;
    }

    .hero-image-container {
        width: 250px;
        height: 250px;
    }

    .feature-card {
        padding: 2rem 1.5rem;
    }

    .testimonial-card {
        padding: 1.5rem;
    }

    .cta-section {
        padding: 2rem 1.5rem;
    }
}
</style>