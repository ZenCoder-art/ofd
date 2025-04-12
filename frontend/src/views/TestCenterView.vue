<template>
    <div class="testing-center-container">
        <div class="bg-shape bg-shape-1"></div>
        <div class="bg-shape bg-shape-2"></div>
        <div class="bg-shape bg-shape-3"></div>

        <section class="page-header">
            <h1 class="page-title">
                <span class="gradient-text">统一检测中心</span>
            </h1>
            <p class="page-description">
                专业检测在线招聘欺诈，保护您的求职安全
            </p>
        </section>

        <section class="detection-methods">
            <div class="tabs-container">
                <div class="tabs-header">
                    <button v-for="(tab, index) in tabs" :key="index" class="tab-button"
                        :class="{ 'active': activeTab === index }" @click="setActiveTab(index)">
                        <div class="tab-icon">
                            <img :src="manualSvg" alt="icon" v-if="index === 0" />
                            <img :src="fileSvg" alt="fileicon" v-if="index === 1" />
                            <img :src="urlSvg" alt="urlicon" v-if="index === 2" />
                        </div>
                        <span>{{ tab.name }}</span>
                    </button>
                </div>

                <div class="tab-content">
                    <div v-if="activeTab === 0" class="tab-panel">
                        <div class="panel-header">
                            <h2>手动输入信息进行检测</h2>
                            <p>请输入您收到的招聘信息，我们将对其进行欺诈风险分析</p>
                        </div>

                        <form class="detection-form" @submit.prevent="submitManualDetection">
                            <div class="form-group">
                                <label for="company-name">公司名称</label>
                                <input type="text" id="company-name" v-model="manualForm.companyName"
                                    placeholder="请输入招聘公司名称" required />
                            </div>

                            <div class="form-group">
                                <label for="job-title">职位名称</label>
                                <input type="text" id="job-title" v-model="manualForm.jobTitle" placeholder="请输入招聘职位名称"
                                    required />
                            </div>

                            <div class="form-group">
                                <label for="job-description">职位描述</label>
                                <textarea id="job-description" v-model="manualForm.jobDescription"
                                    placeholder="请输入完整的职位描述信息" rows="6" required></textarea>
                            </div>

                            <div class="form-group">
                                <label for="contact-info">联系方式</label>
                                <input type="text" id="contact-info" v-model="manualForm.contactInfo"
                                    placeholder="请输入招聘方提供的联系方式" required />
                            </div>

                            <div class="form-group">
                                <label for="salary-info">薪资信息</label>
                                <input type="text" id="salary-info" v-model="manualForm.salaryInfo"
                                    placeholder="请输入招聘方提供的薪资信息" />
                            </div>

                            <div class="form-actions">
                                <button type="reset" class="secondary-button">
                                    <span>重置</span>
                                </button>
                                <button type="submit" class="primary-button">
                                    <span>开始检测</span>
                                    <svg class="button-icon" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M13.75 6.75L19.25 12L13.75 17.25" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M19 12H4.75" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </div>
                        </form>
                    </div>

                    <div v-if="activeTab === 1" class="tab-panel">
                        <div class="panel-header">
                            <h2>上传文件进行检测</h2>
                            <p>上传招聘相关文件，支持PDF、Word、图片等格式</p>
                        </div>

                        <div class="upload-container" @dragover.prevent @drop.prevent="onFileDrop">
                            <div class="upload-area" :class="{ 'dragging': isDragging }"
                                @dragenter.prevent="isDragging = true" @dragleave.prevent="isDragging = false"
                                @drop.prevent="onFileDrop">
                                <div class="upload-icon">
                                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M12 15V3M12 3L8 7M12 3L16 7" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M20 17V19C20 20.1046 19.1046 21 18 21H6C4.89543 21 4 20.1046 4 19V17"
                                            stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" />
                                    </svg>
                                </div>
                                <div class="upload-text">
                                    <h3>拖放文件到此处或</h3>
                                    <label for="file-upload" class="upload-button">选择文件</label>
                                    <input type="file" id="file-upload" @change="onFileChange" multiple
                                        accept=".pdf,.doc,.docx,.jpg,.jpeg,.png" />
                                </div>
                                <p class="upload-hint">支持格式：PDF、Word、JPG、PNG</p>
                            </div>

                            <div v-if="uploadedFiles.length > 0" class="uploaded-files">
                                <h3>已上传文件</h3>
                                <ul class="file-list">
                                    <li v-for="(file, index) in uploadedFiles" :key="index" class="file-item">
                                        <div class="file-info">
                                            <svg class="file-icon" viewBox="0 0 24 24" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <path d="M14 3V7C14 7.55228 14.4477 8 15 8H19" stroke="currentColor"
                                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                                <path
                                                    d="M17 21H7C5.89543 21 5 20.1046 5 19V5C5 3.89543 5.89543 3 7 3H14L19 8V19C19 20.1046 18.1046 21 17 21Z"
                                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                    stroke-linejoin="round" />
                                            </svg>
                                            <span class="file-name">{{ file.name }}</span>
                                        </div>
                                        <button class="remove-file" @click="removeFile(index)">
                                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M18 6L6 18" stroke="currentColor" stroke-width="2"
                                                    stroke-linecap="round" stroke-linejoin="round" />
                                                <path d="M6 6L18 18" stroke="currentColor" stroke-width="2"
                                                    stroke-linecap="round" stroke-linejoin="round" />
                                            </svg>
                                        </button>
                                    </li>
                                </ul>
                            </div>

                            <div class="form-actions">
                                <button type="button" class="secondary-button" @click="clearFiles">
                                    <span>清除所有</span>
                                </button>
                                <button type="button" class="primary-button" @click="submitFileDetection"
                                    :disabled="uploadedFiles.length === 0">
                                    <span>开始检测</span>
                                    <svg class="button-icon" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M13.75 6.75L19.25 12L13.75 17.25" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M19 12H4.75" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div v-if="activeTab === 2" class="tab-panel">
                        <div class="panel-header">
                            <h2>输入招聘网页链接进行检测</h2>
                            <p>输入招聘网页的URL，我们将分析该页面内容是否存在欺诈风险</p>
                        </div>

                        <form class="detection-form" @submit.prevent="submitUrlDetection">
                            <div class="form-group url-input-group">
                                <label for="recruitment-url">招聘网页链接</label>
                                <div class="url-input-container">
                                    <input type="url" id="recruitment-url" v-model="urlForm.url"
                                        placeholder="https://example.com/job/12345" required />
                                    <button type="button" class="paste-button" @click="pasteFromClipboard">
                                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M16 4H18C19.1046 4 20 4.89543 20 6V20C20 21.1046 19.1046 22 18 22H6C4.89543 22 4 21.1046 4 20V6C4 4.89543 4.89543 4 6 4H8"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round" />
                                            <path
                                                d="M15 2H9C8.44772 2 8 2.44772 8 3V5C8 5.55228 8.44772 6 9 6H15C15.5523 6 16 5.55228 16 5V3C16 2.44772 15.5523 2 15 2Z"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round" />
                                        </svg>
                                        <span>粘贴</span>
                                    </button>
                                </div>
                            </div>

                            <div class="form-group">
                                <label for="platform-type">招聘平台类型</label>
                                <select id="platform-type" v-model="urlForm.platformType">
                                    <option value="">-- 请选择平台类型 --</option>
                                    <option value="zhilian">智联招聘</option>
                                    <option value="51job">前程无忧</option>
                                    <option value="lagou">拉勾网</option>
                                    <option value="boss">BOSS直聘</option>
                                    <option value="liepin">猎聘网</option>
                                    <option value="other">其他平台</option>
                                </select>
                            </div>

                            <div class="form-actions">
                                <button type="reset" class="secondary-button">
                                    <span>重置</span>
                                </button>
                                <button type="submit" class="primary-button">
                                    <span>开始检测</span>
                                    <svg class="button-icon" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M13.75 6.75L19.25 12L13.75 17.25" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                        <path d="M19 12H4.75" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>

        <section v-if="showResults" class="detection-results">
            <div class="results-container">
                <div class="results-header">
                    <h2>检测结果</h2>
                    <div class="risk-badge" :class="getRiskLevelClass(detectionResults.riskLevel)">
                        {{ getRiskLevelText(detectionResults.riskLevel) }}
                    </div>
                </div>

                <div class="results-summary">
                    <div class="summary-item">
                        <div class="summary-icon" :class="getRiskLevelClass(detectionResults.riskLevel)">
                            <svg v-if="detectionResults.riskLevel === 'low'" viewBox="0 0 24 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M9 12L11 14L15 10" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round" />
                                <path
                                    d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                    stroke="currentColor" stroke-width="2" />
                            </svg>
                            <svg v-if="detectionResults.riskLevel === 'medium'" viewBox="0 0 24 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path d="M12 16V16.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path
                                    d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                    stroke="currentColor" stroke-width="2" />
                            </svg>
                            <svg v-if="detectionResults.riskLevel === 'high'" viewBox="0 0 24 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path d="M12 16V16.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                                <path
                                    d="M10.29 3.86001L1.82001 18C1.64537 18.3024 1.55296 18.6453 1.55199 18.9945C1.55101 19.3437 1.6415 19.6871 1.81443 19.9905C1.98737 20.2939 2.23672 20.5468 2.53771 20.7239C2.83869 20.901 3.1808 20.9962 3.53001 21H20.47C20.8192 20.9962 21.1613 20.901 21.4623 20.7239C21.7633 20.5468 22.0126 20.2939 22.1856 19.9905C22.3585 19.6871 22.449 19.3437 22.448 18.9945C22.447 18.6453 22.3546 18.3024 22.18 18L13.71 3.86001C13.5317 3.56611 13.2807 3.32313 12.9812 3.15449C12.6817 2.98585 12.3437 2.89726 12 2.89726C11.6563 2.89726 11.3183 2.98585 11.0188 3.15449C10.7193 3.32313 10.4683 3.56611 10.29 3.86001Z"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg>
                        </div>
                        <div class="summary-content">
                            <h3>风险评估</h3>
                            <p>{{ detectionResults.summary }}</p>
                        </div>
                    </div>
                </div>

                <div class="results-details">
                    <h3>详细分析</h3>
                    <div class="details-grid">
                        <div v-for="(detail, index) in detectionResults.details" :key="index" class="detail-item">
                            <div class="detail-header">
                                <div class="detail-icon" :class="getDetailLevelClass(detail.level)">
                                    <svg v-if="detail.level === 'safe'" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M9 12L11 14L15 10" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                        <path
                                            d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                            stroke="currentColor" stroke-width="2" />
                                    </svg>
                                    <svg v-if="detail.level === 'warning'" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" />
                                        <path d="M12 16V16.01" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                        <path
                                            d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
                                            stroke="currentColor" stroke-width="2" />
                                    </svg>
                                    <svg v-if="detail.level === 'danger'" viewBox="0 0 24 24" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" />
                                        <path d="M12 16V16.01" stroke="currentColor" stroke-width="2"
                                            stroke-linecap="round" stroke-linejoin="round" />
                                        <path
                                            d="M10.29 3.86001L1.82001 18C1.64537 18.3024 1.55296 18.6453 1.55199 18.9945C1.55101 19.3437 1.6415 19.6871 1.81443 19.9905C1.98737 20.2939 2.23672 20.5468 2.53771 20.7239C2.83869 20.901 3.1808 20.9962 3.53001 21H20.47C20.8192 20.9962 21.1613 20.901 21.4623 20.7239C21.7633 20.5468 22.0126 20.2939 22.1856 19.9905C22.3585 19.6871 22.449 19.3437 22.448 18.9945C22.447 18.6453 22.3546 18.3024 22.18 18L13.71 3.86001C13.5317 3.56611 13.2807 3.32313 12.9812 3.15449C12.6817 2.98585 12.3437 2.89726 12 2.89726C11.6563 2.89726 11.3183 2.98585 11.0188 3.15449C10.7193 3.32313 10.4683 3.56611 10.29 3.86001Z"
                                            stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" />
                                    </svg>
                                </div>
                                <h4>{{ detail.title }}</h4>
                            </div>
                            <p>{{ detail.description }}</p>
                        </div>
                    </div>
                </div>

                <div class="results-actions">
                    <button class="secondary-button" @click="showResults = false">
                        <span>返回检测</span>
                    </button>
                    <button class="primary-button" @click="downloadReport">
                        <span>下载完整报告</span>
                        <svg class="button-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 15V3M12 15L8 11M12 15L16 11" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round" />
                            <path
                                d="M2 17V20C2 20.5304 2.21071 21.0391 2.58579 21.4142C2.96086 21.7893 3.46957 22 4 22H20C20.5304 22 21.0391 21.7893 21.4142 21.4142C21.7893 21.0391 22 20.5304 22 20V17"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </button>
                </div>
            </div>
        </section>

        <section class="tips-section">
            <h2 class="section-title">
                <span class="gradient-text">防范招聘欺诈小贴士</span>
            </h2>
            <div class="tips-container">
                <div class="tip-card">
                    <div class="tip-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M12 16V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M12 8H12.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>核实公司信息</h3>
                    <p>通过官方渠道查询公司营业执照、工商注册信息，确认公司真实性。</p>
                </div>

                <div class="tip-card">
                    <div class="tip-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12 11C14.2091 11 16 9.20914 16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7C8 9.20914 9.79086 11 12 11Z"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path
                                d="M6 21V19C6 17.9391 6.42143 16.9217 7.17157 16.1716C7.92172 15.4214 8.93913 15 10 15H14C15.0609 15 16.0783 15.4214 16.8284 16.1716C17.5786 16.9217 18 17.9391 18 19V21"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>警惕过高薪资</h3>
                    <p>对于明显高于行业水平的薪资承诺，应保持警惕，这可能是欺诈的迹象。</p>
                </div>

                <div class="tip-card">
                    <div class="tip-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M16 16L12 12L8 16" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M12 8V16" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>不要预付费用</h3>
                    <p>正规招聘不会要求应聘者支付培训费、押金、资料费等费用，收到此类要求应立即警惕。</p>
                </div>

                <div class="tip-card">
                    <div class="tip-icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M22 11.08V12C21.9988 14.1564 21.3005 16.2547 20.0093 17.9818C18.7182 19.709 16.9033 20.9725 14.8354 21.5839C12.7674 22.1953 10.5573 22.1219 8.53447 21.3746C6.51168 20.6273 4.78465 19.2461 3.61096 17.4371C2.43727 15.628 1.87979 13.4881 2.02168 11.3363C2.16356 9.18455 2.99721 7.13631 4.39828 5.49706C5.79935 3.85781 7.69279 2.71537 9.79619 2.24013C11.8996 1.7649 14.1003 1.98232 16.07 2.85999"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M22 4L12 14.01L9 11.01" stroke="currentColor" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                    <h3>使用正规招聘平台</h3>
                    <p>优先使用知名招聘网站和平台，这些平台通常有企业认证机制，可降低遇到欺诈的风险。</p>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import manualSvg from "../components/common/manual.svg"
import fileSvg from "../components/common/file.svg"
import urlSvg from "../components/common/url.svg"
import uploadSvg from "../components/common/upload.svg"
const tabs = [
    { name: '手动输入检测', icon: 'text' },
    { name: '文件上传检测', icon: 'file' },
    { name: '网页链接检测', icon: 'link' }
];

const activeTab = ref(0);

const setActiveTab = (index) => {
    activeTab.value = index;
};

const manualForm = reactive({
    companyName: '',
    jobTitle: '',
    jobDescription: '',
    contactInfo: '',
    salaryInfo: ''
});

const urlForm = reactive({
    url: '',
    platformType: ''
});

const isDragging = ref(false);
const uploadedFiles = ref([]);

const onFileDrop = (event) => {
    isDragging.value = false;
    const files = event.dataTransfer.files;
    handleFiles(files);
};

const onFileChange = (event) => {
    const files = event.target.files;
    handleFiles(files);
};

const handleFiles = (files) => {
    for (let i = 0; i < files.length; i++) {
        uploadedFiles.value.push(files[i]);
    }
};

const removeFile = (index) => {
    uploadedFiles.value.splice(index, 1);
};

const clearFiles = () => {
    uploadedFiles.value = [];
};

const pasteFromClipboard = async () => {
    try {
        const text = await navigator.clipboard.readText();
        if (text.startsWith('http')) {
            urlForm.url = text;
        }
    } catch (err) {
        console.error('Failed to read clipboard contents: ', err);
    }
};

const showResults = ref(false);
const detectionResults = reactive({
    riskLevel: 'medium',
    summary: '该招聘信息存在一定风险因素，建议进一步核实公司信息。',
    details: [
        {
            level: 'safe',
            title: '公司信息',
            description: '公司名称可在工商系统中查询到，成立时间超过2年。'
        },
        {
            level: 'warning',
            title: '联系方式',
            description: '提供的联系方式为个人手机号，而非企业邮箱或固定电话，存在一定风险。'
        },
        {
            level: 'danger',
            title: '薪资承诺',
            description: '承诺的薪资明显高于行业平均水平，且强调"无需经验"，存在高风险。'
        },
        {
            level: 'warning',
            title: '工作地点',
            description: '工作地点描述模糊，未提供具体办公地址，建议实地考察确认。'
        }
    ]
});

const submitManualDetection = () => {
    console.log('Manual detection submitted:', manualForm);
    showResults.value = true;
};

const submitFileDetection = () => {
    console.log('File detection submitted:', uploadedFiles.value);
    showResults.value = true;
};

const submitUrlDetection = () => {
    console.log('URL detection submitted:', urlForm);
    showResults.value = true;
};

const getRiskLevelClass = (level) => {
    switch (level) {
        case 'low':
            return 'risk-low';
        case 'medium':
            return 'risk-medium';
        case 'high':
            return 'risk-high';
        default:
            return '';
    }
};

const getRiskLevelText = (level) => {
    switch (level) {
        case 'low':
            return '低风险';
        case 'medium':
            return '中等风险';
        case 'high':
            return '高风险';
        default:
            return '未知风险';
    }
};

const getDetailLevelClass = (level) => {
    switch (level) {
        case 'safe':
            return 'detail-safe';
        case 'warning':
            return 'detail-warning';
        case 'danger':
            return 'detail-danger';
        default:
            return '';
    }
};

const downloadReport = () => {
    alert('报告下载功能将在实际应用中实现');
};
</script>

<style scoped>
.testing-center-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
    position: relative;
    overflow: hidden;
}

/* Background shapes */
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

@keyframes float {
    0% {
        transform: translate(0, 0) rotate(0deg);
    }

    100% {
        transform: translate(50px, 50px) rotate(10deg);
    }
}

/* Page header */
.page-header {
    padding: 4rem 0 2rem;
    text-align: center;
}

.page-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1rem;
    color: #1a202c;
}

.gradient-text {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #ec4899 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    display: inline-block;
}

.page-description {
    font-size: 1.25rem;
    color: #4a5568;
    max-width: 700px;
    margin: 0 auto;
}

/* Tabs */
.detection-methods {
    margin: 2rem 0 4rem;
}

.tabs-container {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    overflow: hidden;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
}

.tabs-header {
    display: flex;
    border-bottom: 1px solid rgba(229, 231, 235, 0.5);
}

.tab-button {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 1.25rem 1rem;
    background: transparent;
    border: none;
    color: #4a5568;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
}

.tab-button::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    transform: scaleX(0);
    transform-origin: center;
    transition: transform 0.3s ease;
}

.tab-button:hover {
    color: #1a202c;
    background: rgba(79, 70, 229, 0.05);
}

.tab-button.active {
    color: #4f46e5;
    background: rgba(79, 70, 229, 0.08);
}

.tab-button.active::after {
    transform: scaleX(1);
}

.tab-icon {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.tab-content {
    padding: 2rem;
}

.panel-header {
    margin-bottom: 2rem;
    text-align: center;
}

.panel-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a202c;
    margin-bottom: 0.5rem;
}

.panel-header p {
    color: #4a5568;
}

/* Form styles */
.detection-form {
    max-width: 700px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #1a202c;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid rgba(229, 231, 235, 0.8);
    border-radius: 0.5rem;
    background: rgba(255, 255, 255, 0.8);
    color: #1a202c;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
    outline: none;
    border-color: #4f46e5;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
}

.form-group textarea {
    resize: vertical;
    min-height: 120px;
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
    margin-top: 2rem;
}

/* URL input specific styles */
.url-input-group {
    margin-bottom: 2rem;
}

.url-input-container {
    display: flex;
    gap: 0.5rem;
}

.paste-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    background: rgba(79, 70, 229, 0.1);
    color: #4f46e5;
    border: none;
    border-radius: 0.5rem;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.paste-button:hover {
    background: rgba(79, 70, 229, 0.2);
}

.paste-button svg {
    width: 18px;
    height: 18px;
}

/* File upload styles */
.upload-container {
    max-width: 700px;
    margin: 0 auto;
}

.upload-area {
    border: 2px dashed rgba(79, 70, 229, 0.3);
    border-radius: 1rem;
    padding: 3rem 2rem;
    text-align: center;
    background: rgba(255, 255, 255, 0.5);
    transition: all 0.3s ease;
    cursor: pointer;
}

.upload-area.dragging {
    background: rgba(79, 70, 229, 0.1);
    border-color: #4f46e5;
}

.upload-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 1.5rem;
    color: #4f46e5;
    opacity: 0.7;
}

.upload-text h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1rem;
}

.upload-button {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border-radius: 0.5rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-bottom: 1rem;
}

.upload-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
}

input[type="file"] {
    display: none;
}

.upload-hint {
    font-size: 0.875rem;
    color: #6b7280;
}

.uploaded-files {
    margin-top: 2rem;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 0.75rem;
    padding: 1.5rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
}

.uploaded-files h3 {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1rem;
}

.file-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.file-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem;
    border-radius: 0.5rem;
    background: rgba(255, 255, 255, 0.7);
    margin-bottom: 0.5rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
}

.file-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.file-icon {
    width: 20px;
    height: 20px;
    color: #4f46e5;
}

.file-name {
    font-size: 0.875rem;
    color: #1a202c;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 300px;
}

.remove-file {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(239, 68, 68, 0.1);
    color: #ef4444;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s ease;
}

.remove-file:hover {
    background: rgba(239, 68, 68, 0.2);
}

.remove-file svg {
    width: 16px;
    height: 16px;
}

/* Button styles */
.primary-button,
.secondary-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
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
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
}

.primary-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(79, 70, 229, 0.4);
}

.primary-button:disabled {
    background: #9ca3af;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.secondary-button {
    background: rgba(255, 255, 255, 0.8);
    color: #4a5568;
    border: 1px solid rgba(229, 231, 235, 0.8);
}

.secondary-button:hover {
    background: rgba(255, 255, 255, 0.95);
    color: #1a202c;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.button-icon {
    width: 20px;
    height: 20px;
    transition: transform 0.3s ease;
}

.primary-button:hover .button-icon,
.secondary-button:hover .button-icon {
    transform: translateX(3px);
}

/* Results section */
.detection-results {
    margin: 2rem 0 4rem;
}

.results-container {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
}

.results-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(229, 231, 235, 0.5);
}

.results-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a202c;
}

.risk-badge {
    padding: 0.5rem 1rem;
    border-radius: 2rem;
    font-weight: 600;
    font-size: 0.875rem;
}

.risk-low {
    background: rgba(16, 185, 129, 0.1);
    color: #10b981;
}

.risk-medium {
    background: rgba(245, 158, 11, 0.1);
    color: #f59e0b;
}

.risk-high {
    background: rgba(239, 68, 68, 0.1);
    color: #ef4444;
}

.results-summary {
    margin-bottom: 2rem;
}

.summary-item {
    display: flex;
    gap: 1.5rem;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 0.75rem;
    padding: 1.5rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
}

.summary-icon {
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    flex-shrink: 0;
}

.summary-icon svg {
    width: 30px;
    height: 30px;
}

.summary-content h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 0.5rem;
}

.summary-content p {
    color: #4a5568;
    line-height: 1.6;
}

.results-details {
    margin-bottom: 2rem;
}

.results-details h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1.5rem;
}

.details-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.detail-item {
    background: rgba(255, 255, 255, 0.7);
    border-radius: 0.75rem;
    padding: 1.5rem;
    border: 1px solid rgba(229, 231, 235, 0.5);
}

.detail-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
}

.detail-icon {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    flex-shrink: 0;
}

.detail-icon svg {
    width: 20px;
    height: 20px;
}

.detail-safe {
    background: rgba(16, 185, 129, 0.1);
    color: #10b981;
}

.detail-warning {
    background: rgba(245, 158, 11, 0.1);
    color: #f59e0b;
}

.detail-danger {
    background: rgba(239, 68, 68, 0.1);
    color: #ef4444;
}

.detail-item h4 {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1a202c;
}

.detail-item p {
    color: #4a5568;
    line-height: 1.6;
}

.results-actions {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
    margin-top: 2rem;
}

/* Tips section */
.tips-section {
    padding: 4rem 0;
    position: relative;
}

.section-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 3rem;
    color: #1a202c;
}

.tips-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2rem;
}

.tip-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    border: 1px solid rgba(229, 231, 235, 0.5);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
}

.tip-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px -10px rgba(79, 70, 229, 0.2);
    border-color: rgba(79, 70, 229, 0.2);
}

.tip-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    color: #4f46e5;
}

.tip-icon svg {
    width: 30px;
    height: 30px;
}

.tip-card h3 {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #1a202c;
}

.tip-card p {
    color: #4a5568;
    line-height: 1.6;
    font-size: 0.9375rem;
}

/* Responsive styles */
@media (max-width: 768px) {
    .page-title {
        font-size: 2.5rem;
    }

    .tabs-header {
        flex-direction: column;
    }

    .tab-button {
        justify-content: flex-start;
        padding: 1rem;
    }

    .tab-button::after {
        width: 3px;
        height: 100%;
        top: 0;
        left: 0;
        transform: scaleY(0);
    }

    .tab-button.active::after {
        transform: scaleY(1);
    }

    .url-input-container {
        flex-direction: column;
    }

    .details-grid {
        grid-template-columns: 1fr;
    }

    .tips-container {
        grid-template-columns: 1fr;
    }

    .form-actions {
        flex-direction: column;
    }

    .primary-button,
    .secondary-button {
        width: 100%;
    }
}

@media (max-width: 480px) {
    .page-title {
        font-size: 2rem;
    }

    .tab-content {
        padding: 1.5rem 1rem;
    }

    .results-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }

    .summary-item {
        flex-direction: column;
        gap: 1rem;
    }

    .detail-header {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>