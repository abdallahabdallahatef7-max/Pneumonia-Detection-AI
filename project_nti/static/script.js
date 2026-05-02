document.addEventListener('DOMContentLoaded', () => {
    const uploadBox = document.getElementById('upload-box');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    
    const previewSection = document.getElementById('preview-section');
    const imagePreview = document.getElementById('image-preview');
    const removeBtn = document.getElementById('remove-btn');
    const analyzeBtn = document.getElementById('analyze-btn');
    
    const loadingState = document.getElementById('loading-state');
    const resultSection = document.getElementById('result-section');
    const resultCard = document.getElementById('result-card');
    const resultIcon = document.getElementById('result-icon');
    const predictionText = document.getElementById('prediction-text');
    const probabilityFill = document.getElementById('probability-fill');
    const probabilityValue = document.getElementById('probability-value');
    const resetBtn = document.getElementById('reset-btn');

    let currentFile = null;

    // Trigger file input when clicking browse or upload box
    browseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        fileInput.click();
    });

    uploadBox.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle Drag and Drop
    uploadBox.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadBox.classList.add('dragover');
    });

    uploadBox.addEventListener('dragleave', () => {
        uploadBox.classList.remove('dragover');
    });

    uploadBox.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadBox.classList.remove('dragover');
        
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    // Handle File Selection
    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please select a valid image file (JPG, PNG).');
            return;
        }

        currentFile = file;
        
        // Show preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            uploadBox.classList.add('hidden');
            previewSection.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
    }

    // Remove Image
    removeBtn.addEventListener('click', () => {
        currentFile = null;
        fileInput.value = '';
        previewSection.classList.add('hidden');
        uploadBox.classList.remove('hidden');
    });

    // Analyze Button Click
    analyzeBtn.addEventListener('click', async () => {
        if (!currentFile) return;

        // UI State change
        previewSection.classList.add('hidden');
        loadingState.classList.remove('hidden');

        // Prepare FormData
        const formData = new FormData();
        formData.append('image', currentFile);

        try {
            const response = await fetch('/upload/image', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`Server responded with ${response.status}`);
            }

            const data = await response.json();
            displayResult(data);

        } catch (error) {
            console.error('Error during analysis:', error);
            alert('An error occurred during analysis. Please try again.');
            
            // Revert state
            loadingState.classList.add('hidden');
            previewSection.classList.remove('hidden');
        }
    });

    function displayResult(data) {
        // Hide loading
        loadingState.classList.add('hidden');
        resultSection.classList.remove('hidden');

        const prediction = data.prediction; // e.g., "Pneumonia" or "Normal"
        const probability = parseFloat(data.probability) * 100;

        // Reset classes
        resultCard.className = 'result-card';
        
        if (prediction.toLowerCase() === 'normal') {
            resultCard.classList.add('normal');
            resultIcon.innerHTML = "<i class='bx bx-check-shield'></i>";
            predictionText.textContent = "Normal (Healthy)";
        } else {
            resultCard.classList.add('pneumonia');
            resultIcon.innerHTML = "<i class='bx bx-error-alt'></i>";
            predictionText.textContent = "Pneumonia Detected";
        }

        // Animate probability bar
        setTimeout(() => {
            probabilityFill.style.width = `${probability}%`;
            
            // Animate number
            let start = 0;
            const duration = 1000;
            const step = timestamp => {
                if (!start) start = timestamp;
                const progress = timestamp - start;
                const current = Math.min(progress / duration * probability, probability);
                probabilityValue.textContent = current.toFixed(1);
                if (progress < duration) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
            
        }, 100);
    }

    // Reset Flow
    resetBtn.addEventListener('click', () => {
        currentFile = null;
        fileInput.value = '';
        imagePreview.src = '';
        probabilityFill.style.width = '0%';
        probabilityValue.textContent = '--';
        
        resultSection.classList.add('hidden');
        uploadBox.classList.remove('hidden');
    });
});
